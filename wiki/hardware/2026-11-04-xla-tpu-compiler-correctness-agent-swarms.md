# XLA:TPU correctness at hyperscale, with agent swarms

**Source:** [arXiv 2611.00624](https://arxiv.org/abs/2611.00624) (Google), surfaced by [@omarsar0](https://x.com/omarsar0/status/2117613273189376072) with a DAIR Academy page · raw: `raw/twitter/feed/2026-11-03-evening-210222-ranked.json`

**TL;DR.** ML compilers now stack many optimization passes, such as fusion and layout changes, to squeeze peak speed. That creates a hidden tradeoff with correctness. The worst bugs are *silent miscompilations*. The compiler raises no error, but numbers drift or buffers get corrupted, which can ruin a multi-million-dollar training run or quietly degrade live serving. Google describes how it verifies the XLA:TPU compiler at hyperscale. It fuzzes with both synthetic programs and real production graphs. Checks run alongside the existing autotuner. A bisection pipeline narrows a failure in a full workload down to one operation inside a fused kernel. Swarms of AI agents generate stress tests, reproduce failures and write fixes. They are steered away from easy crash bugs and toward silent data corruption. The framework has resolved 142+ bugs, with 103 more findings under review. Reviewer effort grew faster than fix complexity, so agent patches needed adversarial pre-filtering before humans saw them.

<div class="dg-title">Silent wrong answers are found by fuzzing, shrunk by bisection, fixed by agents</div>
<div class="dg-sub">The human reviewer is the bottleneck, so a filter sits in front of them.</div>

```mermaid
flowchart LR
  G["Graphs<br/><small>synthetic + production</small>"] --> Fz["Fuzz + autotune checks<br/><small>numeric drift, corruption</small>"]
  Fz --> B["Bisect<br/><small>down to one fused op</small>"]
  B --> A["Agent swarm<br/><small>repro, stress test, patch</small>"]
  A --> PF{"Adversarial filter<br/><small>before human review</small>"}
  PF -->|pass| H["Merged fix<br/><small>142+ resolved</small>"]
  PF -->|reject| A
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class G input
  class Fz,B,A core
  class PF loop
  class H exit
  linkStyle 5 stroke:#2f9e44,stroke-width:2px
  linkStyle 6 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is input, purple is detection and repair, amber is the review gate and retry loop, green is merged fixes.</div>

## Why it matters

- **Kernel speed has a correctness tax.** The wiki's kernel thread (column-major MoE tile order on 11-02, fused retrieval kernels on 10-29) is all about doing more per launch. Each fusion makes a numerical bug harder to see. This paper is the first at-scale account of what policing that costs.
- **Same lesson as batch invariance (11-01).** That item showed that kernels choosing reduction splits by batch size change logits under concurrent traffic. Silent numeric drift is a production property of optimized compilers, not an edge case.
- **Agents fit well where an oracle exists.** Fuzzing plus a reference execution gives a hard pass/fail check. That is the setting where agent swarms are most reliable. The same pattern appears in the 10-17 kernel-agent work and Berkeley's evolved kernel-optimization system (11-03).

See also: [GPU kernels](gpu-kernels.md), [agent harness engineering](../agentic-systems/agent-harness-engineering.md).
