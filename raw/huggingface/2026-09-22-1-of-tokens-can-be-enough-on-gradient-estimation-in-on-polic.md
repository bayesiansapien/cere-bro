---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.24432
url: https://huggingface.co/papers/2609.24432
arxiv_url: https://arxiv.org/abs/2609.24432
date: 2026-09-22
---

# 1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation

Sparse on-policy distillation (OPD) allocates teacher supervision to a small subset of tokens in student-generated trajectories. However, useful teacher guidance can yield a noisy update when its gradient is estimated from a sampled next token. We study this estimation problem at a fixed prefix in information geometry and propose an information-efficiency ratio (IER) based on a signal-to-noise decomposition. IER characterizes relative gradient estimation error under an optimal scalar baseline. A candidate-set approximation enables token selection based on IER and its combination with existing usefulness scores, while retaining the sampled reverse-KL training objective. On mathematical and medical reasoning tasks, adding IER improves existing selectors in multiple settings, with sparse configurations matching or exceeding full OPD without token selection at small token budgets of 0.1\%--1\%. These results support accounting for both usefulness and gradient-estimation reliability when allocating sparse supervision. Our code is available at https://github.com/BruceSheng1202/IER-OPD.
