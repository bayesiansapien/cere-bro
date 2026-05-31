# RePoT: Recoverable Program-of-Thought via Checkpoint Repair

**arXiv:** [2605.30052](https://arxiv.org/abs/2605.30052) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.30052) · **Date:** 2026-05-31
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-repot-recoverable-program-of-thought-via-checkpoint-repair.md)

## TL;DR

Program-of-Thought (PoT) has an LLM emit a Python program that prints a plan of primitive actions; the problem is that a single invalid action silently invalidates the whole trajectory, with no graceful recovery. RePoT (Recoverable PoT) adds deterministic verified replay: it walks the emitted plan through the environment until the first invalid transition, then makes exactly one more LLM call to resume from the verified prefix. The extra cost is at most one LLM call, and only on the ~14% of problems where PoT fails in the first place. The gains are consistent: +3 to +11 pp over PoT across four closed-model configurations on PuzzleZoo-775, peaking at 96.9% vs 86.3% on gpt-5.4-mini-medium. Against a matched-budget PoT-retry baseline the picture is capability-dependent, RePoT wins decisively on Gemini, ties on GPT-medium and Claude, and loses on GPT-mini, which motivates Adaptive RePoT, a rule-based dispatcher that routes between suffix repair and a fresh retry based on the length of the verified prefix. The controlled Derail-550 benchmark isolates the load-bearing factor: any condition with access to checkpoint information clears far higher than error-only feedback (≥30% on GPT-medium, ≥70% on Gemini, vs ≤3.1%), so it is the checkpoint *state*, not the specific verified-prefix tail, that drives recovery.

## The mechanism

```
PoT (brittle):
  LLM ─► Python plan ─► run ─► first invalid action ─► whole trajectory dead ✗

RePoT (checkpoint repair):
  LLM ─► Python plan
          │
          ▼  deterministic verified replay
  step1 ✓ step2 ✓ ... stepK ✓  │  stepK+1 ✗  ← first invalid transition
                    verified prefix ┘
          │
          ▼  ONE LLM call: resume from verified prefix
  step K+1' ✓ ... ─► success         (cost: ≤1 extra call, only on ~14% PoT failures)

Adaptive RePoT (capability-aware dispatch):
  verified-prefix length long  ─► SUFFIX REPAIR (resume)
  verified-prefix length short ─► FRESH PoT RETRY
```

## What problem it solves

One-shot PoT is efficient when it works but offers no middle ground when it fails: an invalid action partway through a long plan discards every correct step before it, and naive retries throw away the verified prefix and re-pay for the whole trajectory. The field's default recovery signal has been error-only feedback ("that failed, try again"), which Derail-550 shows is nearly useless (≤3.1% recovery). RePoT keeps the correct prefix, localizes the failure point deterministically, and asks the model to fix only the tail.

## Core novelty

The separation of *deterministic verified replay* (a non-LLM environment walk that finds the exact first invalid transition) from *a single LLM repair call* (resume from the verified prefix). Prior recovery either re-runs the whole generation or feeds back only an error string; RePoT feeds back the *verified checkpoint state*, and the controlled benchmark proves that checkpoint state is the causal ingredient, not the specific suffix. Adaptive RePoT then adds capability-aware routing: it dispatches between suffix-repair and fresh-retry based on verified-prefix length, because the right recovery move depends on how strong the underlying model is.

## Key takeaways

- **+3 to +11 pp over PoT** across four closed-model configs on PuzzleZoo-775; peak **96.9% vs 86.3%** on gpt-5.4-mini-medium.
- Cost is **at most one extra LLM call**, incurred only on the ~14% of problems where PoT fails.
- vs matched-budget retry: wins decisively on Gemini (+3.8 pp, 95% CI [+2.2,+5.4]), ties GPT-medium/Claude, **loses on GPT-mini**, a capability-scaling pattern.
- Derail-550: checkpoint-information conditions clear ≥30% (GPT-medium) / ≥70% (Gemini) vs ≤3.1% for error-only feedback, **checkpoint state is the load-bearing signal**.

## Gaps in the study

The capability-dependence is honestly reported but not solved: Adaptive RePoT is "preliminary" and rule-based on prefix length, so the dispatcher itself is hand-tuned rather than learned. Evaluation is on planning/puzzle environments (PuzzleZoo, PlanBench Blocksworld, Derail) where "valid action" is crisply defined; whether deterministic verified replay transfers to open-ended tool-use agents (where transitions are not cleanly verifiable) is the unaddressed question. The "loses on GPT-mini" result means RePoT can actively hurt weak models, so the dispatcher is not optional, it is required for safe deployment.

## Relation to prior wiki state

RePoT is a recovery-and-routing paper wearing a reasoning-paper hat, and it lands squarely in two wiki threads. The agentic-recovery angle complements BeliefTrack (05-30, RL with belief-state rewards cut failure rates 71% by managing when a model should change its mind) and AsyncTool (05-30, agents degrade when tool feedback is delayed): all three are about agents handling imperfect or evolving execution state rather than assuming a clean single pass. The more pointed connection is to routing. Adaptive RePoT's dispatcher, which routes between suffix-repair and fresh-retry based on verified-prefix length and implicitly on model capability, is the same trajectory-level routing move the llm-routing page has been collecting: Step-level Optimization for Computer-Use Agents (05-02) escalated to a frontier model on a Stuck signal; RePoT chooses a *recovery strategy* on a verified-prefix-length signal. The capability-scaling pattern (repair helps strong models, hurts weak ones) is a concrete instance of the wiki's recurring "more compute is not monotonically better" finding, echoed today by When Cloud Agents Meet Device Agents.

## Research angle

The clean lead is replacing the hand-tuned Adaptive RePoT dispatcher with a learned router whose features include verified-prefix length, model identity, and a cheap difficulty estimate, then asking whether it recovers the per-model optimum automatically. Because RePoT *hurts* weak models, this is a routing problem with a real downside risk, which makes it a sharper test of trajectory-routing than the upside-only cascades studied so far. A second angle: the finding that checkpoint *state* (not the suffix text) is load-bearing suggests recovery is fundamentally about giving the model a verified world-state to anchor on, which connects to the world-model-and-belief-management cluster (BeliefTrack, WorldMemArena) and raises the question of whether a persistent verified-state checkpoint could serve general agent recovery, not just PoT plans.

## Links

- [arXiv 2605.30052](https://arxiv.org/abs/2605.30052)
- [LLM routing concept page](../ai-routing/llm-routing.md)
- [Step-level optimization for computer-use agents (05-02)](../ai-routing/2026-05-02-step-level-optimization-computer-use-agents.md)
- [Multi-agent systems concept page](multi-agent-systems.md)
