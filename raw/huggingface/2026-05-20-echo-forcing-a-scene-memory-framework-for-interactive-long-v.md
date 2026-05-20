---
source: farmer/huggingface
farmed: 2026-05-20T09:54:46.703317+00:00
arxiv_id: 2605.16003
url: https://huggingface.co/papers/2605.16003
arxiv_url: https://arxiv.org/abs/2605.16003
date: 2026-05-20
---

# Echo-Forcing: A Scene Memory Framework for Interactive Long Video Generation

Autoregressive video diffusion models enable open-ended generation through local attention and KV caching. However, existing training-free long-video optimization methods mainly focus on stable extension under a single prompt, making them difficult to handle interactive scenarios involving prompt switching, old scene forgetting, and historical scene recall. We identify the core bottleneck as the functional entanglement of historical KV states: stable anchors and recent dynamics are handled by the same cache policy, leading to outdated background contamination, delayed response to new prompts, and loss of long-range memory. To address this issue, we propose Echo-Forcing, a training-free scene memory framework specifically designed for interactive long video generation with three core mechanisms: (1) Hierarchical Temporal Memory, which decouples stable anchors, compressed history, and recent windows under relative RoPE; (2) Scene Recall Frames, which compresses historical scenes into spatially structured KV representations to support long-term recall; and (3) Difference-aware Memory Decay, which adaptively forgets conflicting tokens according to the discrepancy between old and new scenes. Based on these designs, Echo-Forcing uniformly supports smooth transitions, hard cuts, and long-range scene recall under a bounded cache budget. Extensive evaluations on VBench-Long further demonstrate that Echo-Forcing achieves the best overall performance in both long-video generation and interactive video generation settings. Our code is released in this https URL
