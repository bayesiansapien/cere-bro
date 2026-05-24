---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.19990
url: https://huggingface.co/papers/2605.19990
arxiv_url: https://arxiv.org/abs/2605.19990
date: 2026-05-24
---

# Minimalist Visual Inertial Odometry

Visual-Inertial Odometry(VIO), which is critical to mobile robot navigation, uses cameras with a large number of pixels. Capturing and processing camera images requires significant resources. This work presents a minimalist approach to planar odometry, demonstrating that just four visual measurements and an IMU can provide robust motion estimation for differential-drive robots. Our key insight is that four downward-facing photodiodes that sense the world through optical Gabor masks produce signals that encode speed. Based on this, we jointly optimize the mask parameters alongside a Temporal Convolutional Network (TCN) using a physically-grounded simulator. The resulting model decodes speed from just the four measurements produced by the photodiodes. Pairing these estimates with the angular speed from an IMU yields a continuous planar trajectory. We validate our approach with a prototype sensor mounted on a differential drive robot. Across diverse indoor and outdoor terrains, our system closely tracks the reference ground truth without any real-world fine-tuning. Our work shows that minimalist sensing enables efficient and accurate planar odometry.
