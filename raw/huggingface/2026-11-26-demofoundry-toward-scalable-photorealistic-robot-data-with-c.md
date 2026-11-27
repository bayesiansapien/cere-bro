---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.909545+00:00
arxiv_id: 2611.34671
url: https://huggingface.co/papers/2611.34671
arxiv_url: https://arxiv.org/abs/2611.34671
date: 2026-11-26
---

# DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering

Scaling robot learning requires demonstrations that combine realistic visual observations with reliable action supervision. Simulation-based synthesis faces a substantial visual gap relative to real environments, while video-only generation struggles to maintain physically consistent interactions and provide aligned action labels. We present DemoFoundry, an automated framework that couples coding agents with generative rendering to synthesize photorealistic and physically grounded robot demonstrations. Coding agents both construct aligned real--proxy video pairs from existing robot episodes to train a video renderer and write executable interaction programs to generate new demonstrations. Given a scene reference and task instruction, an agent reconstructs task-relevant geometry and writes a control program without requiring target-task human demonstrations. Program execution in a physics simulator produces proxy videos with aligned robot states and actions. The video renderer translates these proxy videos into scene-consistent, photorealistic observations, reducing the need for detailed appearance modeling in each scene. Automated task-execution checks select successful trajectories for rendering and policy learning. Experiments show improved visual quality and action--video consistency. Policies trained on the generated demonstrations outperform raw-simulation training and approach the performance of training on an equal number of real demonstrations.
