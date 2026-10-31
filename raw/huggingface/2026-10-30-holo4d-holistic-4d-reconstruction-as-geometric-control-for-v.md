---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.163171+00:00
arxiv_id: 2610.25276
url: https://huggingface.co/papers/2610.25276
arxiv_url: https://arxiv.org/abs/2610.25276
date: 2026-10-30
---

# Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion

Synthesizing a monocular video from a new camera trajectory requires preserving the observed scene geometry and motion while completing regions that become newly visible. Feed-forward 4D reconstructors recover the structure of the observed scene, whereas video diffusion models provide a generative prior for completing unseen content. We introduce Holo4D, a video reshooting framework that uses reconstructed 3D trajectories as a holistic source-view 4D scaffold. We project these trajectories into the requested views and encode their geometry and source appearance to guide a pretrained video diffusion model. Together with the source video and target cameras, the scaffold grounds generation in reconstructed observations while leaving unsupported regions to the generative prior. Experiments demonstrate the value of trajectory-based conditioning for camera control and novel-view synthesis. The framework accommodates different 4D reconstructors without retraining the video generator, allowing it to benefit from future advances in source reconstruction. More details can be found in our project page.
