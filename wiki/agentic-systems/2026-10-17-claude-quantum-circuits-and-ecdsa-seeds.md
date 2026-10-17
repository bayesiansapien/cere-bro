---
date: 2026-10-17
type: source-summary
topic: agentic-systems
sources:
  - raw/labs/2026-10-17-035202-labs.md
  - raw/gmail/2026-10-17-newsletters.md
  - raw/twitter/feed/2026-10-17-morning-ranked.json
---

# Claude designs quantum circuits and recovers the NIST curve seeds

**TL;DR.** Two Anthropic research posts from 10-16 show evaluator-guided search by a frontier model producing checkable results. **Quantum circuits** ([post](https://www.anthropic.com/research/designing-efficient-quantum-circuits), arXiv [2610.22367](https://arxiv.org/abs/2610.22367); Andi Gu with Alek Kemeny at Anthropic, Susanne Yelin and Mikhail Lukin at Harvard/QuEra): Claude Mythos 5 proposes circuit-generating Python programs inside an OpenEvolve loop; an independent evaluator checks correctness on computational basis states (cheap because these reversible circuits never create superpositions) and scores Toffoli gates and peak qubits. On 7 of 8 tasks (chemistry, optimization, simulation, number theory) the circuits cut both counts versus the best published designs, sometimes by an order of magnitude; on the 8th it found a new reversible architecture for prime-field modular inversion that makes the divsteps algorithm practical. A recurring trick it discovered: replace conditional arithmetic with conditional routing, so an expensive kernel appears once (halving the schoolbook Toffoli count). DAIR Academy featured it the same day (via X). **ECDSA seeds** ([post](https://www.anthropic.com/research/ecdsa-curve-origins)): in under half an hour, an internal Claude model showed the unexplained NSA-supplied seeds for NIST P-192 through P-521 came from C's `lrand48` generator seeded with Unix timestamps from May 1997 to April 1998, recovered via a bit-pattern scan and an LLL lattice attack on the truncated LCG. It also explained six base points (FreeLIP's RNG). This lowers, not raises, backdoor suspicion.

<div class="dg-title">The evaluator, not the model, makes the result trustworthy</div>
<div class="dg-sub">Every reported gain is a circuit the checker verified.</div>

```mermaid
flowchart LR
  S["Plain-language spec<br/><small>one paragraph</small>"] --> P["Claude proposes<br/><small>circuit as Python</small>"]
  P --> E["Evaluator<br/><small>basis-state check</small>"]
  E --> C{"TQ-cost<br/><small>Toffoli x qubits</small>"}
  C -->|best| F["Families<br/><small>up to 5 lineages</small>"]
  F --> P
  C -->|final| O["Verified circuit<br/><small>beats published</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class S input
  class P core
  class E,C,F loop
  class O exit
  linkStyle 4 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is the spec, purple the model, amber the search-and-check loop, green the verified output.</div>

## Relation to prior wiki pages

- Same evaluator-in-the-loop shape as AlphaEvolve-style work and today's Athanor (agents post-training under a frozen evaluator). The common rule: the search can be as creative as it likes because acceptance is mechanical.
- Contrast with "LLMs extend known research but do not create new directions" (Kurate cs.AI #19 this week). The circuit search mostly recombined known families, but the divsteps architecture is a genuinely new structure. Both claims can hold at once.
- Efficiency lens: fewer Toffoli gates and qubits is resource compression for quantum hardware, the same objective as quantization for GPUs.

Concept page: [self-evolving-agents](self-evolving-agents.md).
