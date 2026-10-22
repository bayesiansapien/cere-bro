---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.646546
arxiv_id: 2610.09513
url: https://huggingface.co/papers/2610.09513
arxiv_url: https://arxiv.org/abs/2610.09513
date: 2026-10-21
---

# OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning

Camera trajectories control viewpoint changes in video generation, scene reconstruction, and robotic perception. Generating them from language requires both scene geometry and target-aware framing. We introduce OmniCam, an autoregressive model that generates camera pose sequences from a single panorama and textual trajectory descriptions. Its geometry-grounded pose token learning combines three components: a panoramic point-cloud encoder for omnidirectional geometric context; hybrid absolute-rotation and relative-translation tokenization with temporally consistent quaternion signs; and separate geometric and semantic conditioning streams with an explicit 3D target anchor. We also construct OmniCaT, containing 267,700 trajectories across four camera behaviors. On the reported OmniCaT evaluation, OmniCam reduces trajectory errors by 28--47% and collision rate by 65.8% relative to GenDoP retrained on OmniCaT. Against the best baseline for each metric, the ATE and collision reductions are 43.0% and 62.3%, respectively. Component ablations support the use of geometric and target-aware conditioning, while downstream experiments examine camera-controlled video generation and robotic active perception.
