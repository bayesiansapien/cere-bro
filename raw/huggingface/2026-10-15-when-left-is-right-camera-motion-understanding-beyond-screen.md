---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.234031+05:30
arxiv_id: 2610.17242
url: https://huggingface.co/papers/2610.17242
arxiv_url: https://arxiv.org/abs/2610.17242
date: 2026-10-15
---

# When Left Is Right? Camera-Motion Understanding beyond Screen

Can a vision-language model tell left from right? Modern VLMs solve visual puzzles and follow hour-long videos, yet when asked whether the camera moved left or right, most do no better than a coin flip. Adding camera-motion data or geometric representations has been tried, separately, and neither closes the gap. We argue that camera-motion understanding needs two conditions at once: the representation must couple off-screen camera motion with on-screen flow dynamics, and it must be interpreted by the language model rather than trained as a standalone pose or depth estimator. We propose CameraVLM, which pairs a motion-state representation with state-language alignment. Camera tokens capture how the camera moves off screen, flow tokens capture how the subject and background move on screen, and a two-stage training strategy keeps language in the loop so that both are learned together with camera-motion semantics. With only 9B parameters, CameraVLM outperforms all open-source and camera-motion-specific models by a wide margin across three benchmarks and more than 20 baselines, and matches or surpasses GPT-6 Astra as well as human viewers in a 48-participant study. Project page: https://3dagentworld.github.io/CameraVLM/
