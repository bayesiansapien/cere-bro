---
source: farmer/huggingface
farmed: 2026-07-28T03:19:32Z
arxiv_id: 2607.24280
url: https://huggingface.co/papers/2607.24280
arxiv_url: https://arxiv.org/abs/2607.24280
date: 2026-07-28
---

# From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search

Agentic search enables large language models to solve knowledge-intensive tasks by interleaving multi-step reasoning with retrieval, yet optimizing this with outcome-based reinforcement learning (RL) provides only sparse supervision. Knowledge distillation can supply denser guidance, and advanced proprietary models with their strong reasoning capabilities are promising teachers. While distilling from proprietary models can densify this supervisory signal, conventional logit-matching is precluded by hidden logits and mismatched tokenizers, whereas raw natural language trajectory imitation transfers superficial stylistic artifacts rather than core reasoning competence. To address the heterogeneous distillation problem and bridge the distribution gap, we propose Multi-Agent Protocol Distillation (MAPD), a joint distillation and RL framework uses a structured, style-normalized protocol as an intermediate representation. An offline multi-agent system (MAS) decomposes each query, retrieves supporting evidence, repairs failed searches, and converts the resulting exploration trace into a JSON protocol containing the task type, reasoning plan, and extractive grounding facts. During training, the protocol is provided only to a privileged branch of the student policy, whose token distributions furnish a dense distillation signal alongside the sparse RL objective. Extensive evaluations across seven QA benchmarks demonstrate that MAPD consistently outperforms competitive distillation and RL, achieving average success rates of 39.4% on Qwen3-1.7B and 44.4% on Qwen3-4B. Crucially, the framework generalizes robustly across diverse proprietary teachers while effectively mitigating the student policy from style drift and verbosity degeneration.
