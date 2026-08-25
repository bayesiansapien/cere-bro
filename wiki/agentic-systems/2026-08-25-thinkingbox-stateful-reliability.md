# Thinkingbox: One Success Isn't Reliability

**Source:** HuggingFace Daily Papers (5 upvotes) · [arXiv 2608.22171](https://huggingface.co/papers) · [code](https://github.com/microsoft/thinkingbox) · raw: [`raw/huggingface/2026-08-25-one-success-isn-t-reliability-thinkingbox-a-sandbox-and-benc.md`](../../raw/huggingface/2026-08-25-one-success-isn-t-reliability-thinkingbox-a-sandbox-and-benc.md)

**Authors:** Zhuochun Li, Youngmin Ko, Ali Keramati, Nicola Ferri, Susana Palmaz Lopez Pelaez, Liang-Chun Tsai, Calvin Wang, Mirco Milletari, Tuhin Kundu, Vadim Smolyakov, Kjartan Olafsson, Tommy Guy (Microsoft)

## TL;DR

Thinkingbox is a sandbox plus benchmark for agents doing **stateful business workflows**: retail, hospitality, auto insurance, neobank internal IT, consulting IT/HR support. 507 policy-conditioned workflows, isolated MCP-compatible tool sessions, complete execution traces, and evaluation against the **terminal state of the backend** rather than against the agent's response.

The number that matters is a gap, not a score. The strongest model reaches **65.36% pass@1** and **25.25% pass^20**. Read those together: pass@1 is "succeeded once," pass^20 is "succeeded on all twenty independent attempts." A system that works two times in three on a single try works one time in four when you need it to work every time.

The second finding is worse than the first. **Many failed trials terminate cleanly with valid state-changing actions.** The agent does not crash, does not emit a malformed tool call, does not say it is stuck. It confidently does the wrong thing. Response-level and tool-call-level signals are therefore not proxies for task completion, which invalidates a large fraction of how agents are currently monitored in production.

## What the benchmark actually demands

Four requirements that ordinary tool-use benchmarks do not test:

1. **Gather missing information across multiple turns.** The task is underspecified on purpose; the agent must ask.
2. **Follow domain policies.** Business rules that are not derivable from the tool schemas.
3. **Coordinate dependent tools**, where the output of one gates the legality of the next.
4. **Realize the correct persistent state transition with no collateral effects.** Executable checks accept valid trajectories and reject wrong, missing, **or extra** effects.

That last clause is the one that makes the benchmark hard and useful. Rejecting *extra* effects means an agent that accomplishes the goal plus one unrequested side effect fails, which is the correct standard for anything touching a real backend and almost never how agents are scored.

## Relation to prior wiki state

**It is a direct check on the same day's harness enthusiasm.** [Prime Agent](2026-08-25-prime-agent-self-improving-rlm-harness.md), published to HuggingFace the same day, reports ARC-AGI-3 RHAE going from 30% to **95.5% Best@1**. Best@1 is the best of several attempts. Thinkingbox's entire thesis is that this metric family systematically overstates deployability: their own gap from pass@1 to pass^20 is 40 points. Both papers can be right, and the honest joint reading is that harness engineering has demonstrably raised the ceiling of what an agent *can* do while leaving open how often it does it. Nobody has published a pass^k curve for a harness-optimized agent, and that is now the obvious missing experiment.

**It converges with two Kurate finds this week.** [On the Fragility of Self-Improving Agents](2026-08-25-self-improving-agent-fragility.md) (Kurate cs.AI #14, Salesforce) re-evaluates memory-based self-improving agents under seed variance, task reordering, and underspecification, and finds that single-run results on a default task order hide the failure modes. "Can Agent Memory Systems Track Evolving State?" (Kurate cs.AI #13, UIUC, [arXiv 2608.19652](https://arxiv.org/abs/2608.19652)) argues that memory research optimizes recall while long-horizon agency actually requires tracking **changing** state, which is precisely what Thinkingbox measures. Three papers, three groups, one week, same complaint: **agent evaluation reports capability and ignores variance.**

**It extends the reliability thread already in the wiki.** [SWE-Bench ProMax (08-11)](2026-08-11-swe-bench-promax.md) and the [agent benchmark cluster (08-12)](2026-08-12-agent-benchmark-cluster.md) tracked benchmark saturation and measurement validity. Thinkingbox moves the critique from "the benchmark is too easy" to "the statistic is the wrong one," which is a sharper and more durable objection. It also echoes the variance result the wiki recorded on 08-16, where Prime Intellect found roughly a 50-step spread within a single autonomous-research setting after 24 hours, making most single-run claims noise.

## Key takeaways

- **65.36% pass@1 versus 25.25% pass^20** for the strongest model tested, across proprietary and open-weight.
- Failures are **silent**: clean termination, valid state-changing actions, wrong outcome. Tool-call validity is not a completion signal.
- Evaluation is against **backend terminal state**, with executable per-task checks that reject extra effects as well as missing ones.
- 507 workflows over five business domains, MCP-compatible, released open source.

## Gaps

pass^20 over 507 tasks is a large compute bill, and no per-domain breakdown of the reliability gap is given in the abstract, so it is unclear whether the gap is uniform or concentrated in a few workflow types. The latter would be far more actionable. There is also no analysis of whether the 20 failures are correlated: an agent that fails the same way every time is a fixable bug, while an agent that fails differently each time is a sampling problem, and these demand opposite responses.

Synthetic business environments are a proxy for real ones, and policy-conditioned workflows written by a benchmark team may under-represent the ambiguity of actual enterprise policy.

## Industrial implication

This is the number to quote in any deployment conversation. An enterprise buyer does not care about pass@1 on a workflow that moves money or changes a customer record; they care about the rate at which it silently does something adjacent to correct. The gap between the two metrics, 40 points, is roughly the gap between a demo and a product, and it explains why agent pilots convert to production so slowly despite strong benchmark numbers.

Expect pass^k to become a required reporting statistic for agent work within two quarters, in the way that error bars became required for RL. The first vendor to publish a pass^20 number for a shipped agent product will be doing so from strength.

## Related

- [Agent benchmarks](agent-benchmarks.md) — concept page
- [Prime Agent](2026-08-25-prime-agent-self-improving-rlm-harness.md) — the capability claim this checks
- [On the fragility of self-improving agents](2026-08-25-self-improving-agent-fragility.md)
- [Agent benchmark cluster](2026-08-12-agent-benchmark-cluster.md) · [SWE-Bench ProMax](2026-08-11-swe-bench-promax.md)
- [Measuring Autonomous AI Research](2026-08-16-measuring-autonomous-ai-research.md)
