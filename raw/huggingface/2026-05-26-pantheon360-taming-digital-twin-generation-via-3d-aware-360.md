---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.25449
url: https://huggingface.co/papers/2605.25449
arxiv_url: https://arxiv.org/abs/2605.25449
date: 2026-05-26
---

# Pantheon360: Taming Digital Twin Generation via 3D-Aware 360° Video Diffusion

Generating complete digital twins from videos requires precise camera control, global scene coverage, and strict spatial-temporal consistency constraints that remain challenging for perspective video generators due to their limited field of view (FoV). Their narrow FoV forces long or multi-view trajectories, amplifying cross-view inconsistency and temporal drift. We argue that 360° video generation offers a natural solution: panoramic coverage simplifies trajectory design and provides a strong global context for maintaining coherence. We introduce Pantheon360: Taming Digital Twin Generation via 3D-Aware 360° Video Diffusion, a controllable 360° video generation framework that synthesizes high-fidelity videos from sparse 360° inputs. The key idea is an explicit 3D Cache, reconstructed from the input, which serves as a geometric scaffold for any user-defined camera path. This allows the diffusion model to focus on photorealistic texture refinement while the 3D Cache enforces global geometric consistency. Experiments show that Pantheon360 achieves superior visual quality and unmatched geometric coherence, enabling reliable and flexible 360° scene generation for downstream simulation and digital-twin applications.
