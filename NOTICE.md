# Notices

Amada is built on other people's work. When you share the Amada files, keep this notice with them.

## mmBERT-base (Amada 2.0 and later)

Amada 2.0, 3.0, 3.0.1 and 3.1 are fine-tuned versions of **mmBERT-base**, a multilingual encoder by the Center for
Language and Speech Processing of Johns Hopkins University: https://huggingface.co/jhu-clsp/mmBERT-base
Copyright: the mmBERT-base authors (jhu-clsp). Released under the MIT License:

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
> documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
> rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
> persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
> Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
> WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
> COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
> OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## ModernBERT-large (Amada 1.0)

Amada 1.0 is a fine-tuned version of **ModernBERT-large** by Answer.AI and LightOn:
https://huggingface.co/answerdotai/ModernBERT-large
Licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0
Amada 1.0 was modified from it (fine-tuned for decisions, exported to ONNX).

## Training data

Amada learned from public texts (Wikipedia, FineWeb-2, Project Gutenberg books, government reports, arXiv and PubMed
abstracts), public labelled datasets (QuALITY, ContractNLI, Qasper, CLINC150) and synthetic examples written by large
language models. Each dataset keeps its own license and terms, available on its original page. Amada does not contain
these texts as such: it learned patterns from them.
