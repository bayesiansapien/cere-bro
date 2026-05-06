# Ara: Agent-Native Research Artifacts

**arXiv:** 2604.24658 · [paper](https://arxiv.org/abs/2604.24658) · [HF](https://huggingface.co/papers/2604.24658)
**Tier:** 2 — AI-native research infrastructure
**Raw:** [../../raw/huggingface/2026-05-01-the-last-human-written-paper-agent-native-research-artifacts.md](../../raw/huggingface/2026-05-01-the-last-human-written-paper-agent-native-research-artifacts.md)

## TL;DR

Scientific publication compresses a branching research process into a linear narrative, discarding most of what was discovered. **Ara** replaces the narrative paper with a 4-layer agent-executable package: scientific logic, executable code with full specifications, an exploration graph that preserves the failures, and evidence grounding every claim in raw outputs. On PaperBench: question-answering accuracy 72.4% → 93.7%; on RE-Bench: reproduction success 57.4% → 64.4%. On RE-Bench's open-ended extension tasks, preserved failure traces *accelerate* progress for some agents but *constrain* others.

## The Two Taxes

The framing is sharp:

1. **Storytelling Tax.** Failed experiments, rejected hypotheses, and the branching exploration get discarded to fit a linear narrative. Tolerable for human readers; catastrophic for reproduction agents that need to know *why* a path was abandoned to avoid retrying it.
2. **Engineering Tax.** Reviewer-sufficient prose ("we used a transformer with appropriate hyperparameters") leaves agent-sufficient specification holes. The agent literally cannot execute the paper.

These two taxes are the throughput limits on AI-driven scientific discovery.

## Mechanism

Three artifacts plus three supporting tools:

```
Ara structure (the artifact):
  Layer 1: Scientific logic       ← the claim graph + reasoning
  Layer 2: Executable code         ← runnable, fully specified
  Layer 3: Exploration graph       ← what was tried, what failed, why
  Layer 4: Evidence grounding      ← every claim → raw output

Ecosystem mechanisms (the tools):
  - Live Research Manager  ← captures decisions and dead ends during dev
  - Ara Compiler           ← translates legacy PDFs and repos into Aras
  - Ara-native review      ← automated objective checks (grammar checker
                              for prose), so humans review significance
                              and taste, not formatting
```

## Key surprise

**Preserved failure traces help and hurt.** On RE-Bench's open-ended extensions, failure traces accelerate progress when the agent's capability is below the original researcher's, because the agent learns from what was already tried. But for capable agents, the traces *constrain* — the agent gets stuck inside the prior-run solution box rather than stepping outside it. This is a non-trivial finding: **the optimal prior context for an agent depends on whether the agent can outperform the prior author.**

That observation generalizes well beyond research artifacts. Any context-injection system (memory, retrieval, prior conversation) faces the same trade-off: information that helps weaker users may constrain stronger ones.

## Connection to prior wiki

- **Intern-Atlas (05-01)** — the methodological evolution graph. Ara captures the *intra-paper* exploration graph; Intern-Atlas captures the *inter-paper* methodological lineage. Pair: Ara is the per-artifact representation, Intern-Atlas is the cross-artifact representation. Together they constitute the agent-native research-knowledge stack.
- **Building Pi (Pragmatic Engineer, 04-29)** — Mario Zechner argued that AI-assisted development requires stable, agent-readable harnesses around code. Ara is the same argument applied to research artifacts. Both papers are saying: *human-readable formats are not agent-readable formats; the agent-readable format is now the load-bearing artifact.*
- **AVR / Adaptive Visual Reasoning (04-20)** showed that agents benefit from explicit *failure feedback*. Ara generalizes this from a single trajectory to a research artifact's full exploration graph.
- **The "agent-sufficient specification" gap** echoes the Claude Code docs (04-23-24, 04-25) finding that CLAUDE.md is the load-bearing context for sustained agent work — implicit specification is a deployment risk.

## Research angle

The most interesting open question: **what is the minimal Ara that still captures both taxes?** Layer 3 (exploration graph) is the costly layer to maintain. If you could automatically extract exploration graphs from version-control history (git log + branches + experiment tracking), you'd remove most of the manual cost. Whoever publishes the first *retrofitted Ara from existing repos* (i.e., automatic Ara compilation from git + Weights & Biases logs) sets the new standard. The Ara Compiler in this paper is the first attempt; expect a second wave within 90 days.

The capability-dependent failure-trace effect is the second open thread. A meta-learning result — when to suppress prior failure traces for a more capable agent — would make Ara genuinely adaptive.
