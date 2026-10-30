---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.927621+05:30
arxiv_id: 2610.34186
url: https://huggingface.co/papers/2610.34186
arxiv_url: https://arxiv.org/abs/2610.34186
date: 2026-10-29
---

# HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

Extending Vision-Language-Action models (VLAs) to humanoid robots requires coordinated whole-body control and diverse demonstrations that are costly to collect in real-world scenarios. Although egocentric human demonstrations provide a complementary source of task experience, differences in visual embodiment and missing robot proprioception complicate transfer to humanoid policies. To address these challenges, we introduce HuGe, a family of Humanoid Generalist VLAs pre-trained on over 2,000 hours of egocentric human and robot data. Specifically, HuGe employs three existing representative VLA architectures to predict latent motion tokens for a pretrained whole-body controller, together with hand-control signals. Based on this, we introduce a three-stage training pipeline that combines egocentric pre-training, humanoid adaptation, and downstream fine-tuning. To facilitate transfer across embodiments, we construct pseudo-proprioceptive states through simulation playback during pre-training and modify arm appearance in egocentric observations through re-rendering during downstream fine-tuning. With this pipeline, HuGe achieves the state-of-the-art on simulation benchmark HumanoidArena. Furthermore, real-world experiments on the Unitree G1 indicate that augmenting robot demonstrations with visually adapted egocentric demonstrations significantly increases success on a pick-and-drop task.
