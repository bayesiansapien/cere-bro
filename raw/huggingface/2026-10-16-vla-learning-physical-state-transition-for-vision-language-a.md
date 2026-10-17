---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21306
url: https://huggingface.co/papers/2610.21306
arxiv_url: https://arxiv.org/abs/2610.21306
date: 2026-10-16
---

# VLA-Δ: Learning Physical State Transition for Vision-Language-Action Models

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks. However, most VLAs directly map observations to demonstrated actions without explicit supervision of intermediate physical state changes, making them prone to overfitting observation-action correspondences. Some methods introduce intermediate reasoning or future-state prediction in language, visual, or latent spaces to guide action generation, but do not explicitly supervise the physical state transition itself. We therefore propose VLA-Δ, a general framework that uses physical changes between current and future states as explicit learning targets. To support this objective, we construct a large-scale pretraining dataset and derive physical state-transition annotations covering task-relevant semantics and visual motion changes, providing more direct supervision for continuous action generation. During inference, the model generates actions directly from current observations without additional inference overhead. VLA-Δ achieves performance competitive with the state of the art on LIBERO and RoboTwin, and outperforms π_{0.5} in real-robot experiments. Our code is available at https://github.com/ZJU-OmniAI/VLA-Delta
