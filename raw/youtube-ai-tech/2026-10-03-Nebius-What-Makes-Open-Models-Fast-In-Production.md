# What Makes Open Models Fast in Production (Sujee Maniyam, Nebius)

**Channel:** AI Engineer
**Published:** 2026-10-03
**Source:** https://www.youtube.com/watch?v=TRe1u7dHYiA

## TL;DR
A vendor talk for Nebius Token Factory, a managed inference platform on Nebius-owned hardware that loops inference logs into a "data lab," post-training (LoRA, full fine-tune, distillation, GRPO-style RL, custom quantization) and redeployment. The technical half lists the standard serving stack: per-model engine selection on forked open-source engines, cache-aware routing, speculative decoding with workload-trained draft models, KV cache with CPU offload, prefill/decode disaggregation and calibrated quantization (NVFP4 on Blackwell). Nothing here is novel; it is a checklist of what a competent provider should already do. The one concrete product hook is one-click training of a custom drafter on your own traffic. Several explanations in the talk are technically wrong (see below), which lowers confidence in the presenters, not necessarily in the platform.

## Key Takeaways
- **Positioning:** a third path between closed APIs (no tuning, linear cost) and self-hosting (months of infra work). 60+ open models including GLM, Kimi, DeepSeek.
- **Engine choice is per model.** Nebius maintains internal forks of open engines and deploys each model on whichever performs best.
- **Cache-aware routing:** route requests to replicas that already hold the relevant prefix KV cache, instead of random load balancing. Matters more now that agentic coding sends huge inputs.
- **Speculative decoding:** generic drafters give "up to 30%" improvement; drafters trained on the customer's own production data do better. Productized as Custom Speculator training (EAGLE-3 heads, deployed with vLLM on dedicated endpoints).
- **KV cache with tiered offload** to host memory, claimed 5 to 10x speedups from caching.
- **Prefill/decode disaggregation** on separate GPU pools with KV transfer between them.
- **Quantization** tuned per model to the quality/speed sweet spot; NVFP4 adopted on latest Nvidia chips.
- **Company context:** Nvidia invested $2B; target of 5 GW of Nvidia systems by 2030; early Rubin, Vera and BlueField access; Microsoft and Meta capacity contracts.

## Architecture & Optimization Mechanics
Corrections first. The speaker describes KV caching as caching generated tokens so they need not be regenerated; KV cache actually stores attention keys and values of prior tokens so each decode step avoids recomputing them. The "5 to 10x" figure is meaningless without context: within a request KV cache is mandatory, so the real lever is cross-request prefix reuse, where speedup depends on prefix hit rate. He also calls prefill "CPU intensive"; prefill is GPU compute-bound and decode is memory-bandwidth-bound, which is the entire rationale for disaggregation. And speculative decoding does not "regenerate" on rejection: the target verifies k drafted tokens in one forward pass and keeps the accepted prefix plus one corrected token, so output distribution is unchanged.

The substantive point is drafter specialization. Acceptance rate is the whole game for spec decoding, and it is workload-dependent: a drafter trained on general chat underperforms on narrow distributions (Go code, JSON tool calls, repeated prompt shapes). Training EAGLE-3 heads on your own logs with better-than-KL losses is a distillation problem in disguise, and it compounds with quantization of the target model. Cache-aware routing plus disaggregation is the same architecture as NVIDIA Dynamo and llm-d; Nebius is implementing the consensus stack, not inventing one.

## Grounded Context (Web Enrichment)
The custom drafter is real and documented. Token Factory's Custom Speculator API trains EAGLE-3 style drafters (1 to 7 speculative heads) with KL, LK-alpha or LK-hybrid losses, served via vLLM on dedicated endpoints; Nebius reports LK losses beat KL baselines on acceptance rate across 8B to 685B targets, and exposes acceptance rate and tokens/s in serving metrics. Nebius's own blog frames the gain as workload-dependent rather than citing a universal speedup, which is more honest than the stage claim.

The open-vs-closed claim holds and has strengthened. Artificial Analysis's September 2026 index puts Kimi K3 (59.7) about 6 points behind the leader, Claude Fable 5.1 (65.7), with GLM-5.3 at 59.5, down from a 13-point gap a year earlier; one post-Kimi-K3 reading put the gap at 4 points. The Nvidia $2B investment is accurate but dates to 11 March 2026, seven months before this talk, not "a couple of months." It came with the 5 GW by 2030 target and early Rubin/Vera/BlueField access, so the vertical-integration story is backed by real capital.

Sources: [Nebius Custom Speculator docs](https://docs.tokenfactory.nebius.com/post-training/custom-speculator), [Nebius: Custom Speculator Training](https://nebius.com/services/token-factory/custom-speculator-training), [Nebius blog: train the draft model for your workload](https://nebius.com/blog/posts/train-the-draft-model-for-your-workload), [Nebius enterprise-grade inference](https://nebius.com/services/token-factory/enterprise-grade-inference), [CNBC: Nvidia $2B in Nebius](https://www.cnbc.com/2026/03/11/nebius-nvidia-ai-cloud.html), [DCD: Nvidia invests $2bn in Nebius](https://www.datacenterdynamics.com/en/news/nvidia-invests-2bn-in-ai-cloud-nebius/), [Artificial Analysis gap analysis](https://pasqualepillitteri.it/en/news/14684/open-source-closes-gap-artificial-analysis), [Artificial Analysis on X: Kimi K3](https://x.com/ArtificialAnlys/status/2081926991788626011), [Draft-OPD: on-policy distillation for draft models](https://arxiv.org/pdf/2605.29343)

## Real-World Application / Actionable Step
- Train a workload-specific EAGLE-3 drafter on your own routing or agent traces (vLLM supports EAGLE-3 serving) and measure acceptance rate versus the stock drafter. If acceptance jumps, spec decoding becomes a routing-cost lever: the cheap path for a query class may be "big model plus specialized drafter" rather than "small model."
- Test drafter robustness to target quantization: train the drafter against the FP16 target, deploy against NVFP4/INT4, and quantify acceptance-rate loss. That interaction is under-studied and directly in Amit's lane.
- Add prefix-cache affinity as a feature in the router. Cost per query differs sharply between a cache-hit replica and a cold one, so cost-aware routing should know where prefixes live.
- When benchmarking open models across providers, pin quantization level and engine; the talk's own point is that the "same" model differs materially by provider.
- Finance aside: NBIS is a leveraged bet on neocloud capacity with Nvidia as shareholder; this talk adds no new information to that thesis.
