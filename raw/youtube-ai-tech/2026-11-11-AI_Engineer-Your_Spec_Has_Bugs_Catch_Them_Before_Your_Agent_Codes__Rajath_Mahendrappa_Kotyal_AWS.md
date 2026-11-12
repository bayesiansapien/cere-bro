# Your Spec Has Bugs. Catch Them Before Your Agent Codes. (Rajath Mahendrappa Kotyal, AWS)

**Channel:** AI Engineer
**Published:** 2026-11-11
**Source:** https://www.youtube.com/watch?v=0EnLxIbAvYk

## TL;DR
AWS's Automated Reasoning Group built a specification analyzer (shipped in Kiro as Requirements Analysis) that checks a spec before a coding agent sees it. An LLM rewrites vague requirements, translates them into SMT-LIB formulas, and a solver proves contradictions, ambiguities and gaps. The key trick is sampling the translation 7 to 10 times and clustering by logical equivalence: if the samples disagree, the sentence is ambiguous and goes back to the human as a multiple-choice question. "The LLM translates, the solver checks, the human decides."

## Key Takeaways
- **Bug class targeted:** cross-sentence defects that look fine individually. Example: "when inventory is unavailable, place a back order" vs "no order shall be placed as a back order." Both rules cannot be satisfied at once.
- **Three defect types:** conflict (two rules unsatisfiable together), gap (no rule covers a state, e.g. idle orders), ambiguity (one sentence admits multiple readings, e.g. "remove the record" means delete or soft-hide).
- **Pipeline:** (1) LLM refines wording. (2) If it can't resolve, formalize to SMT and check satisfiability. (3) Re-sample translation N times, cluster interpretations by logical equivalence, then accept, ask the user, or abstain.
- **Cited motivation:** 20-40% accuracy drop from unclear prompts, a large fraction of "valid" code still wrong, about 2x more regressions in deployment. These figures were given without specific citations.
- **Honest limits:** there is no oracle for spec correctness except the user, who holds implicit domain knowledge. Evidence for formalization in agent workflows is still thin.

## Architecture & Optimization Mechanics
- **Self-consistency as an ambiguity detector.** Sampling multiple formalizations and clustering by solver-checked equivalence turns semantic entropy into a measurable signal. Disagreement across samples flags the input, not the model, as the problem. This is semantic-entropy uncertainty estimation with a symbolic equivalence check instead of an NLI model.
- **Neurosymbolic split of labor.** The LLM handles NL to logic (fuzzy, cheap to retry). The SMT solver handles global consistency (exact, but expensive across many requirements). AWS notes the analysis takes minutes, because pairwise and global satisfiability checks grow fast with spec size.
- **Abstention is a first-class output.** When interpretations cannot be resolved, the system refuses to implement rather than guessing. That is the same design as a router's "escalate" path.
- **Weak spot:** the guarantee is only as good as the NL to SMT translation. If all N samples share the same wrong reading, clustering reports high confidence on the wrong formula.

## Grounded Context (Web Enrichment)
This shipped as **Kiro Requirements Analysis** in May 2026 (covered by GeekWire, SiliconANGLE, The New Stack, and Kiro docs at `kiro.dev/docs/specs/analyze-requirements`). AWS reports that about 60% of draft requirements across 35 internal Kiro projects needed refinement before producing valid code. That is a vendor figure, not independently verified. Findings appear as plain-language questions with selectable fixes or dismissal, which matches the talk. The group behind it also builds Bedrock Automated Reasoning checks, so the SMT tooling is mature.

A credible counterpoint from third-party blogs: a disciplined LLM pass that explicitly hunts for contradictions, gaps and ambiguities catches most of the same issues without a solver. The solver's real value is proof of a conflict (no false positives on contradictions) and exhaustive gap checking, which matter most for long, rule-heavy specs. For short specs the prompt-only approach is probably good enough.

## Real-World Application / Actionable Step
- Reuse the "sample N, cluster by equivalence" trick for routing confidence. For a query, sample several cheap-model answers. If they cluster tightly, serve the cheap model. If they scatter, escalate. Use an exact-match or programmatic equivalence check where possible.
- Before handing an agent a multi-constraint experiment spec (e.g. "keep perplexity within 1%, stay under 4 bits, never quantize the router"), run an explicit contradiction/gap pass. For numeric constraints, encode them in Z3 directly. It takes minutes and catches infeasible specs before burning GPU hours.
- Add an abstain path to your agent workflows: unresolved ambiguity means ask, not guess.
