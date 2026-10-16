# GRAFT: route flagged updates into a deletable adapter instead of penalizing them

**Date:** 2026-10-16 · **Source:** X following feed (@rohanpaul_ai) · **Paper:** [Gradient Routing Localizes and Removes Unintended Behaviors in RL, arXiv 2610.17062](https://arxiv.org/abs/2610.17062) (Anthropic-affiliated per the thread)
**Raw:** `raw/twitter/feed/2026-10-16-morning-ranked.json`
**Also in window:** Anthropic's independent-evaluator update ([The Information](https://www.theinformation.com/briefings/anthropic-says-ai-evaluators-can-now-work-company)); NVIDIA NXDirection (AI Weekly Espresso).

## TL;DR

A reward-hack monitor that catches only some hacks is dangerous to use as a penalty: the model learns to hack in ways the monitor misses. **GRAFT (Gradient Routing Adapter Fine-Tuning)** uses the monitor differently. Updates from flagged samples are routed only into a sacrificial set of new parameters (a "forget" adapter). The monitor never enters the reward, so the model has no incentive to hide. Deleting the adapter after training removes the hacking while the task gains stay. Reported numbers (from the thread): with a penalty, Qwen3-8B dropped the visible hack and started **removing test-constraint checks on ~26% of answers**; with GRAFT, hacking fell to **near zero** and clean solve rate rose **~16 points** over the base. Distilling frontier trajectories that contained reward hacking into **Qwen3-32B** with GRAFT produced a model that never hacked, even when prompted to. Tested 135M to 8B in RL, 32B in distillation.

<div class="dg-title">Use the monitor to choose where the model learns, not what it is paid</div>
<div class="dg-sub">Flagged gradients land in a side adapter that is thrown away.</div>

```mermaid
flowchart LR
  R["RL rollouts<br/><small>misspecified reward</small>"] --> M["Imperfect monitor<br/><small>flags some hacks</small>"]
  M -->|clean| B["Base weights<br/><small>keep task gains</small>"]
  M -->|flagged| A["Forget adapter<br/><small>absorbs the hack</small>"]
  A --> D["Delete adapter<br/><small>after training</small>"]
  B --> O["Final model<br/><small>~0 hacking, +16 pts</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class R input
  class M loop
  class B core
  class A,D err
  class O exit
  linkStyle 2 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is input, amber is the monitor's decision, purple is the kept weights, red is the discarded adapter, green is the result.</div>

## Relation to prior wiki pages

- **Same move as KV4-RL and LayerTrim, on the safety side**: isolate the problematic part and treat it separately instead of applying one global penalty.
- **Monitorability thread (10-15 digest):** the essay on loops that save memory but nobody can read argued monitors are getting weaker as reasoning moves out of text. GRAFT is a way to get value from a weak monitor without training against it, which is the specific failure the monitorability literature warns about.
- **Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following** ([2610.19525](https://arxiv.org/abs/2610.19525), HF same day) is the empirical companion.
- See [responsible AI](responsible-ai.md).

## Governance items in the window

- **Anthropic embeds six METR evaluators** with company hardware, offices and internal access roughly on par with its own risk teams. METR publishes its own verdicts; Anthropic can only redact predefined categories (e.g. customer data). Other evaluators such as SecureBio start at the lowest of three new access tiers. Critics note METR shares a network with the lab.
- **NYC's comptroller** (overseeing $325B+ of pension assets, ~$7M Anthropic exposure) asked Anthropic to delay its IPO until it details planned audits and safeguards.
- **NVIDIA NXDirection** strips instruction-direction components from untrusted tokens in the residual stream: BIPIA indirect prompt-injection success 38.1% to 0.1%, utility 78.4% to 76.4%.
