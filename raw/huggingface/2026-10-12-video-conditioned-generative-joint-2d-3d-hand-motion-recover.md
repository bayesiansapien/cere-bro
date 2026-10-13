---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.225191+05:30
arxiv_id: 2610.10512
url: https://huggingface.co/papers/2610.10512
arxiv_url: https://arxiv.org/abs/2610.10512
date: 2026-10-12
---

# Video-Conditioned Generative Joint 2D-3D Hand Motion Recovery

Recovering faithful 3D hand motion from video remains challenging due to frequent occlusions and incomplete visual observations, which make frame-wise pose estimates unreliable and temporally inconsistent. To address this problem, we propose JoHan, a unified generative framework that recovers hand motion directly from video sequences without relying on intermediate per-frame pose predictions. Trained from scratch, our model jointly generates aligned 2D and 3D local hand pose sequences by learning their temporal dynamics and cross-representation correspondence. The generated 2D trajectories exploit direct spatial and temporal cues from the 2D images to guide the following generative 3D motion reconstruction, while the learned motion prior promotes temporal consistency. Their learned 2D-3D correspondence further enables recovery of the hand's global position and orientation relative to the camera. Extensive experiments on challenging benchmarks demonstrate significantly improved accuracy and speed in local hand-pose and camera-space reconstruction. Notably, our method captures much better hand-motion dynamics, producing significantly smoother motion than previous methods while maintaining high per-frame pose accuracy.
