# Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4), Anthropic

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=QSeaZ6qHyXs

Series: [Part 1: Brain vs Hands](2026-10-12-Claude-Managed-Agents-Part1-Brain-Hands.md) | [Part 2: Research Agent](2026-10-12-Claude-Managed-Agents-Part2-Research-Agent.md) | [Part 3: Scheduled Agents and Dreaming](2026-10-12-Claude-Managed-Agents-Part3-Scheduled-Dreaming.md) | **Part 4**

## TL;DR
Closing Q&A on running Claude Managed Agents (CMA) in production. Agents, environments and other resources are managed as YAML via the `ant` CLI in CI, Terraform-style. Anthropic's own eval practice is massive parallel session replay (10,000 sessions) on each new model to strip stale harness assumptions. For builders, the advice is blunt: get high-quality eval data, because ill-posed evals return 100% and mean nothing. Multi-tenancy maps to agent-per-customer, workspace-per-customer, or org-per-customer depending on isolation needs. Plus practical patterns: PR-review agents, QA in the sandbox, GPU via Modal sandboxes, and a coordinator pattern to dodge the custom-tool blocking rule.

## Key Takeaways
- **CI/CD:** check agent/environment definitions into the repo as YAML; `ant` CLI applies them on merge. Same tool syncs one definition across many workspaces.
- **Custom-tool blocking:** while the main thread awaits a custom tool result, sending a new message returns HTTP 400 (ordering guarantee). Otherwise messages queue.
- **Anthropic's internal evals:** early model access, datasets replayed across thousands of parallel cloud sessions, then prompts and harness assumptions are tuned or removed per model release. Generic tasks, not just coding.
- **Builder eval advice:** data quality first; Claude Code can scaffold evals but "garbage in, garbage out". Mine historical sessions and score them to build the dataset.
- **Access control:** resources are workspace-bound; any API key in a workspace sees everything in it. Admins design workspaces around access groups. No per-resource sharing (e.g. share memory but not MCP).
- **Code review bottleneck:** CMA can fan out many sessions/sub-agents per PR to find bugs; Anthropic uses this internally. They admit review throughput is an open problem.
- **QA:** run the app in the sandbox, have Claude drive a browser and self-validate, optionally return a video. No live tunneling into sessions yet.
- **Multi-tenancy options:**
  - Single workspace, single agent, session `metadata` holds `customer_id` (simplest, no hard data segregation).
  - Workspace per customer (data segregation; sync agent definitions via CI).
  - Org per customer (strongest isolation).
  - No on-prem.
- **Custom compute:** CMA sandboxes are uniform. For more RAM or GPUs, use self-hosted sandboxes (Modal, E2B, Daytona; cookbooks exist).
- **Slack-style multiplayer agent:** map thread or channel to session; inject `user.message` tagged with the sender; give the agent an explicit post tool rather than mirroring all output; one agent and memory per channel.
- **Long runs and progress:** outcomes provide the exit criterion; nothing special needed for over 6 hours. Expose a custom `update_status` tool for checkpoints.
- **Coordinator pattern:** put custom tools on a sub-agent so the main thread stays free to receive messages; you interact only with the main thread and CMA routes tool results by ID.

## Architecture & Optimization Mechanics
- **Eval at cloud scale is the moat.** 10,000 parallel sessions per model release is how Anthropic decides which harness patches to delete (see [Part 1](2026-10-12-Claude-Managed-Agents-Part1-Brain-Hands.md) on stale assumptions). Ablation-driven harness pruning is the same discipline as structured pruning: remove components, measure the delta, keep what matters.
- **Coordinator plus tool-owning sub-agent** decouples human-facing latency from blocking I/O. It is the agent-level equivalent of separating the request-accepting frontend from the worker pool in an inference server.
- **Tenancy is coarse.** Workspace equals blast radius. Fine-grained RBAC lives in your integration layer, not CMA. For regulated multi-tenant SaaS this pushes you toward workspace-per-customer plus CI sync, which multiplies operational surface.
- **Opinion:** The eval answer is honest but thin. CMA gives you outcomes (a grader) and a full event log, but no first-party eval runner, dataset management or regression dashboard. The best eval tooling here is the stuff you build.

## Grounded Context (Web Enrichment)
The `ant` CLI accepts YAML for sessions (`ant beta:sessions create`), events, and agent/environment definitions, with agent version pinning and per-session `agent_with_overrides` that can swap model or system prompt without creating a new agent version ([Claude docs: Sessions](https://platform.claude.com/docs/en/managed-agents/sessions), [TrueFoundry guide](https://www.truefoundry.com/blog/how-to-use-claude-managed-agents)). That override is the hook for routing and model A/B tests. Self-hosted sandboxes (Cloudflare, Daytona, Modal, Vercel) went public beta May 19, 2026, with Modal positioned for on-demand GPU ([Claude blog](https://claude.com/blog/claude-managed-agents-updates), [The Decoder](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/)). On AWS's Claude Platform, IAM actions exist for memory stores, and wildcard `Get*` policies silently grant memory read access, which matters for tenant isolation ([AWS docs](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.md)).

Against competitors: a small May 2026 benchmark had CMA (Sonnet 4.6) and Vertex Agent Engine (Gemini 2.5 Pro) both at 30/30 on coding tasks, OpenAI Responses at 27/30 due to sandbox egress blocks, with Vertex cheaper (~$1.45 vs ~$2.50) but slower; CMA led on managed features like mid-stream steering ([AIMultiple](https://aimultiple.com/ai-agent-platforms)). AWS AgentCore offers microVM-per-session isolation and up to 14-day sessions on its Instances compute type, which is stronger per-tenant isolation than CMA workspaces ([AWS docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), [Tutorials Dojo](https://tutorialsdojo.com/amazon-bedrock-agentcore-runtime-cheat-sheet/)). OpenAI's Agents API (Sept 2026) is the closest like-for-like rival ([OpenAI](https://openai.com/index/introducing-the-agents-api/)). For multi-model routing research, CMA's Claude-only constraint is the decisive limitation.

## Real-World Application / Actionable Step
- **Build a routing eval on CMA using `agent_with_overrides`.** Same agent, same task set, sessions fanned out per model (Haiku / Sonnet 5.x / Opus). Collect outcome verdicts, iterations, tokens and runtime from the event log. You get a cost-quality Pareto curve per task class, which is your router's training data.
- **Bootstrap the dataset from history.** Export past session transcripts, label with outcome results, and hold out a fixed regression set. Rerun it on every model release, matching Anthropic's own practice.
- **Version agents in git** (YAML + `ant` in CI) so every eval result is tied to an exact agent version and model.
- **Prefer workspace-per-tenant** for anything with data-segregation requirements; never rely on session metadata for isolation.
- **GPU-bound tools** (e.g. running a quantized model through vLLM inside the agent loop for benchmarking) need a Modal self-hosted sandbox. Use it for agent-driven kernel or quantization sweeps where Claude orchestrates and the GPU does the work.
