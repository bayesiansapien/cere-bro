---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.09932
url: https://huggingface.co/papers/2605.09932
arxiv_url: https://arxiv.org/abs/2605.09932
date: 2026-05-13
---

# FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning

Large language models can now process increasingly long inputs, yet their ability to effectively use information spread across long contexts remains limited. We trace this gap to how attention budget is spent during supervised fine-tuning (SFT) on long sequences: positional biases and attention sinks cause the model to allocate most of its attention to positionally privileged tokens rather than semantically relevant content. This training-time attention dilution (the starvation of content tokens in the attention distribution) weakens the gradient signal, limiting the model's ability to learn robust long-context capabilities. We introduce FocuSFT, a bilevel optimization framework that addresses this problem at training time. An inner loop adapts lightweight fast-weight parameters on the training context to form a parametric memory that concentrates attention on relevant content, and the outer loop performs SFT conditioned on this sharpened representation. Both loops apply bidirectional attention over context tokens while preserving causal masking for responses, reducing the causal asymmetry that gives rise to attention sinks and aligning inner-outer behavior. On BABILong, FocuSFT improves accuracy by up to +14pp across 4K--32K context lengths; on RULER, it raises CWE aggregation from 72.9\% to 81.1\% at 16K; and on GPQA with agentic tool use, it yields a 24\% relative gain in pass@1. Attention analysis shows that FocuSFT reduces attention sink mass by 529times and triples context engagement during training. Code: https://github.com/JarvisPei/FocuSFT
