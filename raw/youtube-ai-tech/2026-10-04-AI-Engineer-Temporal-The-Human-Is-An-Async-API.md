# The Human Is an Async API (Melanie Warrick, Temporal)

**Channel:** AI Engineer
**Published:** 2026-10-04
**Source:** https://www.youtube.com/watch?v=jc3kbZkuHTo

## TL;DR
A vendor talk from Temporal with a live demo: a simulated ice cream delivery fleet run by three agents (fleet and customer agents on Google ADK, which the transcript renders as "80K", and a dispatch agent on LangGraph), all wrapped in Temporal durable execution. The thesis: treat a human as an asynchronous API, not a blocking function call. Pause one workflow with a durable wait condition, deliver the human's answer as a signal, and let everything else keep running. The demo kills the worker mid-approval, sends the approval while it is offline, restarts, and the workflow replays its event history and continues. Correct and useful pattern, but nothing new for anyone who knows workflow engines; the value is the concrete ADK and LangGraph wiring.

## Key Takeaways
- **Failure mode named:** a naive "ask the human" tool call blocks a thread and is lost if the process dies. Humans respond in minutes to weeks, not 200 ms.
- **Two primitives:** `workflow.wait_condition` (durably park one workflow, other coroutines and workflows keep running) and `workflow.signal` (inject external input into a running workflow). Timeouts are built in, so approvals can expire.
- **Temporal mapping:** worker runs code; workflow is the deterministic step sequence (the agent loop lives here); activity is anything non-deterministic (every LLM call and tool call). Workflows deterministic, activities not.
- **ADK wiring:** wrap the model in a `TemporalModel` class, wrap tools with an activity-tool helper, register the Google ADK plugin on the worker.
- **LangGraph wiring:** each node's model and tool calls become activities; LangGraph `interrupt` is bridged to a wait condition, and the signal carries the human's reply.
- **Both directions:** human-initiated (customer changes an order mid-flight, only driver A pauses) and agent-initiated (dispatch flags a high-value order for approval).
- **Recovery is replay, not redo:** on restart the event history is replayed up to the last recorded step, so completed LLM calls are not re-executed or re-billed.
- **Scale claim:** millions of parked workflows, evicted from worker memory while idle.
- **When to involve a human:** when the cost of being wrong is high, balanced against alert fatigue (people rubber-stamp "yes, yes, yes").

## Architecture & Optimization Mechanics
The interesting systems property is that the agent's state is an append-only event log, and recovery means deterministic replay of the orchestration code against recorded activity results. For LLM agents this matters economically: completed model calls are memoized in history, so a crash after 40 tool calls does not re-spend 40 calls of tokens. The flip side is that the orchestration loop must be deterministic, so any sampling, clock reads or randomness must live in activities. Agent frameworks that mutate state inside the loop need adapters, which is exactly what the ADK and LangGraph plugins provide.

For inference work, two consequences. First, parked workflows hold no GPU or KV-cache resources; a human wait of days costs only a history row, unlike long-lived sessions that pin a prefix cache. Resume therefore pays a cold prefill, so long-paused agents should be designed with compact, re-hydratable context rather than relying on cache residency. Second, activity-level retries and timeouts give a natural place to put model fallback: an activity that times out on a large model can retry on a smaller or different provider, which is routing at the durability layer rather than in the agent prompt.

## Grounded Context (Web Enrichment)
The demo is real and public: the `temporal-ai-hitl-adk-langgraph` repo and the "Ziggy's Durable HITL Agents" code-exchange entry match the talk exactly, and Temporal ships documented ADK integrations (the plugin is also listed in Google's ADK docs). Commercially, Temporal is the category leader by a wide margin: it raised a $300M Series D at $5B in February 2026, then a $550M Series E at a $12.55B valuation on September 14, 2026, reports above $250M ARR, 4,300+ paying Cloud customers, and names OpenAI (Codex, image generation) as its largest customer, with OpenAI usage up 60x in a year.

What the talk omits: LangGraph already has its own checkpointer plus `interrupt` for durable human-in-the-loop, so Temporal is additive mainly when you run multiple frameworks or need cross-service retries and history, as in this demo. Lighter alternatives (Restate, DBOS, Inngest) target the same durable-agent niche with less operational weight. The "millions of parked workflows" claim is consistent with Temporal's architecture but was asserted, not shown.

Sources: [Demo repo](https://github.com/temporal-community/temporal-ai-hitl-adk-langgraph), [Ziggy's Durable HITL Agents](https://temporal.io/code-exchange/ziggys-durable-hitl-agents-multi-agent-demo-with-google-adk-langgraph-temporal), [Temporal ADK integration docs](https://docs.temporal.io/develop/go/integrations/google-adk), [ADK Temporal plugin](https://adk.dev/integrations/temporal/), [Temporal multi-agent blog](https://temporal.io/blog/durable-flexible-multi-agent-systems), [Temporal Series D](https://temporal.io/news/temporal-raises-300M-to-make-agentic-ai-real-for-companies), [Series E coverage](https://byteiota.com/temporal-raises-550m-durable-execution-is-now-core-ai-agent-infrastructure/), [$12.55B valuation](https://lapaasvoice.com/temporal-funding-durable-ai-reliability), [Durable agents landscape 2026](https://www.reactify-solutions.com/articles/durable-ai-agents-2026)

## Real-World Application / Actionable Step
- **For long-running eval or distillation pipelines:** wrap each expensive teacher-model call or eval batch as an activity so a crash resumes without re-paying for completed generations. This is the same memoization benefit, applied to research jobs rather than agents.
- **Routing via retries:** prototype a Temporal activity policy where timeout or error on the primary model retries on a cheaper fallback model, and log which path served each request. It gives free production data on when the small model is good enough.
- **Design for cold resume:** for any agent that may pause for humans, budget for a full re-prefill on resume and keep the resumable state compact (summary plus pointers), not the raw transcript.
- **Do not adopt Temporal for a single LangGraph agent;** its built-in checkpointer suffices. Reach for Temporal when orchestration spans frameworks or services.
- **Investment note:** private company, but the $12.55B round and OpenAI dependence confirm durable execution as a real agent-infrastructure layer.
