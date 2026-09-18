---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.20800
url: https://huggingface.co/papers/2609.20800
arxiv_url: https://arxiv.org/abs/2609.20800
date: 2026-09-18
---

# JEPA-Anything: Learning Predictive Models across Different Worlds

World modeling enables intelligence to anticipate consequences, guide interventions, and learn from interaction. Yet predictive models remain domain-specific: can a common learning principle support world modeling across radically different systems? We introduce JEPA-Anything, a domain-agnostic framework based on orthogonal predictive factorization (OPF). Extending joint-embedding predictive architectures, OPF decomposes latent targets into complementary factors, learns them through dedicated pathways, and recombines them within a shared predictive design. We evaluate JEPA-Anything across seven domains: vision, biology, clinical trajectories, control, molecular dynamics, physical fields, and weather. Experiments span representation learning, intervention prediction, out-of-distribution generalization, and long-horizon dynamics, including 10 matched dynamics tasks, forecasting of over 1,000 clinical events, and 100-step molecular rollouts across four systems. Against matched JEPA baselines, JEPA-Anything improves reported metrics on all 10 dynamics tasks and reduces single-intervention prediction error on Interventional Pong by 34.8%. It achieves the lowest one-step and 100-step molecular errors among compared methods in all four systems. Beyond prediction, a factor-nominated biological intervention receives experimental support in cell co-cultures, patient-derived organoids, tumor fragments, and mice; latent orbital modes recover the Keplerian scaling exponent with a fitted slope of -1.4991. These results support a common factorized predictive principle across heterogeneous worlds, connecting world modeling with intervention and experimentally grounded scientific discovery. Code: https://github.com/Gen-Verse/JEPA-Anything
