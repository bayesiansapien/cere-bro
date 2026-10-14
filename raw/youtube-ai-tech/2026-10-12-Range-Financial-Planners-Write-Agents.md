# We Let Our Financial Planners Write the Agents (Matthew Ragone, Range)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=gpmze-6ueGU

*Secondary domain: finance.*

## TL;DR
A certified financial planner (not an engineer) at Range, an all-in-one wealth manager, explains how planners authored the agents they use daily. The insight is that a planner's constraint is not typing speed but being in one place at a time, so the value is agents drafting a cash flow or insurance analysis for client B while the planner is on a call with client A. The unit of work is a "skill": the firm's specific way of doing one task, written down by the domain expert. Five steps, no code: pick, teach, pack, test, ship. Six months in: 24 skills, 17 in planning, organic spread to sales, product and marketing. The method is sound and matches Anthropic's own Skills guidance; the talk is light on metrics (no error rates, no time saved).

## Key Takeaways
- **Reframe:** chatbot use made existing work slightly faster. Async drafting while the human is elsewhere is what changed throughput.
- **Two prerequisites:** the agent works where the work lives (not copy-paste into a chat window), and it knows *how this firm* does it, not how the field works generically.
- **Step 1, Pick:** a frequent workflow where you can judge output at a glance. Prefer low-complexity, high-manual-effort tasks (cash flow analysis, insurance reviews), not the flashiest.
- **Step 2, Teach:** walk through several real past cases and narrate judgment aloud: why you open a document, what you look for, what would make you stop. "That narration is the whole game."
- **Step 3, Pack:** a skill is not a step list. It encodes (a) the questions it must ask before starting, and (b) hard limits. The big limit: it never sends anything to a client.
- **Step 4, Test:** 5 to 10 runs on real cases before anyone else sees it. Each run surfaces an edge case, a missing question, or confident wrongness.
- **Step 5, Ship:** an owner (keeps it current as tax rules change) and a separate reviewer (you do not grade your own work).
- **Bottleneck has moved** from "can the model do it" to "who writes down how we do it, who tests it, who owns it."

## Architecture & Optimization Mechanics
- **Skill = procedural knowledge plus guardrails.** The "questions to ask first" section is a clarification policy: it trades a little latency for fewer wrong-premise drafts. The "limits" section is an action-space restriction (draft only, no send).
- **Human-in-the-loop as the safety boundary.** Every recommendation is reviewed before a client sees it. That makes the system tolerant of imperfect skills, which is why non-engineers can ship them.
- **Peer review maps onto existing culture.** Planners already review each other's plans, so reviewing skills reuses an institutional habit. This is the main reason adoption spread without a mandate.
- **Missing pieces:** no eval harness beyond manual runs, no versioning or regression testing mentioned, no measured accuracy. "Owner keeps it current" will not scale past a few dozen skills without automated regression tests on golden cases.

## Grounded Context (Web Enrichment)
Range is a real wealth manager; a late-2025 funding report put it at about $400M AUM, $9.5B AUA and 5,000+ high-net-worth clients, and said its AI advisor halved messaging to human advisors. The talk does not name the model, but "skill" and "Claude knows how to do the skill" match Anthropic's Agent Skills format (folder with SKILL.md, YAML frontmatter, scripts). Anthropic explicitly positions skills as authorable by domain experts, and the format has spread to Codex CLI, Gemini CLI, Cursor and Copilot. Anthropic launched Claude for Financial Advisors in September 2026 with workflow skills (onboarding, compliance review, rebalancing review, meeting prep) and Schwab, BlackRock, Addepar and Orion connectors, and its financial-services agents follow the same rule Range describes: draft for professional review, never execute or recommend autonomously.

The claim "there isn't much field data on this yet" holds. I found no independent data on non-engineer skill adoption rates. Range's 24-skill figure is self-reported and unaccompanied by quality metrics, so treat it as a case study, not evidence of effectiveness.

## Real-World Application / Actionable Step
- **For your own research workflow:** write skills for repeated, judgeable tasks (e.g. "run a quantization sweep and summarize perplexity/latency deltas," "triage a new pruning paper against our baselines"). Narrate your judgment, not just steps.
- **Always include a "questions first" block and a "never do" block** (e.g. never overwrite checkpoints, never launch >N GPU jobs).
- **Add what Range lacks:** 5 to 10 golden cases per skill as a regression suite, rerun on every edit and every model swap. This also gives you a cheap eval for routing skills to a smaller model.
- **Routing angle:** narrowly scoped skills with explicit questions and limits are the best candidates to route to cheap models. Measure which skills hold quality on a small model and route those first.
