# We Trust AI Agents That Break Every Day (Shy Ruparel, Temporal)

**Channel:** AI Engineer
**Published:** 2026-10-29
**Source:** https://www.youtube.com/watch?v=mJ7q8CuVmbw

## TL;DR
Temporal's 2026 State of Development survey (554 US/UK engineers and leaders, mostly 6+ years of experience) shows a paradox: 85.5% trust agent output at least somewhat, yet 41.1% hit agent failures daily and 16.4% hourly. The top productivity blockers are state tracking (35.7%) and debugging (30.9%), not model quality. The pitch: failures are inevitable, so make them free. Durable execution records every LLM call, tool call and human signal as an event, so a crashed worker resumes from the last completed step without re-spending tokens or writing recovery code. The demo, a 9-stage payout workflow with a local Qwen 9B fraud-check agent and two deliberate worker kills, shows exactly that. A sound architectural message wrapped in a vendor survey.

## Key Takeaways
- **Gap 1, usage vs production:** daily agent use jumped from 47.3% (2025) to 80.8%, but only 49.1% run agents in production or call them core to shipping.
- **Gap 2, trust vs reality:** 85.5% trust vs 41.1% daily failures. Self-described "successful" teams are 1.7x more likely to hit issues continuously, and agent count does not correlate with failure rate (likely they just look harder). 40% say security blocks autonomous agents.
- **Gap 3, prototype vs enterprise:** 51.3% get a prototype to production in hours or less. At 5,000+ employee companies about 1 in 5 take months, versus 1 in 20 elsewhere. Regulated firms spend that time on approvals, audit trails, never-lose-a-payment guarantees.
- **Gap 4, seeing vs recovering:** only 13% are very confident they can observe and debug AI workflows at scale. 22.2% lose progress to crashes and redo work. #1 place people go for help when agents break: YouTube.
- **Cost pressure:** about 8 in 10 say cost limits agent use, so replaying an agent loop after a crash is real money burned.
- **Design pattern:** the deterministic workflow owns money and state. The LLM gives bounded advice inside an activity. If the model fails, the payout continues without the brief. A model outage degrades nothing critical.
- **Mechanics:** workflow state is plain variables rebuilt by replay; retries are a declared policy, not a loop; human approval is a signal persisted even with zero workers alive; timers can wait a year with identical code; bad model output is treated as an activity failure and retried.
- **Claimed adopters:** OpenAI Codex and Replit agents.

## Architecture & Optimization Mechanics
- **Event-sourced memoization of LLM calls.** Each activity's result is persisted in the event history. On replay, completed activities return recorded results, so tokens are spent exactly once per successful step. This is effectively a durable, exactly-once cache keyed by workflow position, which is more robust than prompt-level caching for long agent loops.
- **Determinism boundary.** Workflow code must be deterministic; all nondeterminism (LLM sampling, tool calls, bank APIs, clocks) lives in activities. For agents, that forces a clean split between control flow and model calls, which also makes the LLM swappable (local small model, frontier model, router) without touching orchestration.
- **Observability equals recovery.** The trace you debug is the same history the worker replays, so the two cannot drift. That is the genuinely differentiating claim versus LLM tracing tools.
- **Costs not mentioned:** event history size limits for long agent loops with large payloads (you end up storing blobs externally), replay overhead, workflow versioning pain when you change prompts or code mid-flight, and at-least-once activity semantics. An activity killed mid-flight is retried, so non-idempotent tool calls still need idempotency keys.

## Grounded Context (Web Enrichment)
Secondary coverage confirms the survey: a Qualtrics survey of 554 US and UK engineers, daily agent use rising from 47.3% to 80.8%, 41.1% hitting problems at least daily, and 79.8% saying compute costs meaningfully limit progress (the speaker's "8 in 10"). Commentators echo the framing that state tracking, not hallucination, is the bigger obstacle. Note the sample is drawn from a vendor whose product is state management, so the ranking of blockers is not neutral.

The Codex claim is credible but not officially documented by OpenAI. It comes from a February 2026 a16z podcast guest and aggregator summaries; an OpenAI engineer spoke at Temporal's Replay 2026 about OpenAI's internal Temporal platform used across many teams, without naming Codex. Durable execution for agents has also gone mainstream beyond Temporal: Pydantic AI ships a first-class Temporal integration, and competitors (Restate, DBOS, Inngest, LangGraph checkpointers) offer similar replay semantics, so the pattern matters more than the vendor.

## Real-World Application / Actionable Step
- **Wrap long eval and distillation runs in durable execution.** Multi-hour jobs that call frontier models for teacher labels or LLM-judge scores are the expensive version of this demo. Persist each call's result keyed by (prompt hash, model, params) so a crash, preemption or spot-instance loss never re-buys tokens. Temporal, or a lightweight SQLite memo layer, both work.
- **For routing systems:** put the router decision and each model call in separate activities. You get an exact audit log of which model handled what, replayable for offline router evaluation, which is valuable training data for a learned router.
- **Design rule worth adopting:** deterministic code owns state and side effects; the LLM only advises inside a bounded, retryable step with a fallback path. Make every tool call idempotent before trusting any retry policy.
