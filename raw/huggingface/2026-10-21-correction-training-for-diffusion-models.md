---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.640105
arxiv_id: 2610.14136
url: https://huggingface.co/papers/2610.14136
arxiv_url: https://arxiv.org/abs/2610.14136
date: 2026-10-21
---

# Correction Training for Diffusion Models

Iterative sampling in diffusion models can lead to error accumulation due to exposure bias. The denoiser is trained on real images interpolated with noise, but at inference its inputs are constructed from its own imperfect predictions from the earlier steps, something it has never seen at training time. This might be one reason diffusion models often struggle without additional help, such as CFG. We introduce a correction step for diffusion models which attempts to reduce this training-inference gap. The corrector takes the base model's prediction as input and is trained against the same ground-truth target. This makes correction an explicit learning task, with training inputs provided by the base model. During sampling, at each denoising step, we iteratively refine the denoiser's clean-sample prediction. This allows us to correct predictions at intermediate denoising steps, preventing early artifacts from persisting into the final sample. Although the corrector is trained only on predictions from the base denoiser, it can be applied repeatedly to its own outputs at inference for better results. This simple framework leads to substantial improvement in sample quality while largely preserving diversity. We evaluate our method across DiT, SiT, and JiT. Our method substantially improves upon previously reported FID scores for unguided generation and, notably, unconditional generation, where producing high-quality samples without guidance has been particularly challenging. Our method achieves performance competitive with classifier-free guidance (CFG), and combining correction with CFG further improves diversity and reduces oversaturation typical of CFG. Finally, we show that the additional inference cost of correction can be amortized by distilling the refined predictions back into the base diffusion model, retaining the quality gains without additional inference-time overhead.
