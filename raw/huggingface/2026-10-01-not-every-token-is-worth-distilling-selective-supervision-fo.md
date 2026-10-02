---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350670+05:30
arxiv_id: 2609.29142
url: https://huggingface.co/papers/2609.29142
arxiv_url: https://arxiv.org/abs/2609.29142
date: 2026-10-01
---

# Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD

Direct On-Policy Distillation (Direct-OPD) transfers reinforcement-learning-induced policy improvements from a small model to a larger student by using the token-level log-ratio between post-RL and pre-RL checkpoints as dense supervision on the student's own rollouts. This transfer rewards the policy shift at every state, yet the log-ratio measures only relative change: it can stay fixed even as the probability mass that both checkpoints assign to the student's candidate tokens vanishes. Through an exact construction, we show that the Direct-OPD reward and its update can remain unchanged while the Jensen-Shannon divergence (JSD) and both KL directions between the checkpoints vanish with this mass, and we note that a small JSD bounds how much the teacher's behavior changed. Motivated by this analysis, we propose Selective Supervision for Direct-OPD (S^2D-OPD), which ranks student-sampled states by their teacher-reference JSD and masks Direct-OPD supervision at low-divergence states, retaining only the top 10% of states per response. Across two teacher pairs and four student models ranging from 1.7B to 8B parameters, S^2D-OPD improves held-out accuracy over dense Direct-OPD on AIME and HMMT benchmarks in seven of eight settings and matches it in the eighth, without extra forward passes.
