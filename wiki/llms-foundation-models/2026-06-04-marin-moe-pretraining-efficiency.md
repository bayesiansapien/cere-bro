# Marin / Open Athena: Improving LLM Pretraining Efficiency (dense → MoE, 6.7x)

**Date:** 2026-06-04 (post dated 2026-06-03)
**Source:** Twitter (curated, [@eliebakouch](https://x.com/eliebakouch/status/2062236377991741508)) → Open Athena blog
**Link:** [openathena.ai/blog/pretraining-speedup](https://openathena.ai/blog/pretraining-speedup/)
**Author:** Larry Dial (MARIN project)

## TL;DR

The MARIN project scaled its open pretraining recipe past 100B parameters and 1e23 FLOPs, and published the per-change speedup ladder. Starting from a dense baseline, each improvement is measured separately and reported as theoretical (realized) speedup, where theoretical counts only model FLOPs and realized accounts for hardware utilization (MFU). The stack: 6.7x (3.6x) from dense to Marin MoE V1; 1.4x (1.3x) from raising total experts 64 to 256; 1.3x (1.25x) swapping the optimizer from AdamH to MuonH; 1.2x (1.2x) from partial key offset (PKO); 1.04x (1.04x) from routed-expert normalization plus scaling. The dense→MoE transition was validated at 1e23 FLOPs; the four follow-on changes were each measured against MoE V1, and the stacked recipe showed a 2.1x theoretical speedup over MoE V1 at 3e19 FLOPs. The whole thing is run as a clean scaling-ladder ablation, in the same spirit eliebakouch compared to Microsoft's MAI scaling ladder, and it is fully open.

## Key points

- **The MoE transition is the dominant lever:** 6.7x theoretical / 3.6x realized just from dense → MoE V1. Everything after it is incremental (≤1.4x each). The big win is sparsity; the rest is tuning.
- **Realized lags theoretical, and the gap matters.** 6.7x model-FLOPs becomes 3.6x wall-clock because MFU drops when you go sparse. The blog is unusually honest about reporting both, which is the number that actually predicts cluster time.
- **Optimizer swap is a free 1.3x.** Moving AdamH → MuonH buys 1.3x (1.25x), echoing the Muon-codesign results the wiki has tracked on the architecture side.
- **Stacking is sub-multiplicative.** Individually the four post-MoE changes multiply to more than 2.1x; measured stacked at 3e19 FLOPs they give 2.1x, so the gains partially overlap rather than compounding cleanly.

## Relation to prior wiki state

This blog is the industry-practice mirror of the day's [Gated DeltaNet μP](../inference-efficiency/2026-06-04-gated-delta-network-mup-scaling.md) paper (06-04) and the broader scale-stable-architecture thread. The academic side is deriving how to make efficient architectures *transfer hyperparameters across scale* ([MoE μP](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) 05-17, also Kurate cs.LG #14 this week at ai_rating 9.0; GDN μP 06-04); MARIN is shipping the recipe those derivations enable, complete with a Muon-style optimizer swap that the [Parallax](../inference-efficiency/2026-05-29-parallax-local-linear-attention.md) (05-29) optimizer-codesign result predicted would help. The MAI scaling-ladder comparison eliebakouch draws connects it back to [MAI-Thinking-1](2026-06-03-mai-thinking-1-hill-climbing.md) (06-03), whose whole thesis was that the disciplined hill-climbing *process* is the product. MARIN is the open-recipe version of the same disciplined-ablation philosophy.

It also grounds the wiki's "memory bandwidth and sparsity, not raw FLOPs" framing with realized numbers: the honest 6.7x→3.6x gap is exactly the MFU tax that makes MoE serving harder than the FLOP count suggests, the same physics behind [dMoE](../inference-efficiency/2026-06-01-dmoe-block-level-moe-diffusion-llm.md) (06-01) and MergePipe (06-04).

## Why it is here

Per the wiki's Twitter-as-source rule, this is a substantive blog surfaced through a curated feed ([@eliebakouch](https://x.com/eliebakouch/status/2062236377991741508), HuggingFace) and not covered by today's HF/RSS/Kurate, so it earns a summary page. It is a pretraining-efficiency recipe with reproducible per-change ablations, the kind of practitioner ground truth the wiki values.

## Links

- [Open Athena blog](https://openathena.ai/blog/pretraining-speedup/)
- Source tweet: [@eliebakouch](https://x.com/eliebakouch/status/2062236377991741508) quoting [@classiclarryd](https://x.com/classiclarryd/status/2062209312232272194)
- Related: [Gated DeltaNet μP 06-04](../inference-efficiency/2026-06-04-gated-delta-network-mup-scaling.md) · [MoE μP 05-17](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) · [MAI-Thinking-1 06-03](2026-06-03-mai-thinking-1-hill-climbing.md) · [Parallax 05-29](../inference-efficiency/2026-05-29-parallax-local-linear-attention.md)
