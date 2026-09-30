---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.931134+00:00
arxiv_id: 2609.34470
url: https://huggingface.co/papers/2609.34470
arxiv_url: https://arxiv.org/abs/2609.34470
date: 2026-09-29
---

# Precise Editing and Flexible Referencing for Interactable Worlds

We present EditWorld, a video world model for precise editing and flexible referencing in interactable worlds. Existing video world models primarily focus on navigation, letting users explore generated worlds but offering limited control over how existing world content is modified. EditWorld extends world modeling from exploration to precise modification by streaming editing instructions and reference images during autoregressive generation. To support these capabilities, EditWorld introduces Gated Causal Attention for temporally varying editing conditions and reference images, together with a Sparse Context mechanism that maintains a bounded historical context for long-horizon inference. We further adopt joint autoregressive and bidirectional training with annealed self-resampling, and construct a dedicated data synthesis and annotation pipeline that provides supervision for world editing. We also present WBench-Editing to systematically evaluate streaming world editing capabilities. EditWorld achieves the best overall performance on WBench-Editing with an overall score of 73.8 and an editing score of 80.0, substantially outperforming existing methods on editing-related metrics. https://github.com/leoisufa/EditWorld
