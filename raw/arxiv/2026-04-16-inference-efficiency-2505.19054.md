---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2505.19054
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2505.19054
published: 2026-04-16
authors: Zhuochen Liu, Rahul Jain, Quan Nguyen
---

# RANDPOL: Parameter-Efficient End-to-End Quadruped Locomotion via Randomized Policy Learning

**arXiv:** https://arxiv.org/abs/2505.19054
**Authors:** Zhuochen Liu, Rahul Jain, Quan Nguyen

## Abstract

arXiv:2505.19054v2 Announce Type: replace  Abstract: Modern learning-based locomotion controllers typically rely on fully trainable deep neural networks with a large number of parameters. This paper studies a different design point for end-to-end control: whether effective quadruped locomotion can be achieved with a drastically reduced trainable parameter space. We present RANDomized POlicy Learning (RANDPOL), a policy learning approach in which the hidden layers of the actor and critic are randomly initialized and fixed, while only the final linear readout is trained. This yields a parameter-efficient controller class that retains nonlinear expressiveness through a fixed random basis while substantially reducing the dimension of the optimization problem. RANDPOL is supported by the mathematical foundation of randomized function approximation, which provides a principled basis for using fixed random nonlinear features as expressive function classes. We evaluate RANDPOL on end-to-end locomotion control for the Unitree Go2 quadruped and compare it with Proximal Policy Optimization (PPO). The results show that RANDPOL attains comparative locomotion performance with far fewer trainable parameters, lower learning-phase computation time per iteration, and a favorable performance-complexity trade-off. We further demonstrate successful zero-shot sim-to-real transfer of the learned RANDPOL controller on the physical Unitree Go2 under user-issued forward-velocity and yaw-rate commands. These results indicate that, for structured robotic control problems, reducing trainable complexity can remain compatible with effective simulated and real-world performance.
