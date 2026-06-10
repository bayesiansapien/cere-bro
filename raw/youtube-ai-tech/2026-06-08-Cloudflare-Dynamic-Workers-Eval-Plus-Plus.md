# Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carrie, Cloudflare

**Channel:** AI Engineer  
**Published:** 2026-06-08  
**Source:** https://www.youtube.com/watch?v=SKDJo2CopRs  

## TL;DR
Cloudflare introduces **Dynamic Workers (Eval++)** and **"Code Mode"**, a paradigm shift where AI agents generate and execute TypeScript logic in millisecond-startup V8 isolates instead of performing sequential tool calls. This "Eval++" primitive bypasses the latency and token overhead of LLM-orchestrated loops, effectively turning the agent into a just-in-time software engineer that writes its own optimized execution scripts.

## Key Takeaways
- **Code Mode vs. Tool Calls:** Instead of the LLM calling `search()`, then `calculate()`, then `format()`, the LLM writes a single script that performs all three. This reduces round-trips and token usage by up to 80%.
- **Dynamic Workers (Eval++):** A secure execution environment with millisecond startup and minimal memory footprint, designed specifically for untrusted, AI-generated code.
- **Durable Objects Facets:** Provides stateful "facets" (isolated SQLite instances) for agents, allowing memory and state to persist across sessions and multi-channel (voice/email) interactions.
- **Security-First Isolate:** Unlike VMs, Dynamic Workers start with zero capabilities (no fetch, no env vars) and are granted explicit, granular permissions by the host.

## Architecture & Optimization Mechanics
- **V8 Isolate Sandboxing:** Optimization focuses on sub-millisecond cold starts and high-density multi-tenancy. By avoiding the Linux kernel overhead of containers, Cloudflare can spin up billions of "one-off" execution environments.
- **Resumable Streams:** Leverages Durable Objects to maintain stateful WebSocket connections. If an agent-driven stream is interrupted, the "Durable" nature allows it to resume without re-running the entire inference chain.
- **Inference Optimization:** Shifting the "reasoning" from a multi-turn LLM loop to a single-turn code generation task significantly lowers the total cost of inference (TCO) for complex agentic workflows.

## Grounded Context (Web Enrichment)
As of June 2026, Cloudflare's **"Agents Week"** has confirmed the release of **Project Think**, a batteries-included SDK that integrates these primitives. Web research shows that "Code Mode" is now a standard feature in the **Cloudflare Shell**, and the new **Durable Objects Facets** allows each agent facet to manage its own 10GB SQLite database. This effectively solves the "long-term memory" problem for agents without requiring a separate vector database for simple state management.

## Real-World Application / Actionable Step
- **For Amit:** Stop building multi-turn "ReAct" loops for complex data processing. Instead, prompt the model to generate a **TypeScript facet** that runs in a Dynamic Worker. 
- **Action:** Transition internal tool-routing logic from "JSON-mode" tool calling to "Code-mode" generation. This will reduce latency in the routing layer and allow for more complex logic (loops, conditionals) that standard tool calling handles poorly.
