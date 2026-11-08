# Changelog

Amada is a fast decision model. It does not generate text: given a text and questions, it returns calibrated
probabilities (`noul` yes / no, `choice`, `score` levels, and `p_unknown` "the text does not say").

Every version can be downloaded from the [releases](https://github.com/DevLiamDb/Amada/releases).

---

## [4.0] - in preparation

Messy real-life writing and the weak spots found by the benchmarks. Starts from the 3.1 weights.

- Added: MASSIVE 1.1 (Amazon, CC BY 4.0, 60 voice-assistant intents, 12 languages) and 88milSMS (Université
  Paul-Valéry Montpellier, CC BY 4.0, real French text messages, questions written by GPT-6 Luna, half in French).
- Added: half of the replayed data rewritten with keyboard typos, swapped letters, lost accents, SMS spelling and
  homophones, with the same answers (numbers and negations are never touched).
- Added: answer-type questions (the TREC skill), near-identical support intents (the Banking77 skill, banking left
  out on purpose), scores written for one precise level, more long texts. TREC and Banking77 themselves stay out of training.
- Note: after 4.0, MASSIVE scores are no longer zero-shot.

## [3.1] - 2026-11-07 - current

Short fine-tune of 3.0 to tell near-neighbour labels apart, then recalibrated.

- Added (2026-11-08): `amada-3.1-int4.zip`, the same model with 4-bit weights (196 MB instead of 1.25 GB, needs
  onnxruntime 1.20 or newer). Same tests, same laptop: accuracy 0.897 vs 0.899 in English, 0.983 vs 0.984 in
  11 languages, choice ECE 0.017 vs 0.016, peak RAM 1.15 GB vs 3.2 GB, a little faster. Activations stay in FP32.

- Added: option lists whose distractors are the gold label's nearest labels (embedding similarity) instead of random ones.
- Added: CLINC150, real user requests (150 intents + out-of-scope). Banking77 is still never used for training.
- Changed: 1 epoch (3,440 steps, about 3 h on a T4 GPU), 35k replay of v3 data against forgetting.
- Changed: temperatures refitted on v3.1 validation + half of the bake-off sets; the other half stays unseen for the report.
- Results, public datasets (3.0 -> 3.1): Banking77 0.605 -> 0.611, AG News 0.790 -> 0.800, emotion 0.447 -> 0.471,
  tweet_topic 0.722 -> 0.740, prompt injection 0.810 -> 0.845, SST-2 0.893 -> 0.899, When2Call 0.287 -> 0.324.
- Results, short tests: yes/no 0.961, choice 0.915, score 0.760 (-1 point), 11 languages 0.984.
  ECE yes/no 0.004, choice 0.016 (3.0.1: 0.022), score 0.032 (3.0.1: 0.021). CPU about 117 ms per text.
- Decision models (system-one-benchmark): SST-2 0.900, TREC 0.390, Banking77 0.603, MASSIVE 0.707 English / 0.575
  other languages. Jev 1.13 and Kev-0.8B are ahead; Laya, GLiNER2.5-Decide and Von are behind outside English.
- Known issues: the near-neighbour lists barely helped Banking77 (goal 0.75 missed). TREC is weak. Messy writing
  costs 1.2 points in English and 2.2 points in other languages.

## [3.0.1] - 2026-11-07

Recalibration of 3.0. Same weights, no retraining, identical accuracy. Only the temperatures change.

- Fixed: the 3.0 calibration was fitted on soft targets. Every temperature was above 1 and the model was
  under-confident: choice ECE went up even on its own validation set (0.032 -> 0.076).
- Added: temperatures that depend on text length L, plus list size K for choice:
  `log T = a + l·log(L/512) [+ k·log K + m·log K·log(L/512)]`.
- Results (bake-off, English): ECE choice 0.169 -> 0.022, score 0.129 -> 0.021, yes/no 0.057 -> 0.010.
  11 languages: choice 0.180 -> 0.020.
- Known issue: synthetic "many" lists with 6-20 options are calibrated worse than in 3.0 (ECE 0.050 -> 0.081).

## [3.0] - 2026-11-07

Long texts, many options, trap texts. Starts from the 2.0 weights.

- Added: 8192-token context. Long examples that do not fit are skipped, not cut.
- Added: 42,870 many-option examples (3 to 386 options, 384 label sets, 8 languages), 4,875 trap texts
  (12 languages), long labelled texts (QuALITY, ContractNLI, Qasper, 5,864 long texts written by GPT-6 Luna).
- Changed: token-budget batches (16,384), gradient checkpointing, lower learning rates, 2 epochs (about 9 h on a T4 GPU).
- Results: v3 validation 0.846 overall. Banking77 0.337 -> 0.605, AG News 0.714 -> 0.790.
- Known issues: calibration bug (fixed in 3.0.1). QuALITY 0.44, Qasper 0.57. The second epoch only overfitted.

## [2.0] - 2026-11-06

New base model (mmBERT-base, chosen after a base-model bake-off), multilingual.

- Added: p_unknown ("information not provided"), 11 languages, French and English dictations.
- Data: 368,863 examples (GPT-6 Luna 200k, Cosmos translated about 81k, Cosmos original languages about 70k,
  dictations about 29k).
- Results vs 1.0: 11 languages 41.8 % -> 98.7 %, yes/no 89.6 % -> 96.5 %, choice 83.2 % -> 92.4 %, CPU 381 -> 150 ms.
- Known issues: 512 tokens max, weak on generic many-label classification (Banking77 0.337).

## [1.0]

First version: ModernBERT-large (395M parameters), 48k examples written by GPT-6 Luna, English only, 381 ms on CPU.

- `[Q]` marker for each question, `[OPT]`/`[LVL]` + first token for each option.
- BCE + Brier loss, temperature calibration, ONNX export for CPU.
