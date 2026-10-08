---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.01892
url: https://huggingface.co/papers/2610.01892
arxiv_url: https://arxiv.org/abs/2610.01892
date: 2026-10-07
---

# Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents

Multimodal agents commonly generate free-form reasoning before each action. For small models, limited model capacity can result in lengthy reasoning that provides little useful guidance for action generation while incurring substantial inference cost. To address this challenge, we introduce Selection-based Structured Reasoning (SSR), a framework that reformulates reasoning as selection instead of open-ended generation. SSR represents recurring high-level reasoning as pre-specified, reusable natural-language candidates. At each turn, the model selects from these reasoning candidates based on their likelihoods given the current context, without requiring an auxiliary task head. Using pre-specified reasoning traces enables parallel scoring, where teacher-forced prefilling computes token likelihoods concurrently within and across candidates using a shared context KV cache. We evaluate SSR on seven multimodal search benchmarks using 2B and 4B models. Across multiple reinforcement learning objectives and supervised fine-tuning, SSR delivers significant efficiency gains without sacrificing task performance. SSR achieves an average success rate competitive with leading search agents of the same scale, while reducing per-turn reasoning latency by over 90% and total per-question model inference latency by 28-54%. Project page: https://zfy0314.github.io/ssr-webpage/.
