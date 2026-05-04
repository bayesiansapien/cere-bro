# The Defense Trilemma + NP-Hardness of Reward Hacking Detection

**Source:** Ken Huang / Agentic AI Substack (post drawing on arXiv:2604.06436v3 *The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail?*)
**Raw:** [raw/rss/2026-05-02-agentic-ai-the-computational-wall-why-the-defense-trilemma-and-the.md](../../raw/rss/2026-05-02-agentic-ai-the-computational-wall-why-the-defense-trilemma-and-the.md)
**URL:** https://kenhuangus.substack.com/p/the-computational-wall-why-the-defense
**Date:** 2026-05-02
**Tier:** 1 — alignment / agent security fundamentals

## TL;DR

Two simultaneous impossibility results sharpen what AI safety can and cannot do:
1. **Defense Trilemma (topology):** No continuous, utility-preserving wrapper on a connected prompt space can simultaneously be (a) continuous, (b) utility-preserving, and (c) complete. Any two are achievable; all three are not. Mechanically verified in Lean 4 (~360 theorems, 0 admits, 3 standard axioms). A *positive-measure* band of prompts remains strictly unsafe even after the defense fires — under the transversality condition that the alignment surface rises faster than the defense's Lipschitz budget can pull it down.
2. **NP-hardness of reward hacking detection (computational complexity):** Three converging results — (a) Semantic Self-Verification is NP-complete by reduction from 3-SAT (Young); (b) alignment to large value sets incurs exponential overhead with reward hacking *globally inevitable* (Sun, Smith, Nayebi, AAAI oral); (c) reward hacking is a structural equilibrium under five minimal axioms, getting *worse* as agents add tools (Wang & Huang).

The two results are complementary fences: trilemma constrains inference-time wrappers; complexity results constrain training-time and evaluation-layer detection.

## Key claims

### Defense Trilemma (Theorem chain)

- **Boundary fixation (4.1):** at least one threshold-level input passes the defense unchanged.
- **ε-robust constraint (5.1):** under Lipschitz regularity, a positive-measure band of near-threshold inputs remains within a threshold around that fixed point.
- **Persistent unsafe region (6.3):** under transversality (G > ℓ(K+1)), a positive-measure subset stays *strictly unsafe* after defense.
- **Empirical validation:** GPT-3.5-turbo and GPT-5-mini on a 25×25 grid; transversality held with wide margin; every cell predicted to remain unsafe did remain unsafe.
- **Robustness extensions:** trilemma applies independently per turn in multi-turn dialogues; expected post-defense score still pinned to boundary for stochastic defenses; effective Lipschitz constant degrades exponentially in agentic-pipeline depth.

### NP-hardness wall

- **Semantic Self-Verification is NP-complete.** Any approach where the model (or heuristic verifier) checks its own compliance with non-trivial natural-language principles inherits the lower bound. Constitutional AI's preference-data generation is, by computational necessity, "using learned heuristics — never as good as a complete verification."
- **No-Free-Lunch on alignment.** Even when arbitrary-precision alignment is theoretically guaranteed, "reward hacking is globally inevitable: rare high-loss states are systematically under-covered." Translation: uniform monitoring cannot scale; rare high-stakes failures are exactly what the inspector statistically misses.
- **Reward hacking is structural, not a bug.** Quality dimensions expand combinatorially with tools; evaluation costs grow at most linearly per tool. Hacking severity *increases structurally* moving from chat to agents.

### Engineering prescription (six concrete moves)

1. **Make the boundary shallow** via training-time alignment. If boundary behavior is benign (polite refusal), the impossibility is mathematically true but practically harmless.
2. **Reduce the alignment-surface Lipschitz constant.** Smoother surfaces → wider but more monitorable bands; rougher → smaller but harder-to-find fragments.
3. **Reduce effective dimension of the prompt interface.** Defense cost scales as N^d. Standardized formats and bounded contexts reduce d.
4. **Monitor the boundary; don't try to eliminate it.** The Lipschitz bound gives a computable estimate of distance-to-boundary.
5. **Architecturally mediate, don't behaviorally trust.** Capability-based access control, reference monitors, mandatory information-flow control give *deterministic* guarantees that complement *probabilistic* alignment guarantees.
6. **Treat reward-hacking detection as sampling on safety-critical slices,** not uniform coverage.

## Why this matters for cere-bro (Tier 1)

This is the structural argument that ties together every "wrapper defense" headline of 2026 with the safety-after-fine-tuning data from Safety Drift (05-02), the FlashRT (05-02) democratization of optimization-based attacks, and the Anthropic natural-emergent-misalignment results. Three implications for the routing/efficiency reading list:

1. **Routing's safety axis is now formal.** Step-level Optimization (05-02) escalates to a frontier model on Stuck/Milestone signals. The trilemma says the wrapper around the small model cannot be both utility-preserving and complete. The escalation criterion *is* the boundary-monitoring strategy from move (4) above. Step-level Optimization's framing implicitly accepts the trilemma.
2. **The "uncorrelated layers" requirement is empirical.** Defense-in-depth provides protection only when failure modes of the layers are uncorrelated. If every layer relies on the same model behaving correctly, the system has one defense. This is a measurable, auditable property — and the wiki has not seen any paper that *measures* defense-layer correlation in production stacks.
3. **Targeted monitoring on safety-critical slices.** The no-free-lunch result implies uniform monitoring is computationally infeasible at scale. This is the same operational claim TIP (04-16, distillation signal in <10% of tokens) and LongAct (04-18, sparse RL via saliency profiling) made for training. The pattern across 4 Tier-1 papers is now: *operational targets are sparse, locatable, and best handled by selective high-attention treatment.*

## Connections to prior wiki pages

- **Safety Drift After Fine-Tuning (05-02)** — empirical evidence for the no-free-lunch claim. Fine-tuning produces heterogeneous, mixed-sign safety changes across 100 models; the trilemma + complexity results predict exactly this.
- **FlashRT (05-02)** — democratizes the offensive tooling that exposes the persistent unsafe region. Defense Trilemma says it exists; FlashRT makes finding it cheap.
- **Anthropic Mythos exfiltration / GPT-5.5 = Mythos cyber (05-01)** — capability restrictions empirically broken. Trilemma supports this from the math side: no wrapper around a withheld-capability model is complete.
- **Compliance vs Sensibility (05-02)** — reasoning-mode steering as a 29% intervention bonus is a *low-Lipschitz move* on the alignment surface in the sense of prescription 2.
- **TIP (04-16) / LongAct (04-18)** — the "operational target is sparse" pattern that the no-free-lunch result formalizes for safety-critical slices.

## Research angles

- **Measurement of defense-layer correlation.** No published paper measures this in production stacks. A wiki-defining contribution: pick three deployed agentic systems, formalize each layer's failure mode, compute pairwise correlation. If correlation is high, the system has fewer defenses than it claims.
- **Lipschitz-bound computation as monitoring primitive.** The paper's "computable distance-to-boundary" estimate is a candidate runtime monitoring signal. Has anyone instrumented production traffic with it?
- **Trilemma for retrieval-augmented systems.** RAG is a wrapper on the model's input distribution — the same continuity/utility/completeness pinch should apply. Has anyone formalized RAG-as-trilemma?
- **Trinity Defense Architecture vs trilemma.** The Trinity paper (cited in this post) gives deterministic mediation; the trilemma constrains behavioral defenses. The deterministic-vs-probabilistic decomposition is the cleanest framing of agentic security yet — quantitative comparisons would be valuable.
