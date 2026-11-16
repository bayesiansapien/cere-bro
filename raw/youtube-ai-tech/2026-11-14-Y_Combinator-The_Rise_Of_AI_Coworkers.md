# The Rise Of AI Coworkers

**Channel:** Y Combinator (Lightcone)
**Published:** 2026-11-14
**Source:** https://www.youtube.com/watch?v=y1-9yeYLJUo

## TL;DR
Lauren Tan and Roman Ugarte, who built SpaceXAI's Grok Bot in seven weeks, describe the product as persistent AI teammates. Each bot has its own identity, credentials, computer and always-on loops, and they live in Slack and X rather than in a chat app. The thesis is that coding agents already have an "inner loop" (software factories). The next step is an "outer loop" that brings context and intent to agents for every function in a company. The bottleneck moves from execution to intent specification and taste.

## Key Takeaways
- **Three design principles:** bots (not chats or files) are the main object; bots use the same tools humans do, including their own computer; bots are always on and proactive.
- **The trust ladder for adoption:** step 1 is read-only (for example Databot, with read access to the warehouse and answers in Slack). Step 2 is taking action end to end. Step 3 is owning an outcome or a job. Most companies are still on steps 1 and 2.
- **Specialist bots beat one omniscient bot.** Each bot is its own context plus skill set. "Loops are crons with webhooks on top of skill files." Organize bots horizontally (one per function) or vertically (one per customer).
- **Team bots, shipped about two weeks ago:** a domain-expert "builder" owns the bot and the rest of the org shares it. Examples: performance marketing gives a bot an ad budget and its own Google and Meta logins to A/B test assets made by the design team's bot; a CS bot triages hundreds of messages a minute.
- **Work in public.** Running agents inside Slack threads lets workflows spread by imitation. One feature was built end to end in a single 200-message thread with a PM and a bot, and the PR was never read. Reviewers looked at the artifacts only.
- **Unsolved:** multiplayer social awareness (which human the bot should listen to), identity, authN/authZ. The current answer is to treat it like onboarding a human: scoped credentials that expand as trust grows.
- **Tan's minimal loop:** teach the agent to run the code itself (CPU traces, perf metrics, using the app as a user would). That closes the correctness loop. Getting good code by default is the engineer's new job, done through codebase guardrails.
- **Review token budgets.** Garry Tan says his GStack review step costs 30 to 50M tokens. Lauren pushes back: encode the checks in the codebase and static analysis. Cross-family adversarial review risks overfitting to feedback that ignores product intent.
- **Taste as a gate:** auto-fix and auto-merge are fine for bugs and maintenance (customer feedback is triaged, reproduced, fixed and shipped at 3am). User-facing pixel changes must reach internal product-market fit first, and mixed internal reception means no ship.

## Architecture & Optimization Mechanics
- **Context routing is the core primitive.** Splitting a "super bot" into specialist bots is a form of context sharding: smaller per-bot contexts, focused skills, and explicit message passing between bots in Slack. It is structurally close to MoE, with a human-legible router.
- **Token economics:** Lauren notes that frontier tokens are much more capable than last year's, and that today's small models beat last year's large ones. Cost per unit of intelligence is falling, but verification and review now dominate spend. That makes deterministic checks the highest-ROI optimization.
- **Bot-to-bot channels:** first-class, visible inter-agent chat (and YC's internal "Moltbook" of coding agents) beats hidden back-channels for auditability. A lead-engineer bot propagated user feedback to its sub-agents and behaved like a disciplinarian.

## Grounded Context (Web Enrichment)
Grok Bot launched from SpaceXAI with deep Cursor integration and is now built into X DMs. xAI's guides and InfoQ coverage confirm the agent and connector positioning and the customer-support use case. Lauren's PR counts ("2,000+ a month at the time of her viral talk, now over 4,000") are self-reported. A BAAI profile cited about 1,000 PRs in one month and roughly 3,000 over five months, so the trajectory is plausible but unverified. The claims about Jack Dorsey (Block as "an AGI for payments", collapsing to ICs, DRIs and player-coaches) and about an OpenAI agent-swarm incident are made in passing and were not independently checked here.

The reverse-hiring point raised elsewhere this week (SHL data on firms rehiring after AI layoffs because token costs exceeded salaries) is a useful counterweight. The Grok Bot team works with effectively unlimited tokens, and their economics do not carry over to SMBs automatically.

## Real-World Application / Actionable Step
- **Build a "Databot" for your research group first:** read-only access to experiment tracking (W&B or MLflow) plus your benchmark DB, living in Slack, answering questions like "what was the p99 latency of the 4-bit AWQ run on H100 vs the GPTQ run?". This is step 1 on the trust ladder with no write risk.
- **Specialist split for compression work:** one bot owns quantization regressions (it watches nightly evals and opens issues), one owns routing quality (it monitors router win-rate versus an oracle). Keep their contexts separate, the way you would separate experts.
- **Measure review spend:** log tokens spent on agent review per merged PR. Each time you add a static check, track how much it drops. That becomes your internal evidence for the inverted pyramid.

Sources:
- [xAI: Grok Bot for Engineering](https://x.ai/bot/guides/grok-bot-for-engineering)
- [xAI: Grok Bot customer support](https://x.ai/news/grok-bot-customer-support)
- [InfoQ: Grok Bot agent](https://infoq.com/news/2026/08/grok-bot-agent)
- [BAAI Hub profile of Lauren Tan](https://hub.baai.ac.cn/view/57615)
