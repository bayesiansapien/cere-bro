# GPT-5.5: Launch Analysis and System Card Deep Dive

**Date:** 2026-04-24 (launch) / 2026-04-25 (system card analysis)  
**Sources:** [OpenAI Announcement](https://openai.com/index/introducing-gpt-5-5/) · [Ken Huang System Card Analysis](https://kenhuangus.substack.com/p/unpacking-the-gpt-55-system-card) · [SemiAnalysis Coding Breakdown](https://newsletter.semianalysis.com/p/the-coding-assistant-breakdown-more) · [AI Breakfast](https://aibreakfast.beehiiv.com)  
**Raw:** raw/gmail/2026-04-24-starred.md · raw/gmail/2026-04-25-starred.md

---

## TL;DR

GPT-5.5 ("Spud" pre-train) launched April 24, 2026. First OpenAI pre-train since GPT-4.5. Priced at $5/$30 input/output (2x GPT-5.4, slightly more than Opus 4.7). Built on NVIDIA GB200. SemiAnalysis declares it now frontier-tier for coding — shifting their daily driver from Opus. Key architectural improvement: destructive action avoidance score jumped significantly (0.86 → 0.90), and "perfect reversion" (revert own changes without destroying user work) leapt from 0.18 to 0.52.

---

## What GPT-5.5 Is

- **Training**: post-training (RL) only on GB200 cluster; pre-training still on Hopper
- **Variants**: GPT-5.5 (standard), GPT-5.5 Pro (parallel test-time compute, same price as 5.4 Pro at $30/180), GPT-5.3-Codex-Spark (distilled, runs on Cerebras)
- **Reasoning levels**: xhigh, high, medium, low, non-reasoning — user-selectable cost/capability tradeoff
- **Token efficiency**: benchmarks higher than 5.4 while using fewer tokens ("cost per task" not "cost per token" is the true metric)
- **Pricing**: $5/$30 per million input/output; 2.5x priority tier available; Fast mode also available

## SemiAnalysis Verdict

SemiAnalysis shifted from Opus 4.7 as daily driver to GPT-5.5 for coding. Key findings:
- One major lab releasing a coding-specific checkpoint **every week for 3 months**: GLM-5.1, Qwen3.6-Plus, Kimi K2.6, Composer 2, Gemini 3.1 Pro
- GPT-5.5 "materially better at some tasks than all other models" — arrived at frontier
- SemiAnalysis frames "token efficiency" as the key new competitive dimension: cost per task, not cost per token
- Opus 4.6 Fast is the only Fast/Priority SKU that has gained real traction among SemiAnalysis's users

## System Card Safety Analysis (Ken Huang)

### Agentic Safety — The Critical Metric
GPT-5.5's most important improvement is for agentic deployment in shared workspaces:

| Metric | GPT-5.3-Codex | GPT-5.4-Thinking | GPT-5.5 |
|--------|---------------|-------------------|---------|
| Destructive action avoidance | 0.88 | 0.86 | **0.90** |
| Perfect reversion (own work only) | — | 0.18 | **0.52** |
| User work preserved | — | 0.53 | **0.57** |

"Perfect reversion" — reverting only the agent's own changes while preserving concurrent user edits — jumped nearly 3x. OpenAI specifically trained agents to distinguish "my work" from "the user's work" in shared environments. This directly addresses the failure mode where cleanup agents delete uncommitted user changes.

### Safety Regressions
- Extremism compliance: 1.000 → 0.925
- Hate speech compliance: 0.943 → 0.868 (attributed to translation requests)
- Self-harm: 0.977 → 0.937 (notable regression, warrants attention)

### HealthBench (Medical)
Length-adjusted HealthBench: 56.5 (+2.5 over 5.4). HealthBench Professional (clinician use cases): +3.7 points to 51.8. HealthBench Consensus flat at 95.6.

## New Products Launched Alongside

- **Codex in-app browser**: navigate local dev servers, test web flows from within Codex
- **OpenAI Privacy Filter**: 1.5B open-weight model, bidirectional token classification, 97.43% F1 PII redaction before cloud processing — notable as a local privacy primitive
- **ChatGPT for Clinicians**: targets medical paperwork reduction
- **GPT-5.5 Bio Bug Bounty**: find a universal jailbreak in biological safety checks
- **Workspace Agents**: persistent memory + dedicated cloud environments for enterprise (custom GPT evolution)

## Claude Code Postmortem (same week)

Anthropic simultaneously disclosed that Claude Code's performance issues (widely reported as "AI shrinkflation") were caused by product bugs, not model degradation:
- Reasoning effort was lowered to reduce latency (unintentional capability reduction)
- A caching bug repeatedly cleared short-term context
- Strict system prompts limited response detail
Fixed in v2.1.116. Affected Claude Code and SDK only (not the API directly).

---

## Relation to Prior Wiki Knowledge

**Directly relevant to SemiAnalysis Goodput (04-21)**: SemiAnalysis now names GPT-5.5 as the frontier shift point for coding. Their "token efficiency" framing maps directly to the "cost per task" metric they've been building toward.

**Connects to persistent agent infrastructure (04-23)**: The perfect reversion improvement (0.18→0.52) is exactly the capability needed for Kimi K2.6-style long-running agents that modify shared codebases. Previously this was a known failure mode. It's now significantly better.

**Connects to Claude Code memory systems (04-25)**: The Claude Code postmortem revealed that context management bugs (caching, system prompts) caused perceived capability degradation. Ken Huang's Chapter 8 analysis shows why this matters: Claude Code's eager-flush transcript design is the durability mechanism, and bugs in that layer have outsized impact.

---

## Open Questions

1. GPT-5.5 Pro's parallel test-time compute — does higher reasoning at inference compound the perfect-reversion improvement, or is that independent of reasoning effort level?
2. The extremism and hate regression: are these genuine capability regressions or evaluation artifacts from harder test cases?
3. SemiAnalysis switched to GPT-5.5 for coding. How does Anthropic respond? Mythos is the flagship but restricted. Does the coding market shift before Mythos is broadly available?

---

## Related Pages

- [Claude Code Architecture](2026-04-19-claude-code-architecture.md)
- [Claude Code vs Hermes Permissions](2026-04-23-claude-code-vs-hermes-permissions.md)
- [Persistent Agent Infrastructure](2026-04-23-persistent-agent-infrastructure.md)
