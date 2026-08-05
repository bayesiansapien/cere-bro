---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.03874
url: https://huggingface.co/papers/2608.03874
arxiv_url: https://arxiv.org/abs/2608.03874
date: 2026-08-05
---

# ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficulty and opportunities for cross-task skill reuse. Our experiments show that sequential execution generally improves performance, but the gains vary substantially across models and domains. Moreover, in-context learning performs comparably to explicit skill maintenance on average, suggesting that much of the improvement arises from adaptation to prior context and feedback rather than reusable skill abstraction alone. Explicit skills nevertheless provide selective benefits for tasks requiring reusable procedures or precise outputs. We further find that less capable models tend to accumulate larger, more fragmented collections of task-specific skills. These findings show that current in-context skill evolution mechanisms can support continual adaptation, but still struggle to consistently consolidate experience into robust and transferable skills.
