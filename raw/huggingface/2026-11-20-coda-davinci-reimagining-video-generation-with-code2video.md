---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.382312+00:00
arxiv_id: 2611.26595
url: https://huggingface.co/papers/2611.26595
arxiv_url: https://arxiv.org/abs/2611.26595
date: 2026-11-20
---

# Coda-DaVinci: Reimagining Video Generation with Code2Video

Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompting. The results reveal task-dependent trade-offs: coarse proxies favor natural motion, while medium-grained proxies favor consistency. Physics simulation and proxy-aligned prompting further improve average quality. Guided by these findings, we introduce Coda-DaVinci, a task-adaptive agentic framework for Code2Video generation that selects between proxy-guided and direct generation, adapts modeling granularity to each entity, and coordinates simulation with proxy-grounded prompting. Its multi-agent harness preserves scene assets and guides repairs through visual inspection and independent review. Experiments demonstrate leading instruction following on VTR and scene consistency on R2M, improved physical plausibility over direct generation, and higher visual realism than the compared Code2Video baselines. Long-video evaluations further show gains in event structure and consistency across successive interactions, while revealing limitations in transition stability and adherence to scene settings.
