---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.887244+00:00
arxiv_id: 2610.28950
url: https://huggingface.co/papers/2610.28950
arxiv_url: https://arxiv.org/abs/2610.28950
date: 2026-10-23
---

# HyperDrone: Simulation-to-Reality Transfer at Millions of Frames per Second

We present HyperDrone, an extremely fast quadrotor simulator focused on high-performance batch rendering that is more than 20x faster than existing state-of-the-art batch quadrotor simulators. HyperDrone combines highly optimized multirotor dynamics with HyperLux, a new ray-tracing engine that supports Nvidia OptiX, Vulkan, Apple Metal and WebGPU backends that takes full advantage of modern ray-tracing hardware, capable of running both components entirely on the GPU. HyperLux renders RGB, depth, semantic/instance segmentation, surface normals and optical flow observations at configurable levels of fidelity, including reflections, realistic lighting, motion blur, anti-aliasing, and Physically Based Rendering (PBR). Even in the highest-fidelity settings, HyperLux achieves millions of Frames Per Second (FPS) on consumer-grade GPUs while rendering realistic 3D scenes. We demonstrate the merits of HyperDrone by training a vision-based yaw-control policy purely in simulation and transferring it to a real small-scale quadrotor (Crazyflie) with a camera, running completely onboard.
