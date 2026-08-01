# OpenAI Astra: Ten Advances in Mathematics and Theoretical Computer Science

**Date ingested:** 2026-08-01
**Sources:** [The Decoder (08-01)](https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/) · [The Information (07-31)](https://www.theinformation.com/briefings/exclusive-openai-previews-astra-ai-model-dc) · [OpenAI announcement](https://openai.com/index/ten-advances-in-mathematics/) · [openai/ten-proofs on GitHub](https://github.com/openai/ten-proofs) · [@ns123abc on X](https://x.com/ns123abc/status/2083505040224887272)
**Raw:** [RSS](../../raw/rss/2026-08-01-the-decoder-openai-announces-its-next-major-model-astra-by-dropping.md) · [Twitter](../../raw/twitter/2026-08-01-afternoon.md)

---

## TL;DR

OpenAI announced its next major model family, **Astra**, not with a benchmark table but with ten solved open problems in mathematics and theoretical computer science, each accompanied by a **Lean 4 formalisation** published at `openai/ten-proofs`. Astra is built for long-horizon work: multiple agents cooperating on one problem for hours or days. The problems had seen no progress for at least a decade and in most cases much longer, and four of the ten are **counterexamples to what mathematicians believed**. The number that reframes the result is the cost: OpenAI states the tokens for all ten solutions came to roughly **$2,000 at API rates**. Humans did not supply the mathematical arguments; they collaborated with the model to turn those arguments into papers and took responsibility for accuracy. Astra has no release date and will be the first model to go through a new US federal review framework requiring government approval before public release.

---

## The ten results

From the Lean repository, one file per result:

| Area | Result | Lean file |
|---|---|---|
| High-dimensional geometry | Sphere packing, Cohn–Elkies strength determined exactly | `SpherePacking.lean` |
| Coding theory | Binary and spherical codes | `MetricCodes.lean` |
| Group theory | **Existence of non-sofic groups** | `NonSoficGroup.lean` |
| Operator algebras | **Connes's rigidity conjecture disproven** | `ConnesRigidity.lean` |
| Circuit complexity | Permanent lower bounds | `Permanent.lean` |
| Quantum complexity | Parallel repetition for all entangled games | `QuantumParallelRepetition.lean` |
| Lattice cryptography | Closest Vector Problem hardness | `GapCVP.lean` |
| Convex geometry | Ehrhart's volume conjecture | `EhrhartVolumeInequality.lean` |
| Extremal combinatorics | Multicolor triangle Ramsey numbers | `MulticolorTriangleRamsey.lean` |
| Extremal combinatorics | Compactness and degeneracy conjectures | `CompactnessAndDegeneracy.lean` |

The social summary circulating alongside the announcement also counts **three resolved Erdős problems (#146, #180, #183)** among these. Mathematician Thomas Bloom called the batch "big news" and more significant than prior AI results in mathematics. Non-sofic groups is the one specialists flagged first: whether every group is sofic has been open since Gromov raised it, and a construction settles a question that resisted twenty years of attention.

---

## Why the Lean certificates change the argument

Every previous claim of AI mathematical discovery has run into the same objection, which is that a plausible-looking argument from a language model is not a proof and checking it costs an expert weeks. Publishing machine-checkable Lean 4 certificates moves the burden. A referee no longer has to trust the model, or OpenAI, or the write-up. They run the type-checker.

This is the same primitive that three separate results converged on last week from the agent-reliability side. [LEDGERMIND (07-31)](../agentic-systems/2026-07-31-ledgermind-evidence-ledger.md) proposed that an agent trajectory be a provenance-constrained state machine where reasoning may cite only active evidence-ledger entries, [MemTX (ingested today)](../agentic-systems/2026-08-01-memtx-transactional-belief-commit.md) machine-checks two protocol invariants over 5.5 million states rather than arguing for them in prose, and Google shipped **Science One** with natively maintained verifiable evidence chains. Astra's Lean certificates are the fourth instance and the most consequential, because the verification here is total rather than partial: a Lean proof is either accepted by the kernel or it is not, and there is no LLM judge anywhere in the loop. The [07-31 digest](../daily-digest/2026-07/2026-07-31.md) predicted that provenance would arrive as a compliance requirement before it became a research consensus. It arrived faster than that and as a *marketing* asset, which is a stronger form of adoption.

The important caveat: the repository README does not state whether the formalisations are complete or partial, does not describe how the proofs were produced, and does not say what was human-verified. A Lean file whose main theorem depends on an admitted lemma type-checks and proves nothing. Until someone independently confirms there are no `sorry`s and that the formal statements match the informal claims, the certificates are a strong signal rather than a settled fact. That check is cheap and will happen within days.

---

## What Astra actually is

Both The Decoder and The Information describe the same architecture bet, and it is not "a bigger model." Astra is a **model family for long-running tasks in which multiple agents work a problem together over hours or days**. The mathematical results are a demonstration of that specific capability rather than of raw single-pass reasoning: the problems are ones where the work is a long search over candidate constructions with verification at each step, which is exactly the shape a multi-agent long-horizon system should be good at.

Altman demoed Astra to policymakers and regulators in Washington before any public announcement, and OpenAI has not decided whether to ship it as GPT-6 or as another GPT-5 variant. It will be the first model routed through the new US federal pre-release review.

---

## How this relates to prior wiki pages

**It cuts against the sharpest finding of the last week about what agents can and cannot do.** The [07-31 digest](../daily-digest/2026-07/2026-07-31.md) concluded, reading Frontis-MA1 (a 35B meta-evolution agent that lifts MLE-Bench Lite Medal Average from 39.39% to 71.21% on one RTX 4090) against the [shadow-evaluation result (07-30)](../agentic-systems/2026-07-30-shadow-evaluations-ai-research-agents.md) (frontier agents were handed the central open question from two unpublished NeurIPS 2026 papers, completed all of the engineering unassisted, and had both outputs rejected by the original authors): **give an agent a scored target and it will search hard and well; ask it to decide what target is worth scoring and it will not.** Astra is the strongest available test of the first half and says nothing about the second. Pure mathematics is the ideal case for the "scored target" regime, because a conjecture is a target someone else already decided was worth scoring and Lean is a perfect verifier. Astra did not choose these ten problems. That distinction is the whole story, and it is the one most of today's coverage collapses.

**Noam Brown's own caveat is the load-bearing sentence.** He notes OpenAI **tried and failed** on other major problems including Millennium Prize problems, and that more compute could plausibly solve harder ones. Ten successes out of an unstated number of attempts is a hit rate nobody has published, and the $2,000 figure covers the ten that worked, not the search.

**The $2,000 number is the one to keep.** It is the first credible price tag on a unit of novel mathematics, and it lands in the same week as [Kilo's telemetry (07-31)](../ai-routing/2026-07-31-kilo-open-weights-cost-routing.md) showing open-weight models carrying 79% of a coding-agent workload at a 25x price advantage, and OpenAI's own 80% price cut on GPT-5.6 Luna. Two things are happening at once: the cost of routine intelligence is collapsing, and the cost of a research result that a human specialist would price in months of labour is now four figures. Those are the same trend viewed from opposite ends.

---

## Gaps and what to watch

- **Completeness of the Lean formalisations.** No `sorry`, and formal statements matching the informal theorems. Independently checkable, and the first thing anyone should check.
- **The denominator.** Ten successes over how many attempts, and how much compute in the failures. The $2,000 is solution tokens, not search tokens.
- **Reproducibility.** An internal Astra checkpoint produced these, and no external party can rerun them. The Lean files verify the *output*; nothing verifies the *process*.
- **Human contribution.** "Humans collaborated with the model to turn arguments into papers" is a wide range, spanning copyediting to supplying a missing lemma.

---

## Related pages

- [RL for LLMs](rl-for-llms.md)
- [Agent Benchmarks](../agentic-systems/agent-benchmarks.md)
- [Self-Evolving Agents](../agentic-systems/self-evolving-agents.md)
- [MemTX (08-01)](../agentic-systems/2026-08-01-memtx-transactional-belief-commit.md)
- [LEDGERMIND (07-31)](../agentic-systems/2026-07-31-ledgermind-evidence-ledger.md)
