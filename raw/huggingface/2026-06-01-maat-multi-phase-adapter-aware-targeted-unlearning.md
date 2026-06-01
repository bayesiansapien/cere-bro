---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.30514
url: https://huggingface.co/papers/2605.30514
arxiv_url: https://arxiv.org/abs/2605.30514
date: 2026-06-01
---

# MAAT: Multi-phase Adapter-Aware Targeted Unlearning

Machine unlearning evaluation is structurally skewed: Why-type questions, which probe causal and relational knowledge, comprise less than 0.06% of CounterFact, 0.6% of ZSRE, and less than 1.3% of TOFU, MUSE, and WMDP-Cyber. This near-zero representation means that methods that fail on causal knowledge can score highly in aggregate, and this failure is undetectable without balanced evaluation. We present 5WBENCH, a balanced 5,000-sample benchmark with 1,000 examples per 5W category (Who, What, When, Where, Why), making causal unlearning failures quantifiable for the first time. Using 5WBENCH, we show that no existing baseline simultaneously achieves high forgetting and high retention on Why-type questions: aggressive forgetting degrades retained knowledge, while conservative methods fail to forget causal facts. We present MAAT (Multi-phase Adapter-Aware Targeted Unlearning), a three-phase framework operating on LoRA adapter weights, combining gradient-projected ascent, SVD rank-dimension pruning, task vector negation, and hybrid KL-hidden-state retain repair.
