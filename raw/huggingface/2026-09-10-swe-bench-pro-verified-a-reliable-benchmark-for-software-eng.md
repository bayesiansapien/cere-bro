---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.08149
url: https://huggingface.co/papers/2609.08149
arxiv_url: https://arxiv.org/abs/2609.08149
date: 2026-09-10
---

# SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents

SWE-Bench Pro has emerged as a standard benchmark for evaluating software engineering agents on challenging repository-level tasks. However, our analysis work show that its evaluation is undermined by two sources of unreliability: reward hacking, enabled by leakage of gold solutions or hidden evaluation information, and task quality issues, including misleading problem statements and improperly scoped tests. These issues can inflate benchmark performance and obscure agents' true coding ability. We present SWE-Bench Pro Verified, a verified version of SWE-Bench Pro that addresses both problems. Our approach combines anti-hacking safeguards that eliminate major leakage channels without disrupting normal agent functionality, with task refinement that minimally corrects inconsistencies within flawed instances. Evaluations on SWE-Bench Pro Verified reveal that some models perform substantially worse than previously reported, suggesting that existing results on SWE-Bench Pro may overestimate real software engineering capability. SWE-Bench Pro Verified offers a more trustworthy benchmark for assessing software engineering agents.
