<!-- languages -->
<p align="center"><a href="README.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <b>中文</b></p>
<!-- /languages -->

<div align="center">

<img src="media/logo.png" width="96" alt="Amada 标志：云朵上方的一栋粉色房子">

# Amada

**一款小型决策模型，可读取文本并以概率回答您的问题**

![Python](media/badges/python.svg)
[![ONNX Runtime](media/badges/onnx.svg)](https://onnxruntime.ai/)
![CPU](media/badges/cpu.svg)
![Languages](media/badges/languages.svg)
[![基础模型](media/badges/base.svg)](https://huggingface.co/jhu-clsp/mmBERT-base)
![Size](media/badges/size.svg)
![Claude Code](media/badges/claude.svg)
[![许可证](media/badges/license.svg)](LICENSE)

<br>

**当您的代码只需要一个决定：是或否、选哪项、是多少时，大型 AI 模型却会生成冗长的回答。**

**Amada 可在您自己的 CPU 上，于几十毫秒内给出您可以信赖的概率。**

*由 Liam DB 打造——借助 AI 的帮助。*

[🌐 网站](https://amada.devliam.com/zh) · [⬇️ 下载](https://github.com/DevLiamDb/Amada/releases/latest) · [🏠 PinkHouse 应用](#pinkhouse) · [📊 基准测试](https://amada.devliam.com/zh/benchmark) · [📜 更新日志](CHANGELOG.md)

</div>

---

<div align="center">

<img src="media/demo.gif" width="760" alt="Amada 在终端中回答关于一条客户消息的四个问题">

*Amada 3.1 的真实输出，未经任何修饰。“客户满意吗？”得到 **未提供相关信息**：消息中没有说明，因此 Amada 不会猜测。*

</div>

---

> Amada **不会**编写文本。您提供一段文本和一个或多个问题，它会返回您的代码可直接使用的数字：回答“是”的概率、每个选项所占的比例、量表上的等级，以及**文本中根本没有说明相关信息**的概率。

<div align="center">
<table>
<tr>
<td align="center" width="16%">

**🎯 三类问题**<br>
是 / 否、选择一项、<br>
量表上的等级

</td>
<td align="center" width="16%">

**🤷 会说“我不知道”**<br>
当文本没有给出<br>
答案时，它会如实说明，<br>
而不是猜测

</td>
<td align="center" width="16%">

**📏 概率经过校准**<br>
当它说概率为 80 % 时，<br>
其判断在约 80 % 的情况下<br>
是正确的

</td>
<td align="center" width="16%">

**🏠 100% 本地运行**<br>
仅使用 CPU，无需 GPU、<br>
无需联网，无需账户

</td>
<td align="center" width="16%">

**⚡ 快速**<br>
在笔记本电脑 CPU 上，<br>
回答简短的是 / 否问题<br>
约需 40 ms*

</td>
<td align="center" width="16%">

**🌍 12 种语言**<br>
英语 + 其他 11 种语言，<br>
最多支持 8,192 个 token

</td>
</tr>
</table>
</div>

---

## 为什么选择 Amada

我们于 2026 年 11 月 8 日在完全相同的文本、问题和选项上运行了 **Jev 1.14**（TypeSafe 的闭源决策模型）和 Amada。

| | Jev 1.14（付费 API） | Amada 4.0 |
|---|:---:|:---:|
| 运行位置 | TypeSafe 的服务器 | **您自己的 CPU** |
| 价格 | 每百万个 token $0.042 | **免费** |
| 您的文本是否会离开您的设备 | 会 | **绝不会** |
| 一个简短的是 / 否问题 | ≈ 245 ms（包含网络耗时） | **≈ 40 ms**（快 ×6）* |
| 语音请求，60 个意图 | **≈ 270 ms** | ≈ 390 ms |
| 提示注入（116 条消息） | 0.733 | **0.845** |
| 阅读，11 种语言（Belebele） | **0.947** | 0.554 |
| 胜出的公开数据集 | **7 个中的 6 个** | 7 个中的 1 个 |

\* 一台笔记本电脑上的中位耗时（Intel Core i5-11400H，4 个 CPU 线程，ONNX Runtime），使用 4.0 于 2026 年 11 月 12 日测得：一行屏幕文本耗时 41 ms，一条简短备注耗时 54 ms。实际耗时取决于您的处理器、文本长度和选项数量：60 个选项需要约 390 ms。方法：[方法说明](https://amada.devliam.com/methodology.pdf)。

Amada **并非**在所有方面都更好：Jev 的阅读准确率高出许多，在每种语言以及 7 个公开数据集中的 6 个上都是如此。Amada 在简短问题的速度、价格、隐私和提示注入方面胜出。所有数据，无论好坏，都列在[基准测试页面](https://amada.devliam.com/zh/benchmark)上。

---

## 适用场景

- **内容审核：**在消息到达您的应用或 LLM 之前，判断“这条消息是否含有侮辱内容？”、“这是否是提示注入？”
- **分类：**将电子邮件、工单或评论分发给合适的团队或类别，并为每个类别提供概率。
- **昂贵步骤前的筛选：**先提出一个成本低的是/否问题，仅在需要时才调用大型模型。
- **隐私敏感文本：**不得离开设备的备注和消息。
- **机器人和游戏：**会对用户输入作出反应的 Discord 机器人、游戏角色或家庭自动化系统。
- **小型设备：**INT4 版本加载时需要约 1.2 GB RAM，加载后约需 340 MB。

> ⚠️ 切勿将 Amada 用于涉及真实人物的医疗、法律、财务、安全或其他重要决策。这是由一个人开发的实验性模型。

---

<a name="pinkhouse"></a>

## PinkHouse：作为 Windows 应用的 Amada

PinkHouse 无需 Python 即可在您的 PC 上运行 Amada：一个供您提问的窗口、一个供脚本使用的本地 API（`http://127.0.0.1:8787`，带有 API 密钥），以及一个模型管理器，可从这些版本下载 Amada 的各个版本，并使用 SHA-256 校验每个版本。

要安装，请打开 **PowerShell** 并粘贴：

```powershell
irm https://raw.githubusercontent.com/DevLiamDb/Amada/main/install.ps1 | iex
```

[脚本](install.ps1)会从 [PinkHouse 发布版本](https://github.com/DevLiamDb/Amada/releases?q=pinkhouse&expanded=true)下载最新的 `PinkHouse_Setup_<version>_x64.exe`，校验其 SHA-256 并打开安装程序。无需管理员权限。您也可以从 [PinkHouse 1.0.2 发布版本](https://github.com/DevLiamDb/Amada/releases/tag/pinkhouse-v1.0.2)自行下载安装程序。

> Windows 10 或 11，64 位（已在 Windows 11 上测试）。安装程序不包含模型：首次使用时，请在 **MODELS** 中选择一个（Amada 4.0 INT4 是轻量版，188 MB）。PinkHouse 目前尚不能在 macOS 或 Linux 上运行。

PinkHouse 可免费用于任何场景，无论是在家还是在工作中，但它不是开源软件：它有自己的许可证，与采用 MIT 许可证的模型不同。安装程序会要求您接受该许可证。请阅读[许可证](https://amada.devliam.com/zh/pinkhouse/license)、[使用条款](https://amada.devliam.com/zh/pinkhouse/terms)、[隐私政策](https://amada.devliam.com/zh/pinkhouse/privacy)和[法律声明](https://amada.devliam.com/zh/pinkhouse/legal-notice)。简而言之：没有遥测，您的文本会保留在您的 PC 上，应用仅会联网从这些发布版本下载模型。

---

## 安装

> 要求：**Python 3** 和 **pip**。

```bash
git clone https://github.com/DevLiamDb/Amada.git
cd Amada
pip install -r requirements.txt
```

然后获取模型：

1. 从[最新发布版本](https://github.com/DevLiamDb/Amada/releases/latest)下载 `amada-4.0.zip`（或从同一发布版本下载较小的 `amada-4.0-int4.zip`，188 MB）。
2. 将其解压到与 `play.py` 同级的 `Release/` 文件夹中，以便得到 `Release/amada-4.0/amada_model.onnx` 和 `Release/amada-4.0/tokenizer/`。

> ⚠️ **请将 `tokenizer/` 文件夹放在 `amada_model.onnx` 旁边。**否则，答案会出错。

---

## 使用方法

### 1. 在终端中

```bash
python play.py
```

粘贴一段文本，在空行处按 Enter，然后提问：

```text
Did Lea eat an apple?                          -> yes / no
Which apple did she eat? | red, green, yellow  -> choice
How hungry is she? #                           -> score (none / low / moderate / high)
How happy is she? # not at all, a bit, very    -> score with your own levels
:new = new text    :q = quit
```

其他版本：`python play.py --version 4.0-int4`（需要 onnxruntime 1.20+）、`python play.py --version 3.1`、`python play.py --version 2.0`……

### 2. 在 Python 中

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

### 3. 三种问题类型

| 类型 | 您提问 | Amada 返回 |
|---|---|---|
| **是 / 否** (`noul`) | `Did the customer pay by card?` | 是的概率，以及**文本中没有说明**的概率 |
| **选项** | `What does the customer want? \| a refund, an exchange, ...` | 每个选项对应一个概率，总计 100 % |
| **评分** | `How urgent is it? #` | 每个等级对应一个概率（无、低、中、高，或您自定义的等级） |

它只知道您提供的文本。没有互联网、没有记忆、不会生成文本。

---

## 下载

每个版本都是一个发布版本（标签从 `v1.0` 到 `v4.0`）：一个包含 ONNX 模型及其分词器的 zip 文件。PinkHouse 应用有自己的发布版本（标签为 `pinkhouse-v…`）。

| 版本 | 基础模型 | 最大长度 | 压缩包 | 备注 |
|---|---|:---:|:---:|---|
| **4.0**（当前） | mmBERT-base | 8,192 | 1.16 GB | 混乱的写法、“文本中没有说明”、TREC |
| **4.0 INT4** | mmBERT-base | 8,192 | **188 MB** | 同一模型，4 位权重：内存减少 4×，在 AG News 和 Banking77 上的分数约低 1 分 |
| 3.1 | mmBERT-base | 8,192 | 1.16 GB | 相近标签，在 Banking77 和情绪识别上略有提升 |
| **3.1 INT4** | mmBERT-base | 8,192 | **188 MB** | 同一模型，4 位权重：准确率相同，内存减少 3× |
| 3.0.1 | mmBERT-base | 8,192 | 1.16 GB | 重新校准的 3.0，准确率相同 |
| 3.0 | mmBERT-base | 8,192 | 1.16 GB | 长文本、多个选项、陷阱文本 |
| 2.0 | mmBERT-base | 512 | 1.16 GB | 多语言、“文本中没有说明” |
| 1.0 | ModernBERT-large | 512 | 1.49 GB | 首个版本，仅支持英语 |

各版本的变更：[CHANGELOG.md](CHANGELOG.md)。

---

## 基准测试

<div align="center">

<img src="media/dream_corridor.gif" width="600" alt="网站的酒店走廊场景，以及 Amada 的回答">

</div>

**我们自己的简短测试**（英语：2,000 条文本 · 11 种语言：1,320 条文本）：

| 准确率 | 是 / 否 | 选择题 | 评分 | 英语，所有类型 | 11 种语言 |
|---|:---:|:---:|:---:|:---:|:---:|
| **Amada 4.0** | 0.961 | 0.908 | 0.759 | 0.896 | 0.985 |
| Amada 4.0 INT4 | 0.960 | 0.908 | 0.742 | 0.892 | 0.983 |
| Amada 3.1 | 0.961 | 0.915 | 0.760 | 0.899 | 0.984 |

4.0 的校准误差（ECE，越低越好），在未用于校准的一半英语测试集上：是 / 否 0.009，选择题 0.016，评分 0.048（4.0 INT4：0.008、0.014、0.031）。

**“文本中没有提及”**（是 / 否 / 未说明，939 个留出问题）：4.0 的得分为 **0.963**（3.1：0.917）；在包含拼写错误的相同文本上为 **0.954**（3.1：0.889）。这些文本也用于拟合校准，因此这只是一次检查，并非独立测试。

**公开数据集，零样本**（Amada 在训练期间从未见过这些数据：它只会收到问题和选项名称）。Jev 1.14 由我们在相同文本上运行：

| 数据集 | 任务 | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|---|:---:|:---:|:---:|:---:|
| SST-2 | 电影评论情感 | 0.897 | 0.890 | 0.899 | **0.959** |
| AG News | 新闻主题，4 个标签 | 0.803 | 0.793 | 0.800 | **0.883** |
| Banking77 | 银行支持意图，77 个标签 | 0.586 | 0.574 | 0.611 | **0.788** |
| emotion | 推文情绪，6 个标签 | 0.447 | 0.464 | 0.471 | **0.595** |
| tweet_topic | 推文主题 | 0.718 | 0.711 | 0.740 | **0.820** |
| 提示注入 | 这段文本是否在攻击 AI？ | **0.845** | 0.810 | **0.845** | 0.733 |
| When2Call | AI 代理是否应该调用工具？ | 0.344 | 0.340 | 0.324 | **0.733** |

**11 种语言的公开测试**（平均值，每种语言使用相同的条目）：

| 测试 | Amada 4.0 | Amada 4.0 INT4 | Amada 3.1 | Jev 1.14 |
|---|:---:|:---:|:---:|:---:|
| 是 / 否（机器翻译） | 0.841 | 0.837 | 0.839 | **0.882** |
| 阅读理解（Belebele，4 个答案） | 0.554 | 0.559 | 0.568 | **0.947** |
| 意图（MASSIVE，60 个选项） | 0.834 * | 0.829 * | 0.428 | 0.824 |

\* 并非零样本：Amada 4.0 从 MASSIVE 的训练拆分中学习（测试条目仍未见过）。

**4.0 INT4** 于 12 November 2026 在与 4.0 完全相同的条目上运行（使用 CPU 而非 GPU）。逐个答案进行比较（精确 McNemar 检验），明显的差异是 AG News（-1.0 个百分点）、Banking77（-1.2）、评分（-1.6）和 emotion（+1.7）；其他差异都在随机误差范围内，包括提示注入（仅 116 条文本）。

**速度**（每次只发送一个请求时，单个答案的中位耗时，所有模型使用相同请求 · Amada 在 Intel Core i5-11400H 上运行，使用 4 个 CPU 线程 · Jev 通过其 API 从法国运行）。4.0 和 4.0 INT4 于 12 November 2026 测量，Jev 于 8 November 测量：

| 请求 | Amada 4.0 | Amada 4.0 INT4 | Jev 1.14 |
|---|:---:|:---:|:---:|
| 一行屏幕文本，是 / 否 | 41 ms | **37 ms** | 244 ms |
| 简短备注，是 / 否 | 54 ms | **49 ms** | 247 ms |
| 阅读段落，4 个答案 | 161 ms | 159 ms | 264 ms |
| 语音请求，60 个意图 | 390 ms | 375 ms | **270 ms** |

在与 INT4 相同的运行中，4.0 耗时分别为 40、55、154 和 388 ms：INT4 的速度大致相同（短问题稍快，阅读稍慢）。它主要节省内存：加载后约占用 340 MB RAM，而非 1.4 GB。

**不足之处**，特意列出：TREC（问题期待的答案类型，4.0 为 0.52，高于 0.39）、Banking77（0.59，比 3.1 低 2.5 个百分点）、序数评分（约 76 %）以及很长的文本。杂乱的写法现在影响很小：留出的含拼写错误是 / 否测试在英语中为 0.960，在 11 种语言中为 0.967。

> **坦诚说明：**我们的简短测试使用强力 AI（GPT-6 Luna）的答案，而非人工标注员的答案，并且测试文本与训练数据相似。公开数据集使用人工标签。

---

<details>
<summary><b>🗂️ 文件结构</b></summary>
<br>

```
Amada/
├── play.py            ← 终端聊天 + Python API ← 从这里开始
├── install.ps1        ← 安装 PinkHouse（Windows 应用）
├── requirements.txt   ← numpy、onnxruntime、transformers
├── Release/           ← 将下载的版本解压到这里（不要放在代码仓库中）
│   └── amada-4.0/
│       ├── amada_model.onnx
│       └── tokenizer/  ← 将其放在 ONNX 文件旁边
├── CHANGELOG.md       ← 各版本的变更内容
├── LICENSE            ← MIT
├── NOTICE.md          ← 基础模型的声明（分享时请保留）
└── media/             ← 徽标、徽章和 GIF（图片不适用 MIT 许可，详见 License）
```

</details>

---

<details>
<summary><b>⚙️ 内部工作原理</b></summary>
<br>

```
text + questions ──► tokenizer ──► encoder (mmBERT-base, ONNX, CPU) ──► one head per question type
                                                                     │
                                                                     └── temperatures ──► calibrated probabilities
```

- **一次处理所有问题：**文本和每个问题会一起读取。每个问题以 `[Q]` 标记开头，每个选项以 `[OPT]` 开头，每个等级以 `[LVL]` 开头。
- **三种答案类型：**是 / 否（包括“文本中没有提及”）、选择（每个选项对应一个分数，合计为 100 %）、评分（每个等级对应一个概率）。
- **校准：**从 3.0.1 起，温度取决于文本长度和选项数量。因此，Amada 给出的“95 %”表示实际约为 95 %。
- **耗时随选项数量增长：**每个选项都会被读取。两个选项约需 40 ms，77 个选项约需 720 ms。

</details>

---

<details>
<summary><b>❓ 常见问题</b></summary>
<br>

**我可以在公司或付费产品中使用 Amada 吗？**
可以。Amada 采用 MIT 许可：允许商用。请将版权声明和许可证文本与文件一并保留。

**我可以微调它吗？**
可以，您也可以分享或出售微调后的版本。请将 MIT 声明（以及 NOTICE.md）一并保留。

**我应该使用哪个版本？**
大多数用途请选择 4.0。如果您需要较小的下载文件或较少的 RAM，请选择 4.0 INT4（在某些分类任务上的表现约低 1 个点）；如果您的任务类似 Banking77 或情绪分类，请选择 3.1。较旧的版本可供比较。

**选择题可以有多少个选项？**
两个或更多，没有固定上限：文本、问题和选项合计必须在 8,192 个 token 以内。3.0 及更高版本的训练数据中包含最多 386 个选项的列表。

**需要什么硬件？**
普通 CPU 即可。加载约需 9 秒，加载后约占用 1.4 GB RAM（FP32）；使用 INT4 时最多约 1.2 GB。无需 GPU，下载后无需联网。

**有 API 或托管版本吗？**
没有。Amada 在您自己的电脑上运行。

**答案看起来不对。**
请确认 `tokenizer/` 文件夹与 `amada_model.onnx` 位于同一目录。

</details>

---

## 故事与致谢

<details>
<summary><b>📖 网站：一个夜晚，从 03:00 到 07:12</b></summary>
<br>

[网站](https://amada.devliam.com/zh)通过一个简短的故事介绍 Amada：一个夜晚，一个无法入睡的女孩，一座公园，一条酒店走廊，一间被水淹的房子，以及敲门声。每个场景都会展示一段日记文本和一个问题，并附上 **Amada 对这些确切文本预先计算出的真实回答**。随后她醒来，打开电脑，一台 90 年代风格的桌面电脑展示了基准测试结果。没有突然惊吓。

<div align="center">

<img src="media/dream_knock.gif" width="600" alt="敲门场景：Amada 回答“我不知道”">

</div>

</details>

<details>
<summary><b>🙏 致谢 — 是谁、什么促成了 Amada</b></summary>
<br>

Amada **由 AI 协助构建，我们坦率说明这一点。**

| 人员/项目 | 角色 |
|---|---|
| **Liam DB** ([DevLiamDb](https://github.com/DevLiamDb)) | 创作者。构想、方向、决策、训练运行和测试。 |
| **[Claude Code](https://claude.com/claude-code)** (Anthropic) | 在 Liam DB 的指导下协助编写代码（训练、基准测试、`play.py`、网站）。 |
| **GPT-6 Luna** | 编写了大量训练示例和短测试的参考答案。 |
| **[mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base)** (Johns Hopkins University, CLSP) | Amada 2.0 及后续版本的基础网络（MIT）。 |
| **[ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)** (Answer.AI) | Amada 1.0 的基础网络（Apache-2.0）。 |

**训练数据：**公开文本（Wikipedia、FineWeb-2、Project Gutenberg、政府报告、arXiv 和 PubMed 摘要）、公开标注数据集（QuALITY、ContractNLI、Qasper、CLINC150）以及合成示例。未使用基准测试集进行训练。

**构建所用：**[ONNX Runtime](https://onnxruntime.ai/)、[Hugging Face Transformers](https://huggingface.co/docs/transformers)、[Kaggle](https://www.kaggle.com/)（训练和基准测试）。

**联系创作者：**🌐 [amada.devliam.com](https://amada.devliam.com/zh) · 🐙 [GitHub](https://github.com/DevLiamDb)

</details>

---

## 许可证

**Amada：MIT**（权重、`play.py`、`install.ps1` 和此仓库的代码）

✅ 可用于任何用途，包括商业用途
✅ 可修改、微调或合并
✅ 可分享或出售原版或修改后的版本
📌 请将版权声明（"Copyright (c) 2026 LiamDB"）和许可证文本与文件一并保留

MIT 许可证适用于 Amada 的所有版本，从 1.0 到最新版本，包括权重曾采用 CC BY-NC-ND 4.0 时下载的副本。Amada 不提供任何担保。mmBERT-base (MIT) 和 ModernBERT-large (Apache-2.0) 的声明位于 [NOTICE.md](NOTICE.md) 中，分享文件时必须保留。完整条款请参阅 [LICENSE](LICENSE)。

**图片：不采用 MIT 许可。**`media/` 中的徽标和 GIF 展示了网站，其版权仍归 LiamDB 所有，© 2026，保留所有权利。您可以附上署名 "Amada by LiamDB" 分享这些图片，具体以[网站条款](https://amada.devliam.com/zh/terms)为准。

**PinkHouse：采用单独的许可证。**PinkHouse 应用（`pinkhouse-v…` 版本）不受 MIT 许可证约束：可免费用于任何用途，但源代码闭源，您不得出售、修改或对其进行逆向工程。请参阅 [PinkHouse License](https://amada.devliam.com/zh/pinkhouse/license)。

---

<div align="center">

<img src="media/desktop.gif" width="600" alt="展示基准测试的网站 90 年代桌面风格界面">

由 Liam DB 制作 — 在 AI 的帮助下。· liamdb.work@gmail.com

</div>
