---
title: "Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification (BTTF)"
date: 2026-11-16
arxiv: 2610.06790
source: X Following feed (@rohanpaul_ai summary + arXiv abstract)
topic: hardware
---

# BTTF: turn chip-simulation waveforms into a database agents can query

**TL;DR.** A Google DeepMind and Columbia paper targets the least automated part of chip design: post-simulation verification. Chip simulations log every signal change, and the waveform dumps can exceed 10 GB of text that engineers still scan by hand. No LLM context holds that, and the files have no query interface. The authors note that about 74.6% of LLM-for-EDA (electronic design automation) studies target RTL code generation, leaving waveform debugging largely untouched. BTTF converts the dumps into a compact SQLite database. A team of agents turns plain-English questions into SQL, checks design rules and audits each answer. On 150 expert-labelled verification questions it answers 95.33% correctly with Gemini 2.5 Pro. Splitting the work across specialized agents scored 17.3% higher on a quality audit than one agent, at 1.96x the latency.

<div class="dg-title">Put the trace in a database, not in the prompt</div>
<div class="dg-sub">The context-window problem is solved by changing the data format, not the model.</div>

```mermaid
flowchart LR
  W["Waveform dump<br/><small>10GB+ signal changes</small>"] --> D["SQLite store<br/><small>compact, indexed</small>"]
  Q["Engineer question<br/><small>plain English</small>"] --> A["Query agent<br/><small>writes SQL</small>"]
  D --> A
  A --> R["Rule checker<br/><small>design constraints</small>"]
  R --> U["Auditor<br/><small>verifies answer</small>"]
  U --> O["Answer<br/><small>95.33% correct</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class W,Q input
  class D,A core
  class R,U loop
  class O exit
```

<div class="dg-legend">Blue is input, purple is the store and query agent, amber is checking, green is the verified answer.</div>

## How it relates to prior wiki pages

- **Same move as** [Folio](../agentic-systems/2026-11-15-folio-context-folding.md) (11-15) and SkillCache (today): stop pushing raw bulk into the context and give the agent a structured handle instead.
- **Hardware angle.** Verification is the long pole of chip schedules. If agents can query simulation output, the bottleneck shifts toward simulation compute itself. Relevant to [compute-economics](compute-economics.md) only indirectly, but it is a rare agent paper aimed at the chip pipeline rather than at software.

## Gaps

- 150 questions, one model family (Gemini 2.5 Pro). No comparison against a human verification engineer's time to answer.
- The 1.96x latency cost of the multi-agent split is reported, but the token cost is not.

## Links

- Paper: https://arxiv.org/abs/2610.06790
- Post: https://x.com/rohanpaul_ai/status/2122114049353908599
- Raw: `raw/twitter/feed/2026-11-16-morning-ranked.json`
