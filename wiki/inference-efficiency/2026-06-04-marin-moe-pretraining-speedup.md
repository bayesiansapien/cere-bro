# Marin: Improving LLM Pretraining Efficiency (Dense → MoE recipe)

**Source:** Twitter (@eliebakouch repost of @classiclarryd) → Open Athena / Marin blog
**Link:** [openathena.ai/blog/pretraining-speedup](https://openathena.ai/blog/pretraining-speedup/)
**Date:** 2026-06-03 (surfaced via Twitter morning slot 2026-06-04)
**Raw:** [raw/twitter/2026-06-04-morning.json](../../raw/twitter/2026-06-04-morning.json) (@eliebakouch article)
**Tier:** 1 (MoE pretraining efficiency, scaling recipe)

## TL;DR

Marin (the open pretraining effort) published its dense→MoE transition recipe with a stacked set of architecture and optimizer improvements. Starting from a dense baseline, the cumulative speedup is reported as 6.7x theoretical (3.6x realized wall-clock, accounting for MFU) just from moving dense→MoE V1, then a chain of smaller multipliers on top. This is the empirical, recipe-level companion to the theory papers on MoE scaling that the wiki has been tracking.

## The reported speedups (theoretical / realized)

- **6.7x (3.6x)** — dense baseline → Marin MoE V1. Validated at 1e23 FLOPs.
- **1.4x (1.3x)** — raising total experts from 64 → 256 (more sparsity).
- **1.3x (1.25x)** — optimizer change AdamH → MuonH (a Muon-family optimizer).
- **1.2x (1.2x)** — adding partial key offset (PKO).
- **1.04x (1.04x)** — routed expert normalization + scaling.
- Stacked recipe tested at 3e19 FLOPs gave a 2.1x theoretical speedup over MoE V1.

"Theoretical" counts only model FLOPs; "realized" reflects wall-clock and includes Model FLOPs Utilization. The gap between the two (6.7x vs 3.6x) is the honest part: MoE's routing and expert-parallel communication eat into the FLOP win.

## Relation to prior wiki state

This is the practitioner ground truth under the same-week theory papers. **MoE-μP (05-17) and today's Gated Delta Networks μP (06-04) give closed-form hyperparameter-transfer rules so a lab can pick MoE hyperparameters without sweeping at target scale.** Marin is what the recipe looks like once chosen empirically: the dense→MoE jump is the dominant lever, then sparsity, then the optimizer. The Muon-family optimizer win (AdamH→MuonH, 1.3x) is itself a recurring 2026 thread — Muon and its variants keep showing up as the optimizer that survives at scale.

It also rhymes with **MAI-Thinking-1 (06-03, Microsoft's 1T/35B-active MoE built without third-party distillation)** and **Nemotron 3 Ultra (06-03/06-04, NVIDIA's 550B open-weight MoE at ~10% active sparsity)**: the entire frontier is MoE now, and the open question every team faces is exactly the one Marin documents — how much sparsity, which optimizer, which routing normalization.

## Why it matters

Open, itemized speedup ledgers like this are rare. Most labs ship the model and hide the recipe. Marin reporting each multiplier separately, with the theoretical-vs-realized gap exposed, is the kind of artifact that lets a new team reproduce the dense→MoE transition without re-deriving it. The 3.6x realized number is the one to quote: it is what you actually save in wall-clock, not the headline FLOP count.

## Links

- [Marin blog](https://openathena.ai/blog/pretraining-speedup/)
- Related: [Gated Delta Networks μP 2026-06-04](2026-06-04-gated-delta-networks-mup.md), [MoE-μP 2026-05-17](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)
- Concept: [LLM routing](../ai-routing/llm-routing.md)
