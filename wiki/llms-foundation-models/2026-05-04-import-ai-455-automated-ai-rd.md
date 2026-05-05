# Import AI 455: AI Systems Are About to Start Building Themselves — Jack Clark

**Source:** Import AI 455, 2026-05-04 · [Post](https://importai.substack.com/p/import-ai-455-automating-ai-research)
**Raw:** [`raw/rss/2026-05-04-import-ai-455-ai-systems-are-about-to-start-building-th.md`](../../raw/rss/2026-05-04-import-ai-455-ai-systems-are-about-to-start-building-th.md)
**Tier:** 1 (research direction, AI R&D automation)

## TL;DR

Clark argues there is a 60%+ probability that fully autonomous AI R&D — a model that can train its own successor without human involvement — happens by end of 2028, with a 30% probability for 2027. He builds the argument from public benchmark progress: SWE-Bench (2% in 2023, 93.9% with Claude Mythos Preview today), METR time horizons (30 seconds in 2022, 12 hours with Opus 4.6 in 2026, ~100 hours predicted by end of 2026), CORE-Bench computational reproducibility (21.5% in Sept 2024, declared solved at 95.5% in Dec 2025), MLE-Bench Kaggle competitions (16.9% → 64.4%), Anthropic LLM-training-optimization speedup (2.9x in May 2025 → 52x with Claude Mythos Preview in April 2026; humans take 4–8 hours for 4x). PostTrainBench: AI systems now achieve about half of expert human uplift on fine-tuning a base model. The pattern across all benchmarks is the same shape: introduced low, saturated within 18 months.

The argument: AI R&D is mostly engineering ("99% perspiration"), and AI now does the perspiration. Even without creative breakthroughs, the field can advance by chained-engineering scaling. The ~60% probability accommodates a creativity gap; if creativity also lifts, the timeline shortens.

## Why it matters

This is the most concrete public timeline argument from a frontier-lab insider on automated AI R&D. The wiki has been tracking the substrate (MIT superposition 05-03, predictive interpretability open question 05-04), the operational targets (TIP, LongAct, CvS, Safety Drift), the architecture map (Ken Huang World Models 05-03), and the routing/efficiency stack (MiMo 05-03, AgenticQwen 05-04, Step-Level Optimization 05-02). Clark's piece argues the *integration* of these pieces is what enables automated R&D — and the integration is now within reach.

## Connections

- **Defense Trilemma + NP-hard reward hacking (2026-05-04)** — the adversarial counterpart. If automated R&D is six months away on the optimistic timeline and 30 months on Clark's, then the alignment problem is genuinely on a clock. The trilemma's persistent-unsafe-region result and Wang/Huang's reward-hacking-grows-with-tools result are precisely the failure modes that compound under recursive self-improvement (Clark's footnote 1: "99.9% accurate becomes 60.5% after 500 generations"). Two arguments converge: capability is closing fast; alignment is structurally not.
- **AHE (2026-05-04)** — making harness evolution observable. AHE's contract-based decision structure is the kind of audit-trail primitive that recursive self-improvement requires; without it, alignment failures become invisible until they compound.
- **Anthropic Automated Alignment Researcher** (referenced in Import AI 454) — proof-of-concept of automated alignment research already exists at Anthropic. Clark's 2028 prediction depends on this specific capability scaling.
- **OpenAI Symphony (2026-05-04)** — agents pulling tickets autonomously from Linear is the productized version of "manage other AI systems," which Clark calls the meta-skill of the trajectory.
- **PostTrainBench** — referenced explicitly. AI gets ~half human uplift on fine-tuning. The interesting prediction: when does this cross 100% human uplift, after which AI fine-tunes models *better* than humans?

## Research angle (Tier 1)

1. **Trajectory-aware routing as recursive-improvement substrate.** The "AI manages other AI" pattern (Symphony, Claude Code subagent supervision) is the same routing problem at the multi-agent level. A formalization of multi-agent routing under uncorrelated failure modes is the cleanest open Tier-1 problem the trilemma exposes; Clark's piece adds urgency.
2. **Compounding-error bound for alignment under self-improvement.** Clark gives illustrative numbers (99.9% → 60.5% after 500 generations). A formal bound — given a per-generation alignment-preservation rate, how many generations of self-improvement before the alignment guarantee falls below threshold T — is unbuilt. The trilemma + Sun-Smith-Nayebi's no-free-lunch result give ingredients.
3. **Predictive interpretability as alignment substrate.** The 05-04 digest open prediction (predictive interpretability via superposition geometry) becomes load-bearing under Clark's timeline: empirical-only interpretability does not scale to recursive self-improvement.

## Open questions

- The 60% number is a personal forecast, not a market or a survey. Whether it survives expert aggregation is open.
- "Automated AI R&D" is undefined. Clark's working definition: a frontier model autonomously trains a successor. But "successor" admits weak forms (a smaller fine-tune of itself) and strong forms (a more capable base model). The benchmarks Clark cites mostly cover the weak form.
- The capability-vs-creativity split is the load-bearing assumption. If frontier model creativity scales as fast as engineering, the timeline collapses; if it stalls (Move 37 hasn't been replaced in 10 years), the 60% drops.
- The "machine economy" implication is striking but speculative; Clark himself flags it as such.
