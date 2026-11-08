---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.592270+00:00
arxiv_id: 2611.07909
url: https://huggingface.co/papers/2611.07909
arxiv_url: https://arxiv.org/abs/2611.07909
date: 2026-11-07
---

# EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure

Recent advances in Gaussian splatting have enabled efficient and photorealistic head avatar reconstruction, yet monocular video-based or image-based methods still suffer from under-constrained geometry and texture, leading to artifacts such as blurring, stretching, and temporal instability. We present EDGAR (Efficient Diffusion-Driven Gaussian Avatar Refinement), a conditional diffusion framework designed to enhance the quality of Gaussian avatars by correcting artifacts while preserving identity fidelity. To train EDGAR, we construct EDGAR-SET, a hybrid triplet dataset composed of real-captured and synthetic-rendered samples, which simulates realistic Gaussian avatar failure cases by pairing degraded renderings with ground-truth and reference images. EDGAR refines degraded frames through a fusion block that injects identity features extracted by the self-supervised Sapiens model into a one-step diffusion backbone, enabling effective artifact removal without sacrificing efficiency. Our EDGAR model incorporates a Mixture-of-Experts (MoE) architecture to address diverse degradation types and severity levels. The refined multi-view renderings are subsequently used as pseudo-targets to optimize a single underlying Gaussian avatar, so that the final avatar can be rendered without applying EDGAR to every output frame. Experiments on three different Gaussian avatar reconstruction methods, each evaluated under three different settings, show improvements in both perceptual and reconstruction measures over the raw outputs and an SDEdit-style refinement baseline. In addition, cross-view evaluation demonstrates improved calibrated consistency, while tests under large yaw and open-mouth expressions verify robustness under extreme settings. These results collectively indicate a useful operating regime for recoverable appearance artifacts. The code is available at https://kwanyun.github.io/edgar/
