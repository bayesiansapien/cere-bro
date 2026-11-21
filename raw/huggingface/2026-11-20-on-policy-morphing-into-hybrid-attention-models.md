---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.385639+00:00
arxiv_id: 2611.24809
url: https://huggingface.co/papers/2611.24809
arxiv_url: https://arxiv.org/abs/2611.24809
date: 2026-11-20
---

# On-Policy Morphing into Hybrid Attention Models

Hybrid attention models combine full and linear attention to achieve a better quality--efficiency trade-off. Converting pretrained Transformers into such models requires identifying which layers should retain full attention under a prescribed budget. We identify two off-policy mismatches in FlashMorph's layer selection: (i) continuous branch interpolation and teacher-forced hidden states differ from discrete hybrid computation; and (ii) frozen model weights fail to account for parameter adaptation during subsequent recovery. We introduce FlashMorph2, an on-policy layer-selection method that (I) evaluates sampled discrete hybrid architectures end to end using their own hidden states, and (II) jointly optimizes layer-selection scores and model weights under the recovery objective to reflect post-adaptation performance. Experiments across Qwen3 model scales and linear-attention variants show that FlashMorph2 consistently outperforms existing layer-selection methods, improving average scores over FlashMorph by +2.42 points on RULER, +1.08 on LongBench, and +0.76 on recall-intensive tasks, while completing layer selection in only 0.72--3.57 GPU hours across 0.6B--8B models, demonstrating high efficiency and scalability.
