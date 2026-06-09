---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.03980
url: https://huggingface.co/papers/2606.03980
arxiv_url: https://arxiv.org/abs/2606.03980
date: 2026-06-09
---

# Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill

Reward models (RMs) provide critical feedback signals for LLM post-training, notably in reinforced fine-tuning (RFT) and reinforcement learning (RL) pipelines. However, current reward evaluation relies on heterogeneous criteria such as rule-based verifiers, ground-truth references, procedural checklists, and complex rubrics, where a unified mechanism to integrate all types of evidence remains unexplored. To this end, we propose Skill Reward Model (Skill-RM), a unified framework that reformulates reward modeling as the execution of a reusable Reward-Evaluation Skill. By treating reward computation as a structured agentic task, Skill-RM provides a consistent interface to orchestrate heterogeneous resources, dynamically selecting and aggregating evidence tailored to the specific requirements of each input. This approach enables the reward model to move beyond static evaluation, ensuring consistency and transparency across diverse tasks. Extensive experiments on reward benchmarks and downstream applications, including best-of-N selection and reinforcement learning, demonstrate that Skill-RM consistently outperforms traditional judge baselines. Our findings suggest that Skill-RM not only provides a unified solution for reward modeling but also achieves superior performance through the strategic and dynamic orchestration of evidence. The code is at https://github.com/Qwen-Applications/Skill-RM.
