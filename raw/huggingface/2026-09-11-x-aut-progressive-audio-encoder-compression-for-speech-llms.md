---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11412
url: https://huggingface.co/papers/2609.11412
arxiv_url: https://arxiv.org/abs/2609.11412
date: 2026-09-11
---

# X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale Distillation

Reducing audio-encoder depth lowers the inference cost of speech large language models, but removing complete blocks perturbs the embeddings consumed by the decoder and can cause deletion and premature end-of-sequence errors. We introduce X-AuT, a progressive framework that selects layer combinations through short behavioral probes and restores the pruned model through representation alignment, cross-scale distillation, scheduled student-policy supervision, and LoRA finetuning. The language-model backbone remains frozen, while attention LoRA adapters and the tied output embedding adapt during distillation. Training uses the highest-agreement tier from a transcript-consistency pipeline, followed by source reweighting during finetuning. On ten public Chinese--English benchmarks, compressing Qwen3-ASR-0.6B from 18 to 16 audio-encoder layers reduces macro-average error from 5.61% to 5.27%. The 14-layer model reaches 5.75% with 20.7% fewer audio-tower parameters. Under the matched recipe, the 1.7B teacher yields 5.55% mean error, compared with 8.45% for self-distillation, and progressive 18rightarrow14 pruning outperforms direct pruning (5.75% vs. 6.73%). These single-run results establish two practical operating points and show that the accuracy effects vary across benchmarks. Project website: https://xpeng-ai.github.io/x-aut
