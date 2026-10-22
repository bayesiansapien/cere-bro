---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.641086
arxiv_id: 2610.26837
url: https://huggingface.co/papers/2610.26837
arxiv_url: https://arxiv.org/abs/2610.26837
date: 2026-10-21
---

# SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration

Diffusion Transformers (DiTs) achieve high-fidelity image and video generation, but they suffer from substantial inference costs due to repeated transformer evaluations across many denoising steps. Feature caching reduces this cost by reusing features across denoising steps. Recent forecasting methods extend this idea by extrapolating features to skipped steps instead of reusing them. However, existing forecasting methods extrapolate the features they predict uniformly, even though the spatial-frequency components of these features change most at different stages of denoising. They also overlook that denoising progresses nonuniformly, so equal step intervals can correspond to very different amounts of change. These mismatches amplify forecast errors as more steps are skipped, limiting the achievable acceleration. We propose SpecKCast, a training-free method that forecasts the model output in the frequency domain. SpecKCast applies a 2D discrete cosine transform (DCT) to the output and tracks each coefficient with a lightweight Kalman filter along a band-specific time coordinate derived from the noise schedule. The filter tracks each coefficient's value and rate of change, and the transformer is evaluated only when the filter's forecast uncertainty exceeds a threshold. Experiments on FLUX.1-dev, Qwen-Image, Wan2.1-14B, and HunyuanVideo show that SpecKCast achieves a better trade-off between acceleration and fidelity than existing caching and forecasting methods, reaching up to 6x speedup with less than 0.05 GiB of additional memory.
