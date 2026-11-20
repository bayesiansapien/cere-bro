---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.143910+00:00
arxiv_id: 2611.23994
url: https://huggingface.co/papers/2611.23994
arxiv_url: https://arxiv.org/abs/2611.23994
date: 2026-11-19
---

# WaveView: The Novel View Is in the Noise

Generative novel view synthesis (NVS) employs a diffusion model to render a static or dynamic scene from a target camera view. Explicit warp methods complete a reprojection of the source with video diffusion models, and implicit methods encode the camera parameters or 3D cues. Both add inference overhead, and the generated layout often drifts from the ground truth. We present WaveView, which injects the warped source into the phase of the initial noise of a pretrained generator. The Dual-Tree Complex Wavelet Packet Transform (DT-CWPT) allows local and anisotropic phase injection. The generator is thus constrained less in disoccluded regions and along the epipolar line. WaveView keeps the architecture and adds negligible overhead. On the DL3DV benchmark, it outperforms all baselines in every overlap bin. In the hardest bin, it gains 0.84 dB PSNR on the covisible region over MetaView, which shares its generator, while running 2.1 times faster. For dynamic NVS, fine-tuning AnyView with the same noise raises its zero-shot PSNR on AnyViewBench from 11.58 to 12.35 dB.
