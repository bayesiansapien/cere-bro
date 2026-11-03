---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.497878+05:30
arxiv_id: 2610.42136
url: https://huggingface.co/papers/2610.42136
arxiv_url: https://arxiv.org/abs/2610.42136
date: 2026-11-02
---

# ReLift: Dense 3D Tracking as Lifted Trajectory Repair

Dense 3D tracking from monocular video requires establishing point correspondences over time, estimating their depth, and inferring their trajectories during occlusion. Existing methods typically learn these tasks jointly, a demanding objective given the scarcity of 4D supervision. We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectories, with occluded segments simply interpolated, already rival dedicated 3D trackers using the same geometry. However, lifted trajectories inherit correspondence and depth errors, and under occlusion, their depth comes from the occluder rather than the tracked point. We introduce ReLift, an efficient feed-forward framework that recasts dense 3D tracking as geometric trajectory repair and completion. At its core, a trajectory corrector alternates attention along and across trajectories to preserve reliable observations, repair corrupted positions, and complete missing motion. Using only geometric inputs allows us to train directly on 3D trajectories with simulated lifting errors, decoupling training from images and from any specific tracker or geometry model. Concentrating 4D supervision on trajectory refinement yields a reusable model that consistently improves lifted trajectories across trackers and geometry providers without retraining, so it benefits directly from future advances in either component. On WorldTrack, ReLift achieves state-of-the-art mean accuracy, improving on the strongest baselines by 2.1 APD on all points and 3.0 on dynamic points, with faster configurations remaining competitive with leading 3D trackers while running faster than 4RC. Visit our supplementry page for more examples and code.
