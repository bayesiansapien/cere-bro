---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36601
url: https://huggingface.co/papers/2609.36601
arxiv_url: https://arxiv.org/abs/2609.36601
date: 2026-09-30
---

# SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation

On-policy distillation (OPD) reduces train-test state mismatch by training a student on its own generated trajectories, but weak students may visit teacher-misaligned prefixes where supervision is less representative. We introduce SAKI (Supervision Allocation with KL-constrained Interpolation), which combines a KL-constrained teacher-guided rollout with maximal coupling and reuses realized accept/correction events to route token-level supervision. Accepted positions retain sampled-token reverse-KL supervision, while correction positions receive direct supervision on the teacher's highest-probability token. Under maximal coupling, the correction probability is exactly TV(p_t, q_t), so the same trust-region radius controls rollout deviation and upper-bounds intervention and specialized-supervision frequency. We further implement an engine-resident speculative verifier that preserves the exact-q trajectory distribution and coupling semantics while improving matched-workload rollout throughput by 4.22x. Across seven mathematical reasoning benchmarks, SAKI improves the matched teacher-guided baseline in Mean@8 and Pass@8 for both 1.7B and 0.6B students. Placement controls and fixed-prefix analysis further support correction-triggered routing as a conflict-adaptive supervision signal.
