---
source: farmer/huggingface
farmed: 2026-09-16T13:11:10.933414
arxiv_id: 2609.13770
url: https://huggingface.co/papers/2609.13770
arxiv_url: https://arxiv.org/abs/2609.13770
date: 2026-09-16
---

# Training Specialist Models without Reasoning Trajectories for Domain Expert Distillation

Specialist distillation effectively transfers domain expertise to student models via teacher-generated reasoning trajectories. However, when these specialists are trained solely on question--answer pairs without explicit reasoning supervision, what governs the trajectories they generate? In this work, we show that specialist optimization implicitly selects from this latent trajectory space. To isolate and observe this latent distribution, we leverage student distillation not as a downstream goal, but as an agnostic probe---since students inherit no parameterization or optimization constraints from the specialist, inheriting only the sampled trajectories themselves. Through this probe, our empirical analysis unveils a tight governing relationship: across 27 specialist--student pairings, their specialization--generalization profiles correlate exceptionally strongly. Crucially, explicitly controlling the specialist's distributional drift systematically shifts both the teacher and its distilled student along a controllable trade-off between domain precision and general-capability retention. Across chemistry, physics, and multilingual settings, distilled students systematically reflect these specialist-induced profiles, even across divergent model families. Our findings establish a new view of specialist training: when gold reasoning is absent, tuning choices directly control the latent supervision passed to downstream models.
