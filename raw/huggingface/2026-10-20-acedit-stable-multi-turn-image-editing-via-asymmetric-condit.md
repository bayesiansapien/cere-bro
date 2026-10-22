---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.22328
url: https://huggingface.co/papers/2610.22328
arxiv_url: https://arxiv.org/abs/2610.22328
date: 2026-10-20
---

# ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning

Image editing models produce impressive results for individual edits, but their quality often deteriorates over multiple editing turns. Each editing turn introduces small distribution shifts that accumulate over successive edits, creating a gap between the input distributions encountered during the editor's original training and multi-turn inference. We introduce a training scheme that makes multi-turn image editing stable under this accumulating distribution shift. A key is to force the editor to operate on its own outputs from previous editing turns during training, bringing the principle of Self-Forcing to image editing. The main challenge is that self-generated editing trajectories deviate from ground-truth trajectories, making direct supervision unreliable. We address this challenge through a distillation objective that leverages a teacher image editor to provide a reliable training signal when the model operates on its own previous outputs. We introduce an asymmetric conditioning scheme: while the student performs edits sequentially on its own outputs, the teacher remains anchored to the original clean image and receives a compound editing instruction. Experiments show substantially reduced degradation over long multi-turn sequences while maintaining editing quality and instruction adherence.
