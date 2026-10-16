---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.225350+05:30
arxiv_id: 2610.19698
url: https://huggingface.co/papers/2610.19698
arxiv_url: https://arxiv.org/abs/2610.19698
date: 2026-10-15
---

# RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios

Large language models (LLMs) increasingly tackle complex real-world tasks in specialized domains. However, identifying and correctly applying domain-specific rules remains challenging when scenario information is distributed across multiple files. Existing rule-reasoning benchmarks typically represent scenarios using only a few factual statements, simplifying the identification and application of relevant rules. To address this gap, this paper introduces RuleTrek, a multi-domain benchmark for agentic rule reasoning in complex scenarios. Its rule-grounded construction pipeline extracts structured rule graphs, generates and incrementally composes rule-specific sub-scenarios while ensuring consistency and solvability. To systematically evaluate agentic rule reasoning in complex scenarios, RuleTrek assesses three capabilities in interactive workspaces: Rule Identification (RI), Rule Deduction (RD), and End-to-End Rule Reasoning (E2E). Experiments on 11 frontier LLMs show that the highest RI and RD scores are only 62.47\% and 60.43\%, respectively, while E2E scores range from 26.97\% to 55.29\%. These results demonstrate that current LLM agents face substantial challenges in rule reasoning over complex scenarios. We make our code and dataset publicly available at https://github.com/yuan247/RuleTrek{RuleTrek}.
