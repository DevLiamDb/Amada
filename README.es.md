<!-- languages -->
<p align="center"><a href="README.md">English</a> · <a href="README.fr.md">Français</a> · <b>Español</b> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>
<!-- /languages -->

<div align="center">

<img src="media/logo.png" width="96" alt="Logo de Amada: una casa rosa sobre las nubes">

# Amada

**Un pequeño modelo de decisión que lee un texto y responde a sus preguntas con probabilidades**

![Python](media/badges/python.svg)
[![ONNX Runtime](media/badges/onnx.svg)](https://onnxruntime.ai/)
![CPU](media/badges/cpu.svg)
![Idiomas](media/badges/languages.svg)
[![Modelo base](media/badges/base.svg)](https://huggingface.co/jhu-clsp/mmBERT-base)
![Tamaño](media/badges/size.svg)
![Claude Code](media/badges/claude.svg)
[![Licencia](media/badges/license.svg)](LICENSE)

<br>

**Los grandes modelos de IA escriben respuestas largas cuando su código solo necesita una decisión: sí o no, qué opción, cuánto.**

**Amada le ofrece esa decisión en su propia CPU, en decenas de milisegundos, con una probabilidad en la que puede confiar.**

*Creado por Liam DB — con ayuda de la IA.*

[🌐 Sitio web](https://amada.devliam.com/es) · [⬇️ Descargar](https://github.com/DevLiamDb/Amada/releases/latest) · [🏠 Aplicación PinkHouse](#pinkhouse) · [📊 Comparativa](https://amada.devliam.com/es/benchmark) · [📜 Registro de cambios](CHANGELOG.md)

</div>

---

<div align="center">

<img src="media/demo.gif" width="760" alt="Amada responde en la terminal a cuatro preguntas sobre el mensaje de un cliente">

*Resultados reales de Amada 3.1, sin retoques. «¿Está contento el cliente?» obtiene **INFO NOT PROVIDED**: el mensaje no lo dice, así que Amada no lo adivina.*

</div>

---

> Amada **no** escribe texto. Usted le da un texto y una o más preguntas, y devuelve números que su código puede usar directamente: la probabilidad de que la respuesta sea sí, una proporción para cada opción, un nivel en una escala y la probabilidad de que **el texto simplemente no lo diga**.

<div align="center">
<table>
<tr>
<td align="center" width="16%">

**🎯 Tres tipos de preguntas**<br>
sí / no, elegir una opción,<br>
nivel en una escala

</td>
<td align="center" width="16%">

**🤷 Dice «No lo sé»**<br>
Cuando el texto no da<br>una respuesta, lo indica<br>
en lugar de adivinar

</td>
<td align="center" width="16%">

**📏 Calibrado**<br>
Cuando indica 80 %,<br>
acierta aproximadamente<br>
el 80 % de las veces

</td>
<td align="center" width="16%">

**🏠 100% local**<br>
Solo CPU, sin GPU,<br>
sin internet ni cuenta

</td>
<td align="center" width="16%">

**⚡ Rápido**<br>
~40 ms para una pregunta<br>corta de sí / no<br>
en una CPU de portátil*

</td>
<td align="center" width="16%">

**🌍 12 idiomas**<br>
Inglés + 11 más,<br>
hasta 8,192 tokens

</td>
</tr>
</table>
</div>

---

## Por qué Amada

El 8 de noviembre de 2026, ejecutamos **Jev 1.14** (el modelo de decisión cerrado de TypeSafe) y Amada con exactamente los mismos textos, las mismas preguntas y las mismas opciones.

| | Jev 1.14 (API de pago) | Amada 4.0 |
|---|:---:|:---:|
| Dónde se ejecuta | Servidores de TypeSafe | **su propia CPU** |
| Precio | $0.042 por millón de tokens | **gratis** |
| Su texto sale de su equipo | sí | **nunca** |
| Una pregunta corta de sí / no | ≈ 245 ms (incluye internet) | **≈ 40 ms** (×6 más rápido)* |
| Solicitud de voz, 60 intenciones | **≈ 270 ms** | ≈ 390 ms |
| Inyección de prompts (116 mensajes) | 0.733 | **0.845** |
| Comprensión lectora, 11 idiomas (Belebele) | **0.947** | 0.554 |
| Conjuntos de datos públicos en los que gana | **6 de 7** | 1 de 7 |

\* Tiempo mediano en un portátil (Intel Core i5-11400H, 4 hilos de CPU, ONNX Runtime), medido con 4.0 el 12 de noviembre de 2026: 41 ms para una línea de texto en pantalla, 54 ms para una nota breve. Depende de su procesador, de la longitud del texto y del número de opciones: 60 opciones tardan ~390 ms. Método: [metodología](https://amada.devliam.com/methodology.pdf).

Amada **no** es mejor en todo: Jev es mucho más preciso en comprensión lectora, en todos los idiomas y en 6 de 7 conjuntos de datos públicos. Amada gana en velocidad para preguntas breves, precio, privacidad e inyección de prompts. Todas las cifras, tanto las buenas como las malas, están en la [página de evaluación comparativa](https://amada.devliam.com/es/benchmark).

---

## Para qué sirve

- **Moderación:** «¿Es este mensaje un insulto?», «¿Es esto una inyección de prompts?» antes de que llegue a su aplicación o a su LLM.
- **Clasificación:** dirija correos, tickets o reseñas al equipo o la categoría adecuados, con una probabilidad para cada uno.
- **Filtrado antes de un paso costoso:** haga primero una pregunta sencilla de sí / no y recurra al modelo grande solo cuando sea necesario.
- **Textos sensibles para la privacidad:** notas y mensajes que no deben salir del equipo.
- **Bots y juegos:** un bot de Discord, un personaje de videojuego o un sistema de domótica que responde a lo que escriben las personas.
- **Equipos pequeños:** la versión INT4 necesita alrededor de 1.2 GB de RAM mientras se carga y luego alrededor de 340 MB.

> ⚠️ Nunca use Amada para tomar decisiones médicas, legales, financieras, de seguridad u otras decisiones importantes sobre personas reales. Es un modelo experimental creado por una sola persona.

---

<a name="pinkhouse"></a>

## PinkHouse: Amada como aplicación para Windows

PinkHouse ejecuta Amada en su PC sin Python: una ventana para hacer sus preguntas, una API local para sus scripts (`http://127.0.0.1:8787`, con claves de API) y un gestor de modelos que descarga las versiones de Amada de estas publicaciones y verifica cada una con SHA-256.

Para instalarla, abra **PowerShell** y pegue:

```powershell
irm https://raw.githubusercontent.com/DevLiamDb/Amada/main/install.ps1 | iex
```

El [script](install.ps1) descarga el archivo más reciente `PinkHouse_Setup_<version>_x64.exe` de las [publicaciones de PinkHouse](https://github.com/DevLiamDb/Amada/releases?q=pinkhouse&expanded=true), verifica su SHA-256 y abre el instalador. No se necesitan derechos de administrador. También puede descargar el instalador por su cuenta desde la [publicación de PinkHouse 1.0.2](https://github.com/DevLiamDb/Amada/releases/tag/pinkhouse-v1.0.2).

> Windows 10 u 11, 64 bits (probado en Windows 11). El instalador no incluye ningún modelo: la primera vez, elija uno en **MODELS** (Amada 4.0 INT4 es la versión ligera, 188 MB). PinkHouse aún no funciona en macOS ni Linux.

PinkHouse es gratis para cualquier uso, en casa o en el trabajo, pero no es de código abierto: tiene su propia licencia, a diferencia de los modelos con licencia MIT. El instalador le pide que la acepte. Lea la [Licencia](https://amada.devliam.com/es/pinkhouse/license), los [Términos de uso](https://amada.devliam.com/es/pinkhouse/terms), la [Política de privacidad](https://amada.devliam.com/es/pinkhouse/privacy) y el [Aviso legal](https://amada.devliam.com/es/pinkhouse/legal-notice). En resumen: no hay telemetría, sus textos permanecen en su PC y la aplicación solo se conecta a internet para descargar modelos de estas publicaciones.

---

## Instalación

> Requisitos: **Python 3** y **pip**.

```bash
git clone https://github.com/DevLiamDb/Amada.git
cd Amada
pip install -r requirements.txt
```

Después, obtenga el modelo:

1. Descargue `amada-4.0.zip` de la [última versión](https://github.com/DevLiamDb/Amada/releases/latest) (o el archivo más pequeño `amada-4.0-int4.zip`, de 188 MB, de esa misma versión).
2. Descomprímalo en una carpeta `Release/` junto a `play.py`, de modo que obtenga `Release/amada-4.0/amada_model.onnx` y `Release/amada-4.0/tokenizer/`.

> ⚠️ **Mantenga la carpeta `tokenizer/` junto a `amada_model.onnx`.** Sin ella, las respuestas serán incorrectas.

---

## Uso

### 1. En el terminal

```bash
python play.py
```

Pegue un texto, pulse Enter en una línea vacía y, después, haga preguntas:

```text
Did Lea eat an apple?                          -> yes / no
Which apple did she eat? | red, green, yellow  -> choice
How hungry is she? #                           -> score (none / low / moderate / high)
How happy is she? # not at all, a bit, very    -> score with your own levels
:new = new text    :q = quit
```

Otras versiones: `python play.py --version 4.0-int4` (requiere onnxruntime 1.20+), `python play.py --version 3.1`, `python play.py --version 2.0`...

### 2. Desde Python

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

### 3. Los tres tipos de pregunta

| Tipo | Usted pregunta | Amada devuelve |
|---|---|---|
| **sí / no** (`noul`) | `Did the customer pay by card?` | probabilidad de que sí, más la probabilidad de que **el texto no lo indique** |
| **opción** | `What does the customer want? \| a refund, an exchange, ...` | una probabilidad por opción, 100 % en total |
| **puntuación** | `How urgent is it? #` | una probabilidad por nivel (ninguno, bajo, moderado, alto o sus propios niveles) |

Solo conoce el texto que usted le proporciona. Sin internet, sin memoria, sin generación de texto.

---

## Descargas

Cada versión es una publicación (etiquetas `v1.0` a `v4.0`): un archivo zip con el modelo ONNX y su tokenizador. La aplicación PinkHouse tiene sus propias publicaciones (etiquetas `pinkhouse-v…`).

| Versión | Modelo base | Longitud máx. | Zip | Notas |
|---|---|:---:|:---:|---|
| **4.0** (actual) | mmBERT-base | 8,192 | 1.16 GB | escritura desordenada, «el texto no lo indica», TREC |
| **4.0 INT4** | mmBERT-base | 8,192 | **188 MB** | mismo modelo, pesos de 4 bits: 4× menos RAM, aproximadamente 1 punto menos en AG News y Banking77 |
| 3.1 | mmBERT-base | 8,192 | 1.16 GB | etiquetas de vecinos cercanos, algo mejor en Banking77 y emociones |
| **3.1 INT4** | mmBERT-base | 8,192 | **188 MB** | mismo modelo, pesos de 4 bits: misma precisión, 3× menos RAM |
| 3.0.1 | mmBERT-base | 8,192 | 1.16 GB | 3.0 recalibrada, misma precisión |
| 3.0 | mmBERT-base | 8,192 | 1.16 GB | textos largos, muchas opciones, textos trampa |
| 2.0 | mmBERT-base | 512 | 1.16 GB | multilingüe, «el texto no lo indica» |
| 1.0 | ModernBERT-large | 512 | 1.49 GB | primera versión, solo en inglés |

Qué cambió en cada versión: [CHANGELOG.md](CHANGELOG.md).

---

## Puntos de referencia

<div align="center">

<img src="media/dream_corridor.gif" width="600" alt="La escena del pasillo del hotel en el sitio web, con la respuesta de Amada">

</div>

**Nuestras propias pruebas breves** (inglés: 2,000 textos · 11 idiomas: 1,320 textos):

| Exactitud | Sí / no | Opción | Puntuación | Inglés, todos los tipos | 11 idiomas |
|---|:---:|:---:|:---:|:---:|:---:|
| **Amada 4.0** | 0.961 | 0.908 | 0.759 | 0.896 | 0.985 |
| Amada 4.0 INT4 | 0.960 | 0.908 | 0.742 | 0.892 | 0.983 |
| Amada 3.1 | 0.961 | 0.915 | 0.760 | 0.899 | 0.984 |

Error de calibración de 4.0 (ECE, cuanto menor, mejor), en la mitad de las pruebas en inglés reservada para la calibración: sí / no 0.009, opción 0.016, puntuación 0.048 (4.0 INT4: 0.008, 0.014, 0.031).

**«El texto no lo dice»** (sí / no / no se indica, 939 preguntas reservadas): 4.0 obtiene **0.963** (3.1: 0.917), y **0.954** en los mismos textos con errores tipográficos (3.1: 0.889). Estos textos también ayudaron a ajustar la calibración, así que esto es una comprobación, no una prueba independiente.

**Conjuntos de datos públicos, zero-shot** (Amada nunca los vio durante el entrenamiento: solo recibe la pregunta y los nombres de las opciones). Jev 1.14 ejecutado por nosotros con los mismos textos:

| Conjunto de datos | Tarea | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|---|:---:|:---:|:---:|:---:|
| SST-2 | sentimiento de reseñas de películas | 0.897 | 0.890 | 0.899 | **0.959** |
| AG News | tema de noticias, 4 etiquetas | 0.803 | 0.793 | 0.800 | **0.883** |
| Banking77 | intención de asistencia bancaria, 77 etiquetas | 0.586 | 0.574 | 0.611 | **0.788** |
| emotion | emoción de un tuit, 6 etiquetas | 0.447 | 0.464 | 0.471 | **0.595** |
| tweet_topic | tema de un tuit | 0.718 | 0.711 | 0.740 | **0.820** |
| Inyección de prompts | ¿este texto es un ataque contra una IA? | **0.845** | 0.810 | **0.845** | 0.733 |
| When2Call | ¿debería un agente de IA llamar a una herramienta? | 0.344 | 0.340 | 0.324 | **0.733** |

**Pruebas públicas en 11 idiomas** (promedio, los mismos elementos en cada idioma):

| Prueba | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|:---:|:---:|:---:|:---:|
| Sí / no (traducido automáticamente) | 0.841 | 0.837 | 0.839 | **0.882** |
| Comprensión lectora (Belebele, 4 respuestas) | 0.554 | 0.559 | 0.568 | **0.947** |
| Intenciones (MASSIVE, 60 opciones) | 0.834 * | 0.829 * | 0.428 | 0.824 |

\* No es zero-shot: Amada 4.0 aprendió de la partición de entrenamiento de MASSIVE (los elementos de prueba no se vieron).

**4.0 INT4** se ejecutó el 12 de noviembre de 2026 con exactamente los mismos elementos que 4.0 (en CPU en lugar de GPU). Al comparar respuesta por respuesta (prueba exacta de McNemar), las diferencias claras son AG News (-1.0 punto), Banking77 (-1.2), puntuaciones (-1.6) y emotion (+1.7); las demás están dentro de lo esperable por azar, incluida la inyección de prompts (solo 116 textos).

**Velocidad** (tiempo mediano para una respuesta, una solicitud a la vez, las mismas solicitudes para todos · Amada en un Intel Core i5-11400H, 4 hilos de CPU · Jev a través de su API desde Francia). 4.0 y 4.0 INT4 se midieron el 12 de noviembre de 2026, Jev el 8 de noviembre:

| Solicitud | Amada 4.0 | Amada 4.0 INT4 | Jev 1.14 |
|---|:---:|:---:|:---:|
| Una línea de texto en pantalla, sí / no | 41 ms | **37 ms** | 244 ms |
| Nota breve, sí / no | 54 ms | **49 ms** | 247 ms |
| Pasaje de lectura, 4 respuestas | 161 ms | 159 ms | 264 ms |
| Solicitud de voz, 60 intenciones | 390 ms | 375 ms | **270 ms** |

En la misma ejecución que INT4, 4.0 tardó 40, 55, 154 y 388 ms: INT4 es prácticamente igual de rápido (un poco más rápido con preguntas breves, un poco más lento en lectura). Principalmente ahorra memoria: unos 340 MB de RAM después de cargar, en lugar de 1.4 GB.

**Puntos débiles**, nombrados a propósito: TREC (tipo de respuesta que espera una pregunta, 0.52 en 4.0, frente a 0.39), Banking77 (0.59, 2.5 puntos por debajo de 3.1), puntuaciones ordinales (alrededor del 76 %) y textos muy largos. La escritura descuidada ahora afecta poco: sí / no reservado con errores tipográficos 0.960 en inglés y 0.967 en 11 idiomas.

> **Nota honesta:** nuestras pruebas breves usan respuestas de una IA potente (GPT-6 Luna), no de anotadores humanos, y sus textos se parecen a los datos de entrenamiento. Los conjuntos de datos públicos usan etiquetas humanas.

---

<details>
<summary><b>🗂️ Estructura de archivos</b></summary>
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
<summary><b>⚙️ Cómo funciona internamente</b></summary>
<br>

```
text + questions ──► tokenizer ──► encoder (mmBERT-base, ONNX, CPU) ──► one head per question type
                                                                     │
                                                                     └── temperatures ──► calibrated probabilities
```

- **Una pasada para todas las preguntas:** el texto y cada pregunta se leen juntos. Cada pregunta empieza con un marcador `[Q]`, cada opción con `[OPT]` y cada nivel con `[LVL]`.
- **Tres tipos de respuesta:** sí / no (con «el texto no lo dice»), opción (una puntuación por opción, repartida hasta sumar 100 %) y puntuación (una probabilidad por nivel).
- **Calibración:** desde 3.0.1, las temperaturas dependen de la longitud del texto y del número de opciones. Por eso, un «95 %» de Amada significa aproximadamente 95 %.
- **El tiempo aumenta con las opciones:** se lee cada opción. Dos opciones tardan ~40 ms; 77 opciones, ~720 ms.

</details>

---

<details>
<summary><b>❓ Preguntas frecuentes</b></summary>
<br>

**¿Puedo usar Amada en una empresa o en un producto de pago?**
Sí. Amada cuenta con licencia MIT: se permite el uso comercial. Conserve la línea de derechos de autor y el texto de la licencia junto con los archivos.

**¿Puedo ajustarlo con fine-tuning?**
Sí, y también puede compartir o vender su versión ajustada. Conserve el aviso de MIT (y NOTICE.md) junto con ella.

**¿Qué versión debería usar?**
4.0 para la mayoría de los usos. 4.0 INT4 si necesita una descarga pequeña o poca RAM (aproximadamente 1 punto menos en algunas tareas de clasificación), o 3.1 si su tarea se parece a Banking77 o a la clasificación de emociones. Las versiones anteriores están disponibles para comparar.

**¿Cuántas opciones puede tener una pregunta de elección?**
Dos o más, sin un máximo fijo: el texto, la pregunta y las opciones deben caber juntas en 8,192 tokens. 3.0 y las versiones posteriores se entrenaron con listas de hasta 386 opciones.

**¿Qué hardware necesito?**
Una CPU normal. Unos 9 segundos para cargar y aproximadamente 1.4 GB de RAM después de la carga (FP32); como máximo, unos 1.2 GB con INT4. Sin GPU ni conexión a internet una vez descargado.

**¿Hay una API o una versión alojada?**
No. Amada se ejecuta en su propio equipo.

**Las respuestas parecen incorrectas.**
Compruebe que la carpeta `tokenizer/` esté junto a `amada_model.onnx`.

</details>

---

## Historia y créditos

<details>
<summary><b>📖 El sitio web: una noche, de 03:00 a 07:12</b></summary>
<br>

El [sitio web](https://amada.devliam.com/es) presenta Amada a través de una historia breve: una noche, una chica que no puede dormir, un parque, el pasillo de un hotel, una casa inundada, golpes en una puerta. En cada escena se muestran un texto de diario y una pregunta junto con **la respuesta real de Amada**, calculada de antemano a partir de esos textos exactos. Luego se despierta, enciende el ordenador y un escritorio de los 90 muestra los benchmarks. Sin sobresaltos.

<div align="center">

<img src="media/dream_knock.gif" width="600" alt="La escena de los golpes: Amada responde que no lo sabe">

</div>

</details>

<details>
<summary><b>🙏 Créditos: quién y qué hizo posible Amada</b></summary>
<br>

Amada **se creó con IA, y lo decimos claramente.**

| Quién | Función |
|---|---|
| **Liam DB** ([DevLiamDb](https://github.com/DevLiamDb)) | Creador. La idea, la dirección, las decisiones, las sesiones de entrenamiento y las pruebas. |
| **[Claude Code](https://claude.com/claude-code)** (Anthropic) | Ayudó a escribir el código (entrenamiento, benchmarks, `play.py`, sitio web) bajo la dirección de Liam DB. |
| **GPT-6 Luna** | Escribió gran parte de los ejemplos de entrenamiento y las respuestas de referencia de las pruebas breves. |
| **[mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base)** (Johns Hopkins University, CLSP) | La red base de Amada 2.0 y versiones posteriores (MIT). |
| **[ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)** (Answer.AI) | La red base de Amada 1.0 (Apache-2.0). |

**Entrenado con:** textos públicos (Wikipedia, FineWeb-2, Project Gutenberg, informes gubernamentales y resúmenes de arXiv y PubMed), conjuntos de datos públicos etiquetados (QuALITY, ContractNLI, Qasper, CLINC150) y ejemplos sintéticos. Nunca con los conjuntos de prueba de los benchmarks.

**Desarrollado sobre:** [ONNX Runtime](https://onnxruntime.ai/), [Hugging Face Transformers](https://huggingface.co/docs/transformers), [Kaggle](https://www.kaggle.com/) (entrenamiento y benchmarks).

**Encuentre al creador:** 🌐 [amada.devliam.com](https://amada.devliam.com/es) · 🐙 [GitHub](https://github.com/DevLiamDb)

</details>

---

## Licencia

**Amada: MIT** (pesos, `play.py`, `install.ps1` y el código de este repositorio)

✅ Úselo para cualquier propósito, incluido el uso comercial
✅ Modifíquelo, ajústelo con fine-tuning, combínelo
✅ Comparta o venda la versión original o sus versiones modificadas
📌 Conserve la línea de derechos de autor ("Copyright (c) 2026 LiamDB") y el texto de la licencia junto con los archivos

La licencia MIT se aplica a todas las versiones de Amada, de la 1.0 a la más reciente, incluidas las copias descargadas cuando los pesos estaban bajo CC BY-NC-ND 4.0. Amada se proporciona sin garantía. Los avisos de mmBERT-base (MIT) y ModernBERT-large (Apache-2.0) están en [NOTICE.md](NOTICE.md) y deben conservarse al compartir los archivos. Consulte [LICENSE](LICENSE) para ver los términos completos.

**Imágenes: no están bajo MIT.** El logotipo y los GIF de `media/` muestran el sitio web y siguen siendo © 2026 LiamDB, todos los derechos reservados. Puede compartirlos con el crédito "Amada by LiamDB", tal como permiten los [términos del sitio web](https://amada.devliam.com/es/terms).

**PinkHouse: tiene su propia licencia.** La aplicación PinkHouse (las versiones `pinkhouse-v…`) no está cubierta por la licencia MIT: es gratuita para cualquier uso, pero su código fuente es cerrado, y no puede venderla, modificarla ni aplicar ingeniería inversa. Consulte la [Licencia de PinkHouse](https://amada.devliam.com/es/pinkhouse/license).

---

<div align="center">

<img src="media/desktop.gif" width="600" alt="El escritorio de los 90 del sitio web con los benchmarks">

Creado por Liam DB — con la ayuda de la IA. · liamdb.work@gmail.com

</div>
