# How to Build a Custom Agent Harness (LangChain): middleware as the harness primitive

**Source:** Sydney Runkle, LangChain blog, published 2026-06-03, resurfaced on the X home feed 2026-09-14 via [@shreyanshpatni_](https://x.com/shreyanshpatni_/status/2099180288668750246). [Article](https://langchain.com/blog/how-to-build-a-custom-agent-harness)
**Date:** 2026-09-14
**Raw:** [feed capture](../../raw/twitter/feed/2026-09-14-morning-ranked.json)

## TL;DR

The post's organizing equation is `agent = model + harness`, and its definition of a harness is narrower and more useful than the usual one: **the harness is whatever gets the right context to the model at every step.** Not the loop, not the tools, not memory as separate concerns, but the single job those three serve. Its architectural claim is that the right primitive for customizing a harness is **middleware**: small composable units that hook into the agent loop at fixed points (before and after each model call, before and after each tool call, at startup and teardown), each handling one concern. `create_agent` deliberately implements only the bare loop and exposes middleware as the extension point, in contrast to pre-assembled harnesses like Deep Agents or the Claude Agent SDK that ship an opinionated stack. The interesting part for this wiki is the **capability-to-middleware table**, which is effectively a published taxonomy of what a production harness has to do.

## The taxonomy

Six capabilities, each with a named failure mode:

| Capability | The failure it prevents |
|---|---|
| Prevent context overflow | Long sessions accumulate history until it exceeds the window. Handled by summarization and context-editing middleware. |
| Access and update memory | Knowledge loaded at startup and written back at the end, so the agent improves from real usage. Filesystem, memory and skills middleware. |
| Take actions in an environment | A fixed toolset caps what the agent can do; shell, filesystem and code-interpreter access unlock solutions that are often **more token-efficient**, not just more capable. |
| Delegate tasks | Subagents get clean context windows for sub-tasks; a todo list carries progress across a long run. |
| Handle transient failures | Models and tools fail unpredictably; retry with backoff and model fallback. |
| Enforce policies | PII handling, compliance, approval gates. These fire on every call regardless of what the model does, and the post is explicit that **they do not belong in a prompt**. |

Four levers middleware pulls: deterministic logic (including runtime model swapping by task complexity and message-history rewriting during compaction), tool lifecycle management, custom state shared across hooks, and stream handlers that intercept and transform the output stream.

## Why it is worth a page

**It is the clearest published statement of the boundary between prompt and code in an agent system.** Two of its claims are load-bearing and both are about where logic must *not* live. Policy enforcement must be deterministic middleware because a prompt cannot guarantee it fires. Model selection by task complexity is runtime control, not a prompt instruction. **That is routing, implemented as a harness hook**, which puts it directly on the [LLM routing page](../ai-routing/llm-routing.md)'s territory from an engineering rather than a research direction.

**It also names token efficiency as an argument for environment access**, which is an inversion worth recording. The usual case for giving an agent a shell and a filesystem is capability. The post's case is that an agent that can run a command often solves in one tool call what would otherwise take several thousand tokens of reasoning and retrieval. That is the same economics as [ContextPipe (09-06)](2026-09-06-contextpipe-database-context-assembly.md), which cut total token volume 31% by treating context assembly as query execution: **a token never assembled costs nothing at any cache tier.**

## How this relates to what the wiki already knows

**This is the productized form of what the harness-engineering thread has been assembling from research.** The [agent harness engineering page](agent-harness-engineering.md) has collected the research side: [SoL-Pi (09-11)](2026-09-11-sol-pi-harness-auto-research.md) automatically found four harness optimizations worth 45-49% of tokens, two of which act on the volatile tail of the context; [COBRA-Skills (09-13)](2026-09-13-cobra-skills-robustsgpo-harness-search.md) cut skill-optimization cost 55-58% by using a contextual bandit to decide which candidate skills are worth executing; [Ecdysis (09-12)](2026-09-12-ecdysis-harness-training.md) trained the harness rather than the model. **The gap this article exposes is that none of the research optimizations map onto a named middleware slot.** Online context compaction maps to summarization middleware; observation packing does not map to anything; byte-stable prefix construction, which [Ken Huang's 09-13 post](../inference-efficiency/2026-09-13-prefix-stable-kv-caching-claude-md.md) showed can silently destroy KV cache reuse, has no middleware at all and arguably cannot have one, because it is a property of how the system prompt is *built* rather than of anything the loop does.

**And it intersects the day's loudest social claim.** [@gregisenberg's "agent harnesses are the new GPT wrappers" post](https://x.com/gregisenberg/status/2099202686377742576) made the market argument, that a harness sells finished work rather than software, and that its durable asset is model-independence: "a wrapper was one model doing everything and a harness is a router." The LangChain post is what that abstraction actually looks like in code, and the two together are why the harness theme is now the most-saved theme in the [private curation trail](../../raw/twitter/bookmarks/CURATION-INDEX.md).

## Gaps

No numbers anywhere. No token-cost comparison between a minimal `create_agent` harness and a pre-assembled one, no measurement of what each middleware costs or saves, and no evaluation. It is a design document from a vendor with a product in the category, and should be read as a taxonomy rather than as evidence.

## Related pages

- [Agent harness engineering](agent-harness-engineering.md)
- [Tool calling](tool-calling.md)
- [Agent memory](agent-memory.md)
- [LLM routing](../ai-routing/llm-routing.md)
