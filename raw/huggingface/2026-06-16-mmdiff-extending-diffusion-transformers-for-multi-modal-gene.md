---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16673
url: https://huggingface.co/papers/2606.16673
arxiv_url: https://arxiv.org/abs/2606.16673
date: 2026-06-16
---

# MMDiff: Extending Diffusion Transformers for Multi-Modal Generation

Diffusion transformers have demonstrated remarkable generative capabilities, yet the rich perceptual representations computed across their denoising trajectory are discarded once the content is rendered. We present MMDiff, a framework that transforms a frozen diffusion transformer into a multi-modal generative system that jointly produces images alongside any combination of dense perceptual modalities using lightweight decoder heads. Our central finding is that perceptual information is temporally distributed along the denoising trajectory, and that multi-timestep feature fusion with spatially varying aggregation weights is essential, improving semantic segmentation results by up to 28.7% mIoU over single-timestep extraction. We further adopt concept-driven attention extraction for interpretable spatial guidance, and show that frozen diffusion features are competitive with and complementary to state-of-the-art encoders such as DINOv3. By training only lightweight decoder heads on a frozen backbone, we achieve strong performance in semantic segmentation, salient object detection, and depth estimation, and demonstrate that this framework enables effective synthetic data generation at scale.
