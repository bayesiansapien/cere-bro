---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.06309
url: https://huggingface.co/papers/2606.06309
arxiv_url: https://arxiv.org/abs/2606.06309
date: 2026-06-15
---

# RhymeFlow: Training-Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling

Video generation models based on Diffusion Transformers (DiTs) have achieved remarkable performance in video synthesis, yet they suffer from high inference latency and computational costs due to the quadratic complexity of 3D attention. Existing acceleration methods primarily reduce computational complexity within each individual denoising steps through techniques such as sparse attention and KV-caching. However, they rigidly adhere to the inherent constraint of the standard diffusion pipeline: every frame in the target video sequence must be subjected to a complete, dense denoising process across all diffusion timesteps. We observe that due to the corresponding contents and motions among adjacent frames, when keyframes with critical semantic transitions are anchored, the intermediate states of others often follow more predictable trajectories, which indicates that such uniform, dense denoising process is inherently redundant for natural video data. To this end, we introduce RhymeFlow, a training-free framework that decouples the denoising trajectories of different frames. Specifically, we first identify a sparse set of pivotal key frames that dominate the latent semantic evolution. Then, only these keyframes undergo dense, step-by-step denoising to ensure structural integrity, while non-keyframes progressively skip denoising steps to minimize computational cost. Since skipped intermediate states of non-keyframes break the temporal coherence in keyframe denoising steps, leading to visual degradation, we further introduce a latent trajectory projection module, which enables keyframes to interact with a complete and temporally consistent sequence representation. Extensive experiments on current DiT-based video generation models demonstrate our method outperforms existing baselines with higher inference speed and better visual quality.
