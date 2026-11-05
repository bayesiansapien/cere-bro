# Building the AI Agent Is Easy. Proving It's Safe Isn't (Jonathan Osborne, NatWest)

**Channel:** AI Engineer
**Published:** 2026-11-04
**Source:** https://www.youtube.com/watch?v=5UgnatzpZ9E

## TL;DR
NatWest is moving about a third of the journeys in Cora (its assistant, ~100k conversations a day, 19M retail customers) from scripted flows to RAG answers and action-taking agents. The agent code was cheap. The expensive, reusable asset is the evaluation spine: a deterministic routing funnel that shrinks what the LLM ever sees, quality scored as a vector rather than a number, LLM judges calibrated against humans, CI regression gates, and shadow-mode rollouts. The sharpest finding is that a production LLM judge had near-zero correlation with human scores despite a small mean error.

## Key Takeaways
- **Four failure modes scripted bots never had:** confident hallucination, prompt injection, correct but unhelpful looping, and nondeterminism that breaks classical assertions and years of regression tests.
- **Shrink before you harden.** The routing funnel strips ~20% of traffic (button clicks) by context filter, then deterministic metadata rules, then a gated relevance and rephrase step, then a non-generative neural intent classifier over embeddings, then policy rules. Only residual traffic reaches generative models.
- **Quality is a vector:** safety, task and experience, each monitored and alarmed separately. This separates "hallucinating" from "right but insufferable," which need different fixes.
- **Calibration beats accuracy.** A router that is 94% accurate but 100% confident on its 6% errors is more dangerous than one that is 85% accurate and knows its uncertainty.
- **Headline pass rates hide spread.** Payment agent human eval (111 conversations, 37 journeys, 3 raters each): 83% overall, but 97% happy path, 76% edge cases, 43% on topic changes.
- **Human raters disagree too:** 95% agreement on bias and fairness, only 64% on intent understanding. Matching humans cannot be the judge's target where humans themselves split.
- **Judge leniency is the core trap.** On ~14k complaint-summary cases, the judge's faithfulness mean was 0.97 with tiny variance vs humans at 0.83 with wide variance. Mean error looked fine, correlation was near zero. A judge that cannot discriminate is worthless.
- **The judge model is config.** Swapping only the judge model moved the score margin over threshold from 0.8 to 0.2. Moving the judge to a different model family from the agent narrowed the gap with humans.
- **Ops cadence:** OTel and OpenInference traces, 5% random sample plus all "interesting" sessions (handoffs, failures, long or angry), offline scoring every 4 hours, hard regression gate in CI/CD on prompt and context changes. Air-gapped, zero PII egress, judge reached via internal GenAI gateway, Comet Opik for GenAI and Comet MPM for the classical classifier.
- **Rollout:** shadow mode (model classifies, scripted bot answers) breaks the regulator deadlock of "no production data without approval, no approval without production data." Then brand-by-brand percentage rollout with KPI gates and per-backend kill switches that revert in seconds.
- **Feedback as a gate:** in the complaints tool, handlers cannot rerun an investigation without leaving feedback, which built a 14k label set.

## Architecture & Optimization Mechanics
- **The funnel is an LLM router in production form.** Cheap deterministic and discriminative stages absorb most volume before generative inference. Every stage emits an auditable code, and the whole thing is versioned config that can change without redeploy.
- **Two drift regimes, two instruments.** Generative components regress on change (prompts, context, model swaps), so they need CI gates. The discriminative intent classifier drifts with the world, so it needs input-feature drift, F1 against human labels and retrain thresholds. Osborne argues input-feature drift is the earlier canary, firing before F1 degrades.
- **Judge evaluation should use rank and correlation metrics,** not MAE. Compressed judge scores near the ceiling produce small MAE while carrying no information.
- **Cross-family judging** reduces shared blind spots and self-preference between generator and evaluator.

## Grounded Context (Web Enrichment)
NatWest's public timeline backs the talk. Cora+ launched in June 2024 as an IBM-built generative upgrade. In early 2026 the bank announced an agentic assistant inside Cora, reported as built on OpenAI models after NatWest became the first UK bank to partner directly with OpenAI. It targeted about 25,000 customers by end of Q1 2026, with voice-to-voice and agentic fraud support planned later. NatWest says it is among the first UK banks to put agentic AI in front of customers, but customer counts come from the bank's own statements and lack independent confirmation. Osborne's closing line ("next month I'll find out how much of this is true when we go live") means the payment-agent figures are pre-launch validation, not production results.

The judge findings match the broader research consensus. LLM judges show well-documented leniency, position bias and self-preference toward same-family outputs, which is why cross-family judging and correlation-based calibration have become standard advice. The 64% human agreement on intent is a useful reminder that inter-annotator agreement is the ceiling for any judge on subjective dimensions. A small caveat: the talk was delivered at a Comet-sponsored slot and the tooling recommendations reflect that.

## Real-World Application / Actionable Step
- **For routing research:** report router calibration (ECE, selective accuracy, risk-coverage curves), not only accuracy. A router that knows when to escalate to the larger model or a human is the production requirement.
- **Audit any LLM judge you use** for compression or routing evals: compute Spearman or Kendall correlation with human labels and inspect score variance. If the judge pins near the top, it cannot measure quality loss from pruning or quantization.
- **Pin the judge model as part of the eval config** and re-baseline when it changes. Use a different model family from the system under test.
- **Slice evals by scenario type.** Report happy path, edge case and topic-change (digression) separately when testing compressed or routed models. Aggregate scores hide where quantized models usually break first.
- **Borrow the shadow-mode pattern** to validate a new router or compressed model: run it on live traffic in parallel and log decisions while the incumbent answers.
