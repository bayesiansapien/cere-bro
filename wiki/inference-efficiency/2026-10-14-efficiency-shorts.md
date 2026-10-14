# Efficiency shorts, 2026-10-14

**Sources:** HuggingFace Daily Papers 10-13, Kurate cs.AI, X Following feed, AI Weekly Espresso, The Semiconductor Newsletter · **Raw:** [HF MSAR](../../raw/huggingface/2026-10-13-multi-stream-attention-residuals.md), [HF Thinking Inertia](../../raw/huggingface/2026-10-13-thinking-inertia-llms-keep-thinking-when-told-not-to.md), [Kurate cs.AI](../../raw/kurate/2026-10-14-cs-ai.md)

## Multi-Stream Attention Residuals (MSAR)

[arXiv 2610.13630](https://arxiv.org/abs/2610.13630). Attention Residuals (AttnRes) let each layer attend over the outputs of earlier layers instead of just adding the previous one, which is softmax attention along depth with a single head. MSAR makes it multi-head: each head looks back over depth through a different multi-scale causal convolution of the sequence, and a light mixer folds the streams back into one layer input. Because it expands streams on demand from single-stream storage, there is no persistent multi-stream memory or extra communication. At 18B and 28B MoE scale it beats standard residuals, manifold-constrained Hyper-Connections (mHC) and AttnRes on all 12 downstream benchmarks, and scaling-law fits give a 1.58x iso-loss compute speedup over standard residuals (AttnRes 1.35x, mHC 1.30x). A 1.58x compute multiplier from the residual path alone is large; the open question is the decode-time cost of the depth attention, which the abstract does not report.

## Thinking Inertia: no-think switches do not stop thinking

[arXiv 2610.11765](https://arxiv.org/abs/2610.11765), 222 HF upvotes (#2 on 10-13). Across six LLMs and six prompting interventions, explicit no-think controls do not reliably remove visible inference: models keep reasoning in the pre-answer text, more so as the answer space opens up. Accuracy holds on yes/no and multiple-choice, but open-ended tasks show a trade-off between answer-only compliance and accuracy; giving candidate answers makes answer-only output easier. Cost reading: a "thinking off" flag is not a token budget. Anyone pricing a no-think tier needs to measure emitted tokens, not trust the mode.

## Hybrid Reasoning Agents

[arXiv 2610.18861](https://arxiv.org/abs/2610.18861) (via X). An agent that switches inside one generation between latent reasoning (continuous hidden-state "thoughts") and text for tool calls, through a light HybridLink module, with a lossless hybrid working memory across turns. HybridSFT then HybridRL learn when to think latently and when to act in text. Across 3 scales and 11 benchmarks: +10.4% performance, 35.5-54.7% fewer tokens, 1.8-2.6x faster inference. Joins HyperThink (today) and ELR (10-13) in moving reasoning off the token stream.

## Fewer Bits, More Tries

[arXiv 2610.15372](https://arxiv.org/abs/2610.15372), Kurate cs.AI #12 (ai_rating 6.5). Under a fixed memory budget, a more aggressively quantized model plus more samples can recover capability lost to quantization. Not on HF today. Read alongside the [10-08 FP4 RL entry](2026-10-08-fp4-rl-trace-triage-nemo-dcr.md): the memory saved by low bits is spendable as breadth.

## Linear-attention kernels on TPU (FLAT)

Berkeley's FLAT ships Pallas training kernels for linear attention, Mamba-2 and GLA on TPUs at about 90% of peak HBM bandwidth (1.48 TB/s), per Ion Stoica's repost. See [kernels page](../hardware/2026-10-14-fused-moe-hopper-and-batch-invariance.md).

## UltraBERT: prune a teacher by width, distill only the masked 5%

[arXiv 2610.15028](https://arxiv.org/abs/2610.15028), dmis-lab. 152M and 380M encoders with 32K context. A 1.3B teacher is width-pruned to 380M and 150M and both are distilled, but logit distillation is applied only to sequences with 5% masking (classification-style); 50% masking is used for retrieval, with separate LM heads. 150M matches RoBERTa-large on classification at 2.3x smaller; 99%+ passkey recall to 32K, with long context added only in the last 100B of 2T tokens. The finding that distillation is "not automatically useful across every capability" is the same selective-supervision lesson as today's OPD trio.

## Disaggregated inference, from the feed

A widely shared practitioner thread argues GPU compute-to-bandwidth ratios keep decode bandwidth-bound for 5+ years, so prefill and FFN should run on GPUs, decode attention on large-SRAM parts, and linear-attention layers (about 1 FLOP per byte) on cheap older-node silicon next to a B300. It links the HeteroPanacea simulator ([arXiv 2608.03741](https://arxiv.org/abs/2608.03741)). SGLang reports up to 6.6x throughput per chip on Vera Rubin with disaggregated serving for Qwen3.8 Flash Next. Intel's D270 (480GB LPDDR5X, 1.3 PFLOPS FP8, 1.5 TB/s, 350W) and Credo/AMD's OmniConnect Weaver (terabytes of LPDDR beside HBM) are the capacity-over-bandwidth bet in hardware.

## Agent traffic and prefix caching

Agent turns resend a long, nearly identical prefix (system prompt, tool schemas, history) and ask for a short tool call. A prefix-cache miss means paying the full prefill again on every turn. This is why IBM's 98% hit rate made its open agent factory 11.5x cheaper ([routing page](../ai-routing/2026-10-14-session-routing-arena-max-cohere-teams.md)) and why Gemini 4 Argon's 95% cached-input discount matters ([Argon](../llms-foundation-models/2026-10-14-gemini-4-argon.md)).

## Related

[kv-cache.md](kv-cache.md) · [quantization.md](quantization.md) · [attention mechanisms](../llms-foundation-models/attention-mechanisms.md) · [memory hierarchy](../hardware/memory-hierarchy.md)
