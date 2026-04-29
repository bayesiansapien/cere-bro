# DeepSeek V4: Architecture and Industry Impact

**Date:** 2026-04-24  
**Sources:** [Ken Huang Analysis](https://kenhuangus.substack.com/p/deepseek-v4-the-next-frontier-of) · [AI Breakfast](https://aibreakfast.beehiiv.com) · [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5) · [DeepSeek API docs](https://api-docs.deepseek.com/news/news260424)  
**Raw:** raw/gmail/2026-04-25-starred.md · raw/gmail/2026-04-27-starred.md

---

## TL;DR

DeepSeek V4 (released April 24, 2026) is a two-variant MoE model: V4-Pro (1.6T total / 49B active params) and V4-Flash (284B / 13B active). Built entirely on Huawei Ascend 950PR — the first frontier-class model without NVIDIA hardware. Three architectural innovations: Manifold-Constrained Hyper-Connections (mHC) for training stability, a hybrid CSA/HCA attention system cutting inference FLOPs 73%, and Engram Conditional Memory for O(1) factual retrieval. Simultaneously, DeepSeek cut input cache costs by 90%, accelerating the race toward near-zero inference margins.

---

## Architecture

### Model Variants

| Model | Total Params | Active Params | Use Case |
|-------|-------------|---------------|----------|
| V4-Pro | 1.6T | 49B | Frontier reasoning, coding |
| V4-Flash | 284B | 13B | High-throughput, cost-sensitive |

Both support 1M-token context windows. V4-Pro achieves 97% accuracy on Needle-in-a-Haystack at full 1M token context — functionally usable, not just advertised.

V4-Pro reasoning modes: Non-think (speed), High (default), Max (best quality). In Max mode: 91.2 MMLU-Pro, 90.1 GPQA Diamond, 93.5 LiveCodeBench, 3206 Codeforces Elo (outperforms 96.3% of human competitive programmers).

### Key Architectural Innovations

**Manifold-Constrained Hyper-Connections (mHC):** Training stability mechanism for extreme scale. Constrains parameter updates to lie on learned manifold subspaces, preventing gradient explosions during MoE routing at 1.6T scale — problem that killed previous large MoE attempts.

**Hybrid Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA):** Different attention regimes applied at different sequence positions. Combined, they cut inference FLOPs by 73% versus standard attention. This is distinct from DeepSeek V2's MLA (which reduced KV cache by 93.3%) — V4's approach targets compute, not just memory.

```
Standard Attention: O(n²) per layer, full KV materialization
DeepSeek V2 MLA:    O(n²) compute, O(n) KV via low-rank projection
DeepSeek V4 CSA/HCA: O(n²) → compressed → 73% fewer FLOPs
```

**Engram Conditional Memory:** Separates factual storage from computational reasoning for the first time in a production model. Functions as an O(1) key-value retrieval system — the model "looks up" facts rather than recomputing them through attention. Named after the neuroscience concept of memory traces. This is a meaningful architectural departure: prior MoE models stored knowledge diffusely across expert weights; Engram externalizes it to a dedicated module.

### Infrastructure

Runs natively on Huawei Ascend 950PR — no NVIDIA dependency. This is the first frontier-class model trained and deployed entirely on Chinese domestic semiconductor infrastructure. The geopolitical implication: U.S. export controls on H100/H200/A100 chips may not be able to contain Chinese AI capability development.

### Pricing and Economics

V4 at 1/6th the API cost of Opus 4.7/GPT-5.5. Input cache costs cut 90% simultaneously. A 94% hallucination rate on factual tests (rarely admits ignorance) is the known tradeoff — high token intensity required for reliable outputs.

The 90% cache cost reduction accelerates an industry-wide pricing collapse. If inference margin approaches zero for open-weight models, the competitive moat shifts entirely to: data quality, tooling ecosystems, and control of execution environments.

---

## Prior Context

**Extends DeepSeek V2/V3 lineage:** V2 (May 2024) introduced MLA and fine-grained MoE, reducing KV cache 93.3%. V3 (December 2024) scaled to 671B total / 37B active, trained for ~$5.6M. V4 is the third generational leap — each one compressing cost while expanding capability.

**Connects to SemiAnalysis Goodput (04-21):** The 73% FLOPs reduction from CSA/HCA is exactly the kind of "goodput" efficiency SemiAnalysis was measuring. Less compute per token means higher actual throughput on the same hardware. DeepSeek V4 achieves this architecturally; the SemiAnalysis framing showed why it matters commercially.

**Connects to GPT-5.5 (04-24):** Both drop on the same day. Two very different strategies: OpenAI post-trains on GB200 hardware for quality; DeepSeek builds on Huawei hardware for accessibility. The gap in safety compliance (V4's 94% hallucination rate vs GPT-5.5's more conservative stance) reflects different optimization targets.

**Hardware page relevance:** V4's Ascend 950PR deployment is the first concrete data point on Huawei's viability as a training platform at frontier scale.

---

## Open Questions

1. Does Engram Conditional Memory degrade under distribution shift, or does the separation of factual storage make it more robust to knowledge updates?
2. Can the CSA/HCA approach compose with existing KV cache optimizations (like MLA from V2), or do they target different parts of the compute graph?
3. The 94% hallucination rate is strikingly high — is this a training choice (don't teach the model to refuse), or an architectural consequence of Engram failing to distinguish uncertain from known facts?

---

## Related Pages

- [GPT-5.5 Launch and System Card](2026-04-24-gpt-55-launch-system-card.md)
- [SemiAnalysis GPU Cluster Goodput](../hardware/2026-04-21-semianalysis-gpu-cluster-goodput.md)
