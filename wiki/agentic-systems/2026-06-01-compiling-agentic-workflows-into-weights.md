# Compiling Agentic Workflows into Weights

**TL;DR.** A full agentic workflow can be distilled into the WEIGHTS of a small model and run at roughly two orders of magnitude (about 100x) lower inference cost while keeping near-frontier task quality. Instead of keeping an external orchestrator looping above the LLM on every request, the whole procedure is compiled into a fine-tuned model, producing what the work calls a "subterranean agent". The compiled procedure is not just the final outputs. It includes the multi-step LLM calls, tool invocations, intermediate scratchpads, and decision points, so the student model internalizes the orchestration LOGIC itself. Classic agent frameworks run a planner loop above the model on every request, and that loop is where most of the cost and latency live. Compiling the loop into weights removes the per-call orchestration overhead, because many model calls collapse into one forward pass.

```
classic:   orchestrator loop → LLM call → tool → LLM call → ...   (per request)

compiled:  single fine-tuned model forward pass   (loop internalized)
```

## Key points

- A multi-step agent workflow is compiled into the weights of one small fine-tuned model, the "subterranean agent".
- Reported cost reduction is about 100x at inference, while keeping near-frontier quality on the evaluated tasks.
- The student internalizes orchestration logic, not just final answers: planner steps, tool calls, scratchpads, and decision points.
- Savings come from collapsing many model calls plus orchestration overhead into a single forward pass.
- Best fit is high-volume narrow workflows where the loop is stable and repeated constantly.

## Gaps in the study

- "Near-frontier quality" is shown on the evaluated narrow tasks. It is unclear how broad that set is.
- Brittleness when the workflow itself must change is not characterized: a compiled loop cannot be edited as easily as an external orchestrator.
- Generalization beyond high-volume narrow workflows and degradation on out-of-distribution requests are open.

## How it relates to prior wiki pages

This sits directly inside a debate surfaced today on Twitter about where the agent ceiling actually lives.

- The **binding constraint thesis** (IntuitMachine repost) argues that an agent's ceiling is MIN(model capability, harness quality), and that right now the harness, not the model, is the binding constraint. The implication is to keep the orchestrator external and improve it.
- **Life-Harness** (same DAIR.AI newsletter) argues you can improve a frozen agent by patching the runtime harness and interface rather than the weights.

Compiling-into-weights is the OPPOSITE move: it dissolves the harness INTO the weights. One camp says keep the orchestrator external and make it better, the other says bake it into the model to kill per-call cost. The tension is real and unresolved. The likely resolution is by workload: high-volume narrow workflows (support bots, fixed pipelines) compile cleanly and get the ~100x win, while frontier open-ended agents still need the external loop because the procedure keeps changing. Mechanistically this is knowledge distillation applied to a whole control loop, not just to outputs.

## Links

- Source: [DAIR.AI "Top AI Papers of the Week"](https://www.linkedin.com/pulse/top-ai-papers-week-dair-ai-nhbpe) (via Gmail starred, 2026-05-31)
- Related concept pages: [multi-agent-systems.md](multi-agent-systems.md), [tool-calling.md](tool-calling.md), [knowledge-distillation.md](../inference-efficiency/knowledge-distillation.md)
- Raw source: [raw/gmail/2026-06-01-starred.md](../../raw/gmail/2026-06-01-starred.md)
