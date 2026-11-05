---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.361667+05:30
arxiv_id: 2611.02079
url: https://huggingface.co/papers/2611.02079
arxiv_url: https://arxiv.org/abs/2611.02079
date: 2026-11-04
---

# ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost

Harness optimization can substantially improve LLM agents without modifying model weights, but existing methods primarily optimize response quality. Extending them to joint quality--cost optimization introduces a challenge: applying the deployment preference during intermediate updates can prematurely reject candidates that are valuable for later improvements. We introduce ParetoSaddler, which addresses this mismatch by separating intermediate candidate promotion from final deployment selection. At each iteration, an optimizer updates a parent harness to produce a candidate, and then compares the two over repeated executions and uses Bayesian bootstrap Pareto support to promote candidates showing credible progress in either quality or cost. Promoted candidates receive broader development evaluation and remain available as parents for later optimization steps. We evaluate ParetoSaddler on ClawMark and GAIA2 using domain-disjoint splits. On ClawMark, ParetoSaddler improves quality from 70.86\% to 81.35\% while reducing cost from \1.17 to 1.01 per task; on GAIA2, it improves quality from 56.22\% to 62.89\% while reducing cost from \0.78 to 0.45 per task. The Pareto-selected harnesses also achieve higher quality at lower cost than quality-only harness optimization. Analysis shows that Pareto-aware optimization retains intermediate candidates that would be discarded by deployment preference but can support later improvements, while Bayesian bootstrap screening filters out candidates whose gains are weakly supported across runs.
