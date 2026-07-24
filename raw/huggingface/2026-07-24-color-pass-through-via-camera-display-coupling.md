---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.12746
url: https://huggingface.co/papers/2607.12746
arxiv_url: https://arxiv.org/abs/2607.12746
date: 2026-07-24
---

# Color Pass-Through via Camera-Display Coupling

When a real-world scene is captured by a smartphone camera and viewed on its screen, the displayed image often differs noticeably from the original scene in color, brightness, and contrast. This gap persists despite substantial advances in both modern cameras and displays. A key reason is that most pipelines factor the high-dimensional capture-to-display process into two separately calibrated camera and display stages, and then connect them through low-dimensional color transforms, leading to information bottlenecks and inevitable error accumulation. To address this systemic challenge, we propose Color Pass-Through, an end-to-end learned framework that operates directly on captured images. Our key insight is to treat the camera and display as a coupled system rather than calibrating them in isolation. Coupling the camera and display yields two practical advantages: (1) it brings the entire real-world scenes to the display via end-to-end optimization, and (2) it allows efficient one-step calibration for each distinct observer via complete capture-to-display path. We validate Color Pass-Through using both digital and human observers. Compared with representative baselines, our method achieves an average gain of +2.0 points on a 5-point user study and more than 2x improvement on quantitative metrics, demonstrating improved reproduction of the perceived color of the original scene.
