# Evals for High-Stakes AI Agents | Doneyli De Jesus & Annabell Schäfer, Langfuse

**Channel:** AI Engineer
**Published:** 2026-10-18
**Source:** https://www.youtube.com/watch?v=obfPzbapMIM

*Workshop, AI Engineer New York. Vendor talk (Langfuse); the method is tool-agnostic.*

## TL;DR
Agents fail while every system metric stays green: a support agent says "refund issued" without ever calling the refund tool, and you find out weeks later. Langfuse's answer is the "AI engineering loop" (trace, monitor, build datasets, run experiments, evaluate) with a regulated-industry twist: start from ground truth built by domain experts, have them write free-text critiques in an annotation queue, let an LLM cluster those comments into failure modes, then turn each mode into a scored evaluator (mix of LLM judges and deterministic code checks) that gates every prompt or model change in CI. The demo is a banking assistant with PII masking, persona impersonation and an "investment advice" hard limit.

## Key Takeaways
- **Silent failure is the core risk.** Check tool-call evidence, not the agent's own claim of success.
- **Entry point depends on stakes.** Low-stakes internal tools: ship with tracing and frustration monitors, add evals later. Regulated, customer-facing: ground truth first.
- **Three ways to get ground truth in regulated settings:** expert curation, shadow runs (humans keep doing the work while the agent runs in parallel), or full human-in-the-loop then gradually automate the slices you trust.
- **Expert-friendly annotation:** a binary or 1 to 10 score plus a dictated free-text comment, about 30 seconds per trace. One hour of expert time covers about 100 traces.
- **Do not ask experts to invent categories.** Collect raw critiques, then use an LLM to cluster them into failure modes (e.g. missing citation, wrong formal register, dispute not resolved, out of scope, unsolicited upsell).
- **Blend evaluator types.** LLM judges for fuzzy criteria, regex/exact-match code for anything deterministic. Code evaluators give the same output 100% of the time.
- **Multiple datasets per agent:** a red-team/prompt-injection set, a per-use-case set (disputes), out-of-scope requests.
- **CI gating:** a prompt version promoted to "production" triggers a GitHub Action that runs the experiment and fails on per-score thresholds.
- **PII:** masking function redacts card numbers and SSNs before traces are persisted.
- **Business dashboards:** 1,400 deflected interactions in 7 days for under $7 in tokens; 18% thumbs-down; 89 investment-advice-risk cases flagged.
- **Anti-pattern:** "please fix my agent, make no mistakes" via MCP produces slop. Automate instrumentation, failure-mode mining and experiment fan-out; keep humans for taste and dataset curation.
- **Judge calibration (Q&A):** have one human label a representative sample, tune the judge to agree with it, start biased toward false positives and tighten over time.
- **Scale:** 150,000+ developers, 21 of the Fortune 50, 90B+ observations a month; storage moved from Postgres to ClickHouse.

## Architecture & Optimization Mechanics
- **The failure-mode taxonomy comes from the data, not from up front.** This is open coding then axial coding from qualitative research, done with an LLM doing the clustering. It avoids the common trap of measuring generic "helpfulness" scores that do not match how the product actually fails.
- **Score = failure mode.** Each mode becomes a named score with a threshold. Gating on a vector of scores, not one aggregate, stops a gain in one area from hiding a regression in another.
- **Deterministic checks as anchors.** Exact-match and regex evaluators provide a variance-free floor; judges cover the rest. Judges should only grade things code cannot.
- **Trigger on config, not code.** Prompt version, model ID and tool set are the agent's real "source code," so changes to those must be what triggers CI.
- **Observability as eval data.** Production traces flow back into datasets once a human confirms them as good examples, closing the loop.

## Grounded Context (Web Enrichment)
ClickHouse acquired Langfuse on 16 January 2026, alongside a $400M Series D at a $15B valuation. Langfuse says open source and self-hosting continue unchanged ([ClickHouse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), [SiliconANGLE](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/), [Langfuse](https://langfuse.com/blog/joining-clickhouse)). That explains the ClickHouse hard dependency mentioned in Q&A. The method closely tracks the Hamel Husain and Shreya Shankar error-analysis approach and Shankar et al.'s "Who Validates the Validators?" (EvalGen, 2024), which showed judge criteria drift as people grade more outputs. That is a reason to re-check judge agreement regularly, as the speakers suggest.

The weak spot is the business dashboard. "1,400 interactions that did not go to a human" counts deflection, not resolution; with an 18% thumbs-down rate and "dispute not resolved" as a top-3 failure mode, many of those deflections may be unresolved customers. The talk hand-waves judge calibration with no agreement metric (Cohen's kappa or TPR/TNR against human labels), which is the number auditors in regulated industries will ask for.

## Real-World Application / Actionable Step
- **For your LLM router:** treat a routing-policy change (threshold, candidate model set, cost weight) as a config change that triggers a CI eval. Gate on per-failure-mode scores across query slices, not on mean quality. A router that saves 40% cost while doubling "wrong-format" failures on one slice should fail the gate.
- **Mine router failure modes from traces.** Sample 100 queries routed to the cheap model, have a domain expert write one-line critiques, cluster with an LLM. Those clusters become the features your router is missing.
- **Quantization and pruning gates:** for each compressed checkpoint, run the same blended evaluator suite. Deterministic checks (JSON validity, exact-match tool calls) catch the specific breakages low-bit models show first.
- **Report judge agreement.** For every LLM judge, keep a 100-item human-labeled set and report TPR/TNR. Re-run monthly.
