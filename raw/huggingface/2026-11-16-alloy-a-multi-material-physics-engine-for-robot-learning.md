---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.004678+00:00
arxiv_id: 2611.16312
url: https://huggingface.co/papers/2611.16312
arxiv_url: https://arxiv.org/abs/2611.16312
date: 2026-11-16
---

# Alloy: A Multi-Material Physics Engine for Robot Learning

Robots handle much more than rigid objects: towels, cables, water, sand. The simulators used to train robots at scale are strongest on rigid bodies, and adding another material usually means a second engine and hand-written glue between the two. We present Alloy, an open-source physics engine for robot learning in which rigid robots, cloth, cables, liquids, granular material and soft bodies share one scene. Each object is described once; Alloy assigns it to a solver suited to its material, couples the solvers inside every control step, and runs the scene in many parallel worlds on one GPU, or on a CPU. Every world carries a health grade, to help tell a failure of the physics from a failure of the policy. Alloy is built on Newton, MuJoCo Warp and Warp, and it is written to be driven by coding agents: its documentation ships inside the package, every error names its fix, and the engine is exposed as tools over the Model Context Protocol. In a cold test, agents that had never seen Alloy installed a pre-release from the package index and trained policies for walking, cable handling and pouring on a single GPU. We also report how throughput grows with the number of worlds, depth-camera throughput, agreement with closed-form references, and a reliability test over a thousand worlds.
