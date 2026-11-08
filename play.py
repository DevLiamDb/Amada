"""Play with Amada (ONNX, CPU). Models live in Release/amada-<version>/ (amada_model.onnx + tokenizer/).
Default: the newest release.

    python play.py                  # newest release
    python play.py --version 2.0    # an older one (1.0, 2.0, 3.0, 3.0.1, ...)
    python play.py --model path/to/amada_model.onnx

1. Paste a text (several lines OK), then press Enter on an empty line.
2. Ask questions, one per line:
     Did Lea eat an apple?                         -> yes/no
     Which apple did she eat? | red, green, yellow -> choice
     How hungry is she? #                          -> score (none/low/moderate/high)
     How happy is she? # not at all, a bit, very   -> score with your own levels
   :new = new text    :q = quit
"""
import argparse, json, os, sys, time
import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
RELEASE = os.path.join(HERE, "Release")


def release_model(version):
    return os.path.join(RELEASE, f"amada-{version}", "amada_model.onnx")


def releases():
    """installed versions, oldest first (numeric sort: 3.0 < 3.0.1 < 3.1)."""
    vs = [d[len("amada-"):] for d in os.listdir(RELEASE) if d.startswith("amada-")] if os.path.isdir(RELEASE) else []
    vs = [v for v in vs if os.path.exists(release_model(v))]
    return sorted(vs, key=lambda v: [int(x) for x in v.split(".") if x.isdigit()])


V1_MODEL, V2_MODEL, V3_MODEL = release_model("1.0"), release_model("2.0"), release_model("3.0")
DEFAULT_MODEL = release_model(releases()[-1]) if releases() else V1_MODEL
DEFAULT_LEVELS = ["none", "low", "moderate", "high"]
MAX_LEN = 512          # fallback when the model folder has no pytorch/amada_meta.json
TYPE_ID = {"noul": 1, "choice": 2, "score": 3}


def model_dir(model_path):
    """folder holding the tokenizer + amada_meta.json next to the ONNX (tokenizer/, or pytorch/ for releases with weights)."""
    for sub in ("tokenizer", "pytorch"):
        d = os.path.join(os.path.dirname(model_path), sub)
        if os.path.exists(os.path.join(d, "tokenizer_config.json")):
            return d
    sys.exit(f"no tokenizer/ folder next to {model_path} (a wrong tokenizer silently ruins the answers)")


def load_tokenizer(model_path):
    return AutoTokenizer.from_pretrained(model_dir(model_path))


class Amada:
    def __init__(self, model_path):
        self.tok = load_tokenizer(model_path)
        meta = os.path.join(model_dir(model_path), "amada_meta.json")
        self.max_len = json.load(open(meta)).get("max_len", MAX_LEN) if os.path.exists(meta) else MAX_LEN
        self.Q, self.OPT, self.LVL = self.tok.convert_tokens_to_ids(["[Q]", "[OPT]", "[LVL]"])
        so = ort.SessionOptions()
        so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        self.sess = ort.InferenceSession(model_path, so, providers=["CPUExecutionProvider"])

    def _ids(self, text, lead_space=False):
        if lead_space and not text.startswith(" "):
            text = " " + text
        return self.tok(text, add_special_tokens=False)["input_ids"]

    def ask(self, state, questions):
        """questions: list of {"type", "text", "options"/"levels"} -> list of results."""
        q_part, q_pos, opt_pos, q_type = [], [], [], []
        for q in questions:
            q_pos.append(len(q_part))
            q_part += [self.Q] + self._ids(q["text"], True)[:48]
            t = TYPE_ID[q["type"]]
            q_type.append(t)
            opts = q.get("options") if t == 2 else q.get("levels") if t == 3 else []
            marker = self.OPT if t == 2 else self.LVL
            rel = []
            for o in opts:
                rel.append(len(q_part))
                q_part += [marker] + self._ids(o, True)[:16]
            opt_pos.append(rel)
        q_part += [self.tok.sep_token_id]
        budget = self.max_len - 2 - len(q_part)
        state_ids = self._ids(state)
        cut = len(state_ids) > budget
        ids = [self.tok.cls_token_id] + state_ids[:budget] + [self.tok.sep_token_id]
        off = len(ids)
        ids += q_part

        Qn, On = len(questions), max([len(r) for r in opt_pos] + [1])
        feed = {
            "input_ids": np.array([ids], dtype=np.int64),
            "attention_mask": np.ones((1, len(ids)), dtype=np.int64),
            "q_pos": np.array([[off + p for p in q_pos]], dtype=np.int64),
            "q_type": np.array([q_type], dtype=np.int64),
            "opt_pos": np.zeros((1, Qn, On), dtype=np.int64),
            "opt_mask": np.zeros((1, Qn, On), dtype=bool),
        }
        for j, rel in enumerate(opt_pos):
            for k, p in enumerate(rel):
                feed["opt_pos"][0, j, k] = off + p
                feed["opt_mask"][0, j, k] = True
        outs = self.sess.run(None, feed)
        p_yes, probs = outs[0], outs[1]
        p_unk = outs[2] if len(outs) > 2 else None          # v2: p_unknown ("info not provided")
        out = []
        for j, q in enumerate(questions):
            if q["type"] == "noul":
                out.append({"p_yes": float(p_yes[0, j])})
                if p_unk is not None:
                    out[-1]["p_unknown"] = float(p_unk[0, j])
            else:
                opts = q.get("options") or q.get("levels")
                out.append({"probs": dict(zip(opts, probs[0, j, :len(opts)].tolist()))})
        return out, cut


def parse_question(line):
    if "|" in line:
        text, opts = line.split("|", 1)
        return {"type": "choice", "text": text.strip(), "options": [o.strip() for o in opts.split(",") if o.strip()]}
    if "#" in line:
        text, lv = line.split("#", 1)
        levels = [o.strip() for o in lv.split(",") if o.strip()] or DEFAULT_LEVELS
        return {"type": "score", "text": text.strip(), "levels": levels}
    return {"type": "noul", "text": line.strip()}


def bar(p, width=20):
    n = round(p * width)
    return "#" * n + "." * (width - n)


def show(q, r):
    if q["type"] == "noul":
        p = r["p_yes"]
        verdict = "YES" if p >= 0.5 else "NO"
        pu = r.get("p_unknown")
        if pu is not None and pu >= 0.5:
            verdict = "INFO NOT PROVIDED"
        print(f"  {verdict}  yes {p*100:5.1f}%  [{bar(p)}]" + (f"  unknown {pu*100:4.1f}%" if pu is not None else ""))
    else:
        items = sorted(r["probs"].items(), key=lambda kv: -kv[1]) if q["type"] == "choice" else r["probs"].items()
        best = max(r["probs"], key=r["probs"].get)
        for name, p in items:
            mark = ">" if name == best else " "
            print(f"  {mark} {name:<22} {p*100:5.1f}%  [{bar(p)}]")


def read_text():
    print("\nPaste the text, then an empty line:")
    lines = []
    while True:
        try:
            l = input()
        except EOFError:
            sys.exit(0)
        if not l.strip():
            if lines:
                return "\n".join(lines)
            continue
        lines.append(l)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=None, help="path to an amada_model.onnx")
    ap.add_argument("--version", default=None, help=f"release to load: {', '.join(releases()) or 'none installed'}")
    args = ap.parse_args()
    args.model = args.model or (release_model(args.version) if args.version else DEFAULT_MODEL)
    if not os.path.exists(args.model):
        sys.exit(f"model not found: {args.model}")
    print(f"loading Amada ({os.path.getsize(args.model) / 1e9:.1f} GB)...", flush=True)
    t0 = time.time()
    amada = Amada(args.model)
    print(f"ready in {time.time()-t0:.0f}s | {args.model} | max {amada.max_len} tokens")
    print(__doc__.split("2.", 1)[1].split("\n", 1)[1])

    state = read_text()
    while True:
        try:
            line = input("\n? ").strip()
        except EOFError:
            break
        if not line:
            continue
        if line == ":q":
            break
        if line == ":new":
            state = read_text()
            continue
        q = parse_question(line)
        if q["type"] == "choice" and len(q["options"]) < 2:
            print("  need at least 2 options after |")
            continue
        t0 = time.time()
        (r,), cut = amada.ask(state, [q])
        show(q, r)
        print(f"  ({(time.time()-t0)*1000:.0f} ms{f', text cut to {amada.max_len} tokens' if cut else ''})")


if __name__ == "__main__":
    main()
