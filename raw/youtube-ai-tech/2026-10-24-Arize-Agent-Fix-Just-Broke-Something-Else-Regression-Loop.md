# Your Agent Fix Just Broke Something Else (Sofia Jakovcevic, Arize AI)

**Channel:** AI Engineer
**Published:** 2026-10-24
**Source:** https://www.youtube.com/watch?v=v5tm5EAzsAs

## TL;DR
Agent behavior lives in runtime trajectories, not in the diff. A one-line "confirm before any action" prompt change raised action safety +17 points and dropped task completion -17 points (users abandoned sessions mid-confirmation), netting zero. The fix is a five-step regression loop built from production traces (curate dataset, define evals, run baseline, test the change, gate in CI), where every production failure becomes a new test. The pitch for what comes next: coding agents wired to observability backends so they debug and fix agents themselves.

## Key Takeaways
- **"The diff tells you what changed, the trace tells you what happened."** Traces are the new source of truth for agent logic.
- **Single-metric wins hide regressions.** Always track multiple dimensions (safety, completion, cost, latency) per change.
- **Dataset composition (4 buckets):** representative traffic, known failures, edge cases, and successful workflows to protect. The last is the one teams forget.
- **Evaluator choice:** code evals for deterministic checks, LLM-as-judge for subjective ones (hallucination, trajectory efficiency, task completion).
- **Model swaps need ROI proof:** a model 5x more expensive must show measured gains on the same suite before switching.
- **CI gate:** each PR runs the experiment suite. No merge until regression thresholds pass.
- **Every failure becomes a test**, so the suite grows harder over time.
- After iteration, the demo agent reached +18 safety and +6 completion vs baseline, showing the tradeoff is resolvable, not inherent.

## Architecture & Optimization Mechanics
- This is the same problem as compression regression: a 4-bit quant can improve one benchmark while silently degrading tool calling or multi-turn completion. Per-dimension gates catch it. Averages hide it.
- **Routing relevance:** the "5x more expensive model" case is exactly the routing ROI question. Replaying production traces through candidate models with a fixed eval suite gives per-query-class win rates, which is the training signal a router needs.
- **Trajectory-level metrics** (step count, tool-call sequence divergence) are cheap, label-free signals of behavior drift, useful for both prompt and model changes.
- Weak spot: heavy reliance on LLM-as-judge with no mention of judge variance. A ±17 point swing on a 100-row dataset can be partly noise. No confidence intervals were shown.

## Grounded Context (Web Enrichment)
The trace-to-test loop is now industry consensus across vendors (Arize, Braintrust, Arthur, FutureAGI), with the shared caveat that static offline suites go stale as traffic shifts and are a regression gate, not a full ship gate. Recommended practice is per-axis thresholds rather than an aggregate score, which matches the talk's net-zero example.

The research-grade addition is arXiv 2603.02601, which frames CI gates as statistical decisions with PASS/FAIL/INCONCLUSIVE verdicts and uses behavioral fingerprinting of execution traces. It reports 86% regression detection power vs 0% for binary pass/fail testing across 7,605 trials and five models. That directly addresses the talk's blind spot: with stochastic agents, a gate needs sample-size-aware statistics, not single-run scores.

## Real-World Application / Actionable Step
- For every quantization or pruning variant, run a **per-dimension regression gate** (accuracy, tool-call validity, format adherence, latency, refusal rate). Fail on any single axis, never on the average.
- Build the eval set from 4 buckets, including a "protected successes" slice. Compressed models often fail first on cases the baseline handled easily.
- Use **repeated runs plus a three-valued verdict** (pass/fail/inconclusive) with bootstrap CIs before declaring a compression or routing change neutral.
- For routing: log production traces, replay them through cheap and expensive candidates, and use per-class win rates as router labels.
