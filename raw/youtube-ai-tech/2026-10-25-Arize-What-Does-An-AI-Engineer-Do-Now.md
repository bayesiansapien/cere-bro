# What Does an AI Engineer Do Now? (Aparna Dhinakaran, Arize AI)

**Channel:** AI Engineer
**Published:** 2026-10-25
**Source:** https://www.youtube.com/watch?v=ImnZ7s68jw8

## TL;DR
The AI engineer's job has shifted from doing each step of build → eval → ship → monitor → improve to **building the loop that does those steps**. Agents write features, agents review code, and agents read telemetry. Arize's always-on agent "Signal" is the worked example: triggered on a schedule, by events, or by metrics, it loads traces, APM data, and repo access into a proxied sandbox, finds issues, opens PRs, persists findings and learned skills to memory, then tears down the sandbox and credentials. The irreducible human work is defining "good" and **evaluating the evaluators** against golden human labels.

## Key Takeaways
- **Karpathy funnel framing:** ~6B barely use LLMs, 1 to 2B casual, ~20M professionals, ~5,000 at labs running thousands of agents. The AI engineer's role is to close the lab-to-enterprise gap.
- **Then vs now:** write the feature → build the loop that writes it. Read the diff → build agents and evals that review. Set up telemetry → make agents the primary consumers of telemetry.
- **Always-on agent anatomy:**
  - **Triggers:** cadence (every 3 to 6h), events (Slack complaints), metric thresholds.
  - **Run:** fresh sandbox with traces, third-party logs and metrics, repo, keys. A single egress proxy. Everything inside is traced.
  - **Persist vs discard:** issues, traces, and learned skills persist (skills saved to repo). Sandbox, credentials, and repo access are discarded.
  - **Durability:** state lives outside the sandbox, so a crashed harness resumes from the failed step.
  - **Memory of issues:** tracks previously seen and escalating issues across runs.
- **Harness- and model-agnostic:** Claude Code, Cursor, Codex. Swapping models lets them measure PR and issue quality vs cost.
- **Trace the coding agents too,** not just production agents, to understand the whole "agent factory."
- **Trust the judge:** golden datasets, measure judge-human agreement, and ship an evaluator only once aligned. Same evals run offline (pre-ship) and online (production).

## Architecture & Optimization Mechanics
- **Model-swapping within the agent is a routing testbed.** Signal running the same issue-detection task across model tiers, scored by evals, produces exactly the cost-quality frontier a router needs. Lesson: build model choice in as a parameter from day one, so routing experiments are free.
- **Ephemeral sandbox + external durable state** mirrors stateless inference servers with external KV/prefix caches. Compute is disposable and state is persisted and resumable.
- **Telemetry for agents, not humans:** agent consumers can read raw traces at volume, so log richer structured data (token counts, expert routing stats, cache hit rates) rather than dashboard-friendly aggregates.
- Weak spot: no data on Signal's precision (false-positive issues), PR acceptance rate, or cost per run. "Agents fix agents" without these numbers is a product vision, not a demonstrated result.

## Grounded Context (Web Enrichment)
The Karpathy reference checks out: on Oct 11, 2026, he posted a four-tier "napkin math" funnel (6B / 1 to 2B / 20M / ~5,000) revisiting an April post on the widening capability-perception gap. He describes the top tier as thousands of agents collaborating for weeks (finding zero-days, advancing math research) and argues human review is already lagging. Commentators note the top-tier claims rely on his insider observation and are not externally verifiable.

The "evaluate the evaluators" emphasis aligns with 2026 research showing LLM judges can have high test-retest reliability yet poor validity, with sizeable position bias and verdict flips across reruns. So alignment against human labels is necessary, not optional, and Arize's practice of gating evaluator releases on agreement is the right default. The always-on, sandboxed, triggered pattern matches what other agent platforms converged on this year (durable execution, single-egress sandboxes, persisted skills).

## Real-World Application / Actionable Step
- Build a **small always-on research agent** for compression experiments: triggered when a benchmark run finishes, it reads logs and eval outputs, flags regressions vs the baseline, and opens an issue with evidence. Persist findings across runs.
- Expose **model tier as a config knob** in every agent pipeline you own, and log eval scores per tier. That data doubles as routing training data.
- Maintain a **golden set (100 to 200 labels)** for every judge used in quantization/routing comparisons, and report judge-human agreement in internal writeups.
- Trace your coding agents (Claude Code, Cursor) on research repos to see where agent time and tokens go. Often the cheapest optimization is in the harness, not the model.
