---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.416888+00:00
arxiv_id: 2610.11287
url: https://huggingface.co/papers/2610.11287
arxiv_url: https://arxiv.org/abs/2610.11287
date: 2026-10-09
---

# REMORY: Learning Residual Memory for Context Compaction

Long-horizon agents compact their history to continue within a finite context window, but a textual summary alone may not support every subsequent decision. We introduce REMORY, a neural memory network that supplements the summary with a bounded sequence of soft memory tokens. Given the history and summary, the network learns to generate tokens that help a frozen LLM approximate the continuation it would produce with the full history. The tokens are conditioned on the summary and appended after it, forming an analogue of a residual connection along the sequence dimension. On SummHay, REMORY improves source attribution at nearly unchanged insight coverage and approaches the full-context joint score using only 5.2% of the input positions. Across long-horizon agent benchmarks, Qwen3.8-27B and GLM-5.3-Flash show consistent gains with residual memory. Both models also exhibit substantially fewer repeated tool outputs and tool errors on BrowseComp and Terminal-Bench 2.1.
