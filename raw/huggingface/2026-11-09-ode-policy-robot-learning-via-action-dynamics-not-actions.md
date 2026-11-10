---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.208808+00:00
arxiv_id: 2611.01729
url: https://huggingface.co/papers/2611.01729
arxiv_url: https://arxiv.org/abs/2611.01729
date: 2026-11-09
---

# ODE Policy: Robot Learning via Action Dynamics, Not Actions

Most robot policies, whether trained by imitation learning (IL) or reinforcement learning (RL), map observations to action values at discrete control steps and leave the continuity of physical motion to be learned implicitly. We propose ODE policy, which learns the dynamics of the action rather than the action itself. A neural ordinary differential equation (ODE) learns the vector field of the action by matching the integrated actions to the targets over short action chunks in IL and single control steps in RL. A lightweight diversity head captures multi-modal behavior by randomizing the direction of the field. At deployment, each action is integrated from the previous one, so the executed trajectory is continuous by construction. We evaluate it as a visuomotor policy, as the action head of vision-language-action (VLA) and world action models (WAMs), and as the actor of model-based RL against 14 baselines on unimanual, bimanual, dexterous, locomotion, and loco-manipulation tasks. In IL, against flow matching, it reaches 5.9times the success, 5.4times the generalization, and 3.9times the mode balance after one epoch, and generates actions 10.8times faster. It mostly moves more smoothly than human demonstrations. On 14 real-world tasks across single-arm, dual-arm, dexterous, and humanoid robots, it achieves the highest success rate. In RL, it further speeds up SuperMimic for humanoid motion tracking and smooths its actions. Efficient in learning, data, parameters, and execution, ODE policy offers a promising path to scaling robot learning.
