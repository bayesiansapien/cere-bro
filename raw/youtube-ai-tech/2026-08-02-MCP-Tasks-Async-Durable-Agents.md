# MCP Tasks (async): Why Aren't Any Agents Supporting Them?

**Channel:** AI Engineer
**Published:** 2026-08-02
**Source:** https://www.youtube.com/watch?v=s4r6nk5WsZw

## TL;DR
Cornelia Davis (Temporal) answers her own title question bluntly: nobody implemented MCP Tasks on the client side because the November 2025 experimental spec was genuinely bad. It was stateful, it exposed an unfilterable `tasks/list` endpoint that collapses at scale, and it tunneled human-in-the-loop input through a long-lived connection that the reference implementation processed FIFO, so with several tasks in flight you could only answer the oldest one. The redesign strips the protocol to a stateless core with Tasks as a formal extension, replaces the elicitation tunnel with a simple client-to-server update endpoint, and pushes durability responsibility onto clients that must persist task IDs. She demos a working client implementation built as a durable workflow, including surviving a server that was not running when the work was submitted.

## Key Takeaways
- **Durability is a spec requirement, not an implementation detail.** Once a task is launched it must survive client crashes, server crashes, dropped connections, and humans who go on vacation mid-approval. The demo accidentally proved this: she submitted a purchase order before starting either process, and it was still captured and completed.
- **`tasks/list` is the design flaw that killed adoption.** With a million tasks in flight and no filter parameter, recovering the one task you care about means scanning all of them. It has been removed.
- **The FIFO elicitation bug is the practical killer.** In V1, multiple concurrent tasks in `input_required` could only be answered in submission order on the client side. Davis had to write custom protocol handling to work around it. This alone makes V1 unusable for any real multi-agent deployment.
- **The task lifecycle survived the redesign unchanged.** `working` to `input_required` back to `working`, then `completed`, `cancelled`, or `failed`. Davis calls this "actually sound," and the real server-side work is mapping this generic lifecycle onto your domain state machine.
- **Statelessness shifts the durability burden to the client.** Clients "should" persist task IDs, but the spec itself notes that without persistence the task is unrecoverable. Davis flags that this should have been a MUST, and she is right.
- **Polling still does not scale.** A million tasks means a million clients polling `tasks/get`. The unfinished piece is the notifications protocol: one endpoint answering "did anything change, and which one," so clients pull only on a real event.
- **Signaling into a running process is the whole game.** Temporal's signal primitive maps directly onto the new `tasks/update` endpoint, which is why the durable-workflow framing works so cleanly here.

## Architecture & Optimization Mechanics
The V1-to-V2 change is a textbook case of the same lesson distributed systems learned in the microservices era: stateful protocols do not survive contact with scale. The specific mechanism matters for anyone building agent infrastructure. In V1, `tasks/result` held a connection open while the server elicited input back through it, which means the server holds per-task connection state, the client holds per-task connection state, and every network blip forces a resumption problem with no clean resume point. In V2, every interaction is an independent request-response against a stable task handle, so the only state that must survive is the task ID itself, and that is the client's problem to persist.

For inference-serving work the analogy is direct and useful. A long-running async tool call is structurally identical to a queued batch inference job, and the same tradeoffs apply. Polling burns request overhead proportional to fleet size times poll frequency, exactly the way naive scheduler polling burns GPU-adjacent CPU cycles. The notifications-based design Davis describes as "showing promise" is the same fix as an event-driven completion callback replacing a busy-wait loop: one cheap change-detection endpoint, then a targeted fetch. If you are building any agent system that fans out long-running work, design for the notification path now rather than shipping polling and retrofitting later.

The lifecycle-to-domain-state-machine mapping is the underrated piece of engineering advice in the talk. The protocol gives you five generic states. Your actual invoice processor, or in Amit's case your quantization sweep or eval run, has its own richer state machine with retries and approval gates. The implementation work is the projection function between them, and getting that projection wrong is what makes tasks feel harder than they are.

## Grounded Context (Web Enrichment)
Davis hedges throughout with "there's a new one coming out in July." It already shipped. The 2026-07-28 MCP specification landed five days before this talk was published, so everything she frames as forthcoming is now live. That release is the largest change since MCP launched: a fully stateless protocol core, a formal extensions framework, Multi Round-Trip Requests, header-based routing, cacheable list results, hardened authorization, and a 12-month deprecation policy. Both Tasks and MCP Apps graduated from experimental core features to official extensions in the same release. It shipped under the Agentic AI Foundation, a directed fund under the Linux Foundation, which is where MCP now lives.

Her account of why `tasks/list` died is slightly incomplete. She frames it as a scale problem, which is true, but the deeper reason published with the spec is scoping: once protocol sessions are gone, "list tasks across clients" has no well-defined caller scope at all. The endpoint was not merely slow, it was semantically undefined in a stateless world. That reframing strengthens rather than weakens her argument, and it explains why the fix was deletion rather than adding a filter parameter.

One small correction: she names the body stewarding MCP as the "Agoric AI Foundation." It is the Agentic AI Foundation (AAIF). Angie Jones's May 2026 developer-experience post that she credits for the stateless direction is real and is the canonical pre-announcement of this redesign. The final V2 lifecycle is `tools/call` returning a task handle, then `tasks/get`, `tasks/update`, and `tasks/cancel`, which matches her slide exactly.

## Real-World Application / Actionable Step
Any long-running job Amit's team exposes to an agent (a quantization sweep, a full eval harness run, a distillation job) is an MCP Task whether or not it is labeled one, and the odds are it is currently implemented as a fire-and-forget with a status-check tool the model has to remember to call. Migrate one of those to the 2026-07-28 Tasks extension and take three things for free: a defined lifecycle the model can reason about, durability across server restarts, and a real approval gate via `input_required` for anything that costs serious GPU hours.

The concrete first step is smaller than a migration. Audit whether your job IDs are persisted client-side. Under the stateless spec, a client that loses the task ID has permanently orphaned a running job, and Davis is correct that the spec's "should" understates this. If your agent holds job IDs only in conversation context, a compaction or restart silently strands work that is still consuming GPUs. Write them to durable storage before touching anything else.

Then design the completion path around notifications rather than polling from day one. A fleet of agents polling a sweep-status endpoint every few seconds is pure overhead that grows linearly with fleet size, and it is exactly the pattern the spec authors are now working to eliminate.

Sources:
- [The 2026-07-28 Specification, Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [MCP 2026-07-28: From Local Tool to Distributed Protocol, AAIF](https://aaif.io/blog/mcp-2026-07-28-whats-changing-and-how-to-migrate)
- [MCP Is Growing Up, Agentic AI Foundation](https://aaif.io/blog/mcp-is-growing-up)
- [MCP just got its biggest update ever, VentureBeat](https://venturebeat.com/infrastructure/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents)
- [Model Context Protocol prepares to break with its stateful past, The Register](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)
- [MCP 2026-07-28 spec: what changed, what breaks, Stacktree](https://stacktr.ee/blog/mcp-2026-spec-changes)
