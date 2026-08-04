# MCP Apps: Extending the Frontier

**Channel:** AI Engineer
**Published:** 2026-08-02
**Source:** https://www.youtube.com/watch?v=-jY2T2PiJBE

## TL;DR
Ido Salomon and Liad Yosef, creators of MCP-UI and co-maintainers of the official MCP Apps spec, argue that the chat text box is a dead end for information density and that the web is fragmenting into brand-owned UI "atoms" that personal assistants compose on demand. MCP Apps is now the first official MCP extension (SEP-1865, co-authored with Anthropic and OpenAI), shipping in Claude, ChatGPT, VS Code, Cursor, and Copilot. The strategic claim: this is a new application distribution channel with a larger addressable market at launch than the Apple App Store had, and the host, not the vendor, now owns the user journey.

## Key Takeaways
- **The real blocker to MCP adoption was branding, not plumbing.** Companies resisted building MCP servers because it reduced them to "a textual database" and erased brand identity. Shipping UI back through the protocol removes that objection, which is why Shopify, ElevenLabs, Postman, and Block moved early.
- **Transport is deliberately boring.** A tool result links to an MCP resource under a `ui://` prefix containing HTML. The host preloads it (not fetched at call time in practice) and renders it in a sandboxed iframe via a React or web component from the MCP-UI SDK.
- **Bidirectional control is the actual spec contribution.** The app never calls the vendor backend directly. It posts an event to the host through a callback, and the host decides whether to invoke a tool. Three escalating levels of control are standardized: notify the chat, request a tool call, or hand a full prompt to the model.
- **View tools invert the direction.** Already in the spec and shipping soon: the host writes into the app, so "fill out this form for me" lets the model drive the rendered widget. This is MCP's answer to Google's Web MCP.
- **Reusable views are the open performance problem.** Heavy apps (Autodesk's 3D renderer was the example given) re-render from scratch every call. The working group is exploring a server-supplied view identifier so the model updates an existing view instead of rebuilding it.
- **MCP Apps is generation-agnostic.** It is the envelope, not the renderer. Predefined UI, declarative UI (JSON Render, A2UI), and fully generative UI all ride inside it. Claude's ask-it-to-generate-a-UI feature is an MCP App under the hood.
- **Write once, run everywhere is real today.** The same codebase renders in LibreChat and ChatGPT, which is the strongest practical argument for building on the spec rather than a host-specific format.

## Architecture & Optimization Mechanics
The interesting cost structure here is that MCP Apps moves presentation out of the token stream. A PostHog funnel described in prose burns hundreds of output tokens and still leaves the user parsing text. The same funnel as a preloaded `ui://` resource costs roughly zero incremental output tokens per render, because the HTML is a cached resource fetched once per session rather than generated per turn. That is a meaningful serving-cost lever: for any high-frequency tool whose output is tabular or visual, a static UI resource plus a small structured payload beats model-generated markdown on latency, cost, and fidelity simultaneously.

The generative UI spectrum maps cleanly onto a cost/flexibility tradeoff worth reasoning about explicitly. Predefined UI is a cache hit with zero generation cost and zero flexibility. Declarative UI (A2UI, JSON Render) generates a small constrained JSON payload, so it is cheap to produce, cheap to validate, and safe to render, at the price of a fixed component catalog. Fully generative HTML is the most expensive per turn and the hardest to sandbox. The unsolved reusable-views problem is the same problem as KV cache invalidation in a different domain: you want to identify the stable prefix of a view and mutate only the delta, and the spec currently forces full recomputation every time.

The three-level control hierarchy also matters for anyone building routing. Level one (notify) needs no model call at all. Level two (suggest a tool call) needs a cheap classifier at most. Level three (run a prompt) needs the frontier model. A host that routes these three levels to the same model is overspending on the majority of interactions.

## Grounded Context (Web Enrichment)
The timeline in the talk is loose and worth correcting. The speakers say MCP-UI was created "in May last year" and elsewhere that "in 2026 we had an amazing year of standardizing MCP UI." The record is that MCP-UI originated in summer 2024, SEP-1865 was proposed on 21 November 2025, and MCP Apps went live as the first official MCP extension on 26 January 2026. So the standardization year was 2025, and 2026 is the deployment year. The talk's own framing of "just a few months ago we partnered with Anthropic and OpenAI" is the accurate version of the claim.

On the competitive picture, the talk undersells how settled interoperability already is. Google published a joint A2UI and MCP Apps guide positioning the two as complementary rather than rival: A2UI is a declarative wire format riding on AG-UI for the declarative band, MCP Apps is the coded-integration band, and the current consensus recommendation is to use MCP Apps when shipping a real product integration into ChatGPT or Claude, and A2UI when the agent should pick a display at runtime from a safe component catalog. The stack has stratified into MCP for tool calls, A2UI for UI description, and AG-UI for streaming updates to the frontend, which is a more coherent division of labor than the "spectrum" framing suggests.

The distribution claim holds up but the arithmetic in the talk is sloppy. ChatGPT's roughly 800 million weekly users is a real figure, and combined host reach across Claude, ChatGPT, VS Code, Cursor, and Copilot does exceed a billion. The "170 times the Apple App Store's TAM at launch" comparison is rhetorically fine but ignores that App Store users had payment rails and an install model, neither of which MCP Apps has solved. Block's agentic commerce launch, mentioned in the talk as same-day news, is the first serious attempt at closing that gap.

## Real-World Application / Actionable Step
Treat MCP Apps as an inference-cost optimization, not a UI feature. For any internal tool Amit's team exposes to agents (eval dashboards, routing-decision traces, quantization sweep results), the current pattern is almost certainly "model reads a JSON blob and writes markdown about it," which pays full generation cost on every single call to re-describe a fixed layout. Replace the highest-frequency one with a `ui://` resource: the HTML is preloaded once, the tool returns only the changed numbers, and the per-call output token cost drops to the payload size.

Concretely, take the routing-decision trace viewer. Today explaining which model a query was routed to and why costs a paragraph of generated text per query. As an MCP App it costs a few hundred bytes of structured data against a cached view, and it becomes clickable, so drilling into "why did this query go to the big model" is a level-two control event rather than another full generation. Instrument both versions and measure output tokens per interaction. The delta is the number that justifies the work.

Second, adopt the three-level control hierarchy as a routing taxonomy independent of MCP. Most agent interactions in a production system are level one or two and are being served by a frontier model because nobody classified them. That is the cheapest routing win available and it does not require adopting the protocol at all.

Sources:
- [MCP Apps spec, modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx)
- [MCP Apps: Bringing UI Capabilities To MCP Clients](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
- [A2UI + MCP Apps: Combining declarative and custom agentic UIs](https://developers.googleblog.com/a2ui-and-mcp-apps/)
- [Agent UI Standards Multiply: MCP Apps and Google's A2UI](https://thenewstack.io/agent-ui-standards-multiply-mcp-apps-and-googles-a2ui/)
- [MCP Apps vs A2UI: Which Agent UI Standard Should You Use?](https://sunpeak.ai/blogs/mcp-apps-vs-a2ui/)
