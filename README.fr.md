<!-- languages -->
<p align="center"><a href="README.md">English</a> · <b>Français</b> · <a href="README.es.md">Español</a> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>
<!-- /languages -->

<div align="center">

<img src="media/logo.png" width="96" alt="Logo d’Amada : une maison rose au-dessus des nuages">

# Amada

**Un petit modèle de décision qui lit un texte et répond à vos questions avec des probabilités**

![Python](media/badges/python.svg)
[![ONNX Runtime](media/badges/onnx.svg)](https://onnxruntime.ai/)
![CPU](media/badges/cpu.svg)
![Langues](media/badges/languages.svg)
[![Modèle de base](media/badges/base.svg)](https://huggingface.co/jhu-clsp/mmBERT-base)
![Taille](media/badges/size.svg)
![Claude Code](media/badges/claude.svg)
[![Licence](media/badges/license.svg)](LICENSE)

<br>

**Les grands modèles d’IA rédigent de longues réponses alors que votre code a seulement besoin d’une décision : oui ou non, quelle option, quelle quantité.**

**Amada vous fournit cette décision sur votre propre CPU, en quelques dizaines de millisecondes, avec une probabilité fiable.**

*Créé par Liam DB — avec l’aide de l’IA.*

[🌐 Site web](https://amada.devliam.com/fr) · [⬇️ Télécharger](https://github.com/DevLiamDb/Amada/releases/latest) · [🏠 Application PinkHouse](#pinkhouse) · [📊 Benchmark](https://amada.devliam.com/fr/benchmark) · [📜 Journal des modifications](CHANGELOG.md)

</div>

---

<div align="center">

<img src="media/demo.gif" width="760" alt="Amada répond à quatre questions sur le message d’un client dans le terminal">

*Résultats réels d’Amada 3.1, sans aucune retouche. « Le client est-il satisfait ? » renvoie **INFORMATION NON FOURNIE** : le message ne le précise pas, alors Amada ne fait pas de supposition.*

</div>

---

> Amada **ne rédige pas** de texte. Vous lui fournissez un texte et une ou plusieurs questions, et il renvoie des nombres que votre code peut utiliser directement : la probabilité d’une réponse affirmative, une part pour chaque option, un niveau sur une échelle et la probabilité que **le texte ne le précise tout simplement pas**.

<div align="center">
<table>
<tr>
<td align="center" width="16%">

**🎯 Trois types de questions**<br>
oui / non, choisir une option,<br>
niveau sur une échelle

</td>
<td align="center" width="16%">

**🤷 Répond « Je ne sais pas »**<br>
Quand le texte ne donne<br>
pas de réponse, il le dit<br>
au lieu de deviner

</td>
<td align="center" width="16%">

**📏 Calibré**<br>
Quand il annonce 80 %,<br>
il a raison environ<br>
80 % du temps

</td>
<td align="center" width="16%">

**🏠 100% local**<br>
CPU uniquement, pas de GPU,<br>
pas d’Internet, pas de compte

</td>
<td align="center" width="16%">

**⚡ Rapide**<br>
~40 ms pour une courte<br>
question oui / non<br>
sur le CPU d’un ordinateur portable*

</td>
<td align="center" width="16%">

**🌍 12 langues**<br>
Anglais + 11 autres,<br>
jusqu’à 8,192 tokens

</td>
</tr>
</table>
</div>

---

## Pourquoi Amada

Nous avons exécuté **Jev 1.14** (le modèle décisionnel fermé de TypeSafe) le 8 novembre 2026, et Amada sur exactement les mêmes textes, les mêmes questions et les mêmes options.

| | Jev 1.14 (API payante) | Amada 4.0 |
|---|:---:|:---:|
| Où il s’exécute | Les serveurs de TypeSafe | **votre propre processeur** |
| Prix | $0.042 par million de jetons | **gratuit** |
| Votre texte quitte votre machine | oui | **jamais** |
| Une courte question oui / non | ≈ 245 ms (internet inclus) | **≈ 40 ms** (×6 plus rapide)* |
| Requête vocale, 60 intentions | **≈ 270 ms** | ≈ 390 ms |
| Injection de prompt (116 messages) | 0.733 | **0.845** |
| Lecture, 11 langues (Belebele) | **0.947** | 0.554 |
| Jeux de données publics où il l’emporte | **6 sur 7** | 1 sur 7 |

\* Temps médian sur un ordinateur portable (Intel Core i5-11400H, 4 threads CPU, ONNX Runtime), mesuré avec 4.0 le 12 novembre 2026 : 41 ms pour une ligne de texte à l’écran, 54 ms pour une courte note. Cela dépend de votre processeur, de la longueur du texte et du nombre d’options : 60 options prennent ~390 ms. Méthode : [méthodologie](https://amada.devliam.com/methodology.pdf).

Amada n’est **pas** meilleur partout : Jev est bien plus précis en lecture, dans toutes les langues, et sur 6 des 7 jeux de données publics. Amada l’emporte en vitesse pour les questions courtes, en prix, en confidentialité et face aux injections de prompt. Tous les chiffres, bons comme mauvais, figurent sur la [page des benchmarks](https://amada.devliam.com/fr/benchmark).

---

## À quoi cela peut servir

- **Modération :** « Ce message est-il une insulte ? », « S’agit-il d’une injection de prompt ? » avant qu’il n’atteigne votre application ou votre LLM.
- **Tri :** acheminer les e-mails, tickets ou avis vers la bonne équipe ou catégorie, avec une probabilité pour chacune.
- **Filtrage avant une étape coûteuse :** poser d’abord une question oui / non peu coûteuse, et appeler le grand modèle uniquement si nécessaire.
- **Textes sensibles sur le plan de la confidentialité :** notes et messages qui ne doivent pas quitter la machine.
- **Bots et jeux :** un bot Discord, un personnage de jeu ou une domotique qui réagit à ce que les gens écrivent.
- **Petites machines :** la version INT4 nécessite environ 1.2 GB de RAM pendant son chargement, puis environ 340 MB.

> ⚠️ N’utilisez jamais Amada pour prendre des décisions médicales, juridiques, financières, de sécurité ou toute autre décision importante concernant des personnes réelles. Il s’agit d’un modèle expérimental créé par une seule personne.

---

<a name="pinkhouse"></a>

## PinkHouse : Amada sous forme d’application Windows

PinkHouse exécute Amada sur votre PC sans Python : une fenêtre pour poser vos questions, une API locale pour vos scripts (`http://127.0.0.1:8787`, avec des clés API) et un gestionnaire de modèles qui télécharge les versions d’Amada depuis ces versions et vérifie chacune d’elles avec SHA-256.

Pour l’installer, ouvrez **PowerShell** et collez :

```powershell
irm https://raw.githubusercontent.com/DevLiamDb/Amada/main/install.ps1 | iex
```

Le [script](install.ps1) télécharge le fichier `PinkHouse_Setup_<version>_x64.exe` le plus récent depuis les [versions de PinkHouse](https://github.com/DevLiamDb/Amada/releases?q=pinkhouse&expanded=true), vérifie son SHA-256 et ouvre le programme d’installation. Aucun droit d’administrateur n’est nécessaire. Vous pouvez également télécharger vous-même le programme d’installation depuis la [version 1.0.2 de PinkHouse](https://github.com/DevLiamDb/Amada/releases/tag/pinkhouse-v1.0.2).

> Windows 10 ou 11, 64 bits (testé sur Windows 11). Le programme d’installation ne contient aucun modèle : la première fois, choisissez-en un dans **MODELS** (Amada 4.0 INT4 est la version légère, 188 MB). PinkHouse ne fonctionne pas encore sur macOS ou Linux.

PinkHouse est gratuit pour tout usage, à la maison ou au travail, mais n’est pas open source : il possède sa propre licence, contrairement aux modèles sous licence MIT. Le programme d’installation vous demande de l’accepter. Lisez la [Licence](https://amada.devliam.com/fr/pinkhouse/license), les [Conditions d’utilisation](https://amada.devliam.com/fr/pinkhouse/terms), la [Politique de confidentialité](https://amada.devliam.com/fr/pinkhouse/privacy) et les [Mentions légales](https://amada.devliam.com/fr/pinkhouse/legal-notice). En bref : aucune télémétrie, vos textes restent sur votre PC et l’application se connecte uniquement à Internet pour télécharger les modèles depuis ces versions.

---

## Installation

> Prérequis : **Python 3** et **pip**.

```bash
git clone https://github.com/DevLiamDb/Amada.git
cd Amada
pip install -r requirements.txt
```

Téléchargez ensuite le modèle :

1. Téléchargez `amada-4.0.zip` depuis la [dernière version](https://github.com/DevLiamDb/Amada/releases/latest) (ou le fichier plus petit `amada-4.0-int4.zip`, 188 MB, depuis la même version).
2. Décompressez-le dans un dossier `Release/` à côté de `play.py`, afin d’obtenir `Release/amada-4.0/amada_model.onnx` et `Release/amada-4.0/tokenizer/`.

> ⚠️ **Conservez le dossier `tokenizer/` à côté de `amada_model.onnx`.** Sans lui, les réponses sont erronées.

---

## Utilisation

### 1. Dans le terminal

```bash
python play.py
```

Collez un texte, appuyez sur Entrée sur une ligne vide, puis posez des questions :

```text
Did Lea eat an apple?                          -> yes / no
Which apple did she eat? | red, green, yellow  -> choice
How hungry is she? #                           -> score (none / low / moderate / high)
How happy is she? # not at all, a bit, very    -> score with your own levels
:new = new text    :q = quit
```

Autres versions : `python play.py --version 4.0-int4` (nécessite onnxruntime 1.20+), `python play.py --version 3.1`, `python play.py --version 2.0`...

### 2. Depuis Python

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

### 3. Les trois types de questions

| Type | Vous demandez | Amada renvoie |
|---|---|---|
| **oui / non** (`noul`) | `Did the customer pay by card?` | la probabilité que la réponse soit oui, ainsi que la probabilité que **le texte ne le précise pas** |
| **choix** | `What does the customer want? \| a refund, an exchange, ...` | une probabilité par option, 100 % au total |
| **score** | `How urgent is it? #` | une probabilité par niveau (aucun, faible, modéré, élevé, ou vos propres niveaux) |

Il ne connaît que le texte que vous lui fournissez. Pas d’accès à Internet, pas de mémoire, pas de génération de texte.

---

## Téléchargements

Chaque version est une release (tags `v1.0` à `v4.0`) : un fichier zip contenant le modèle ONNX et son tokenizer. L’application PinkHouse a ses propres releases (tags `pinkhouse-v…`).

| Version | Modèle de base | Longueur max. | Zip | Remarques |
|---|---|:---:|:---:|---|
| **4.0** (actuelle) | mmBERT-base | 8,192 | 1.16 GB | écriture approximative, « le texte ne le précise pas », TREC |
| **4.0 INT4** | mmBERT-base | 8,192 | **188 MB** | même modèle, poids sur 4 bits : 4× moins de RAM, environ 1 point de moins sur AG News et Banking77 |
| 3.1 | mmBERT-base | 8,192 | 1.16 GB | étiquettes proches, un peu meilleur sur Banking77 et les émotions |
| **3.1 INT4** | mmBERT-base | 8,192 | **188 MB** | même modèle, poids sur 4 bits : même précision, 3× moins de RAM |
| 3.0.1 | mmBERT-base | 8,192 | 1.16 GB | 3.0 recalibré, même précision |
| 3.0 | mmBERT-base | 8,192 | 1.16 GB | textes longs, nombreuses options, textes pièges |
| 2.0 | mmBERT-base | 512 | 1.16 GB | multilingue, « le texte ne le précise pas » |
| 1.0 | ModernBERT-large | 512 | 1.49 GB | première version, anglais uniquement |

Pour connaître les changements apportés à chaque version : [CHANGELOG.md](CHANGELOG.md).

---

## Évaluations comparatives

<div align="center">

<img src="media/dream_corridor.gif" width="600" alt="La scène du couloir de l’hôtel sur le site web, avec la réponse d’Amada">

</div>

**Nos propres tests courts** (anglais : 2,000 textes · 11 langues : 1,320 textes) :

| Précision | Oui / non | Choix | Score | Anglais, tous types | 11 langues |
|---|:---:|:---:|:---:|:---:|:---:|
| **Amada 4.0** | 0.961 | 0.908 | 0.759 | 0.896 | 0.985 |
| Amada 4.0 INT4 | 0.960 | 0.908 | 0.742 | 0.892 | 0.983 |
| Amada 3.1 | 0.961 | 0.915 | 0.760 | 0.899 | 0.984 |

Erreur de calibration de 4.0 (ECE, plus faible est préférable), sur la moitié des tests anglais mise de côté pour la calibration : oui / non 0.009, choix 0.016, score 0.048 (4.0 INT4 : 0.008, 0.014, 0.031).

**« Le texte ne le dit pas »** (oui / non / non indiqué, 939 questions mises de côté) : 4.0 obtient **0.963** (3.1 : 0.917), et **0.954** sur les mêmes textes avec des fautes de frappe (3.1 : 0.889). Ces textes ont aussi contribué à l’ajustement de la calibration ; il s’agit donc d’une vérification, pas d’un test indépendant.

**Jeux de données publics, zéro-shot** (Amada ne les a jamais vus pendant l’entraînement : il ne reçoit que la question et les noms des options). Jev 1.14 exécuté par nos soins sur les mêmes textes :

| Jeu de données | Tâche | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|---|:---:|:---:|:---:|:---:|
| SST-2 | sentiment d’avis sur des films | 0.897 | 0.890 | 0.899 | **0.959** |
| AG News | sujet d’actualité, 4 labels | 0.803 | 0.793 | 0.800 | **0.883** |
| Banking77 | intention d’assistance bancaire, 77 labels | 0.586 | 0.574 | 0.611 | **0.788** |
| emotion | émotion d’un tweet, 6 labels | 0.447 | 0.464 | 0.471 | **0.595** |
| tweet_topic | sujet d’un tweet | 0.718 | 0.711 | 0.740 | **0.820** |
| Injection de prompt | ce texte est-il une attaque contre une IA ? | **0.845** | 0.810 | **0.845** | 0.733 |
| When2Call | un agent IA doit-il appeler un outil ? | 0.344 | 0.340 | 0.324 | **0.733** |

**Tests publics dans 11 langues** (moyenne, mêmes éléments dans chaque langue) :

| Test | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|:---:|:---:|:---:|:---:|
| Oui / non (traduction automatique) | 0.841 | 0.837 | 0.839 | **0.882** |
| Compréhension écrite (Belebele, 4 réponses) | 0.554 | 0.559 | 0.568 | **0.947** |
| Intentions (MASSIVE, 60 options) | 0.834 * | 0.829 * | 0.428 | 0.824 |

\* Pas en zéro-shot : Amada 4.0 a appris à partir de la partition d’entraînement de MASSIVE (les éléments de test restent inconnus).

**4.0 INT4** a été exécuté le 12 novembre 2026 sur exactement les mêmes éléments que 4.0 (sur CPU plutôt que GPU). En comparant les réponses une à une (test exact de McNemar), les différences nettes concernent AG News (-1.0 point), Banking77 (-1.2), les scores (-1.6) et emotion (+1.7) ; les autres différences relèvent du hasard, y compris pour l’injection de prompt (116 textes seulement).

**Vitesse** (temps médian pour une réponse, une requête à la fois, mêmes requêtes pour tous · Amada sur un Intel Core i5-11400H, 4 threads CPU · Jev via son API depuis la France). Les mesures de 4.0 et 4.0 INT4 datent du 12 novembre 2026, celles de Jev du 8 novembre :

| Requête | Amada 4.0 | Amada 4.0 INT4 | Jev 1.14 |
|---|:---:|:---:|:---:|
| Une ligne de texte à l’écran, oui / non | 41 ms | **37 ms** | 244 ms |
| Note courte, oui / non | 54 ms | **49 ms** | 247 ms |
| Passage à lire, 4 réponses | 161 ms | 159 ms | 264 ms |
| Requête vocale, 60 intentions | 390 ms | 375 ms | **270 ms** |

Lors de la même exécution qu’INT4, 4.0 a pris 40, 55, 154 et 388 ms : INT4 est à peu près aussi rapide (un peu plus rapide pour les questions courtes, un peu plus lent en compréhension écrite). Il réduit surtout la mémoire utilisée : environ 340 MB de RAM après chargement, au lieu de 1.4 GB.

**Points faibles**, volontairement précisés : TREC (type de réponse attendu à une question, 0.52 pour 4.0, contre 0.39 auparavant), Banking77 (0.59, 2.5 points de moins que 3.1), les scores ordinaux (environ 76 %) et les textes très longs. Les textes mal rédigés pénalisent désormais peu : oui / non, sur des textes avec fautes de frappe mis de côté, 0.960 en anglais et 0.967 dans 11 langues.

> **Remarque en toute honnêteté :** nos tests courts utilisent des réponses d’une IA puissante (GPT-6 Luna), et non d’annotateurs humains ; leurs textes ressemblent aux données d’entraînement. Les jeux de données publics utilisent des étiquettes humaines.

---

<details>
<summary><b>🗂️ Structure des fichiers</b></summary>
<br>

```
Amada/
├── play.py            ← terminal chat + Python API ← START HERE
├── install.ps1        ← installs PinkHouse, the Windows app
├── requirements.txt   ← numpy, onnxruntime, transformers
├── Release/           ← unzip the downloaded versions here (not in the repository)
│   └── amada-4.0/
│       ├── amada_model.onnx
│       └── tokenizer/  ← keep it next to the ONNX
├── CHANGELOG.md       ← what changed in each version
├── LICENSE            ← MIT
├── NOTICE.md          ← notices of the base models (keep them when sharing)
└── media/             ← logo, badges and GIFs (images: not MIT, see License)
```

</details>

---

<details>
<summary><b>⚙️ Fonctionnement interne</b></summary>
<br>

```
text + questions ──► tokenizer ──► encoder (mmBERT-base, ONNX, CPU) ──► one head per question type
                                                                     │
                                                                     └── temperatures ──► calibrated probabilities
```

- **Un seul passage pour toutes les questions :** le texte et chaque question sont lus ensemble. Chaque question commence par un marqueur `[Q]`, chaque option par `[OPT]`, chaque niveau par `[LVL]`.
- **Trois types de réponse :** oui / non (avec « le texte ne le dit pas »), choix (un score par option, ramené à 100 % au total), score (une probabilité par niveau).
- **Calibration :** depuis 3.0.1, les températures dépendent de la longueur du texte et du nombre d’options. C’est pourquoi un « 95 % » donné par Amada signifie environ 95 %.
- **Le temps augmente avec le nombre d’options :** chaque option est lue. Deux options prennent ~40 ms, 77 options ~720 ms.

</details>

---

<details>
<summary><b>❓ FAQ</b></summary>
<br>

**Puis-je utiliser Amada dans une entreprise ou un produit payant ?**
Oui. Amada est sous licence MIT : l’utilisation commerciale est autorisée. Conservez la mention de copyright et le texte de la licence avec les fichiers.

**Puis-je l’affiner ?**
Oui, et vous pouvez aussi partager ou vendre votre version affinée. Conservez la mention MIT (et NOTICE.md) avec celle-ci.

**Quelle version dois-je utiliser ?**
4.0 pour la plupart des usages. 4.0 INT4 si vous avez besoin d’un téléchargement léger ou de peu de RAM (environ 1 point de moins sur certaines tâches de classification), ou 3.1 si votre tâche ressemble à Banking77 ou à la détection des émotions. Les versions plus anciennes sont là pour comparaison.

**Combien d’options une question à choix peut-elle comporter ?**
Deux ou plus, sans maximum fixe : le texte, la question et les options doivent tenir ensemble dans 8,192 tokens. Les versions 3.0 et ultérieures ont été entraînées avec des listes allant jusqu’à 386 options.

**Quel matériel me faut-il ?**
Un processeur ordinaire. Environ 9 secondes pour le chargement et environ 1.4 GB de RAM après le chargement (FP32) ; environ 1.2 GB au maximum avec INT4. Pas de GPU, pas d’internet une fois le téléchargement effectué.

**Existe-t-il une API ou une version hébergée ?**
Non. Amada fonctionne sur votre propre ordinateur.

**Les réponses semblent incorrectes.**
Vérifiez que le dossier `tokenizer/` se trouve à côté de `amada_model.onnx`.

</details>

---

## Histoire et crédits

<details>
<summary><b>📖 Le site web : une nuit, de 03:00 à 07:12</b></summary>
<br>

Le [site web](https://amada.devliam.com/fr) présente Amada à travers une courte histoire : une nuit, une fille qui n’arrive pas à dormir, un parc, le couloir d’un hôtel, une maison inondée, des coups frappés à une porte. Dans chaque scène, un texte de journal intime et une question sont présentés avec **la véritable réponse d’Amada**, calculée à l’avance à partir de ces textes précis. Puis elle se réveille, allume son ordinateur et un bureau des années 90 affiche les benchmarks. Pas de jumpscares.

<div align="center">

<img src="media/dream_knock.gif" width="600" alt="La scène des coups frappés : Amada répond qu’elle ne sait pas">

</div>

</details>

<details>
<summary><b>🙏 Crédits — qui et quoi ont permis de créer Amada</b></summary>
<br>

Amada a été **créé avec l’IA, et nous le disons clairement.**

| Qui | Rôle |
|---|---|
| **Liam DB** ([DevLiamDb](https://github.com/DevLiamDb)) | Créateur. L’idée, l’orientation, les décisions, les entraînements et les tests. |
| **[Claude Code](https://claude.com/claude-code)** (Anthropic) | A contribué à écrire le code (entraînement, benchmarks, `play.py`, site web) sous la direction de Liam DB. |
| **GPT-6 Luna** | A rédigé une grande partie des exemples d’entraînement et des réponses de référence des tests courts. |
| **[mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base)** (Johns Hopkins University, CLSP) | Le réseau de base d’Amada 2.0 et des versions ultérieures (MIT). |
| **[ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)** (Answer.AI) | Le réseau de base d’Amada 1.0 (Apache-2.0). |

**Entraîné sur :** des textes publics (Wikipedia, FineWeb-2, Project Gutenberg, rapports gouvernementaux, résumés d’articles d’arXiv et de PubMed), des jeux de données publics annotés (QuALITY, ContractNLI, Qasper, CLINC150) et des exemples synthétiques. Jamais sur les jeux de test des benchmarks.

**Construit avec :** [ONNX Runtime](https://onnxruntime.ai/), [Hugging Face Transformers](https://huggingface.co/docs/transformers), [Kaggle](https://www.kaggle.com/) (entraînement et benchmarks).

**Retrouvez le créateur :** 🌐 [amada.devliam.com](https://amada.devliam.com/fr) · 🐙 [GitHub](https://github.com/DevLiamDb)

</details>

---

## Licence

**Amada : MIT** (poids, `play.py`, `install.ps1` et code de ce dépôt)

✅ Utilisez-le pour tout usage, y compris commercial
✅ Modifiez-le, affinez-le, fusionnez-le
✅ Partagez ou vendez la version originale ou vos versions modifiées
📌 Conservez la mention de copyright (« Copyright (c) 2026 LiamDB ») et le texte de la licence avec les fichiers

La licence MIT s’applique à toutes les versions d’Amada, de 1.0 à la plus récente, y compris aux copies téléchargées lorsque les poids étaient sous CC BY-NC-ND 4.0. Amada est fourni sans garantie. Les mentions de mmBERT-base (MIT) et de ModernBERT-large (Apache-2.0) figurent dans [NOTICE.md](NOTICE.md) et doivent être conservées lorsque vous partagez les fichiers. Consultez [LICENSE](LICENSE) pour connaître l’intégralité des conditions.

**Images : pas sous licence MIT.** Le logo et les GIF dans `media/` représentent le site web et restent © 2026 LiamDB, tous droits réservés. Vous pouvez les partager en indiquant le crédit « Amada by LiamDB », comme le permettent les [conditions du site web](https://amada.devliam.com/fr/terms).

**PinkHouse : sa propre licence.** L’application PinkHouse (les versions `pinkhouse-v…`) n’est pas couverte par la licence MIT : son utilisation est gratuite quel qu’en soit l’usage, mais son code source est fermé, et vous ne pouvez ni la vendre, ni la modifier, ni la rétroconcevoir. Consultez la [licence PinkHouse](https://amada.devliam.com/fr/pinkhouse/license).

---

<div align="center">

<img src="media/desktop.gif" width="600" alt="Le bureau des années 90 du site web avec les benchmarks">

Créé par Liam DB — avec l’aide de l’IA. · liamdb.work@gmail.com

</div>
