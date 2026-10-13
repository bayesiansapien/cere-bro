---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.216979+05:30
arxiv_id: 2610.13113
url: https://huggingface.co/papers/2610.13113
arxiv_url: https://arxiv.org/abs/2610.13113
date: 2026-10-12
---

# Continually Post-training Small Models via Synthetic Self-distillation

Continual post-training faces a dual challenge of acquisition and retention: models must learn new capabilities while preserving prior knowledge. While Self-Distillation Fine-Tuning (SDFT) mitigates this using self-supervision with in-context demonstrations, it relies on strong in-context learning and instruction-following abilities. Consequently, SDFT fails on smaller models critical for low-latency, on-device use. To enable continual learning at smaller scales, we first identify the root cause of failure. We show that poor acquisition and forgetting correlate linearly with the post-trained model's distribution shift, revealing the necessity of in-distribution learning. We thus introduce Synthetic Self-Distillation (SynthSelf), imitating SDFT's in-distribution rewrite by outsourcing the task to a minimally larger, same-family aligner. Coupled with off-policy supervision and rejection sampling, this provides the high-quality supervision small models require without breaking their original distribution. Evaluations spanning 4 acquisition datasets (including a mixture) and 14 retention benchmarks show SynthSelf consistently outperforms 6 methods (including off- and on-policy distillation) across 3 small model scales. Extensive further analyses confirm SynthSelf paves the way toward effective small-model continual learning.
