# Hidden FLOPs on consumer cards, and the GPU-hour getting dearer

**Sources:**
- [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) (GitHub README, v1.0.0), surfaced on the X Following feed via [@lxfater](https://x.com/lxfater/status/2113891680000901380)
- DeepInfra pricing email, received 2026-10-25 (`raw/gmail/2026-10-26-newsletters.md`), [pricing page](https://deepinfra.com/pricing)
- [The Information: data center late fees hit $5M+ per day](https://www.theinformation.com/articles/data-center-late-fees-hit-5-million-per-day-spawning-new-insurance) (`raw/rss/`)
- AI Weekly, 2026-10-25 (CNBC figures on Nvidia's neocloud exposure and CoreWeave credit default swaps)
- X feed: [Nscale filing and lead times](https://x.com/rohanpaul_ai/status/2114372948169810375), [DRAM/substrate lead times](https://x.com/StockSavvyShay/status/2114351741953319282), [CoreWeave funding gap](https://x.com/StockSavvyShay/status/2114364210369196242), [Musk on neocloud debt](https://x.com/StockSavvyShay/status/2114445373129576948)
**Topic:** GPU hardware, compute economics

## TL;DR

Two stories about the price of a FLOP. **gpu-unlock** is a Linux kernel module that runs before the NVIDIA driver binds an Ampere GeForce card (GA102/103/104/106), uses a known firmware-unlock technique to write the protected "speed selector" registers, then hands the card to the unmodified driver. The effect is to double the issue rate of FP16/BF16-input, FP32-accumulate tensor instructions, a rate NVIDIA keeps at half on GeForce versus the professional parts built on the same silicon. On a 3090 Ti at 450 W, dense BF16 GEMM goes from 87.5 to 157.4 TFLOPS and TF32 from 42.6 to 82.6; user reports on 3090, 3080, 3070 and 3060 show +25% to +81%, lowest on power-capped cards. Real workloads gain less: LLM prefill +14-36%, while decode (memory-bandwidth bound) and INT8 do not change. Outputs were bit-identical before and after. **Meanwhile, rented compute is getting more expensive.** DeepInfra raises GPU-hour rates on November 9: A100 80GB $0.89 to $1.49 (+67%), H100 $2.20 to $2.90, H200 $2.69 to $3.49, B200 $3.69 to $4.89, B300 $4.89 to $5.89, citing industry-wide hardware cost increases, while serverless per-token prices stay flat. The constraint is upstream of the GPU: Nscale's IPO filing shows about 25,000 active GPUs against 461,000 active and contracted, transformer lead times exceed 160 weeks, and data center tenants now demand $5M+ per day in late-delivery penalties.

<div class="dg-title">Same silicon, two prices: a firmware limit and a power limit</div>
<div class="dg-sub">One FLOP ceiling is set by product segmentation, the other by the grid.</div>

```mermaid
flowchart LR
  G["GA102 silicon<br/><small>same die, pro and GeForce</small>"] --> L["Firmware rate cap<br/><small>half-rate BF16 into FP32</small>"]
  L -->|gpu-unlock| U["Full issue rate<br/><small>87 to 157 TFLOPS BF16</small>"]
  U --> P["Prefill<br/><small>+14-36%</small>"]
  U --> D["Decode<br/><small>unchanged, bandwidth bound</small>"]
  H["Datacenter GPUs<br/><small>ship in months</small>"] --> W["Power and gear<br/><small>160+ week transformers</small>"]
  W -->|scarce| R["GPU-hour rent<br/><small>A100 +67% at DeepInfra</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class G,H input
  class L,W loop
  class U,P exit
  class D,R err
  linkStyle 1 stroke:#2f9e44,stroke-width:2px
  linkStyle 6 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the hardware, amber is the cap that binds, green is the unlocked throughput, red is what does not improve or gets dearer.</div>

## Key findings

- **The cap is an issue-rate limit, not a clock limit.** gpu-unlock writes SS0 = 0x88888888 (full BF16 rate) and the 4-bit SS1 selector, performs a function-level reset, and lets the stock driver bind. It is opt-in via the kernel command line and needs no driver patch per NVIDIA release.
- **Gains follow the roofline.** Compute-bound kernels (GEMM, prefill, diffusion, FlashAttention) speed up; bandwidth-bound decode does not. A 4090 fork claims 165 to 331 TFLOPS of instruction throughput; that one is secondhand and unverified.
- **Rent is rising at the old end too.** The largest DeepInfra increase is on the A100, the oldest card. Older GPUs are not getting cheaper as new ones arrive, because the scarce input is energized rack space.
- **Neocloud credit is under stress.** CNBC (via AI Weekly): Nvidia has $7B invested in AI cloud providers plus $164.5B in guarantees and commitments ($171.5B total); five-year CoreWeave default insurance costs about 1,082 basis points, above the ~1,000 usually read as distress. Musk says debt markets have "almost entirely shut off" for AI-only neoclouds.
- **Supply lead times.** DRAM, SSDs, hard drives and ABF substrate run 2-5x normal lead times (ABF near a year vs three months), so GPUs are the only balanced part of the chain.

## Relation to prior wiki pages

- **Extends the "memory sets the rent" result (10-24)**, where H200 rent rose 160% vs 40% for the H100 because buyers pay for memory, not FLOPs. gpu-unlock is the mirror case: doubling FLOPs on a 3090 leaves decode untouched because decode is memory-bound. Both say bandwidth, not compute, prices inference.
- **Confirms the operator gap (10-23, SemiAnalysis):** about 50% output differences on identical B200s from stack choices alone. Here, 80% of GEMM throughput on a 3090 was a firmware setting. Hardware headline FLOPs are not delivered FLOPs.
- **Tension with the token-arbitrage thread (10-25)**, where inference resellers earned $10-20 per GPU-hour on rented B300s. If rent rises 20-30% while per-token serverless prices stay flat (DeepInfra's own choice), reseller margins compress unless stack efficiency improves.
- **Updates [compute-economics](compute-economics.md)**: power and electrical gear, not GPUs, are now the binding constraint, and penalties for missing them are priced at $5M/day.

## Research angle

For local inference, the unlock moves the prefill/decode balance: prefill gets cheaper, so prefill-heavy workloads (long prompts, RAG, speculative-decoding verification) benefit most on consumer cards. Expect NVIDIA to close the firmware path in a driver or VBIOS update; treat the user reports as unreproduced until a benchmark suite confirms them.

Related: [compute-economics](compute-economics.md) · [gpu-kernels](gpu-kernels.md) · [memory premium (10-24)](2026-10-24-memory-premium-h200-micron-roadmap.md) · [token arbitrage (10-25)](../ai-industry/2026-10-25-token-arbitrage-neocloud-squeeze.md)
