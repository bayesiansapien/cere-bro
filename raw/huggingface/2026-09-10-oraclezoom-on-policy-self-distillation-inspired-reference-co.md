---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.06490
url: https://huggingface.co/papers/2609.06490
arxiv_url: https://arxiv.org/abs/2609.06490
date: 2026-09-10
---

# OracleZoom: On-Policy Self-Distillation Inspired Reference-Constrained Recursive Image Super Resolution

Recursive Super-Resolution (SR) extends fixed-scale SR to extreme magnification by repeatedly feeding predictions back into the same model, analogous to zooming an image repeatedly. However, ground truth availability at every scale, especially at depth, remains challenging as the required source resolution grows geometrically, leaving deeper predictions unsupervised. We present OracleZoom, an on-policy distillation-inspired, reference-constrained framework that trains on its trajectory while carrying the last ground-truth evidence beyond the supervision boundary. Direct and cross-scale supervision constrain verifiable content, while a no-reference quality objective guides unresolved fine-scale detail. A KL-constrained pretrained latent prior limits quality-driven drift, while EMA consistency stabilizes the supervision boundary. Across seven datasets, OracleZoom achieves the state-of-the-art SR quality across zooming scales, averaging 0.713 CLIPIQA, with larger gains on deeper scales, while significantly reducing hallucinations. Code, data, and models are available at https://dipta007.github.io/OracleZoom/ .
