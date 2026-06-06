---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.01886
url: https://huggingface.co/papers/2606.01886
arxiv_url: https://arxiv.org/abs/2606.01886
date: 2026-06-06
---

# Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents

Financial AI agents often fail for a simple reason: they make users carry the complexity. A user must repeatedly restate goals, risk preferences, portfolio context, past judgments, and shifting market assumptions, while the agent answers, retrieves, acts, and forgets. In finance, this is not just inconvenient. In tasks such as market analysis, copy-trading review, and trade preparation, forgotten context and stale memory can create latency, repeated errors, weak auditability, and unsafe decisions.
  We propose the interaction-native knowledge harness (InKH), an architecture for financial LLM agents that absorbs complexity into the system. InKH converts user, market, portfolio, and tool events into structured operational knowledge. It uses passive knowledge injection to assemble a bounded working context buffer before the main model step, temporal graph memory for low-latency retrieval, a wiki audit surface for human-readable governance, and background extraction with maturity, decay, and write-time invalidation.
  We evaluate InKH on a reproducible controlled synthetic benchmark with 24 random seeds, 4 rounds, 80 episodes per round, and 6 baselines, producing 46,080 baseline-conditioned evaluations. InKH achieves mean task quality of 0.815 at 900 ms latency. Compared with agent-driven wiki-walk memory, it reduces latency by 82.95 percent, token cost by 82.29 percent, and stale-knowledge usage by 96.58 percent, while improving quality by 0.108 and traceability by 0.461. Compared with a temporal-graph system without invalidation, it improves quality by 0.050 and reduces stale-memory usage by 96.58 percent with comparable serving cost.
  The results support a design thesis for financial AI: adoption happens when complexity is absorbed by the system rather than transferred to the user. The benchmark validates architecture-level behavior, not live trading performance.
