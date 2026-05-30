---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.13857
url: https://huggingface.co/papers/2605.13857
arxiv_url: https://arxiv.org/abs/2605.13857
date: 2026-05-30
---

# MoZoo:Unleashing Video Diffusion power in animal fur and muscle simulation

The creation of cinematic-quality animal effects necessitates the precise modeling of muscle and fur dynamics, a process that remains both labor-intensive and computationally expensive within traditional production workflows. While generative diffusion models have shown promise in diverse artistic workflows, their capacity for high-fidelity animal simulation remains largely unexploited. We present MoZoo, a generative dynamics solver that bypasses conventional refinement to synthesize high-fidelity animal videos from coarse meshes under multimodal guidance. We propose Role-Aware RoPE (RAR-RoPE) which employs role-based index remapping to synchronize motion alignment while decoupling reference information via fixed temporal offsets. Complementing this, Asymmetric Decoupled Attention partitions the latent sequence to enforce a unidirectional information flow, effectively preventing feature interference and improving computational efficiency. To address the scarcity of high-quality training data, we introduce MoZoo-Data, a synthetic-to-real pipeline that leverages a rendering engine and an inverse mapping approach to construct a large-scale dataset of paired sequences. Furthermore, we establish MoZooBench, a comprehensive benchmark with 120 mesh-video pairs. Experimental results demonstrate that MoZoo achieves high-fidelity fur simulation across diverse animal skeletons and layouts, preserving superior temporal and structural consistency.
