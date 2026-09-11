---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.06702
url: https://huggingface.co/papers/2609.06702
arxiv_url: https://arxiv.org/abs/2609.06702
date: 2026-09-10
---

# PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents

Sequential memory agents process long documents by reading chunks one after another while maintaining a compact memory state, coupling document traversal to reasoning depth. This coupling introduces sensitivity to evidence placement and ties inference latency linearly to document length. We introduce PARSER, which decouples reading from reasoning. A bank of lightweight subagents each bound to a single chunk read the entire document in parallel, while a lead agent reasons in depth through iterative scatter--gather rounds: at each round it broadcasts a query to all subagents, aggregates the returned evidence, and formulates a deeper follow-up query conditioned on what has been found so far. This decoupled design concentrates all learnable behavior in the lead agent, which is optimized with reinforcement learning, while the subagents remain frozen off-the-shelf models. On multi-hop QA with contexts ranging from 7K to 896K tokens, PARSER with a 4B backbone outperforms the strongest sequential memory baseline by 5.7 points on average and by 12.0 points at 896K tokens. Scaling to a 9B backbone, PARSER surpasses DeepSeek-V4-Pro by 6.3 points. Controlled experiments confirm that PARSER is robust to perturbations in evidence position, order, and distance, conditions that cause large accuracy swings in sequential methods, while reducing inference latency by up to 11x.
