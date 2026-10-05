---
title: "Semiconductor process monitor (BCN, digital etch, atomic pitch splitting) and B300 GPU-hour pricing"
date: 2026-10-05
sources:
  - https://thesemiconductornewsletter.substack.com/p/weekly-monitor-on-semiconductor-process-e90
  - https://deepinfra.com/deepcluster
  - https://x.com/StockSavvyShay/status/2106731371985301739
  - https://x.com/Marktechpost/status/2106085095199367621
tags: [semiconductor, process, 2d-materials, beol, gpu-pricing, b300, asic-share]
---

# Process research of the week, plus what a B300 hour costs

**TL;DR.** The Semiconductor Newsletter's weekly process monitor picked seven papers. The strongest is **wafer-scale epitaxy of p-type boron carbon nitride** (Nature, 09-30): a dual-precursor scheme makes wafer-scale monolayer BCN with a 1.90 eV bandgap, and p-type transistors reach about **100 cm²/V·s hole mobility, over 0.9 mA/µm on-current and a 10⁸ on/off ratio**. That attacks the missing half of complementary 2D logic, since good p-type 2D materials have been scarce. The most industrial item is **imec's six-month pilot-line evaluation of AlixLabs' Atomic Pitch Splitting**, a plasma atomic-layer-etch step that splits one patterned line into two and could replace parts of multi-patterning flows (LELE, SADP, SAQP) that add masks and loops. No results yet; it is a milestone, not proof. On the compute-pricing side, DeepInfra now sells dedicated **NVIDIA B300 clusters of 256 to 5,000 GPUs at $2.99 per GPU-hour on a three-year term and $1.98 on five years, against a $6.50 public-cloud reference**.

## The seven process items

- **p-type BCN epitaxy** (Nature): wafer-scale, strong device metrics; open questions are composition uniformity, contacts, thermal budget and yield.
- **Digital etching of Si fins to 6 nm** (arXiv): cyclic oxidation plus vapor HF removes 2.5 to 10.2 nm per cycle; changing the anneal ramp chemistry cut fin thickness variation from about 17 nm to 3 nm. Near-term target is Josephson-junction barriers, not CMOS.
- **Air-cushion vs roll-to-plate nanoimprint** (Discover Nano): air-cushion reaches full contact in about 10 s and a cycle under a minute; bubble-free roll pressing needs about 750 s.
- **Monolithic 3D memristor-TFT reservoir stack** (Nature Communications): back-end-compatible layers coupled for computing, not just density.
- **Amorphous boron nitride low-k dielectric** (review): k about 2.58 with about 50 GPa modulus, versus about 4.3 GPa for porous SiCOH, so it could escape the porosity-strength trade-off; reliability data still thin.
- **Low-resistance contacts to oxygen-doped WSe₂** (Nature Communications): contact resistance, not mobility, now limits scaled 2D transistors.
- **Atomic Pitch Splitting at imec**: measures CD uniformity, line-edge roughness, pitch walking and stochastic defects over six months.

## Compute-economics signals from the same window

- **DeepInfra (newsletter):** Batch API at 20% below real-time for jobs returned within 24 hours (up to 50,000 requests per file); Flex tier 20% cheaper for latency-tolerant work; prompt-cache retention on select models. DeepSeek-V4.1-Flash lists at $0.14 in, $0.42 out, $0.004 cached per million tokens.
- **UBS rack forecast (via X):** annual AI rack capacity grows about 4x to **104.5 GW by 2030**; Nvidia triples to about 51 GW and holds about 48% share, custom ASICs settle near 43% after 2028, AMD near 9 GW.
- **DGX Spark 64GB (via X):** GB10 Grace Blackwell desktop with up to 1 petaFLOP FP4 and 64GB unified memory, pitched for local 30-35B agents; two units pool 128GB over ConnectX-7 at 546 GB/s combined. The 10-03 digest noted it costs $4,999, half the memory of the original for 25% more.

## How this relates to prior wiki pages

- **Supply gates (10-04)** named HBM, CoWoS and 3nm as the caps on accelerator shipments ([page](2026-10-04-supply-chokepoints-cerebras-broadcom-memory.md)). Today's process items sit further out: pitch splitting and 2D p-type logic are about cost per transistor after 2028, not this year's shipments.
- **GPU-hour price as a compression signal.** A five-year B300 hour at $1.98 against a $6.50 cloud reference is a 70% discount for commitment. It fits [compute-economics](compute-economics.md)' thread that compute is becoming long-dated debt (Broadcom's $42B loan to Anthropic, 10-03).
- Updates [compute-economics](compute-economics.md) and [memory-hierarchy](memory-hierarchy.md) (BEOL dielectric note).

**Raw source:** `raw/gmail/2026-10-05-newsletters.md` (The Semiconductor Newsletter, DeepInfra); X Following feed.
