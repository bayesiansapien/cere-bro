---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35514
url: https://huggingface.co/papers/2609.35514
arxiv_url: https://arxiv.org/abs/2609.35514
date: 2026-09-30
---

# One Proposal for Every Margin: Zero-Shot Amortized Sequential Importance Sampling for Binary Matrices

In ecology, psychometrics, and the analysis of social and financial networks, binary matrices are often analyzed conditional on their observed row and column sums, which restricts the problem to a finite sample space of matrices with the same margins. Two fundamental problems are to count this space and to sample uniformly from it. Sequential importance sampling (SIS) addresses both with independent weighted samples and an unbiased count estimator, but its efficiency depends critically on the proposal distribution. Existing proposals are analytically designed, and their accuracy can vary substantially with the margins. We show that the ideal SIS proposal, under which every weight equals the count and the variance vanishes, is exactly the policy of a generative flow network (GFlowNet) with unit reward on every matrix that has the given margins. We therefore propose MarginFlow, a framework that turns the design of the proposal into a learning problem and amortizes it across margins by exploiting their self-similarity. Every partial matrix is itself an instance with reduced margins, so one set transformer that reads the remaining margins serves every margin. We train MarginFlow on a pool of 1904 margins and evaluate it zero-shot on 1190 held-out margins, synthetic and real, from 3times3 to 870times6. On 1187 of the 1190 margins it matches or beats the best of 31 analytically designed configurations, chosen post hoc for each margin, and its median effective sample fraction is 99.8%. On the 56 margins where that best loses more than one nat of effective sample size, MarginFlow wins every one and raises the median effective sample fraction from 10.3% to 94.1%.
