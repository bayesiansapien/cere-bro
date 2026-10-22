# A Bank Built Its Own Coding Agent. It Took Off (Felippe Felisola Caso & Francesco Galletta, Monzo)

**Channel:** AI Engineer
**Published:** 2026-10-20
**Source:** https://www.youtube.com/watch?v=adfw3xJBx1o

## TL;DR
Monzo's in-house remote coding agent, Agent Chip, now authors over 10% of all merged PRs across its tech org and runs 1,800+ tasks per day. The thesis: the agent is not the moat. The pre-existing platform (alerting, staging, queues, deploy tooling, DB abstractions) plus an MCP gateway and a sandboxed orchestration layer made a provider-agnostic agent cheap to build and easy to compose into new use cases. "LLMs" here is a pun for "lots of little multipliers."

## Key Takeaways
- **Scale of surface area:** 3,000+ backend services, ~13,000 data warehouse models, dozens of ML predictors (credit, fincrime). The agent operates across all of it.
- **Adoption path:** Started January 2026 as a Slack emoji reaction that turned any message into a prompt. Went viral internally, then became an always-on teammate (Slack mentions, code review, Linear tickets).
- **MCP gateway first:** Built before the remote agent, to give local coding agents deterministic, curated access to internal services and knowledge sources, with centralized authn/authz per agent.
- **Sandbox architecture:** Isolated Kubernetes namespace, one pod per sandbox. The agent image pins exact tools, CLIs and credentials. An egress proxy whitelists what the agent can reach (repos, selected external endpoints). Non-determinism is confined to the innermost box.
- **Use cases that compound:** incident triage (joins incident channel, reads logs, traces, code, stays deliberately terse), squad-to-squad "ask channels" auto-drafting answers, reactive data-quality alert triage ("Agent Chip on Call"), and a proactive variant that predicts downstream data breakage from backend diffs before the next batch run.
- **Non-engineer contribution:** Business users get a staging-tested draft PR before an engineer is pulled in. Review rigor is unchanged; the entry cost drops.
- **Model-agnostic by design:** The agent box can be swapped for any model, and they claim dynamic per-purpose model selection.

## Architecture & Optimization Mechanics
- **Control plane vs. non-deterministic plane separation** is the core design pattern: gateway (auth, tool curation) and orchestration (sandbox lifecycle, egress) are deterministic; only the model loop is free.
- **Tool exposure is a curated, server-side decision**, not a per-agent prompt choice. That makes swapping models a config change rather than a security re-review.
- **Composability:** once the agent is itself a platform primitive, new workflows (incident, on-call, proactive data checks) are thin wrappers. Value scales with platform maturity, not model capability.
- **Missing from the talk:** no cost per task, no PR acceptance or revert rate, no breakdown of which model(s) handle which task class. "10% of merged PRs" says nothing about PR size or difficulty. Treat it as an adoption metric, not a productivity metric.

## Grounded Context (Web Enrichment)
Monzo published "Building Agent Chip: Monzo's in-house agentic tool" on its blog (13 Aug 2026), consistent with the talk: internal-tool integration, incident support and non-engineer contributions, with development ongoing. The jab that they "built Claude Tag 6 months before Anthropic released it" checks out on timing: Anthropic launched Claude Tag in Slack on 23 June 2026 (beta for Team and Enterprise, single shared Claude per channel, admin-scoped tools and data, ambient mode), replacing the older Claude-in-Slack app. Agent Chip went viral internally in January 2026.

The strategic question this raises: off-the-shelf Slack agents now cover the "@agent in a thread" UX, so the durable differentiator for in-house builds is exactly what Monzo emphasizes, the regulated-environment sandbox and curated internal tool gateway. For most companies without Monzo's platform maturity, buying Claude Tag or similar is likely the better call. The "if you're not building your own harness, are you even a serious tech company" framing is hype; Monzo's own argument is that the platform, not the harness, did the work.

## Real-World Application / Actionable Step
- **Routing angle:** Monzo's swap-the-model box is the ideal insertion point for an LLM router. Their task mix (terse incident triage, long code changes, SQL drafting for business users, Q&A) is heterogeneous and a strong candidate for per-task-class routing to cheaper models. If pitching routing internally, frame it as a drop-in at the orchestration layer with per-task-class quality gates.
- **Metric to steal:** track agent-authored share of merged PRs, but pair it with revert rate and cost per merged PR. Without those two, a router cannot prove it preserved quality while cutting spend.
- **For your own agent tooling:** put tool curation and auth in a gateway, not in prompts. It makes A/B testing compressed or distilled models against frontier models a safe config flip.
