# MiniMax M3 and Step 3.7 Flash: open-weight efficiency at the frontier

**Date:** 2026-06-03 (released over the 05-31/06-01 weekend)
**Source:** Twitter (@kilocode) → Kilo Code blog
**Links:** [Kilo writeup](https://kilo.codes/dNgp08L)
**Tier:** 1/2 — sparse attention, MoE efficiency, open weights (industry release, not a paper)

## TL;DR

Two Chinese labs dropped open-weight models the same weekend, both pushing cost-efficiency rather than raw capability. **MiniMax M3** is the headline for this wiki: it claims to be the first open-weight model to combine a 1M-token context window, frontier coding/agentic performance, and native multimodality in one system. The efficiency engine is **MiniMax Sparse Attention (MSA)**, which cuts per-token compute at 1M context to roughly 1/20th of the previous generation, giving ~9x faster pre-filling and ~15x faster decoding. **Step 3.7 Flash** (StepFun) is a 196B-parameter MoE that sparsely activates only ~11B per token, with a 256K window, selectable reasoning tiers, and an Apache 2.0 license; early testers call it "as good as Gemini Flash 3.0 at half the cost."

```
MiniMax M3 — MiniMax Sparse Attention (MSA):
  dense attention @1M ctx:  O(per-token compute) = 1×   ─► prefill/decode bound
  MSA @1M ctx:              ≈ 1/20× per-token compute
                            ─► ~9× faster prefill · ~15× faster decode
  + 1M context · frontier coding/agentic · native multimodal · open weights

Step 3.7 Flash (StepFun):  196B total, ~11B active/token (MoE), 256K ctx, Apache-2.0
```

## Relation to prior wiki state

- **MSA is a production deployment of the exact sparse-attention-vs-eviction debate today's [VaSE](2026-06-03-vase-value-aware-stochastic-kv-eviction.md) paper is fighting over.** VaSE argues training-free *eviction* (static cache footprint) can match *selection-based sparse attention* (full cache, sparse attend) on reasoning tasks. MSA is sparse attention shipped at 1M context with order-of-magnitude prefill/decode wins. The academic debate and the production frontier are converging on the same lever: at long context, do not attend densely.
- **Confirms the [RTPurbo / "Full Attention Strikes Back"](2026-05-24-rtpurbo-full-to-sparse-attention.md) (05-24) thesis at scale.** RTPurbo argued full-attention LLMs are intrinsically sparse and the useful token budget is query-dependent, with ~9.36x prefill speedup at 1M. MSA's ~9x prefill / ~15x decode at 1M is the same regime arriving as a shipped open-weight model, not a research prototype.
- **Extends the wiki's [prompt-cache economics](kv-cache.md) thread.** The SemiAnalysis 05-01 framing was that frontier-lab unit economics now hinge on long-context serving cost. Two open-weight labs competing explicitly on tokens-per-dollar at 1M context is that economic pressure showing up in the open ecosystem, not just closed APIs.
- **The Step 3.7 Flash / M3 sparse-MoE pairing (196B/11B active; M3's MSA) continues the MoE-everywhere thread** the digest flagged as a concept-page gap (dMoE 06-01, κ-SwiGLU 06-02). Active-parameter counts an order of magnitude below total are now the default for cost-competitive open models.

## Gaps / caveats

- Marketing-grade claims from a vendor blog, not a paper: the 1/20 compute, 9x prefill, 15x decode figures are MiniMax's own and unaudited; no independent long-context quality benchmark at 1M is cited.
- MSA's accuracy cost at 1M (does the 1/20 compute hold retrieval and multi-hop accuracy, or only perplexity?) is not characterized in the available writeup.
- Step 3.7 Flash weights are Apache 2.0; M3 weights were "expected shortly" at writeup time, so M3's openness was not yet verifiable.

## Links

- Raw: `raw/twitter/2026-06-02-evening.md` (@kilocode thread) · Kilo blog https://kilo.codes/dNgp08L
- Related: [VaSE 06-03](2026-06-03-vase-value-aware-stochastic-kv-eviction.md) · [RTPurbo 05-24](2026-05-24-rtpurbo-full-to-sparse-attention.md) · [KV Cache](kv-cache.md)
