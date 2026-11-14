<!-- languages -->
<p align="center"><a href="README.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <b>Deutsch</b> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>
<!-- /languages -->

<div align="center">

<img src="media/logo.png" width="96" alt="Amada-Logo: ein rosa Haus über den Wolken">

# Amada

**Ein kleines Entscheidungsmodell, das einen Text liest und Ihre Fragen mit Wahrscheinlichkeiten beantwortet**

![Python](media/badges/python.svg)
[![ONNX Runtime](media/badges/onnx.svg)](https://onnxruntime.ai/)
![CPU](media/badges/cpu.svg)
![Sprachen](media/badges/languages.svg)
[![Basismodell](media/badges/base.svg)](https://huggingface.co/jhu-clsp/mmBERT-base)
![Größe](media/badges/size.svg)
![Claude Code](media/badges/claude.svg)
[![Lizenz](media/badges/license.svg)](LICENSE)

<br>

**Große KI-Modelle schreiben lange Antworten, wenn Ihr Code nur eine Entscheidung braucht: ja oder nein, welche Option, wie viel.**

**Amada liefert Ihnen diese Entscheidung auf Ihrer eigenen CPU, in wenigen Dutzend Millisekunden, mit einer Wahrscheinlichkeit, der Sie vertrauen können.**

*Von Liam DB entwickelt — mit Unterstützung von KI.*

[🌐 Website](https://amada.devliam.com/de) · [⬇️ Herunterladen](https://github.com/DevLiamDb/Amada/releases/latest) · [🏠 PinkHouse-App](#pinkhouse) · [📊 Benchmark](https://amada.devliam.com/de/benchmark) · [📜 Änderungsprotokoll](CHANGELOG.md)

</div>

---

<div align="center">

<img src="media/demo.gif" width="760" alt="Amada beantwortet vier Fragen zu einer Kundennachricht im Terminal">

*Echte Ausgaben von Amada 3.1, nicht nachbearbeitet. Auf „Ist der Kunde zufrieden?“ folgt **INFO NOT PROVIDED**: In der Nachricht steht es nicht, deshalb rät Amada nicht.*

</div>

---

> Amada schreibt **keine** Texte. Sie geben dem Modell einen Text und eine oder mehrere Fragen, und es gibt Zahlen zurück, die Ihr Code direkt verwenden kann: die Wahrscheinlichkeit für Ja, einen Anteil für jede Option, einen Wert auf einer Skala und die Wahrscheinlichkeit, dass **der Text dazu einfach keine Auskunft gibt**.

<div align="center">
<table>
<tr>
<td align="center" width="16%">

**🎯 Drei Fragetypen**<br>
ja / nein, eine auswählen,<n>
Wert auf einer Skala

</td>
<td align="center" width="16%">

**🤷 Sagt „Ich weiß es nicht“**<br>
Wenn der Text<br>
keine Antwort gibt, sagt es das,<br>
statt zu raten

</td>
<td align="center" width="16%">

**📏 Kalibriert**<br>
Wenn das Modell 80 % angibt,<n>
liegt es in etwa<br>
80 % der Fälle richtig

</td>
<td align="center" width="16%">

**🏠 100% lokal**<br>
Nur CPU, keine GPU,<br>
kein Internet, kein Konto

</td>
<td align="center" width="16%">

**⚡ Schnell**<br>
~40 ms für eine kurze<br>
Ja-/Nein-Frage<br>
auf einer Laptop-CPU*

</td>
<td align="center" width="16%">

**🌍 12 Sprachen**<br>
Englisch + 11 weitere,<br>
bis zu 8,192 Tokens

</td>
</tr>
</table>
</div>

---

## Warum Amada

Wir haben **Jev 1.14** (TypeSafes geschlossenes Entscheidungsmodell) am 8. November 2026 und Amada mit genau denselben Texten, denselben Fragen und denselben Optionen ausgeführt.

| | Jev 1.14 (kostenpflichtige API) | Amada 4.0 |
|---|:---:|:---:|
| Wo es läuft | TypeSafes Server | **Ihre eigene CPU** |
| Preis | $0.042 pro Million Tokens | **kostenlos** |
| Ihr Text verlässt Ihren Rechner | ja | **nie** |
| Eine kurze Ja-/Nein-Frage | ≈ 245 ms (Internet inbegriffen) | **≈ 40 ms** (×6 schneller)* |
| Sprachanfrage, 60 Intents | **≈ 270 ms** | ≈ 390 ms |
| Prompt-Injection (116 Nachrichten) | 0.733 | **0.845** |
| Leseverständnis, 11 Sprachen (Belebele) | **0.947** | 0.554 |
| Öffentliche Datensätze, bei denen es besser abschneidet | **6 von 7** | 1 von 7 |

\* Medianzeit auf einem Laptop (Intel Core i5-11400H, 4 CPU-Threads, ONNX Runtime), mit 4.0 am 12. November 2026 gemessen: 41 ms für eine Bildschirmtextzeile, 54 ms für eine kurze Notiz. Sie hängt von Ihrem Prozessor, der Textlänge und der Anzahl der Optionen ab: 60 Optionen dauern ~390 ms. Methode: [Methodik](https://amada.devliam.com/methodology.pdf).

Amada ist **nicht** überall besser: Jev ist beim Leseverständnis in jeder Sprache und bei 6 von 7 öffentlichen Datensätzen deutlich genauer. Amada punktet bei kurzen Fragen mit Geschwindigkeit, beim Preis, beim Datenschutz und bei Prompt-Injection. Alle Zahlen, die guten wie die schlechten, finden Sie auf der [Benchmark-Seite](https://amada.devliam.com/de/benchmark).

---

## Wofür es nützlich ist

- **Moderation:** „Ist diese Nachricht eine Beleidigung?“, „Ist das eine Prompt-Injection?“, bevor sie Ihre App oder Ihr LLM erreicht.
- **Sortieren:** E-Mails, Tickets oder Rezensionen mit einer Wahrscheinlichkeit für jede Kategorie an das richtige Team oder die passende Kategorie weiterleiten.
- **Vorprüfung vor einem teuren Schritt:** Stellen Sie zuerst eine kostengünstige Ja-/Nein-Frage und rufen Sie das große Modell nur bei Bedarf auf.
- **Datenschutzsensibler Text:** Notizen und Nachrichten, die den Rechner nicht verlassen dürfen.
- **Bots und Spiele:** Ein Discord-Bot, eine Spielfigur oder eine Hausautomation, die auf Texteingaben reagiert.
- **Kleine Rechner:** Die INT4-Version benötigt beim Laden etwa 1.2 GB RAM, danach etwa 340 MB.

> ⚠️ Verwenden Sie Amada niemals für medizinische, rechtliche, finanzielle, sicherheitsrelevante oder andere wichtige Entscheidungen über echte Menschen. Es ist ein experimentelles Modell, das von einer einzelnen Person entwickelt wurde.

---

<a name="pinkhouse"></a>

## PinkHouse: Amada als Windows-App

PinkHouse führt Amada ohne Python auf Ihrem PC aus: mit einem Fenster für Ihre Fragen, einer lokalen API für Ihre Skripte (`http://127.0.0.1:8787`, mit API-Schlüsseln) und einer Modellverwaltung, die die Amada-Versionen aus diesen Releases herunterlädt und jede einzelne mit SHA-256 überprüft.

Öffnen Sie zur Installation **PowerShell** und fügen Sie Folgendes ein:

```powershell
irm https://raw.githubusercontent.com/DevLiamDb/Amada/main/install.ps1 | iex
```

Das [Skript](install.ps1) lädt die neueste `PinkHouse_Setup_<version>_x64.exe` aus den [PinkHouse-Releases](https://github.com/DevLiamDb/Amada/releases?q=pinkhouse&expanded=true) herunter, überprüft deren SHA-256 und öffnet das Installationsprogramm. Administratorrechte sind nicht erforderlich. Sie können das Installationsprogramm auch selbst aus dem [PinkHouse-1.0.2-Release](https://github.com/DevLiamDb/Amada/releases/tag/pinkhouse-v1.0.2) herunterladen.

> Windows 10 oder 11, 64-Bit (getestet unter Windows 11). Das Installationsprogramm enthält kein Modell: Wählen Sie beim ersten Start eines unter **MODELS** aus (Amada 4.0 INT4 ist die kompakte Version mit 188 MB). PinkHouse läuft noch nicht unter macOS oder Linux.

PinkHouse ist für jede Nutzung kostenlos, zu Hause oder bei der Arbeit, aber es ist keine Open-Source-Software: Es hat eine eigene Lizenz, anders als die MIT-lizenzierten Modelle. Das Installationsprogramm fordert Sie auf, diese zu akzeptieren. Lesen Sie die [Lizenz](https://amada.devliam.com/de/pinkhouse/license), die [Nutzungsbedingungen](https://amada.devliam.com/de/pinkhouse/terms), die [Datenschutzerklärung](https://amada.devliam.com/de/pinkhouse/privacy) und den [Rechtlichen Hinweis](https://amada.devliam.com/de/pinkhouse/legal-notice). Kurz gesagt: keine Telemetrie, Ihre Texte bleiben auf Ihrem PC und die App geht nur online, um Modelle aus diesen Releases herunterzuladen.

---

## Installation

> Anforderungen: **Python 3** und **pip**.

```bash
git clone https://github.com/DevLiamDb/Amada.git
cd Amada
pip install -r requirements.txt
```

Laden Sie anschließend das Modell herunter:

1. Laden Sie `amada-4.0.zip` aus dem [neuesten Release](https://github.com/DevLiamDb/Amada/releases/latest) herunter (oder das kleinere `amada-4.0-int4.zip`, 188 MB, aus demselben Release).
2. Entpacken Sie es in einen `Release/`-Ordner neben `play.py`, sodass Sie `Release/amada-4.0/amada_model.onnx` und `Release/amada-4.0/tokenizer/` erhalten.

> ⚠️ **Belassen Sie den Ordner `tokenizer/` neben `amada_model.onnx`.** Ohne ihn sind die Antworten falsch.

---

## Verwendung

### 1. Im Terminal

```bash
python play.py
```

Fügen Sie einen Text ein, drücken Sie die Eingabetaste in einer leeren Zeile und stellen Sie dann Fragen:

```text
Did Lea eat an apple?                          -> yes / no
Which apple did she eat? | red, green, yellow  -> choice
How hungry is she? #                           -> score (none / low / moderate / high)
How happy is she? # not at all, a bit, very    -> score with your own levels
:new = new text    :q = quit
```

Andere Versionen: `python play.py --version 4.0-int4` (benötigt onnxruntime 1.20+), `python play.py --version 3.1`, `python play.py --version 2.0`...

### 2. Aus Python

```python
from play import Amada, release_model

amada = Amada(release_model("4.0"))
answers, cut = amada.ask(
    "BOOM. Three knocks on my door. Then nothing.",
    [{"type": "noul", "text": "Is it my mother knocking?"},
     {"type": "score", "text": "How scary is it?", "levels": ["none", "low", "moderate", "high"]}],
)
print(answers)   # [{'p_yes': ..., 'p_unknown': ...}, {'probs': {'none': ..., ...}}]
```

### 3. Die drei Fragetypen

| Typ | Ihre Frage | Amada gibt zurück |
|---|---|---|
| **Ja / Nein** (`noul`) | `Did the customer pay by card?` | Wahrscheinlichkeit für Ja sowie die Wahrscheinlichkeit, dass **der Text keine Aussage dazu enthält** |
| **Auswahl** | `What does the customer want? \| a refund, an exchange, ...` | eine Wahrscheinlichkeit pro Option, insgesamt 100 % |
| **Bewertung** | `How urgent is it? #` | eine Wahrscheinlichkeit pro Stufe (keine, niedrig, mittel, hoch oder Ihre eigenen Stufen) |

Amada kennt nur den Text, den Sie eingeben. Kein Internet, kein Gedächtnis, keine Textgenerierung.

---

## Downloads

Jede Version ist ein Release (Tags `v1.0` bis `v4.0`): eine ZIP-Datei mit dem ONNX-Modell und seinem Tokenizer. Die PinkHouse-App hat eigene Releases (Tags `pinkhouse-v…`).

| Version | Basismodell | Maximale Länge | ZIP-Datei | Hinweise |
|---|---|:---:|:---:|---|
| **4.0** (aktuell) | mmBERT-base | 8,192 | 1.16 GB | fehlerhafte Schreibweise, „der Text enthält keine Aussage dazu“, TREC |
| **4.0 INT4** | mmBERT-base | 8,192 | **188 MB** | dasselbe Modell, 4-Bit-Gewichte: 4× weniger RAM, etwa 1 Punkt niedriger bei AG News und Banking77 |
| 3.1 | mmBERT-base | 8,192 | 1.16 GB | ähnliche Labels, etwas besser bei Banking77 und Emotion |
| **3.1 INT4** | mmBERT-base | 8,192 | **188 MB** | dasselbe Modell, 4-Bit-Gewichte: gleiche Genauigkeit, 3× weniger RAM |
| 3.0.1 | mmBERT-base | 8,192 | 1.16 GB | 3.0 neu kalibriert, gleiche Genauigkeit |
| 3.0 | mmBERT-base | 8,192 | 1.16 GB | lange Texte, viele Optionen, Fangfragen-Texte |
| 2.0 | mmBERT-base | 512 | 1.16 GB | mehrsprachig, „der Text enthält keine Aussage dazu“ |
| 1.0 | ModernBERT-large | 512 | 1.49 GB | erste Version, nur Englisch |

Was sich in den einzelnen Versionen geändert hat: [CHANGELOG.md](CHANGELOG.md).

---

## Benchmarks

<div align="center">

<img src="media/dream_corridor.gif" width="600" alt="Die Hotelflurszene der Website mit Amadas Antwort">

</div>

**Unsere eigenen Kurztests** (Englisch: 2,000 Texte · 11 Sprachen: 1,320 Texte):

| Genauigkeit | Ja / nein | Auswahl | Bewertung | Englisch, alle Typen | 11 Sprachen |
|---|:---:|:---:|:---:|:---:|:---:|
| **Amada 4.0** | 0.961 | 0.908 | 0.759 | 0.896 | 0.985 |
| Amada 4.0 INT4 | 0.960 | 0.908 | 0.742 | 0.892 | 0.983 |
| Amada 3.1 | 0.961 | 0.915 | 0.760 | 0.899 | 0.984 |

Kalibrierungsfehler von 4.0 (ECE, niedriger ist besser), bei der Hälfte der englischen Tests, die für die Kalibrierung zurückgehalten wurde: Ja / nein 0.009, Auswahl 0.016, Bewertung 0.048 (4.0 INT4: 0.008, 0.014, 0.031).

**„Der Text sagt es nicht“** (Ja / nein / nicht angegeben, 939 zurückgehaltene Fragen): 4.0 erreicht **0.963** (3.1: 0.917) und **0.954** bei denselben Texten mit Tippfehlern (3.1: 0.889). Diese Texte haben auch bei der Anpassung der Kalibrierung geholfen. Dies ist daher eine Überprüfung, kein unabhängiger Test.

**Öffentliche Datensätze, Zero-Shot** (Amada hat sie beim Training nie gesehen: Es erhält nur die Frage und die Namen der Optionen). Jev 1.14 von uns mit denselben Texten ausgeführt:

| Datensatz | Aufgabe | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|---|:---:|:---:|:---:|:---:|
| SST-2 | Stimmung in Filmkritiken | 0.897 | 0.890 | 0.899 | **0.959** |
| AG News | Nachrichtenthema, 4 Labels | 0.803 | 0.793 | 0.800 | **0.883** |
| Banking77 | Bank-Support-Absicht, 77 Labels | 0.586 | 0.574 | 0.611 | **0.788** |
| emotion | Emotion eines Tweets, 6 Labels | 0.447 | 0.464 | 0.471 | **0.595** |
| tweet_topic | Thema eines Tweets | 0.718 | 0.711 | 0.740 | **0.820** |
| Prompt-Injection | Ist dieser Text ein Angriff auf eine KI? | **0.845** | 0.810 | **0.845** | 0.733 |
| When2Call | Sollte ein KI-Agent ein Tool aufrufen? | 0.344 | 0.340 | 0.324 | **0.733** |

**Öffentliche Tests in 11 Sprachen** (Durchschnitt, dieselben Elemente in jeder Sprache):

| Test | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|:---:|:---:|:---:|:---:|
| Ja / nein (maschinell übersetzt) | 0.841 | 0.837 | 0.839 | **0.882** |
| Leseverständnis (Belebele, 4 Antworten) | 0.554 | 0.559 | 0.568 | **0.947** |
| Absichten (MASSIVE, 60 Optionen) | 0.834 * | 0.829 * | 0.428 | 0.824 |

\* Nicht Zero-Shot: Amada 4.0 hat aus dem Trainingssplit von MASSIVE gelernt (die Testelemente bleiben ungesehen).

**4.0 INT4** wurde am 12. November 2026 mit genau denselben Elementen wie 4.0 ausgeführt (auf CPU statt GPU). Antwort für Antwort verglichen (exakter McNemar-Test) sind die deutlichen Unterschiede AG News (-1.0 Punkt), Banking77 (-1.2), Bewertungen (-1.6) und Emotion (+1.7); die übrigen liegen im Zufallsbereich, einschließlich Prompt-Injection (nur 116 Texte).

**Geschwindigkeit** (Medianzeit für eine Antwort, jeweils eine Anfrage, dieselben Anfragen für alle · Amada auf einem Intel Core i5-11400H, 4 CPU-Threads · Jev über seine API aus Frankreich). 4.0 und 4.0 INT4 wurden am 12. November 2026 gemessen, Jev am 8. November:

| Anfrage | Amada 4.0 | Amada 4.0 INT4 | Jev 1.14 |
|---|:---:|:---:|:---:|
| Eine Zeile Bildschirmtext, ja / nein | 41 ms | **37 ms** | 244 ms |
| Kurze Notiz, ja / nein | 54 ms | **49 ms** | 247 ms |
| Lesetext, 4 Antworten | 161 ms | 159 ms | 264 ms |
| Sprachanfrage, 60 Absichten | 390 ms | 375 ms | **270 ms** |

Im selben Lauf wie INT4 benötigte 4.0 40, 55, 154 und 388 ms: INT4 ist etwa gleich schnell (bei kurzen Fragen etwas schneller, beim Lesen etwas langsamer). Es spart vor allem Speicher: etwa 340 MB RAM nach dem Laden statt 1.4 GB.

**Schwachstellen**, bewusst genannt: TREC (Art der Antwort, die eine Frage erwartet, 0.52 in 4.0, gegenüber 0.39 zuvor), Banking77 (0.59, 2.5 Punkte unter 3.1), Ordinalbewertungen (etwa 76 %) und sehr lange Texte. Fehlerhafte Schreibweise kostet jetzt wenig: zurückgehaltene Ja-/Nein-Texte mit Tippfehlern: 0.960 auf Englisch und 0.967 in 11 Sprachen.

> **Ehrlicher Hinweis:** Unsere Kurztests verwenden Antworten einer starken KI (GPT-6 Luna), nicht von menschlichen Annotatoren, und ihre Texte ähneln den Trainingsdaten. Die öffentlichen Datensätze verwenden menschliche Labels.

---

<details>
<summary><b>🗂️ Dateistruktur</b></summary>
<br>

```
Amada/
├── play.py            ← Terminal-Chat + Python-API ← HIER STARTEN
├── install.ps1        ← installiert PinkHouse, die Windows-App
├── requirements.txt   ← numpy, onnxruntime, transformers
├── Release/           ← entpacken Sie die heruntergeladenen Versionen hier (nicht ins Repository)
│   └── amada-4.0/
│       ├── amada_model.onnx
│       └── tokenizer/  ← neben der ONNX-Datei aufbewahren
├── CHANGELOG.md       ← Änderungen in jeder Version
├── LICENSE            ← MIT
├── NOTICE.md          ← Hinweise zu den Basismodellen (beim Teilen beibehalten)
└── media/             ← Logo, Badges und GIFs (Bilder: nicht MIT, siehe Lizenz)
```

</details>

---

<details>
<summary><b>⚙️ Funktionsweise im Inneren</b></summary>
<br>

```
text + questions ──► tokenizer ──► encoder (mmBERT-base, ONNX, CPU) ──► one head per question type
                                                                     │
                                                                     └── temperatures ──► calibrated probabilities
```

- **Ein Durchlauf für alle Fragen:** Der Text und jede Frage werden gemeinsam gelesen. Jede Frage beginnt mit einer `[Q]`-Markierung, jede Option mit `[OPT]`, jede Stufe mit `[LVL]`.
- **Drei Antwortarten:** Ja / nein (mit „Der Text sagt es nicht“), Auswahl (ein Wert pro Option, zusammen 100 %), Bewertung (eine Wahrscheinlichkeit pro Stufe).
- **Kalibrierung:** Seit 3.0.1 hängen die Temperaturen von der Textlänge und der Anzahl der Optionen ab. Deshalb bedeutet „95 %“ von Amada etwa 95 %.
- **Die Dauer steigt mit der Anzahl der Optionen:** Jede Option wird gelesen. Zwei Optionen dauern ~40 ms, 77 Optionen ~720 ms.

</details>

---

<details>
<summary><b>❓ FAQ</b></summary>
<br>

**Kann ich Amada in einem Unternehmen oder einem kostenpflichtigen Produkt verwenden?**
Ja. Amada steht unter der MIT-Lizenz: Die kommerzielle Nutzung ist erlaubt. Bewahren Sie den Copyright-Vermerk und den Lizenztext bei den Dateien auf.

**Kann ich das Modell feinabstimmen?**
Ja, und Sie dürfen Ihre feinabgestimmte Version auch weitergeben oder verkaufen. Bewahren Sie den MIT-Hinweis (und NOTICE.md) dabei auf.

**Welche Version sollte ich verwenden?**
4.0 für die meisten Anwendungsfälle. 4.0 INT4, wenn Sie einen kleinen Download oder wenig RAM benötigen (bei einigen Klassifizierungsaufgaben etwa 1 Punkt niedriger), oder 3.1, wenn Ihre Aufgabe Banking77 oder Emotion ähnelt. Die älteren Versionen dienen zum Vergleichen.

**Wie viele Optionen kann eine Auswahlfrage haben?**
Zwei oder mehr, ohne festgelegtes Maximum: Text, Frage und Optionen müssen zusammen in 8,192 Tokens passen. 3.0 und spätere Versionen wurden mit Listen von bis zu 386 Optionen trainiert.

**Welche Hardware benötige ich?**
Eine normale CPU. Etwa 9 Sekunden zum Laden und nach dem Laden etwa 1.4 GB RAM (FP32); mit INT4 höchstens etwa 1.2 GB. Keine GPU, nach dem Download kein Internet erforderlich.

**Gibt es eine API oder eine gehostete Version?**
Nein. Amada läuft auf Ihrem eigenen Computer.

**Die Antworten wirken falsch.**
Prüfen Sie, ob sich der Ordner `tokenizer/` neben `amada_model.onnx` befindet.

</details>

---

## Geschichte & Mitwirkende

<details>
<summary><b>📖 Die Website: eine Nacht, 03:00 bis 07:12</b></summary>
<br>

Die [Website](https://amada.devliam.com/de) stellt Amada anhand einer kurzen Geschichte vor: eine Nacht, ein Mädchen, das nicht schlafen kann, ein Park, ein Hotelflur, ein überflutetes Zuhause, Klopfen an einer Tür. In jeder Szene werden ein Tagebuchtext und eine Frage zusammen mit **Amadas echter Antwort** gezeigt, die vorab anhand genau dieser Texte berechnet wurde. Dann wacht sie auf, schaltet ihren Computer ein, und ein 90er-Jahre-Desktop zeigt die Benchmarks. Keine Schreckmomente.

<div align="center">

<img src="media/dream_knock.gif" width="600" alt="Die Klopfszene: Amada antwortet: Ich weiß es nicht">

</div>

</details>

<details>
<summary><b>🙏 Mitwirkende — wer und was Amada möglich gemacht hat</b></summary>
<br>

Amada wurde **mit KI entwickelt, und wir sagen das ganz offen.**

| Wer | Rolle |
|---|---|
| **Liam DB** ([DevLiamDb](https://github.com/DevLiamDb)) | Ersteller. Die Idee, die Ausrichtung, die Entscheidungen, die Trainingsläufe, die Tests. |
| **[Claude Code](https://claude.com/claude-code)** (Anthropic) | Half unter der Leitung von Liam DB beim Schreiben des Codes (Training, Benchmarks, `play.py`, Website). |
| **GPT-6 Luna** | Verfasste einen großen Teil der Trainingsbeispiele und der Referenzantworten für die kurzen Tests. |
| **[mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base)** (Johns Hopkins University, CLSP) | Das Basisnetzwerk von Amada 2.0 und späteren Versionen (MIT). |
| **[ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)** (Answer.AI) | Das Basisnetzwerk von Amada 1.0 (Apache-2.0). |

**Trainiert mit:** öffentlichen Texten (Wikipedia, FineWeb-2, Project Gutenberg, Regierungsberichten, arXiv- und PubMed-Abstracts), öffentlichen gelabelten Datensätzen (QuALITY, ContractNLI, Qasper, CLINC150) und synthetischen Beispielen. Niemals mit den Testdatensätzen der Benchmarks.

**Basiert auf:** [ONNX Runtime](https://onnxruntime.ai/), [Hugging Face Transformers](https://huggingface.co/docs/transformers), [Kaggle](https://www.kaggle.com/) (Training und Benchmarks).

**Finden Sie den Ersteller:** 🌐 [amada.devliam.com](https://amada.devliam.com/de) · 🐙 [GitHub](https://github.com/DevLiamDb)

</details>

---

## Lizenz

**Amada: MIT** (Gewichte, `play.py`, `install.ps1` und der Code dieses Repositorys)

✅ Für alles verwendbar, auch für die kommerzielle Nutzung
✅ Ändern, feinabstimmen und zusammenführen
✅ Die Originalversion oder Ihre geänderten Versionen weitergeben oder verkaufen
📌 Den Copyright-Vermerk ("Copyright (c) 2026 LiamDB") und den Lizenztext bei den Dateien aufbewahren

Die MIT-Lizenz gilt für jede Amada-Version, von 1.0 bis zur neuesten, einschließlich Kopien, die heruntergeladen wurden, als die Gewichte
unter CC BY-NC-ND 4.0 standen. Amada wird ohne Gewährleistung bereitgestellt. Die Hinweise zu mmBERT-base (MIT) und ModernBERT-large (Apache-2.0)
finden Sie in [NOTICE.md](NOTICE.md) und müssen beim Weitergeben der Dateien beibehalten werden. Die vollständigen Bedingungen finden Sie unter [LICENSE](LICENSE).

**Bilder: nicht MIT-lizenziert.** Das Logo und die GIFs in `media/` zeigen die Website und bleiben © 2026 LiamDB, alle Rechte vorbehalten. Sie dürfen sie mit dem Hinweis "Amada by LiamDB" weitergeben, wie es die [Nutzungsbedingungen der Website](https://amada.devliam.com/de/terms) erlauben.

**PinkHouse: eigene Lizenz.** Die PinkHouse-App (die `pinkhouse-v…`-Releases) fällt nicht unter die MIT-Lizenz: Sie ist kostenlos für jede Nutzung, aber quelloffen ist sie nicht, und Sie dürfen sie weder verkaufen noch ändern oder zurückentwickeln. Siehe die [PinkHouse-Lizenz](https://amada.devliam.com/de/pinkhouse/license).

---

<div align="center">

<img src="media/desktop.gif" width="600" alt="Der 90er-Jahre-Desktop der Website mit den Benchmarks">

Erstellt von Liam DB — mit Hilfe von KI. · liamdb.work@gmail.com

</div>
