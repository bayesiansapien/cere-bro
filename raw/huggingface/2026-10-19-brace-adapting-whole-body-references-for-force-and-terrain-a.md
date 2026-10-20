---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.07052
url: https://huggingface.co/papers/2610.07052
arxiv_url: https://arxiv.org/abs/2610.07052
date: 2026-10-19
---

# BRACE: Adapting Whole-Body References for Force and Terrain Aware Humanoid Motion Tracking

Whole-body tracking has become the interface through which operators drive humanoid robots, yet the references it consumes are recorded on level ground and carrying nothing, so the tracker is aware of neither the forces the robot must exchange with objects nor the terrain it must stand on. Existing controllers address one side of this gap: force-capable policies command an end-effector force but prescribe no whole-body pose, while terrain-adaptive trackers treat loads as disturbances to reject rather than wrenches to command. We present BRACE, a whole-body tracker that exerts and compensates commanded hand forces from diverse poses while following a flat-ground reference on sloped terrain. Rather than leaving the tracker to absorb the load and the slope, BRACE folds both into the reference it follows: terrain conformance lifts footholds and root onto the local surface, and a wrench transformation resolves the hand displacement that produces a force jointly with the center-of-mass and center- of-pressure shifts it induces, bounded by teacher-specific arm-effort limits. Separate exertion and compensation teachers are distilled by DAgger into one flow-matching student that runs on proprioception alone, without a height map or measured wrench, so a teleoperator (even in remote locations) can supply a flat- ground trajectory and the robot resolves slope and load onboard. We extensive experiments on the Unitree-G1 to demonstrate the ability of BRACE to exert, compensate force and handle diverse terrain in simulation and real robot experiments.
