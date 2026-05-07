---
source: farmer/huggingface
farmed: 2026-05-08T00:00:00Z
arxiv_id: "2605.01234"
url: https://huggingface.co/papers/2605.01234
arxiv_url: https://arxiv.org/abs/2605.01234
date: 2026-05-07
---

# TT4D: A Pipeline and Dataset for Table Tennis 4D Reconstruction From Monocular Videos

We present TT4D, a large-scale, high-fidelity table tennis dataset. It provides 140+ hours of reconstructed singles and doubles gameplay from monocular broadcast videos, featuring multimodal annotations like high-quality camera calibrations, precise 3D ball positions, ball spin, time segmentation, and 3D human meshes over time. This rich data provides a new foundation for virtual replay, in-depth player analysis, and robot learning. The dataset's combination of scale and precision is achieved through a novel reconstruction pipeline. Prior methods first partition a game sequence into individual shot segments based on the 2D ball track, and only then attempt reconstruction. However, 2D-based time segmentation collapses under occlusion and varied camera viewpoints, preventing reliable reconstruction. We invert this paradigm by first lifting the entire unsegmented 2D ball track to 3D through a learned lifting network. This 3D trajectory then allows us to reliably perform time segmentation. The learned lifting network also infers the ball's spin, handles unreliable ball detections, and successfully reconstructs the ball trajectory in cases of high occlusion. This lift-first design is necessary, as our pipeline is the only method capable of reconstructing table tennis gameplay from general-view broadcast monocular videos. We demonstrate the dataset's fidelity through two downstream tasks: estimating the racket's pose and velocity at impact, and training a generative model of competitive rallies.
