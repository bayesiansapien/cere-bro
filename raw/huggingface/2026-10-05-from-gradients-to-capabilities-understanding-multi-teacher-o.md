---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.02179
url: https://huggingface.co/papers/2610.02179
arxiv_url: https://arxiv.org/abs/2610.02179
date: 2026-10-05
---

# From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation

Multi-teacher on-policy distillation (MOPD) aims to combine the strengths of RL-trained teachers in a single student, but how teacher signals affect parameter changes remains underexplored. We study Qwen3-1.7B with four domain teachers trained with RL from the same initialization as the student, comparing gradients, optimizer updates, and task learning curves, with additional SmolLM3-3B diagnostics. We find that several factors influence teacher signals. First, loss averaging implicitly weights responses: token averaging favors longer responses, and equalizing domain contributions retains this weighting within domains. Second, Adam's first moment reduces differences in parameter updates: the cosine similarity is 0.83 between teachers and 0.96 between averaging rules, despite differences in raw gradients. Third, BF16 rounding hides small changes: about 97\% of FP32 master weights differ from initialization, but only 7--11\% of BF16 weights do. Finally, the top-64 intersection KL gradient closely matches Qwen's full-vocabulary gradient, but the effect on task performance depends on averaging: mathematics accuracy is 2.6 points higher than with sampled-token policy-gradient (PG) under response averaging and 2.1 points lower under global token averaging.
