---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.924587+00:00
arxiv_id: 2611.28833
url: https://huggingface.co/papers/2611.28833
arxiv_url: https://arxiv.org/abs/2611.28833
date: 2026-11-24
---

# Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?

Frontier language models can now read and edit the weights of a neural network much like code and thereby improve a small model, an approach known as Weight-Space Programming (WSP). We further explore applying WSP to a language model itself, which we call Self-WSP. Specifically, Qwen3.5-0.8B reads its own weights, proposes an edit, and then continues with the edited weights as both problem solver and editor. We find many cases of genuine self-improvement. Self-edits can raise GSM8K accuracy from 11.8% to 62.2% and MATH500 accuracy from 7.0% to 32.2%, sometimes by changing only 16 parameters, and in some cases repeated self-editing keeps improving the model. A closer look, however, reveals that these gains lack interpretability. The model shows little understanding of the edits it makes, and WSP driven by random search sometimes performs comparably. Self-WSP thus holds promise as a path toward recursive self-improvement (RSI), but realizing this promise requires further exploration.
