# SusVibes: vibe-coded agent output passes tests but is insecure

**Date:** 2026-06-12
**Source:** Twitter (@bayesiansapien curated repost, via @HowToAI_) — Carnegie Mellon
**Links:** [Repost](https://nitter.net/HowToAI_/status/2064952595056332808#m)

> Note: surfaced via a curated social repost; the underlying paper link was not captured in the farm. Claims below are from the repost text and should be confirmed against the primary source when available.

## TL;DR

Carnegie Mellon built **SusVibes, a benchmark of 200 real-world repository-level software-engineering tasks** pulled from open-source projects, and handed them to top coding agents including SWE-Agent powered by Claude 4 Sonnet. The agents did what was asked: code that worked, passing functional tests **61% of the time**. The alarming part is what passing hides — **over 80% of those functionally-correct solutions contained security vulnerabilities.** Functional correctness and security are nearly decoupled, and the strongest models are the ones most able to ship working-but-insecure code.

## Why it matters

The "vibe coding" workflow — describe intent, accept whatever passes the tests — optimizes for the exact signal (tests green) that SusVibes shows is blind to security. The better the agent at making tests pass, the more confidently it ships the vulnerability. This is a measurement problem first: functional-test pass rate, the field's default agent-coding metric (SWE-bench and descendants), does not measure the thing that breaks in production.

## Relation to prior wiki state

- **Confirms and sharpens [SABER (06-06)](2026-06-06-saber-operational-safety-coding-agents.md)**, which argued operational safety of coding agents is undertested relative to capability. SusVibes puts a number on it: 80%+ of passing solutions insecure. Two papers in a week saying the same thing — coding-agent evaluation measures capability, not safety — is a pattern, not a coincidence.
- **Feeds the wiki's "benchmark accuracy does not predict deployment robustness" thread** (AgentLens lucky-pass, 05-14; SpecBench reward hacking, 05-21). SusVibes is the security-specific instance: the headline metric (functional pass) and the deployment-critical metric (no vulnerabilities) diverge by 80 points.
- **Direct tension with this week's industry move.** Cursor shipped Auto-review (06-11), a classifier that grades agent *action* risk in context — the production-side bet that you govern autonomy with a reviewer. SusVibes is the research-side evidence that you have to: the agent's own "tests pass" judgment is not a safety signal.

## Gaps

- Surfaced via social repost; the 61% / 80% figures and the exact threat model (which vulnerability classes, how detected) need the primary paper.
- "Most advanced models build the trap" is a provocative framing; whether weaker models are *safer* or just less functional is the controlled comparison to check.

## Links

- Raw: `raw/twitter/2026-06-12-afternoon.md` (@bayesiansapien repost of @HowToAI_)
- Related: [SABER 06-06](2026-06-06-saber-operational-safety-coding-agents.md) · [SpecBench 05-21](../agentic-systems/2026-05-21-specbench-reward-hacking-coding-agents.md) · [AgentLens 05-14](../agentic-systems/2026-05-14-agentlens-lucky-pass-swe-eval.md)
</content>
