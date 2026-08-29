# What Does an Evaluation License? A Commit-Bound Census of Claim-Relative Inference in Inspect Evals

**Source:** HuggingFace Daily Papers · [arXiv 2608.19269](https://arxiv.org/abs/2608.19269)
**Raw:** [raw/huggingface/2026-08-28-what-does-an-evaluation-license-a-commit-bound-census-of-cla.md](../../raw/huggingface/2026-08-28-what-does-an-evaluation-license-a-commit-bound-census-of-cla.md)

---

## TL;DR

An eval artifact specifies a computation: a task, a scorer, and a reported metric. Run it and you get a number. This paper's argument is that the number does not automatically **license** the claim attached to it, because reproducing the claim requires historical evidence and semantic grounding that the artifact usually does not carry. The authors formalize that missing layer, then run a census over **all 124 mechanically eligible units in Inspect Evals at a pinned commit**. The result is the headline: **110 of 124 stop before deterministic inference is possible**, because the evidence or the semantic grounding needed to replay the claim is unavailable. Only 14 close. That is not a robustness score, and the paper is careful about this: the output is **typed stops, instability witnesses, and stable substructure**, not a robust/not-robust label.

---

## What the formalism actually says

Four objects. A **frozen substrate D** (the evidence you are allowed to use, pinned so the audit is reproducible). A **grounded family F** (the set of admissible semantic readings of the eval, since "correct" in an eval usually admits more than one defensible interpretation). A **claim query q** (the thing someone asserted on the basis of the metric, for example "model A beats model B on this task"). And the **identified set**: the set of answers to q that survive across everything in F given D.

If the identified set is a single value, the claim is licensed. If it is a range, the eval supports a weaker claim than the one being made. If required evidence or grounding is missing, inference **stops** and you get a typed reason for the stop rather than a fabricated answer. That typing is the useful engineering artifact here: instead of one aggregate "this eval is unreliable," you get a machine-readable reason per unit.

The census also separates results by **claim resolution** (exact value, winner, complete ordering, pairwise relation) and by **primary versus review family**. That separation matters because the claim resolutions do not degrade together: an eval can be too unstable to license "model A scored 62.3" while still cleanly licensing "model A beat model B." Most published claims are pairwise or winner claims, so this is the practically important distinction, and it is the one the paper's structure is built to surface.

---

## How this relates to what the wiki already knows

**This is the formal floor under a pattern this wiki declared established three weeks ago.** The [agent-benchmarks page](../agentic-systems/agent-benchmarks.md) recorded on 08-11 that four papers in two days each found a widely trusted benchmark was substantially measuring an artifact of its own construction: [SWE-Bench ProMax (08-11)](../agentic-systems/2026-08-11-swe-bench-promax.md) citing that nearly 60% of unsolved SWE-bench Verified instances contain flawed tests, [A²E (08-11)](../agentic-systems/2026-08-11-harness-evolution-cluster.md) showing model-harness combinations vary by task type so no single-harness leaderboard number is a model property, Evo-Bench building machinery to separate harness-improving capability from base model strength, and [StreamArena (08-10)](../agentic-systems/2026-08-10-streamarena-streammind.md) finding a baseline reading only the last four frames matches complex streaming models. **Every one of those is an instance of the general failure this paper names.** They each found a specific eval whose metric did not license its claim. This paper asks the question structurally and answers it for a whole suite at once.

**The 110-of-124 number reframes what "the measurement crisis" means.** The prior framing on this wiki was that some benchmarks are broken and should be replaced with better ones, which is what DSAgentBench, VibeLifeBench and SPIEval (08-12) were built to do. This paper's finding is that the deficiency is not mostly in benchmark *design*, it is in what evaluation artifacts **carry**. A well-designed eval that does not ship the historical evidence and semantic grounding needed to replay a claim produces an unlicensed claim just as reliably as a badly designed one. **Building better benchmarks does not fix this; shipping more with the benchmark does.**

**It also gives a name to a habit this wiki has been practicing informally.** The methodological rule the agent-benchmarks page adopted on 08-10 is: before believing any agent-capability number, find the cheapest baseline that could produce it. That is a manual, per-case search for alternative semantics. The grounded family F is that search, formalized and enumerated, which means it can be run once per suite rather than re-invented per reader.

**And it lands on a live open thread.** The 08-26 and 08-28 Looking Ahead sections both predicted that a harness paper would publish a pass^k curve within 60 days, on the grounds that Microsoft's Thinkingbox (08-25) measured a top model collapsing from 65.36% pass@1 to 25.25% pass^20, so single-attempt numbers on stateful benchmarks are indefensible. This paper supplies the vocabulary for why: **a pass@1 number on a stochastic stateful task has a wide identified set, and reporting it as a point estimate is an unlicensed claim resolution.** Five consecutive harness papers have made exactly that move.

---

## Gaps

- **One suite, one commit.** Inspect Evals is a good choice (broad, maintained, mechanically parseable) but it is one ecosystem. Whether 110/124 is characteristic or specific to how Inspect packages evals is unknown, and the obvious next census is lm-evaluation-harness or HELM.
- **"Mechanically eligible" is doing work.** The 124 units are the ones the tooling could process. What fraction of the whole suite that is, and whether ineligible units are systematically different, decides how to read the ratio.
- **No cost of compliance.** The paper says what is missing. It does not estimate what it would take an eval author to ship enough substrate and grounding to close a stop, which is the number that decides whether this becomes practice or stays a diagnosis. A typed-stop taxonomy is exactly the input a "what would it cost to fix each class" follow-up needs.
- **The audit's own semantics.** Choosing the grounded family F is itself an interpretive act. The paper's design decision to return typed stops rather than force one evaluator meaning is the right defence, but the family is still authored, not derived.

---

## Related pages

- [Agent Evaluation & Benchmarks](../agentic-systems/agent-benchmarks.md)
- [Responsible AI](responsible-ai.md)
- [SWE-Bench ProMax (08-11)](../agentic-systems/2026-08-11-swe-bench-promax.md)
