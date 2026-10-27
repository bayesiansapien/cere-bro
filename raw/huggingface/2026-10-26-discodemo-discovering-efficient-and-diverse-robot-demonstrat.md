---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.799556+00:00
arxiv_id: 2610.32093
url: https://huggingface.co/papers/2610.32093
arxiv_url: https://arxiv.org/abs/2610.32093
date: 2026-10-26
---

# DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

Behavior cloning for robotic manipulation is highly sensitive to the coverage of its training data, yet collecting diverse successful demonstrations remains costly. We study reinforcement learning (RL) not as a deployable controller, but as a data generator for downstream visuomotor imitation learning. Our key premise is that multiple successful solution modes cover a broader range of successful trajectories than repeatedly collecting a single narrow solution. We introduce DiscoDemo, which trains a privileged latent-conditioned RL generator with a parallel reverse curriculum and a success-gated diversity objective to discover diverse solutions while preserving task success. The trained generator produces multiple successful closed-loop behaviors, which are safety-filtered and exported as a static dataset for downstream imitation learning. Across four manipulation tasks, DiscoDemo produces broader successful-state coverage and improves downstream visuomotor policies in both simulation and the real world. Averaged across tasks, downstream success increases to 62% from 40% for the strongest baseline in simulation, and to 78% from 39% on the real robot, respectively. These results suggest that successful solution diversity improves imitation learning for a pretrained flow-matching VLA and remains complementary to corrective data collection. Project page: https://davian-robotics.github.io/DiscoDemo
