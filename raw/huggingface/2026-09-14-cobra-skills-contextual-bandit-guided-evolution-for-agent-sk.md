---
source: farmer/huggingface
farmed: 2026-09-14T06:17:21.172209+00:00
arxiv_id: 2609.11682
url: https://huggingface.co/papers/2609.11682
arxiv_url: https://arxiv.org/abs/2609.11682
date: 2026-09-14
---

# COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization

Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce COBRA-Skills, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space. COBRA-Skills couples contextual-bandit-guided prioritization with evidence-grounded skill evolution, selectively allocating evaluations to promising or informative candidates while continually refining the skill population from execution feedback. Across six heterogeneous agent benchmarks and three target models, COBRA-Skills consistently achieves the strongest average performance among compared methods, while reducing optimization cost by 55--58\% relative to SkillOpt and using only 50 unique optimization examples per benchmark. Further analyses show that COBRA-Skills remains robust to changes in the agent harness and performs effectively when the target model itself is used for skill generation and refinement.
