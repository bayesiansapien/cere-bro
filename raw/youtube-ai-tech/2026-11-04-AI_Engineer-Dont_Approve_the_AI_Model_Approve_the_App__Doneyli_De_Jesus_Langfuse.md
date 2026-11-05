# Don't Approve the AI Model. Approve the App (Doneyli De Jesus, Langfuse)

**Channel:** AI Engineer
**Published:** 2026-11-04
**Source:** https://www.youtube.com/watch?v=-uBABM2AuFg

## TL;DR
A top-five bank told Langfuse it does not certify models, it certifies applications. The resulting method is a golden dataset per application, traces as audit evidence, multi-dimensional scoring (deterministic code, trajectory checks and LLM judges), and per-dimension thresholds set by risk and domain experts that gate any config change (prompt, model, tool). A 10-K analyst agent went from 60% numeric accuracy to about 95% by giving it a calculator tool, clearing the bank's 85% gate. Approval cycles dropped from weeks to minutes.

## Key Takeaways
- **Public benchmarks are irrelevant to the approver.** Banks treat internal data and context as proprietary, so the only evidence that counts is performance on their own tasks.
- **Three deployment requirements in regulated finance:** on-prem (banks are re-standing up data centers with GPUs), gated with no internet egress (zero-data-retention promises are not enough), and air-gapped access.
- **Grounded is not correct.** One model scored 97% on groundedness but about 60% on numeric accuracy. It cited the right sources and still did the arithmetic wrong.
- **Fix the harness, not the model.** Offloading math to a deterministic Python tool lifted numeric accuracy to about 95%. Approving the harness means a future model swap does not reset certification.
- **Three evaluator types, blended:** deterministic scorers (same input, same output), trajectory or path evaluation (did the agent take the right steps, not just land on a plausible answer), and LLM-as-judge for qualitative aspects. Pure LLM judging "won't cut it."
- **Per-dimension gates, not averages.** A run passing groundedness and completeness but scoring 0 on binary regulatory compliance must fail outright. One dimension can veto promotion.
- **Domain experts set thresholds.** Risk owners define the bar per use case. Failures in critical dimensions feed an annotation queue for experts; reviewed traces become candidates for the golden dataset.
- **Every config change triggers re-gating.** Prompt promotion, model swap or new tool reruns the full eval (datasets of 150 and 1,500 questions in this engagement).

## Architecture & Optimization Mechanics
- **Unit of certification = (model, system prompt, tools, retrieval config).** Treating the model as a swappable component is what lets cheaper or compressed models be adopted without new approvals, as long as the app clears the same gates.
- **Tool offloading as capability substitution:** deterministic tools for arithmetic remove the need for a larger model to get numbers right. A small model plus tools passed a gate it failed alone. That is direct evidence that harness design moves the cost-quality Pareto frontier.
- **Gate logic:** `promote = all(score_d >= threshold_d for d in dims)` with some dimensions binary. This is a conjunctive, veto-style criterion, which is stricter and more informative than a weighted mean.
- **Closed loop:** traces, then scores, then failure-mode curation, then expert annotation, then golden-set refresh. The benchmark co-evolves with production failures.

## Grounded Context (Web Enrichment)
Langfuse was acquired by ClickHouse in January 2026, alongside ClickHouse's $400M Series D at a $15B valuation. Langfuse already ran on ClickHouse for both cloud and self-hosted deployments, which explains the talk's emphasis on on-prem, air-gapped operation. The method is sound but not novel. It closely mirrors what NatWest presented at the same event (multi-dimensional scoring, CI regression gates, expert labels), suggesting "app-level eval gates" is becoming the consensus pattern in regulated AI. The bank is unnamed and the 60% to 95% result comes from one use case, so treat it as illustrative rather than a benchmark.

The regulatory backdrop has shifted in the bank's favor for this approach. In April 2026 US agencies replaced SR 11-7 with new interagency model risk guidance (Fed SR 26-2, OCC Bulletin 2026-13), which reportedly leaves generative and agentic AI out of scope pending an RFI. With no model-level rulebook for LLMs, banks are defining their own application-level evidence standards, which is exactly the vacuum this framework fills. Third-party risk guidance still applies to vendor models, reinforcing the on-prem preference.

## Real-World Application / Actionable Step
- **Frame compression and routing work as "app-preserving" changes.** When proposing a quantized, pruned or routed model to an enterprise, ship it with an app-level eval showing every dimension still clears its gate. That is the language approvers use.
- **Evaluate compressed models with tools enabled.** A pruned or 4-bit model plus a calculator or code tool may match the full model on the app, even if raw benchmarks drop. Measure the harnessed system, not the bare model.
- **Use veto dimensions in your own eval suites.** Mark safety or format-validity checks as binary gates so a compression method cannot hide a catastrophic regression behind a good average.
- **Add trajectory evaluation for agentic benchmarks** of routed or compressed models. Smaller models often reach plausible answers via skipped steps, which output-only scoring misses.
