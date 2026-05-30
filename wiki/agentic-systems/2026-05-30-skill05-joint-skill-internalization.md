# Skill0.5: Joint Skill Internalization and Utilization for OOD Agentic RL

**Source:** HuggingFace Daily Papers (2026-05-30) · arxiv 2605.28424
**Raw:** [raw/huggingface/2026-05-30-skill05-joint-skill-internalization-and-utilization-for-out.md](../../raw/huggingface/2026-05-30-skill05-joint-skill-internalization-and-utilization-for-out.md)

## TL;DR

Skill-based RL for LLM agents has a rigid dichotomy. **Full externalization** keeps every skill in the prompt context, which works but incurs prohibitive token overhead. **Full internalization** bakes every skill into the weights, which is cheap at inference but overfits on easy tasks and creates knowledge conflicts on hard ones. **Skill0.5** breaks the dichotomy by routing skills based on what type they are. General cognitive skills (reasoning patterns, broad heuristics) get internalized into the weights via privileged distillation. Task-specific skills (per-environment routines, per-domain procedures) stay externalized and get dispatched dynamically. A difficulty-aware router streams tasks into mastery tiers and applies the right strategy: privileged distillation for hard tasks to build cognitive scaffolding, diagnostic probing on easy tasks to detect and penalize shortcut-taking. On ALFWorld and WebShop, Skill0.5 beats both memory-based and skill-based RL baselines on in-distribution and out-of-distribution tasks.

## Architecture

```
                ┌─────── Task arrives ───────┐
                │                            │
                ▼                            ▼
       ┌─────────────────┐          ┌─────────────────┐
       │ Hard (low mastery)        │ Easy (high mastery)
       │  → privileged   │          │  → diagnostic   │
       │    distillation │          │    probing      │
       │  internalize    │          │  penalize       │
       │  general skills │          │  shortcuts      │
       └────────┬────────┘          └────────┬────────┘
                │                            │
                └──────────┬─────────────────┘
                           ▼
              ┌────────────────────────┐
              │  Skill router (diff-   │
              │  iculty-aware)         │
              │  routes per-task to    │
              │  ext / int branch      │
              └────────────────────────┘
```

## Why this is the right frame

The internalize-vs-externalize tradeoff is real but the right axis is not "all or nothing" — it is skill type. General reasoning patterns reused across tasks earn their place in the weights; per-domain procedures don't, because they only matter for one slice of tasks and they break when transferred. Skill0.5 makes that axis explicit and routes per-task by difficulty signal. The diagnostic-probing-on-easy-tasks branch is the genuinely clever piece: on tasks the model has mastered, the router shifts to probing for shortcut-taking and penalizes shortcuts, which prevents the standard RL pathology of the model learning a brittle shortcut on easy tasks and getting credit for it.

## Connection to prior wiki state

This pairs naturally with the [05-28 IB-TPO paper](../inference-efficiency/2026-05-28-ib-tpo-information-bottleneck-tree-policy.md) (the paper that formalized information-bottleneck-style filtering in tree policy optimization to drop noisy tree branches) and the [05-23 ACC paper](../inference-efficiency/2026-05-23-acc-agent-trajectory-long-context-training.md) (the paper that argued long-context agent training signal is concentrated in a small fraction of tokens). Three papers in seven days agree at three layers: routing, internalization, and gradient — that the right move is **not** uniform application of training compute, but selective application based on a difficulty or signal-density signal. Skill0.5 ports the same principle to the skill-management layer of an agentic stack.

## Gaps

The router itself is described as "difficulty-aware" but how difficulty is estimated (a learned predictor, a heuristic, a hand-set threshold) is not detailed in the abstract. The benchmarks are ALFWorld and WebShop, which are narrow agentic environments; whether Skill0.5 generalizes to broader environments (computer-use, browser-agent over open web, real coding tasks) is the next question. The ablation breakdown — how much of the gain comes from privileged distillation vs diagnostic probing vs the routing layer itself — is not in the abstract.

## Industrial implication

Production agent stacks today are running into context bloat as more skills get crammed into the prompt. Anthropic's Skills feature (the official skill-loading abstraction in Claude Code), Cursor's per-project Rules, and Kilo Code's skill libraries all suffer from the same problem: every additional skill increases prompt cost on every call, even when it's not relevant. Skill0.5's general-vs-task-specific split is the natural fix. Expect to see this pattern show up in the next generation of agent harnesses (Claude Code, Cursor, Kilo) — internalize the general patterns once via finetune, keep task-specific skills external and routed.

## Related wiki pages

- [PANDO — online skill distillation (2026-05-30)](2026-05-30-pando-online-skill-distillation.md)
- [agentic-systems concept page](agentic-systems.md)
