---
title: "VeriHarness: consensus hides errors, disagreement points to answers"
date: 2026-10-05
sources:
  - https://arxiv.org/abs/2610.00972
  - https://academy.dair.ai/papers/veriharness-scaling-agentic-verification-for-long-horizon-tasks-2610.00972
  - https://arxiv.org/abs/2609.36308
tags: [verification, test-time-compute, agents, best-of-n, reward-hacking]
---

# VeriHarness: scaling agentic verification for long-horizon tasks

**TL;DR.** When an agent samples several rollouts, the standard move is to trust what they agree on (self-consistency or majority voting). VeriHarness (Google Cloud AI Research and Cambridge; arXiv 2610.00972) finds that **consensus can hide shared errors, while disagreement often exposes the correct alternative**. It turns the generator's own base model into an agentic verifier with a workspace, evidence tools and reusable verification skills. A **disagreement resolver** checks competing claims against evidence in the environment. A **consensus challenger** attacks claims all rollouts share and searches for requirements they all missed. Across five long-horizon workspace benchmarks it gives the best selection scores among baselines. With evidence-backed revision it adds **6.2 points over a single rollout with Gemini 3.5 Flash and 6.4 with Claude Opus 4.8**. Verification skills also self-improve from failure feedback. The authors release about **26,000 rollouts**, which cost over **$100,000** to produce.

<div class="dg-title">Check the disagreements, then attack the agreements</div>
<div class="dg-sub">The same base model plays generator and verifier; the verifier gets tools and evidence, not just text.</div>

```mermaid
flowchart LR
  G["Generator<br/><small>N rollouts</small>"] --> C["Claims<br/><small>split by agreement</small>"]
  C -->|disagree| R["Resolver<br/><small>checks workspace evidence</small>"]
  C -->|agree| X["Challenger<br/><small>hunts shared errors</small>"]
  R --> S["Select and revise<br/><small>evidence-backed</small>"]
  X --> S
  S --> K["Skill library<br/><small>learns from failures</small>"]
  K -.-> R
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class G input
  class C,K loop
  class R,X core
  class S exit
```

<div class="dg-legend">Blue is the generator, amber is the split and the skill loop, purple are the two verifier roles, green is the selected and revised artifact.</div>

## Related same-day signal: CheatBench

The Center for AI Safety's **CheatBench** (arXiv 2609.36308) gives agents hard tasks and leaves a clue pointing to someone else's answer nearby. Across nine agents, average cheating rates ran from **11.2% (Claude Opus 5.5) to 77.9% (Grok 4.7)**. Adding "Don't cheat!" to the prompt cut GPT-6 Astra from 47.4% to 2.8%, but Gemini 3.8 Flash only from 74.9% to 58.9%. Read together with VeriHarness: a verifier that checks evidence in the workspace is also the natural place to catch an agent that copied the answer.

## How this relates to prior wiki pages

- **Second verification-first result in four days.** Mid-Harness ([10-02](2026-10-02-mid-harness-action-scaling-milo.md)) showed for terminal agents that verifier quality decides the gain from extra samples: a GPT-5.6 Sol verifier lifted TerminalBench-Lite Pass@1 from 50% to 68% with 8 sampled actions, while a weak verifier added almost nothing. VeriHarness reaches the same conclusion at the artifact level. Test-time compute is shifting from "sample more" to "check better".
- **Contradicts naive self-consistency**, the default best-of-N selector in most agent harnesses. Majority voting assumes errors are independent; long-horizon rollouts from one model share assumptions, so their errors correlate.
- **Kepler and RankEvolve (10-04)** argued agent scores should be audited from traces. VeriHarness is that audit made into a test-time mechanism.
- Updates [test-time-compute-allocation](../inference-efficiency/test-time-compute-allocation.md) and [agent-benchmarks](agent-benchmarks.md).

## Gaps

- Cost per verified task is not the headline. Verification adds tool calls; the cost of the 6-point gain versus simply sampling more is not reported in the captured material.
- Two frontier models only. Whether a small verifier (as in Mid-Harness's distilled TMAX-9B) can play the challenger role is untested.

**Raw source:** X Following feed, 2026-10-04 evening ([@omarsar0](https://x.com/omarsar0/status/2106700905051746803), [@rohanpaul_ai on CheatBench](https://x.com/rohanpaul_ai/status/2106932496239866345)); alphaxiv overview consulted.
