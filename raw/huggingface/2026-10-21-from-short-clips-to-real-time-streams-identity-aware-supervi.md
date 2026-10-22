---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.642425
arxiv_id: 2610.26681
url: https://huggingface.co/papers/2610.26681
arxiv_url: https://arxiv.org/abs/2610.26681
date: 2026-10-21
---

# From Short Clips to Real-Time Streams: Identity-Aware Supervision and Context-Efficient Generation for Video Face Swapping

Video face swapping transfers the reference identity to a target video while preserving its other attributes and motion. Despite recent progress in reference-guided flow-based methods, jointly achieving faithful identity transfer, high fidelity, and real-time generation over long video streams remains challenging. To address this challenge, we rethink the task-specific structure of reference-guided video face swapping. First, face swapping changes only identity while preserving most visual content, yet flow-matching supervision is weakly sensitive to these changes. We therefore develop Joint Rec-ID Loss, which balances explicit identity supervision and latent reconstruction according to the noise level. Second, the target video already provides non-edited attributes and temporal dynamics, enabling generation with fewer spatial tokens and shorter temporal contexts through Face-RoI Generation and Short-Context Rollout Training. By integrating these designs, we propose StreamingSwap, a reference-guided flow-matching framework for real-time streaming video face swapping. We also introduce HumanFaceVid, comprising 1,000 hours of cinematic training data and evaluation sets of 200 short and 200 long videos. Experiments demonstrate that our method achieves competitive identity transfer and visual quality at 20 FPS on a single NVIDIA RTX 4090 GPU, with stable generation over videos up to 10 minutes long. Project webpage: https://aim-uofa.github.io/StreamingSwap/
