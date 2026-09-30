---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934805+00:00
arxiv_id: 2609.35611
url: https://huggingface.co/papers/2609.35611
arxiv_url: https://arxiv.org/abs/2609.35611
date: 2026-09-29
---

# On-Policy Self-Distillation for Multi-Turn Image Editing

Instruction-based image editing has achieved strong performance in single-turn settings, yet practical editing is often iterative, with each instruction applied to the output of the previous turn. We find that existing editing models degrade rapidly under recursive editing and attribute this failure to a train-test mismatch in the conditioning distribution: models are trained on clean source images but must repeatedly condition on their own imperfect outputs at inference time. To address this, we propose MT-OPSD, an on-policy self-distillation framework that trains the model on self-generated conditioning states with editing supervision from a clean-conditioned teacher, without requiring multi-turn annotations. We further introduce LME-Bench, a benchmark of 100 ten-turn editing sessions for evaluating long-horizon robustness. Experiments across three editing backbones show that MT-OPSD substantially improves long-horizon editing success and reduces multi-turn collapse while largely preserving single-turn editing quality.
