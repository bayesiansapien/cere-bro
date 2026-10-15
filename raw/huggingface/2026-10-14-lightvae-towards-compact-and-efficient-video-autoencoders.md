---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.509453+00:00
arxiv_id: 2610.14726
url: https://huggingface.co/papers/2610.14726
arxiv_url: https://arxiv.org/abs/2610.14726
date: 2026-10-14
---

# LightVAE: Towards Compact and Efficient Video Autoencoders

Latent diffusion models enable high-quality video generation, but video VAE encoding and decoding remain computationally expensive. Existing methods use stage-specific lightweight operators, yet either constrain spatial and temporal computation jointly or remove temporal computation altogether, without distinguishing their compression sensitivities in pretrained Conv3D. To address these limitations, we present LightVAE, a compression framework that exploits redundancy in temporal modeling and network depth. LightVAE exactly reparameterizes eligible causal Conv3D layers into an aggregate spatial response and a difference-driven temporal correction. Based on their distinct compression sensitivities, temporal low-rank compression (TLR) keeps the aggregate spatial kernel dense and applies layer-specific low-rank approximation only to the temporal correction. An algebraically equivalent folded implementation converts the arithmetic savings into practical acceleration. LightVAE further uses width-preserving block pruning to reduce depth and probe-guided feature alignment, guided by feedback from a frozen teacher suffix, to recover quality after compression. The framework also extends to video encoders. Across three video VAE backbones and two GPU platforms, LightVAE consistently accelerates decoding. For the Wan VAE family, it achieves up to 2.24times and 1.11times the decoding throughput of state-of-the-art efficient VAE decoders on NVIDIA H100 and RTX~5090, respectively, with higher DAVIS PSNR and lower LPIPS. On MiniMax-H3, it achieves up to 2.97times the original decoding throughput while retaining 99.51\% of the original model's overall VBench-2.0 score. Our code is available at https://github.com/ModelTC/LightVAE.
