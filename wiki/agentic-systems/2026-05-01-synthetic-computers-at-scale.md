# Synthetic Computers at Scale: Long-Horizon Productivity Simulation

**arXiv:** 2604.28181 · [paper](https://arxiv.org/abs/2604.28181) · [HF](https://huggingface.co/papers/2604.28181)
**Tier:** 2 — agent training infrastructure, synthetic data
**Raw:** [../../raw/huggingface/2026-05-01-synthetic-computers-at-scale-long-horizon-productivity-simulation.md](../../raw/huggingface/2026-05-01-synthetic-computers-at-scale-long-horizon-productivity-simulation.md)

## TL;DR

To train productivity agents that can do real long-horizon work, you need realistic *user computers* — folder hierarchies, content-rich documents, simulated collaborators. This paper builds a methodology to **synthesize 1,000 fully-populated computers** at scale, then runs **8+ hour, 2,000+ turn agent simulations on each** that produce a month's worth of fake-but-plausible work. The simulations yield "experiential learning signals" that improve agent performance on both in-domain and out-of-domain productivity benchmarks. The pitch: persona populations are abundant at billion scale, so this can in principle generate millions or billions of synthetic user worlds.

## Mechanism

Two-agent loop on each synthetic computer:

```
┌─────────────────────────────────────────────────────────────┐
│  Synthetic computer: filesystem, docs, spreadsheets, emails │
│  populated to look like a real user's workspace             │
└─────────────────────────────────────────────────────────────┘
        │                                          │
        ▼                                          ▼
┌─────────────────────┐              ┌──────────────────────────┐
│  Objective agent    │              │  Worker agent (the user)  │
│  Generates user-    │ ───────────▶ │  Navigates filesystem,   │
│  specific objectives│              │  collaborates, produces  │
│  requiring multiple │              │  artifacts until done    │
│  deliverables and   │              │  (>2000 turns, >8 hours) │
│  ~1 month of work   │              │                          │
└─────────────────────┘              └──────────────────────────┘
```

The interesting design choice is **decoupling objective generation from execution**. The objective agent works "outside" the computer with full visibility (so objectives are realistic for that user); the worker agent works "inside" the computer (so trajectories are realistic for an agent). This separation prevents the objective agent from generating tasks that an agent would never naturally encounter.

## Why this is Tier 2

The single biggest gap in agent training is **realistic long-horizon trajectories at scale**. ClawGym (04-30) covered medium-horizon tasks (single workflow). Persistent Agent Infrastructure (04-23) covered the runtime side. This paper covers the data side — the long-horizon, multi-day-equivalent training corpus that's been impossible to gather from real users without privacy and consent issues.

The validation is the part to keep: improvements appear on both **in-domain and out-of-domain** productivity evaluations. If the gains transferred only in-domain, you'd suspect overfitting to synthetic distribution. Cross-distribution improvement suggests the long-horizon training signal is real.

## Connection to prior wiki

- **ClawGym (04-30)** dual-route synthesis (persona-driven + skill-grounded) is the *medium-horizon* analog. Synthetic Computers is the *long-horizon* extension — same persona-driven principle, scaled to month-long workflows.
- **Persistent Agent Infrastructure (04-23)** raised the question: how do you do RL on agents that mutate persistent state? Synthetic Computers is the data side of the answer — the training corpus must contain trajectories where state mutation matters.
- **OccuBench (04-16) / Claw-Eval-Live (05-01)** show frontier agents fail real workflows. Synthetic Computers is the training-side bet for closing that gap.
- **LWM-based simulation** is shared with OccuBench — both treat the simulated environment as a fully-rendered model of a real workspace, not a stripped-down sandbox.

## Open problems

1. **Distribution shift between synthetic personas and real users.** "Personas at billion scale" sounds clean, but the synthetic worker agent's behavior is still LLM-driven. If the LLM has biases (e.g., overly thorough documentation, formulaic email tone), the corpus inherits them. Cross-distribution gains don't fully rule this out.
2. **Compute cost.** 8+ hours per simulation × 1,000 computers = ~10,000 GPU-hours of agent runtime *just to generate the corpus*. The "billions of synthetic worlds" pitch assumes inference cost continues to drop on the SemiAnalysis trajectory (also today). At current cost it is hyperscaler-scale only.
3. **Composition with verifiable grading.** Synthetic Computers produces trajectories; Claw-Eval-Live grades them. The natural next paper: train on Synthetic Computers data, evaluate on Claw-Eval-Live, see whether the eval gap closes.

## Research angle

The "billions of synthetic user worlds" pitch is, at base, **an argument that agent training should scale via simulated environments rather than real-user logs**. If true, this changes which data assets matter: the bottleneck is no longer scraping real workflows but having enough compute to simulate plausible ones. That argument is consistent with the SemiAnalysis (today) thesis on token economics — once tokens are cheap enough, simulated training corpora become preferable to real ones.
