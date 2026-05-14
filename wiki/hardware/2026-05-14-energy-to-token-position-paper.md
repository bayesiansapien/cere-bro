# Inference as energy-to-token production: a position paper

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.11733](https://arxiv.org/abs/2605.11733)
**Raw:** [raw](../../raw/huggingface/2026-05-14-position-llm-inference-should-be-evaluated-as-energy-to-toke.md)
**Tier:** 1. Hardware-bounded inference, deployment economics, datacenter ceilings

## TL;DR

A position paper arguing that LLM inference benchmarks (accuracy, latency, throughput, hardware utilization) all miss the binding constraint at deployment scale. The real output is a quality-conditioned token produced under joint constraints from effective compute, delivered datacenter power, cooling capacity, PUE, and utilization. The paper formalizes this as a Token Production Function with token rate bounded by both compute-per-token and energy-per-token ceilings. It does not claim that price dispersion across providers is causal evidence of marginal cost; price is used only as directional motivation. The core question is when the binding constraint moves from theoretical peak compute toward delivered power, cooling, and operational efficiency.

## Why it matters

The wiki has been tracking the capacity-binding-constraint thread for two months: [ByteDance's $30B PRC-chip commitment](../ai-industry/2026-05-08-lambert-china-ai-labs.md) (05-08), [Broadcom-OpenAI-Microsoft chip deal](../ai-industry/2026-05-10-broadcom-openai-microsoft-chip.md) (05-10), [Anthropic-Colossus capacity deal](../ai-industry/2026-05-08-anthropic-colossus-deal-capacity.md) (05-08), [NVIDIA $40B in AI partners](../daily-digest/2026-05/2026-05-12.md) (05-12), [SemiAnalysis Cerebras "Faster Tokens Please"](../../raw/rss/2026-05-13-semianalysis-cerebras-faster-tokens-please.md) (05-13). Every one of those is implicitly arguing the same thing the Position paper makes explicit: the cost floor on inference is no longer set by FLOPs but by delivered watts. The Position paper is the first arXiv-side framing in the wiki that formalizes this.

The Cerebras-vs-Groq-vs-NVIDIA debate from SemiAnalysis on 05-13 hinges on exactly this question. The SemiAnalysis piece quotes "past a certain threshold of intelligence, developers prefer faster tokens to smarter tokens." Translated into the Position paper's frame: above some compute floor, the binding constraint moves toward energy-per-token, which is where SRAM machines (Cerebras, Groq) shift the frontier.

## What the framing changes

The standard chart for inference is throughput (tokens/sec/gpu) vs interactivity (tokens/sec/user). The paper argues this chart is incomplete because it does not include the energy axis. Under the Token Production Function, two ceilings bound the same token rate:

```
Token rate ≤ min( compute_per_token_ceiling,
                  energy_per_token_ceiling )

  where energy_per_token = effective_power_delivered / PUE / utilization
```

The implication: a hardware platform with high theoretical FLOPS but low effective-power-per-rack can be energy-bound at the rack level even when it is not compute-bound at the chip level. The argument is that as datacenter buildouts hit grid limits (the Anthropic-Colossus and ByteDance commitments are exactly the binding-grid-capacity move), the energy-per-token ceiling becomes the load-bearing one and the compute-per-token ceiling stops mattering.

## Connections

- **SemiAnalysis Cerebras** ([2026-05-13](../../raw/rss/2026-05-13-semianalysis-cerebras-faster-tokens-please.md)) is the empirical complement: the wafer-scale engine wins on the interactivity dimension that HBM-based GPUs cannot match, precisely because the SRAM-per-flop ratio reframes the energy ceiling.
- **Baidu Ernie 5.1 at 6% pre-training cost** ([2026-05-12 digest](../daily-digest/2026-05/2026-05-12.md)) is the training-side analogue: when frontier-spend pulls against grid-capacity ceilings, the cost-engineering frontier matters more than the FLOPs frontier. The Position paper extends that argument from training to inference.
- **Opus 4.6/4.7 Fast** (SemiAnalysis, 2026-05-13): the Anthropic decision to keep an explicit fast-mode tier (6x price for 2.5x interactivity) is the revealed preference for tokens-on-energy-budget over tokens-on-flops-budget.
- **Cerebras IPO** ([2026-05-04](../hardware/2026-05-04-cerebras-40b-ipo.md)): the IPO valuation depends on this framing being accepted by the market. Position paper is the academic version of the same thesis.

## Research angle

1. **A measured benchmark.** This is a position paper, not an empirical study. The most important follow-up: an open benchmark of inference platforms scored on energy-per-token at fixed quality + latency targets, not throughput. InferenceMax (referenced in the SemiAnalysis Cerebras piece) measures throughput-interactivity at fixed hardware. The Position paper implies we need an axis that adds delivered power. Whoever ships that benchmark sets the new evaluation standard for two years.
2. **PUE-conditioned pricing.** The framing predicts that API prices should converge on energy-per-token across providers in the steady state, but with PUE and grid-rate variance dominating. Tracking whether listed prices start to correlate with regional grid carbon intensity is the falsifiable prediction.
3. **Routing implication.** If inference is energy-bound, multi-model routing systems ([Netflix State of Routing](../ai-routing/2026-05-08-netflix-state-of-routing-model-serving.md), [Sakana Conductor](../ai-routing/2026-05-11-conductor-sakana-orchestrating-frontier-models.md)) should optimize on energy-per-token-at-quality, not latency-at-quality. None of the routing papers in the wiki currently use this objective. That gap is the cleanest near-term routing research direction.

## Where it lives

Update [gpu-kernels.md](gpu-kernels.md) — the energy ceiling is the missing third axis next to compute and memory in the existing GPU optimization narrative. New connection from [llm-routing.md](../ai-routing/llm-routing.md) — routing-as-energy-allocation is now an open research direction.
