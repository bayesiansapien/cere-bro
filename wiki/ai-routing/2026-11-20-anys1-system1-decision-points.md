# AnyS1: One System-1 for the Decision Points of Any Agent Workflow (2611.23751)

**TL;DR.** Agents call a big model (System-2) at every step, even when the step is just picking among a few known options. Dual-system agents already hand those picks to a small model (System-1), but each environment needs hand-written hooks. AnyS1 finds the decision points automatically from human-written procedural skills, whose instructions already say where choices arise and which options apply. Offline, it mines enumerable decisions from over 1,000 public skills, collects execution-grounded states in isolated containers (the Any-DP dataset) and trains one calibrated 4B pointer model with label smoothing. At run time, routine decisions resolve in one forward pass of the 4B model, with fallback to System-2 when confidence drops below a calibrated threshold. On three unseen benchmarks and several System-2 families, episode cost falls 75-91% and model-call time 63-92% versus an uncompiled System-2 agent, with reliability preserved and the threshold transferring zero-shot.

<div class="dg-title">Skills already say where the cheap decisions are</div>
<div class="dg-sub">A 4B pointer model answers enumerable choices; the big model only sees the rest.</div>

```mermaid
flowchart LR
  K["Skill docs<br/><small>1,000+ public skills</small>"] --> D["Decision points<br/><small>mined, enumerable</small>"]
  D --> S1["4B System-1<br/><small>one forward pass</small>"]
  A["Agent step<br/><small>workflow state</small>"] --> S1
  S1 --> C{"Confident?<br/><small>calibrated threshold</small>"}
  C -->|yes| O["Action<br/><small>75-91% cheaper episode</small>"]
  C -->|no| S2["System-2<br/><small>frontier model</small>"]
  S2 --> O
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class K,A,D input
  class S1,S2 core
  class C loop
  class O exit
  linkStyle 4 stroke:#2f9e44,stroke-width:2px
  linkStyle 5 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is input, purple is a model, amber is the confidence router, green is the action.</div>

## Relation to prior wiki pages
- **Confidence cascades, generalized.** [LuthorSQL (11-17)](2026-11-17-luthorsql-system1-cascade.md) answered text-to-SQL locally when a validator was confident and cut API cost 33%. AnyS1 applies the same escalate-on-low-confidence rule to every enumerable step of any workflow.
- **Same day as** Claude Code's advisor tool going viral on X (Sonnet runs the session, Opus is consulted only at decision points) and an "Drex Router" step-level model picker: the step, not the query, is becoming the unit of routing.
- Builds on the decision-model ("System One", e.g. Jev) line tracked on the [routing page](llm-routing.md) since 11-14.

## Gaps
- Only enumerable choices qualify; open-ended generation steps still go to System-2. The cost cut is against an uncompiled agent, not against a prompt-cached or smaller-default baseline.

## Sources
- [Paper](https://arxiv.org/abs/2611.23751) · raw: `raw/huggingface/2026-11-19-thinking-fast-anywhere-one-system-1-for-the-decision-points.md`

Concept page: [LLM routing](llm-routing.md)
