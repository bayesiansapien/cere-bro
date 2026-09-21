---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.21749
url: https://huggingface.co/papers/2609.21749
arxiv_url: https://arxiv.org/abs/2609.21749
date: 2026-09-21
---

# GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills

Skills can improve the performance of Large Language Model (LLM) agents by providing task-specific procedural guidance, while skill optimization further improves their effectiveness through iterative refinement. However, existing skill optimization methods typically represent skills as unstructured natural-language instructions, creating two key challenges: 1) Unstructured skills often lack explicit workflow-level guidance and contain substantial redundancy, making them difficult for LLMs to execute; 2) the vast search space of unconstrained natural-language skills makes skill optimization ineffective. To address these challenges, we propose representing skills as graph-structured natural-language artifacts. In graph-structured skills, each node represents an execution step together with its operational guidance, while directed edges encode context-dependent transitions between steps. Compared to unstructured skills, graph-structured skills can provide clear workflow-level guidance. Moreover, the proposed graph-structured skill can also facilitate skill optimization. Building on this structured representation, we introduce GraphSkillEvo, a population-based evolutionary optimization framework with mutation and crossover operators for graph-structured skills. By maintaining multiple candidate skills and combining effective components, GraphSkillEvo enables broader and more comprehensive exploration of the structured skill space than purely LLM-based iterative self-refinement. Extensive experiments across five agent benchmarks demonstrate that GraphSkillEvo consistently outperforms the strong skill optimization baseline SkillOpt, improving average accuracy by 4.01% on GPT-5.4-nano and 1.76% on GPT-5.4. Our code is available at https://github.com/ruisun7/GraphSkillEvo.
