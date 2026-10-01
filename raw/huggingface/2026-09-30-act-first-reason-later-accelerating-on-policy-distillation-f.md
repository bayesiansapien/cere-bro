---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36608
url: https://huggingface.co/papers/2609.36608
arxiv_url: https://arxiv.org/abs/2609.36608
date: 2026-09-30
---

# Act First, Reason Later: Accelerating On-Policy Distillation for Multi-Turn Agents via Reference-Conditioned Inverse Dynamics

On-policy distillation (OPD) trains multi-turn language agents with dense teacher supervision on student-generated responses. However, standard think-then-act rollouts require lengthy reasoning before each short action, delaying environment transitions and experience collection. Generating actions directly reduces this delay but can degrade rollout quality. To address this, we propose ActFirst-OPD, an act-first, reason-later training framework that decouples environment interaction from full-response generation. The student infers and executes actions through reference-conditioned inverse dynamics using its current interaction context and a reference next observation, and switches to autonomous next-action prediction when the resulting transition deviates from the reference trajectory. From the collected interaction contexts, the student asynchronously generates full think-then-act responses for token-level teacher supervision. Experiments across 0.6B-, 1.7B-, and 4B-parameter Qwen3 students show that ActFirst-OPD achieves average wall-clock training speedups of 2.3times on ALFWorld, 1.8times on WebShop, and 4.9times on ScienceWorld over Vanilla OPD. It matches or exceeds all compared OPD baselines in mean task success rate across eight of nine benchmark-model settings. These results demonstrate that reasoning need not block acting during multi-turn agent distillation.
