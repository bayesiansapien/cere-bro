# Every Company Is Building Agents That Can't Work Together

**Channel:** AI Engineer (Justin Schroeder, Standard Agents / FormKit)
**Published:** 2026-11-10
**Source:** https://www.youtube.com/watch?v=3Krz7Rdd4JI

## TL;DR
Businesses keep building narrow, domain-specific agents instead of handing everything to one frontier model plus MCP and skill files, and Schroeder argues they are right to: narrow agents give control, bounded blast radius, and evaluable efficacy. The missing piece is a standard for the harness itself (MCP, A2A, skills and AGENTS.md cover everything around it). He launches the open-source Standard Agent Specification, a TypeScript-defined agent runtime contract, plus Standard Agent Builder as its first runtime.

## Key Takeaways
- **Three reasons businesses build agents anyway:** integration (a business is its processes; handing core processes to a general agent is too risky), trust ("if an agent can do anything, it might do anything"), and efficacy (does it actually improve the process).
- **Narrow agent beats broad skill:** a Gmail agent on DeepSeek V4.1 Flash with 6 scoped tools is cheaper, evaluable, and "benchmaxing" on a single task becomes a feature rather than a bug.
- **Agent definition:** deterministic software that harnesses non-deterministic model outputs toward an objective. Agent is an instance of a harness.
- **Five principles:** vendor agnostic, domain specific, coupled to a model, composable, portable. Model coupling is deliberate: pin a specific model, quant, and provider, with an escalation fallback to a smarter model.
- **Spec primitives:** model, prompt (owns one side of a conversation, composable/includable), tools (function, sub-prompt, or full sub-agent), sub-agents, hooks (before tool call, filter messages, etc.), parent hooks (child auto-registers with parent, zero config), effects (scheduled code), threads (sandbox with own messages, KV, virtual filesystem, gated code execution, decision models, HTTP/WebSocket endpoints).
- **Two-sided conversations:** side A and side B can each be a prompt, human, or deterministic handler. Prompt-vs-prompt gives built-in QA loops (worker plus reviewer).
- **Everything is code (TypeScript)** so agents can be packed as npm packages and written by coding agents without a build step. Runtimes can be written in any language that executes the TS.
- **Demo:** Claude Code (Opus 5.5) generated a battery warranty agent from a process PDF in 5 min 21 s, pinned to DeepSeek V4.1 Flash, 94% prompt-cache hit rate, exposed over HTTP, WebSocket, and as an MCP server.

## Architecture & Optimization Mechanics
- **Routing by construction.** Instead of a runtime router picking a model per query, the spec pushes routing to design time: each sub-agent is pinned to the cheapest model that passes its eval, with a defined escalation path on failure. This is a static, per-task cascade. It exploits model "jaggedness" (e.g. a weak general model that is excellent and cheap at one task, like the 3D zen-garden example).
- **Tool-set shrinkage is a cost and accuracy lever.** Sending 6 tools instead of hundreds cuts prompt tokens and decision entropy, and keeps prefixes stable, which is why the demo hits 94% cache.
- **Hierarchical composition** (small agents under a parent, or exposed as MCP to a frontier model) is structurally an MoE at the agent level: a gating parent dispatching to specialist experts with their own small models.
- **Weak spots:** pinning to a specific quant and provider fights vendor agnosticism in practice, and the spec says nothing about how to measure when a pinned agent should be re-routed as models improve. TypeScript-only definitions also exclude the Python-heavy ML stack.

## Grounded Context (Web Enrichment)
The spec is live as version 0.1.0 (docs mirrored at standardagentspec-com.pages.dev), MIT licensed, published by the FormKit / Standard Agent Builder team. It defines model, prompt, agent rules, tools, hooks, and endpoints with TypeScript as the runtime. Do not confuse it with Oracle's "Open Agent Specification (Agent Spec)" (arXiv 2510.04173), a declarative JSON/YAML, framework-agnostic format with a similar name and overlapping goals. Two competing "agent spec" efforts at v0.x signals the harness layer is still unstandardized; adoption, not design, will decide.

The "Jeepa paper" cited is GEPA (Reflective Prompt Evolution, 2025), which reported prompt optimization beating GRPO fine-tuning on several tasks with far fewer rollouts. That supports the narrower claim "for a fixed narrow task, optimize the prompt before the weights," not the blanket claim that prompt tuning always beats model tuning.

## Real-World Application / Actionable Step
- Treat routing as a two-level problem: design-time pinning per sub-task (cheap model that passes eval) plus runtime escalation on low confidence. Benchmark your query-level router against this static cascade baseline.
- For any agent you ship, cap the tool set per sub-agent and measure cache hit rate and tool-selection accuracy as a function of tool count.
- Run GEPA-style prompt optimization on a small pinned model (e.g. a Flash-tier model) for one narrow task before reaching for distillation or fine-tuning; only distill if prompt optimization plateaus.
- Skim the 0.1.0 spec for the hooks and effects lifecycle; it is a reasonable checklist even if you never adopt the standard.
