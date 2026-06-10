---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.05304
url: https://huggingface.co/papers/2606.05304
arxiv_url: https://arxiv.org/abs/2606.05304
date: 2026-06-10
---

# What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems

Multi-agent systems (MAS) built on large language models are typically organized around roles, pipelines, and turn schedules, while the content that agents pass to one another is often left as unconstrained natural language. However, this free-form communication can rapidly inflate token usage, consume the shared context window, and ultimately affect both system performance and inference cost. We analyze five common inter-agent communication strategies across two MAS topologies, finding that no fixed strategy is universally optimal. Instead, effective inter-agent messages consistently preserve action-centered information needed by downstream agents. Building on this, we propose the PACT (Protocolized Action-state Communication and Transmission), which treats inter-agent communication as a public state-update problem and projects each raw agent output into a compact action-state record before it enters shared history. Across different MAS topologies, PACT consistently improves the performance-cost trade-off, achieving comparable or stronger task performance with substantially fewer tokens. The gains extend to production coding harnesses: PACT lifts OpenHands' resolve rate at -10% tokens-per-resolved, and is resolve-neutral on SWE-agent while halving input tokens. Our code is publicly available at https://github.com/iNLP-Lab/PACT.
