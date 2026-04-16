---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2511.04671
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2511.04671
published: 2026-04-16
authors: Maximus A. Pace, Prithwish Dan, Chuanruo Ning
---

# X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations

**arXiv:** https://arxiv.org/abs/2511.04671
**Authors:** Maximus A. Pace, Prithwish Dan, Chuanruo Ning

## Abstract

arXiv:2511.04671v2 Announce Type: replace-cross  Abstract: Human videos are a scalable source of training data for robot learning. However, humans and robots significantly differ in embodiment, making many human actions infeasible for direct execution on a robot. Still, these demonstrations convey rich object-interaction cues and task intent. Our goal is to learn from this coarse guidance without transferring embodiment-specific, infeasible execution strategies. Recent advances in generative modeling tackle a related problem of learning from low-quality data. In particular, Ambient Diffusion is a recent method for diffusion modeling that incorporates low-quality data only at high-noise timesteps of the forward diffusion process. Our key insight is to view human actions as noisy counterparts of robot actions. As noise increases along the forward diffusion process, embodiment-specific differences fade away while task-relevant guidance is preserved. Based on these observations, we present X-Diffusion, a cross-embodiment learning framework based on Ambient Diffusion that selectively trains diffusion policies on noised human actions. This enables effective use of easy-to-collect human videos without sacrificing robot feasibility. Across five real-world manipulation tasks, we show that X-Diffusion improves average success rates by 16% over naive co-training and manual data filtering. The project website is available at https://portal-cornell.github.io/X-Diffusion/.
