---
title: "AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios"
date: 2026-05-29
arxiv: https://arxiv.org/abs/2605.27995
source: huggingface
tier: 2
topic: agentic-systems
---

# AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios

> Every agent tool-use benchmark assumes the tool returns instantly. Real tools don't. AsyncTool injects realistic latency and runs multiple tasks simultaneously to test whether agents can use idle time. Most current models can't, and current eval is measuring a fictional regime.

```
Standard tool-eval benchmarks:                  AsyncTool (this paper):

  Agent ► call(A) ─[0ms]─► result(A)            Agent ─► call(A)  [latency 5s]
        ► call(B) ─[0ms]─► result(B)                  ─► call(B)  [latency 2s]
        ► call(C) ─[0ms]─► result(C)                  
                                                  while waiting for A:
  Single task, no real wall-clock                   start task 2's call(D) ?
  No idle-time decisions                            poll B since it should be done ?
                                                    track which results have come back ?

Failure modes AsyncTool measures:
  ── poor task switching while one tool is in-flight
  ── dropping dependency tracking across concurrent tasks
  ── losing state when an awaited result returns mid-other-task
  ── blind-waiting (idle-time wasted on a single in-flight call)

Step-level / sub-task-level / task-level metrics
  ─► measures coordination, not just final accuracy
```

## TL;DR

Existing tool-use benchmarks measure agent capability under the unrealistic assumption that tool responses return instantly and that the agent handles one task at a time. AsyncTool changes both: multiple heterogeneous tasks are presented simultaneously, tool calls have realistic response latency, and the agent's job is to use idle wait-time on one tool to push the other tasks forward. The authors construct a diverse async multitasking dataset via a hybrid data evolution strategy and score models at the step, sub-task, and task levels, with efficiency-oriented metrics. Result: delayed tool feedback causes clear performance degradation in current LLM-based agents. The models that do better are the ones that coordinate task switching, track dependencies across tasks, and maintain state across interleaved interactions. The paper names the key failure modes (blind waiting, dependency loss, mid-task state collapse) and frames them as the *temporal reasoning* gap in current agents.

## Why this matters

This is the *temporal* axis of the agent-evaluation rigor wave that has been the dominant theme of May. **LiveBrowseComp** (2026-05-28, the paper that showed agents on BrowseComp answer 44.5 percent of questions with no tools, confirming rather than discovering) and **HRBench** (2026-05-28, the hybrid-reasoning mode-switching benchmark with no dominant strategy across scales) both attacked static benchmarks for measuring memory not capability. AsyncTool adds: even when you measure capability, you have been measuring it in a zero-latency world. Production agents wait. Until now we did not know what they do while waiting; AsyncTool shows the answer is "mostly nothing useful."

The blind-waiting failure mode is particularly important for cost. Production agent stacks budget wall-clock time, not just token count; an agent that waits 5 seconds on a tool that another agent could have used to do other work is paying real money for nothing. The paper's efficiency-oriented metrics (task coordination, completion efficiency) are the eval that matters for production agent unit economics.

## Connections

- **LiveBrowseComp / HRBench / Chartographer / Narrow Exploration** (2026-05-26 through 2026-05-28): the eval-rigor cluster. Static benchmarks measure memory. AsyncTool adds the wall-clock axis.
- **Cloud-Device hybrid agent paper** (2026-05-29, the hybrid-MAS paper out today): identifies that the Pareto frontier of power/cost/performance is task-dependent. AsyncTool gives the missing wall-clock dimension to that frontier.
- **AgingBench** (2026-05-27, surfaced via @bayesiansapien retweet of @omarsar0): a *longitudinal* benchmark for agent reliability. AsyncTool is the *intra-session-wall-clock* sibling.
- **GTA-2 tool-agent benchmark** (2026-04-20): the next-gen of GTA-2 should incorporate AsyncTool's latency model.

## Research angle

The right architectural fix is unclear from the paper. Three candidates:
1. *Promise/await primitives in the agent control loop*: explicit non-blocking returns, with the agent deciding when to check.
2. *Speculative tool calls*: agent issues several speculative requests; only the relevant one is consumed.
3. *Background agent fleet*: borrow the dynamic-workflow pattern from today's Claude Code release (parallel subagents) and apply it to single-agent tool calling.

AsyncTool would be a strong evaluation target for any of the three. Industrial relevance is high: most enterprise tool integrations have multi-second latency.
