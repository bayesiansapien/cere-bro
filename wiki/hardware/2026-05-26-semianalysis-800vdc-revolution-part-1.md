# SemiAnalysis: Inside the 800VDC Revolution — Part 1

**Source:** [SemiAnalysis newsletter](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part), 2026-05-26, by Nicolas Bontigui (with DG Matrix, Novos Power, Aran Industries).
**Topic:** Datacenter power architecture / AI training infrastructure.

## TL;DR

Across every major datacenter conference in H1 2026, vendors are pitching 800VDC (800-volt direct current) as the next forced shift in AI datacenter power distribution. The argument: tokens per watt is now the binding constraint, GPU rack density is climbing past the point where 415V AC plus rack PSUs can deliver power without prohibitive copper and conversion losses, and 800VDC removes one or two voltage conversion stages between the utility feed and the GPU board. The piece frames it as the same kind of architectural shift as water-cooling: looked excessive, became mandatory because physics did not negotiate. Part 1 covers the why and the high-level pitch; Part 2 will go into the failure modes (DC arc protection, breaker engineering, isolation, vendor cap tables).

```
                AC era                                  800VDC era
  ┌────────────────────────────────┐       ┌─────────────────────────────────┐
  │ utility ►13.2kV AC ►480V AC    │       │ utility ►800V DC distribution   │
  │ ►PDU ►rack PSU (AC/DC)         │       │  ►rack-level DC/DC step-down    │
  │ ►VRM ►GPU                      │       │  ►VRM ►GPU                      │
  │ (3-4 conversion stages)        │       │  (2 conversion stages)          │
  │ ~10-12 pct distribution losses │       │  ~3-5 pct distribution losses   │
  └────────────────────────────────┘       └─────────────────────────────────┘
```

## Why this matters now

- GPU rack density is moving from 30-50 kW today (H100/B200 era) to 130-250 kW with GB300 NVL72 and successors. At those densities the copper cross-section required for 415V AC distribution becomes physically unwieldy at the rack inlet. 800V DC halves the conductor cross-section for the same delivered power.
- AI infrastructure is the first datacenter workload where the gross power bill is large enough that 5-7 percentage points of distribution loss is worth ripping out the AC architecture for. SemiAnalysis frames the calculus explicitly as tokens-per-watt.
- The transition is also a vendor-shift moment. Today's incumbents (Schneider, Vertiv, ABB) own the AC architecture; pure-play DC vendors (DG Matrix, Novos Power) and a long tail of HVDC component startups stand to capture the new design surface.

## Key claims from Part 1

- 800VDC distribution to the rack with rack-internal DC/DC step-down to the GPU board's preferred rail is the architecture being demonstrated by multiple vendors in 2026.
- Removing two conversion stages reduces facility-level conversion losses on the power path by roughly 5-7 percentage points at full utilization, compounded by a copper-mass reduction that lowers material cost per delivered megawatt.
- DC busbars at 800V need substantially different protection devices (DC arc faults do not self-extinguish at zero-crossing). This is the hardest engineering subsystem and the main risk in adoption timelines.
- The shift parallels prior forced architectural shifts in the datacenter (raised floor, hot aisle containment, direct liquid cooling). Each looked excessive at first; each became standard once compute density made the prior architecture untenable.

## How this relates to prior wiki pages

This connects directly to the **2026-05-14 energy-to-token position paper** (the framework that argued tokens-per-watt should be the unified efficiency metric, replacing the model-side FLOPs-per-token and infra-side PUE silos). 800VDC is a concrete infrastructure move in exactly that frame: every conversion stage that gets removed is more tokens per delivered watt. It also extends the [SemiAnalysis GPU cluster goodput piece (2026-04-21)](../hardware/2026-04-21-semianalysis-gpu-cluster-goodput.md), which argued the marginal value of a GPU is gated as much by power-delivery efficiency as by compute throughput. 800VDC is the supply-side response to the demand-side throughput problem the goodput piece described.

## Research angle

The interesting open problem is at the intersection of architecture and power: model architectures with different sparsity, MoE routing, and attention patterns have different time-varying power draws, and 800VDC's DC/DC step-down efficiency is load-dependent. A coherent tokens-per-watt analysis at the model level (which is where the wiki's interest lives) eventually has to model the power-electronics efficiency curve as a function of the architecture's instantaneous draw. That is the next bridge between the AI-architecture side and the hardware-infrastructure side, and right now it does not exist.

## Industry implication

Hyperscalers will use 800VDC adoption as a competitive lever on tokens-per-dollar; smaller datacenter operators that cannot retrofit will face a structural cost disadvantage on AI workloads through 2027-2028. Hardware-side vendors with DC-native power conversion silicon and DC arc-protection devices are about to be sharply repriced.
