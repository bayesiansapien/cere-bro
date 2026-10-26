# How to Write Your First AI Eval (SallyAnn DeLucia, Arize AI)

**Channel:** AI Engineer
**Published:** 2026-10-25
**Source:** https://www.youtube.com/watch?v=gv4w23xYj-0

## TL;DR
A hands-on workshop on building an LLM-as-judge eval for a multi-agent travel planner. Recipe: read traces first, define "good" with concrete criteria (answers the follow-up, matches requested days, stays within budget), judge one quality per eval, write a 6-part spec (task, success, failure, what's judged, 3 pass bullets, 3 fail bullets), turn it into a judge prompt with variable mapping, iterate in a playground on ~20 traces, then align against human labels and run online. The newer angle: **decision models** (OpenAI's Decisions API, TypeSafe's Jev) as cheap, fast, probability-returning judges that may replace explanation-generating LLM judges for many checks.

## Key Takeaways
- **Why evals beat vibes:** without them you cannot detect prompt regressions, compare models objectively, or gate CI.
- **Evals ≠ unit tests:** many valid outputs, and the logic is only visible in traces. "Traces are the logs, evals are the tests."
- **Eval taxonomy:** LLM-as-judge (label + explanation), decision models (probability + label, no explanation), code evals (JSON validity, keyword, ROUGE/BLEU), annotations/golden sets, agent-as-judge (complex success criteria), plus production-only user feedback and business metrics.
- **Concrete over vague:** replace "helpful/accurate" with checkable statements tied to the input.
- **One criterion per LLM judge.** Multi-criteria is tolerable for decision models and agent-as-judge.
- **Start small and grow:** Arize's own agent Alex began with ~4 evals (QA correctness, frustration, jailbreak, toxicity) and now runs 32.
- **Dataset by span type:** root spans (`parent_id = null`) for end-to-end checks, tool spans for tool-output correctness.
- **Labels:** binary by default. Add "partially correct" or "N/A" when it carries decision value. Set optimization direction and keep explanations.
- **Metrics vs evals:** a metric says something is broken. An eval names the failure mode.
- **Every stakeholder defines success:** product, engineering, support, domain experts, security.

## Architecture & Optimization Mechanics
- **Decision models are judge compression.** Replacing a generative judge (reasoning + label) with a single-pass classifier returning calibrated probabilities is essentially distilling the judge. Cost drops by orders of magnitude, latency falls, and you get a continuous score usable as a router or reward signal.
- **Router training signal:** a probability-returning predicate ("is this answer within budget?") is exactly the soft label a quality-aware router needs. Decision-model judges make large-scale, per-query quality labeling for routing affordable.
- **Variable mapping** decouples eval templates from trace schemas. Useful when the same eval must score FP16 vs quantized model traces with different instrumentation.
- Weak spot: the workshop never quantifies judge-human agreement. "Alignment" is mentioned only as a next step, yet it is the step that makes the eval trustworthy. A judge running on GPT-4.1-mini without measured agreement is still vibes, just automated.

## Grounded Context (Web Enrichment)
The decision-model reference is current. OpenAI's **Decisions API** entered public beta on Oct 6, 2026 (`/v1/decisions`, running on GPT-6 Luna) with three output types: predicates (probability a statement is true), choices (fixed set with confidences), and scores (rubric scale). Pricing is $0.10 per M input tokens with no output charge. TypeSafe's Jev is a cheaper competitor at ~$0.042/M. Langfuse added decision-model evaluators the next day, so tooling adoption is fast.

The "one criterion per judge" advice has research support. The Multi-Crit benchmark (arXiv 2511.21662) found that judging several criteria in one pass induces inter-criterion dependencies, with judges tending to assign the same preference direction across criteria and missing conflicts. Decomposed per-criterion grading (Farzi et al., criteria-based relevance judgments) is the established alternative. Practitioner evidence also favors binary over 5-point scales for human alignment. A controlled cross-model study of single vs multi-criterion prompting is still missing.

## Real-World Application / Actionable Step
- Benchmark **Decisions API / Jev as a routing oracle**: for a set of queries, get predicate probabilities ("is the small model's answer correct?") and compare against expensive LLM-judge labels. If agreement is high, use decision models to label routing training data at scale.
- In compression evals, write **one binary judge per failure mode** (format break, instruction drift, factual error) rather than one holistic score. Holistic judges under-detect correlated degradations.
- Always run an **alignment step**: label 50 to 100 examples yourself, report judge-human Cohen's kappa, and only then trust the judge on quantized-vs-baseline comparisons.
- Try converting an existing LLM-judge eval into a decision-model predicate and compare cost, latency, and agreement. This is a quick, publishable-quality ablation.
