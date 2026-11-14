---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.532334+00:00
arxiv_id: 2611.16961
url: https://huggingface.co/papers/2611.16961
arxiv_url: https://arxiv.org/abs/2611.16961
date: 2026-11-13
---

# The Value of Thinking: Learning When to Reason in Hybrid Decision Models

Existing adaptive-reasoning methods shorten the explicit reasoning a model writes, or skip it by switching modes; either way the answer is still written out token by token. Rather than deciding how much to think, we explore a different paradigm, zero-or-T thinking: a single model either answers from the implicit thinking inside one forward pass, generating no token, or performs full autoregressive reasoning at a cost of T tokens when that is worth paying. We realise it in a hybrid decision model (HDM), where one frozen backbone serves both modes and a lightweight self-routing block chooses between them. The block estimates the value of thinking, the utility the slow mode is expected to add over the fast one, from what that implicit thinking has already produced, and the slow mode runs only where that value exceeds a price λ set per request. Where no per-decision label exists, as in episodic agentic tasks, we introduce Calibrated Decision Policy Optimisation (CDPO), a reinforcement-learning recipe that trains the block from episode-level returns. We evaluate HDM on MMLU-Pro, AGIEval, GPQA-Diamond, JevBench, BANKING77 and MiniWoB. Specifically, on JevBench HDM-4B scores 0.857 against Jev's 0.851 (+0.7%) at a median 0.179\,s against 0.652 (-72.5%). On the agentic venue MiniWoB HDM-27B cuts token cost by 80.1%.
