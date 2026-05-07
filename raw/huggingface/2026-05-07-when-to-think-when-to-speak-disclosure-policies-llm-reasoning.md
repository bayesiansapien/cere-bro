---
source: farmer/huggingface
farmed: 2026-05-08T00:00:00Z
arxiv_id: "2605.03314"
url: https://huggingface.co/papers/2605.03314
arxiv_url: https://arxiv.org/abs/2605.03314
date: 2026-05-07
---

# When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning

In single-stream autoregressive interfaces, the same tokens both update the model state and constitute an irreversible public commitment. This coupling creates a silence tax: additional deliberation postpones the first task-relevant content, while naive early streaming risks premature commitments that bias subsequent generations. We introduce Side-by-Side (SxS) Interleaved Reasoning, which makes disclosure timing a controllable decision within standard autoregressive generation. SxS interleaves partial disclosures with continued private reasoning in the same context, but releases content only when it is supported by the reasoning so far. To learn such pacing without incentivizing filler, we construct entailment-aligned interleaved trajectories by matching answer prefixes to supporting reasoning prefixes, then train with SFT to acquire the dual-action semantics and RL to recover reasoning performance under the new format. Across two Qwen3 architectures/scales (MoE Qwen3-30B-A3B, dense Qwen3-4B) and both in-domain (AIME25) and out-of-domain (GPQA-Diamond) benchmarks, SxS improves accuracy-content-latency Pareto trade-offs under token-level proxies (e.g., inter-update waiting).
