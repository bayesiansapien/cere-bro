---
title: "Shorts 2026-11-09: distillation, linear attention, latent bridges, harnesses, evals"
date: 2026-11-09
raw: ../../raw/huggingface/
tags: [distillation, linear-attention, moe, harness, benchmarks, safety]
---

# Shorts, window ending 2026-11-09

Papers from the HuggingFace 11-07 list (served again for 11-08) and this week's Kurate leaderboards that matter but do not need a full page.

## Compression and distillation
- **BCSM, Bidirectional Centered Score Matching** ([2611.04279](https://arxiv.org/abs/2611.04279), Kurate cs.AI #4). Few-step distillation of discrete diffusion LMs. Token-wise KL gives weak supervision when steps are cut aggressively; full concrete score matching is O(V^2). BCSM builds an O(K) active set from teacher and student top candidates and factorizes the pairwise loss to O(K). Up to 6x fewer function evaluations with +16.9% relative HumanEval and +15.1% MMMU at single-step inference.
- **StepX-OPD** ([2611.04386](https://arxiv.org/abs/2611.04386)). Merges multi-teacher on-policy distillation and step distillation for text-to-image diffusion into one stage, so frozen specialists supervise the few-step student on states its own rollout visits. Beats the 40-step Flow-OPD model at four steps; ~37% fewer GPU-hours on SD3.5-Medium. Same "supervise on the student's own states" principle as on-policy LLM distillation (see [knowledge distillation](knowledge-distillation.md)).
- **GIST** ([2611.06395](https://arxiv.org/abs/2611.06395), Kurate cs.AI #1). Offline RLVR (RL with verifiable rewards on a fixed response pool) supervises every token. The Gibbs-optimal target shows correct responses matter through their low-probability tokens and wrong ones through the policy's high-probability mode. GIST selects responses by temperature and supervises only mismatch tokens; accuracy rises on GSM8K, MATH-500, MBPP for three models. Another entry in the selective-token-training pattern (TIP, LongAct).

## Architectures
- **Muir** ([2611.08376](https://arxiv.org/abs/2611.08376)). Linear attention (a fixed-size recurrent KV state instead of a growing cache). Finds erase gates are far less sensitive than write gates, so they can be low-rank, and slow-decaying state rows dominate readout. Fuses gates into one low-rank projection, adds a matched-filter readout, reinvests saved parameters into a wider FFN, and adds a stable large-chunk parallel update for wide matrix units. 166M-1.34B: perplexity -1.8-2.0% vs Gated DeltaNet-2 and -2.5-3.6% vs Transformer.
- **SAE Interprets MoE** ([2611.08089](https://arxiv.org/abs/2611.08089), ByteDance Seed). An SAE on an MoE layer's output decomposes each latent exactly over experts. On Qwen3-30B-A3B, *contribution* is far more concentrated than *gating*: most features have one or two dominant experts, with sub-domain specialists (Java vs front-end web, geometry vs arithmetic). Relevant to expert pruning and per-expert precision: router frequency is a poor proxy for which experts matter.

## Latent communication between models
- **PLatour / PACT-Check** ([2611.06976](https://arxiv.org/abs/2611.06976)). Prefill-to-autoregressive cross-model transfer: a big model's prompt representations feed a small model's generation through zero-initialized linear bridges. It beats open baselines, but controlled tests show some gains reappear with *uninformative* sender signals or receiver-only training: the bridge acts as a parameter-efficient adapter. PACT-Check measures how much gain truly comes from communication. A useful skepticism tool for the latent-communication wave (Coca-Cola, SwarmEvolve the same window).

## Agents and harnesses
- **Harness-S** ([2611.04277](https://arxiv.org/abs/2611.04277), 66 HF upvotes). Builds a fixed pool of "sibling" harnesses, each evolved to repair a different failure of a base harness. During RL, only when every base rollout fails does an adaptive harness router pick top-k siblings, whose successful trajectories replace the failed group. The policy then performs better back under the original harness on AppWorld, SWE-Gym, DBBench: harness-elicited behavior transfers into weights. See [harness engineering](../agentic-systems/agent-harness-engineering.md).
- **EvoMemState** ([2611.03743](https://arxiv.org/abs/2611.03743)). Personal-agent memory that adds relational states (validity, scope, conflicts between facts) and an RL-generated per-request reasoning state on top of stored facts. See [agent memory](../agentic-systems/agent-memory.md).

## Evaluation cost and safety
- **BestRand** ([2611.00883](https://arxiv.org/abs/2611.00883)). Benchmark-subset error is long-tailed: random subsets are usually fine but occasionally very wrong. BestRand keeps random sampling's cheapness while cutting high-error risk 50.2% and estimation error 16.4% at 51.3% of competitors' construction cost, over 70+ benchmarks.
- **Identically trained models break on different jailbreaks** ([2610.34074](https://arxiv.org/abs/2610.34074)). 150 1B models: two post-training seeds on the same pretraining run correlate 0.984 in per-prompt non-refusal; a new pretraining seed drops it to 0.811, a new data recipe to 0.779. The best attack template transfers across pretraining seeds only 27% of the time. A jailbreak result on one checkpoint is mostly a property of that pretraining run. See [responsible AI](../responsible-ai/responsible-ai.md).
