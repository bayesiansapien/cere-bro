# The One Thing Every AI Agent Framework Agrees On (Mislav Ivanda, Daytona)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=WWIFiQi9U4w

## TL;DR
Agent frameworks disagree on almost everything (what an agent is, who controls behavior, language), yet every one of them has converged on the same three-call sandbox interface: create, run, delete. Ivanda's argument is that the execution boundary, not the framework, is the irreversible architectural choice. Frameworks, models, prompts and even sandbox vendors are swappable; whether tools and code run on the host or inside an isolated VM shapes every tool you write and is painful to retrofit. The speaker sells sandboxes, but the industry evidence supports him.

## Key Takeaways
- **Three isolation tiers:**
  1. Allowlists, approval prompts, hooks. Weak: approving `python -c` grants sockets, filesystem and arbitrary execution. You defined what the model should use, not what it can use.
  2. Embedded runtimes (V8, QuickJS). Subtle hole: the generated glue code is isolated, but tool calls (send email, query DB, delete DB) still execute on the host. A compromised agent acts through its tools.
  3. Separate VM/sandbox controlled via API. A compromised sandbox is not a compromised app; discard and respawn.
- **Frameworks are deleting alternatives, not adding sandboxes:** CrewAI removed its local code interpreter (April 2026), AG2 retired local executors, OpenAI Agents SDK ships a native SandboxAgent, Claude Agent SDK uses process-level sandboxing (bubblewrap-style), Mastra similar.
- **Usage evolution:** short-lived code runners, then the whole agent living inside the sandbox, now thousands of concurrent sandboxes for RL rollouts, post-training, benchmarks and subagent fan-out.
- **Swappable:** framework (same language, an agent can refactor it), model/prompt (needs regression tests), most features (evals, tracing, memory), sandbox vendor. **Exception:** durable execution, which is architectural.
- **Not swappable:** the execution boundary. Teams prototype on the host and never move, until something kills the product.

## Architecture & Optimization Mechanics
- The key insight is the tier-2 failure mode: isolation of code without isolation of capabilities. Security is defined by the tool surface, not by where the interpreter runs.
- The concurrency point matters for training infra: agent RL needs thousands of cheap, fast-booting, disposable environments. Sandbox cold-start latency and density become part of the RL throughput budget, alongside inference GPUs (see the Modal async RL talk from the same conference).
- Sandbox APIs are effectively commoditized (create/exec/delete), so differentiation is on boot latency, snapshotting/resume, and price per concurrent environment.

## Grounded Context (Web Enrichment)
The CrewAI claim checks out and the backstory is stronger than the talk suggests. CrewAI's docs mark CodeInterpreterTool as removed and point to E2B or Modal. A CERT/CISA advisory (VU#221883, revised May 2026) lists several CrewAI CVEs, including one where the tool silently fell back to an in-process "SandboxPython" when Docker was unreachable. CrewAI removed the tool, its Docker sandbox and the fallback entirely. That is exactly Ivanda's tier-1/tier-2 failure in the wild: a soft sandbox that degrades to host execution.

OpenAI's "next evolution of the Agents SDK" (April 15, 2026) introduced sandbox agents with manifests, snapshots, resume and pluggable providers (Modal, Daytona, Docker, E2B, Vercel, Cloudflare, Blaxel). The APIs are still marked beta. Net: the convergence thesis is accurate, and the vendor bias is mostly in implying VMs are always necessary. Process-level sandboxes (bubblewrap, seccomp) are adequate for many local coding workflows with trusted inputs.

## Real-World Application / Actionable Step
- For any agentic eval or RL harness you build (routing evals, compressed-model agent benchmarks), run tool execution in a disposable sandbox from day one and write tools against the sandbox API, not the host filesystem. Retrofitting later is the expensive path.
- Audit existing agent setups for the tier-2 hole: list every tool that executes on the host with real credentials. Those are your blast radius regardless of where generated code runs.
- When benchmarking compressed or routed models on agentic tasks, include sandbox boot and exec latency in end-to-end numbers; at high concurrency it can rival model latency.
