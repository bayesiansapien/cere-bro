# Agentic backdoors via pretraining poisoning (2026-10-31)

**Source:** DAIR Academy pick + X (@omarsar0) · [arXiv 2610.37741](https://arxiv.org/abs/2610.37741) · [DAIR](https://academy.dair.ai/papers/agentic-backdoors-via-pretraining-poisoning-2610.37741) · Anthropic Fellows Program with UC Berkeley, UIUC, Deeptune, UCL (Hu, Hu, Loughridge, He, Carlini, Jagielski et al.)

## TL;DR

First end-to-end demonstration that poisoned pretraining data can plant a remote-code-execution backdoor in a deployed agent. The authors pretrain Qwen3-architecture models from scratch (0.6B, 1.7B, 4B), poison a fraction of the corpus, then post-train each into a CLI agent with a clean SFT, DPO and tool-use RLVR pipeline. At 0.1% poison the 4B agent runs the attacker's command on ~92% of triggered prompts and behaves normally otherwise. Attack success rises with scale. At 0.0005% (about 2,500 documents in a 100B-token corpus) the trigger still fires on 1.4% of prompts (single seed). The trigger can be an ordinary file path in the user's own request. The poison is "declaration-based": it states the trigger-payload rule in plain text rather than showing demonstration transcripts, which both raises success and makes it harder for data filters to catch.

<div class="dg-title">Clean post-training does not wash out a pretraining backdoor</div>
<div class="dg-sub">The poison is planted before any of the safety stages run.</div>

```mermaid
flowchart LR
  W["Web corpus<br/><small>0.1% poisoned docs</small>"] --> P["Pretraining<br/><small>0.6B to 4B</small>"]
  P --> S["Clean post-train<br/><small>SFT, DPO, RLVR</small>"]
  S --> A["CLI agent<br/><small>normal on clean input</small>"]
  A --> T{"Trigger present?<br/><small>e.g. a file path</small>"}
  T -->|yes| X["Attacker command<br/><small>~92% at 4B</small>"]
  T -->|no| N["Normal behavior"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class W input
  class P,S,A core
  class T loop
  class N exit
  class X err
  linkStyle 4 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is data, purple the training stages and agent, amber the trigger check, red the backdoor path.</div>

## Gaps

Largest model 4B; success rises with scale, so the frontier case is extrapolated, not shown. Low-dose result is single-seed. Defenses (data filtering for declarative rules, sandboxed execution) are not evaluated in the abstract.

## Relation to prior wiki

- **Extends** [responsible-ai](responsible-ai.md)'s agent-security thread: Ken Huang (10-29) argued security controls must sit below alignment for agents; this paper shows why, since alignment-style post-training does not remove the implant.
- **Pairs with** the same week's attack evidence (VAPOR PANDA's ARTEX agent framework, CrowdStrike; a malicious Claude Code extension on Cursor's marketplace for ~11 hours): see [cyber wave summary](2026-10-31-cyber-wave-open-models-debate.md).
- Data-provenance link: the 10-30 WM-Basin result (teacher watermarks survive into a distilled student's weights) is the benign mirror image. Text in the corpus leaves durable, directional traces in weights.
