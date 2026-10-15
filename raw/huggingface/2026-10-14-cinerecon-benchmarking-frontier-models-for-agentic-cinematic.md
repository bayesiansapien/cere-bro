---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.505186+00:00
arxiv_id: 2610.16577
url: https://huggingface.co/papers/2610.16577
arxiv_url: https://arxiv.org/abs/2610.16577
date: 2026-10-14
---

# CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction

Reconstructing reference videos as editable dynamic 3D scenes is an important path toward controllable video generation for filmmaking: these scenes provide modifiable, renderable visual proxies that enable explicit control over scene layout, subject actions, and camera behavior. To evaluate agents' ability to reconstruct editable dynamic 3D scenes from dynamic reference videos, we introduce CineRecon, a benchmark comprising 50 reference videos and 360 annotated evaluation clips. The reference videos span film, real-world footage, and games. Given a complete video, an agent uses tools to construct, animate, render, and refine its reconstruction. We evaluate this task under three representation settings: Proxy, Simplified, and Detailed. These settings increase geometric and appearance requirements while retaining the same requirements for spatial relations, camera behavior, and subject dynamics. This design tests whether agents can reproduce the events in a video when detailed appearance is unnecessary, and how performance changes as representation requirements increase. For evaluation, we construct checklists that associate observable properties and events with specific entities and times. A vision-language judge compares timestamp-aligned reference and rendered frames across 11 categories, grouped into camera, static, and dynamic consistency dimensions. We evaluate 12 models using their corresponding agent harnesses and find failures across all three dimensions. Subject motions and interactions remain difficult to reproduce even under the Proxy setting.
