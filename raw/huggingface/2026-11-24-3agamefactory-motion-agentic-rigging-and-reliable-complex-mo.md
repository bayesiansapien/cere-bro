---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.918122+00:00
arxiv_id: 2611.30013
url: https://huggingface.co/papers/2611.30013
arxiv_url: https://arxiv.org/abs/2611.30013
date: 2026-11-24
---

# 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets

Animating arbitrary 3D assets from instructions requires both structural inference and motion control, yet existing motion benchmarks mostly cover conventional human or animal skeletons with simple instructions. We introduce DivDynBench, which evaluates rigging and motion generation across six morphology categories, with instructions requiring multi-phase part coordination and explicit timing, angle, repetition, and trajectory constraints. With large language models, we systematically compare three common paradigms: specialized motion generation, video generation followed by motion recovery, and direct agent-driven generation. We analyze their control capabilities, cross-morphology adaptability, and generation costs. Guided by this comparison, we propose an Agentic Motion Framework in which an agent writes compact parametric skeleton and motion programs, and a deterministic executor performs rigging, kinematic solving, and geometric correction. Compact parameter control reduces generation overhead and improves rigging reliability and motion-control accuracy, providing practical guidance for deploying complex 3D motion generation.
