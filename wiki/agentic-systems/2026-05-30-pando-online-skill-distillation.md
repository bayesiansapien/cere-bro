# PANDO: Single-Rollout Online Skill Distillation for Web Agents

**Source:** HuggingFace Daily Papers (2026-05-30) · arxiv 2605.24785
**Raw:** [raw/huggingface/2026-05-30-pando-efficient-multimodal-ai-agents-via-online-skill-distil.md](../../raw/huggingface/2026-05-30-pando-efficient-multimodal-ai-agents-via-online-skill-distil.md)

## TL;DR

Most efficiency work on web agents pushes more inference-time compute (rollouts, verifiers, offline skill discovery, specialist stacks). PANDO inverts the question: can an agent become *more efficient as it accumulates experience*, not more expensive? It maintains a structured Skill Library, demotes low-confidence skills, routes via a hierarchical policy, compresses visual observations, and uses cache-aware prompting. All distillation happens online during a single rollout pass with no pre-evaluation discovery budget. On the full 910 VisualWebArena tasks, PANDO hits **58.3% success** against SGV's 54.0% and WALT's 45.2%, while using **58% fewer tokens than SGV and 61% fewer than WALT**. The paper also introduces three trajectory-level efficiency metrics (Action Repetition Rate, Step Overhead Ratio, Prompt Cache Utilization) that make agent inefficiency visible beyond terminal success.

## Architecture

```
                ┌──── Skill Library ────┐
                │  rules · routines     │   ← updated online during rollout
                │  with confidence c_s  │     (no pre-eval discovery budget)
                └───────────┬───────────┘
                            │
   ┌── progress reflection ─┤  demote skills with low c_s
   │                        │  promote skills that close subgoals
   │                        ▼
   │       ┌──── hierarchical router ────┐
   │       │ subgoal → skill class → step │
   │       └──────────────┬───────────────┘
   │                      │
   │                      ▼
   │       ┌── visual compression of obs ──┐
   │       │  + cache-aware prompt layout  │  ← maximize prompt-cache reuse
   │       └──────────────┬────────────────┘
   │                      │
   └──────► single-rollout execution ◄── observation
```

## Key claims

- VisualWebArena full set (910 tasks): **58.3%** vs SGV 54.0% vs WALT (reproduction) 45.2%.
- Token reduction: **58% fewer than SGV, 61% fewer than WALT**.
- No pre-evaluation discovery budget. All skill acquisition happens during the evaluated rollouts.
- 300-task ablation: rules and routines deliver most of the success gain; routing, compression, and cache-aware prompting convert the larger library into lower marginal token cost.
- Three new efficiency metrics: Action Repetition Rate (loops), Step Overhead Ratio (waste vs. minimum), Prompt Cache Utilization (cache reuse).

## Why this matters

The wiki has covered three recent threads PANDO connects:

1. **Routing as policy** — Conductor (Sakana, 05-11), CaRE (05-11), MISA (05-11), Cloud-Device hybrid (05-29). PANDO's hierarchical router is the agent-side instance: instead of routing across models or across heads, it routes across *skills* in the library.
2. **Cache economics** — the wiki tracked Cursor's 2026-05-29 cost report that input tokens now dominate cost as agents accumulate context. PANDO directly attacks this by making prompt-cache reuse an explicit metric.
3. **Self-managing agent memory** — WorldMemArena (today, 05-30) characterizes how harness-based agent memory is more flexible but costlier than RAG. PANDO is one concrete instantiation of harness memory, but with the cost penalty mitigated via cache-aware layout and skill demotion.

## Gaps and limits

- VisualWebArena-only evaluation. Generalization to TerminalBench (LiteCoder-Terminal sets that bar), SWE-Bench, or coding agents not shown.
- "Online skill distillation" hides the question of *forgetting* — when the library accumulates over thousands of tasks, demotion alone may not be sufficient.
- The skill structure is hand-designed (rules + routines + library). Whether the structure itself can be learned is open.

## Research angle

PANDO sharpens a question the routing cluster has been circling. Conductor (Sakana) and CaRE route across model pools. MISA routes across attention heads. PANDO routes across an *online-distilled skill library*. The three are the same architectural move at three different granularities. The next paper that will matter here is one that unifies them: a single router that learns to allocate, per task and per step, across (model, head, skill), with a shared confidence signal driving all three axes. Conf-KV (today's KV cache paper) hints at one possible signal source — the model's own next-token confidence.

## Related concept pages

- [Agentic systems](agentic-systems.md)
