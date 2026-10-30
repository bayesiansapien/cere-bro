---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.923703+05:30
arxiv_id: 2610.31670
url: https://huggingface.co/papers/2610.31670
arxiv_url: https://arxiv.org/abs/2610.31670
date: 2026-10-29
---

# Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

Robot foundation models are typically evaluated through costly closed-loop rollouts, motivating low-cost offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To test this, we propose Sensorimotor Alignment (S^2), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that S^2 correlates positively with downstream robot task success across model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. S^2 can also identify promising vision-language model (VLM) backbones before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, S^2 offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With S^2, we extend PRH to robotics and make sensorimotor alignment measurable, offering a low-cost, representation-level view of robot foundation models that closed-loop success rates alone cannot reveal.
