---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.389813+00:00
arxiv_id: 2611.25604
url: https://huggingface.co/papers/2611.25604
arxiv_url: https://arxiv.org/abs/2611.25604
date: 2026-11-20
---

# PAD: Policy-Aware Data Valuation for Autonomous Driving

End-to-end autonomous driving increasingly depends on scaling training demonstrations, yet data growth does not guarantee proportional gains. However, additional data do not guarantee better policies: a demonstration that benefits one planner may be redundant or harmful to another. Existing curation methods typically infer data value from intrinsic sample properties or training-dependent proxies that do not measure downstream policy utility. To address this, we introduce Policy-Aware Data Valuation (PAD), a framework that assigns each candidate demonstration a utility specific to the target driving policy. PAD combines scene-level calibration feedback with projected policy gradients and a regularized approximation of local training geometry, producing scalable influence-based values for the policy. A controlled group-removal study establishes the directional fidelity of these values, while cross-planner analysis shows that the same candidate pool induces markedly different rankings across planner families. On DiffusionDrive, PAD improves EPDMS over real-only training by 3.5 points on NavTest and 5.0 points on NavHard. Policy-specific curation consistently outperforms real-only and full-pool training across diffusion-, regression-, and flow-matching-based planners while substantially reducing scene-level regressions. These results establish policy-aware data valuation as a basis for replacing indiscriminate data accumulation with targeted policy improvement, enabling more efficient and reliable scaling of autonomous-driving systems.
