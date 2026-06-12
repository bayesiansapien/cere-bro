---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.08039
url: https://huggingface.co/papers/2606.08039
arxiv_url: https://arxiv.org/abs/2606.08039
date: 2026-06-12
---

# MuJoCo-Drones-Gym: A GPU-Accelerated Multi-Drone Simulator for Control and Reinforcement Learning

Robotic simulators are a cornerstone of modern research in aerial robotics, serving both as a vehicle for the development of new control algorithms and as the data source for training reinforcement learning (RL) policies. Yet, existing quadcopter learning environments often face a trade-off between physical fidelity, multi-agent support, and the throughput required by modern deep RL pipelines. In this paper, we present MuJoCo-Drones-Gym, an open-source Gymnasium-compatible multi-drone environment built on top of the MuJoCo physics engine. MuJoCo-Drones-Gym supports an arbitrary number of Bitcraze Crazyflie 2.x nano-quadcopters and exposes a modular API for selecting (i)~the physics model (rigid-body MuJoCo, explicit Python dynamics, or any subset of ground effect, blade drag, and inter-drone downwash), (ii)~the action interface (per-motor RPMs, collective normalized thrust, velocity setpoints, or PID waypoint commands), and (iii)~the observation space (kinematic state vectors, RGB / depth / segmentation cameras, or neighbourhood adjacency information). A PettingZoo ParallelEnv wrapper enables drop-in multi-agent reinforcement learning, while a suite of seven task environments, hover, velocity tracking, multi-drone hover, waypoint navigation, formation flight, gate racing, and a generic multi-agent template, demonstrates the breadth of the interface. We describe the environment design, the underlying physics and quadcopter dynamics, and illustrate its use through control and learning examples that mirror those of the closely related gym-pybullet-drones project, while taking advantage of MuJoCo's improved contact handling, rendering, and parallelizability.
