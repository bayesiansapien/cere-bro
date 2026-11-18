---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.113300+00:00
arxiv_id: 2611.17610
url: https://huggingface.co/papers/2611.17610
arxiv_url: https://arxiv.org/abs/2611.17610
date: 2026-11-17
---

# More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs

Evaluations of multi-agent language models often compare communicating architectures against a single greedy pass. This practice confounds coordination with sample multiplicity and inference compute. We synthesize nine primary empirical evaluations comprising 516 unique multi-agent configurations organized along a resource vector R with six dimensions and a baseline ladder with four categories. Against baselines with a single pass (Category A), multi-agent accuracy differences are negative overall and near zero when omitting the largest contributing study. When evaluated against baselines matched on sample count (Category B) or resource budget (Category C), multi-agent systems average -0.042 in accuracy, and multilevel random effects modeling on the log odds scale remains negative across sensitivity checks. Multi-agent accuracy equals or falls below the baseline in 74% of these comparable contrasts, and study means are nonpositive in almost all evaluated studies. Across studies reporting both baselines, moving from a greedy pass to a sampled baseline shifts accuracy differences by -0.038 on average. Because communication adds no information when agents share identical evidence, positive returns require partitioned evidence, external verification, or error diversity across models. We provide a reviewer checklist and accounting utilities.
