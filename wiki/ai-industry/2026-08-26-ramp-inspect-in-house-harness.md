# Ramp's Inspect: a non-AI company builds its own harness and writes 75% of its PRs with it

**Source:** Gergely Orosz, [The Pragmatic Engineer, "Why Ramp built its own in-house coding agent, Inspect"](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect) (2026-08-25) · [raw](../../raw/rss/2026-08-25-pragmatic-engineer-why-ramp-built-its-own-in-house-coding-agent-inspect.md)

---

## TL;DR

Ramp, a fintech, built its own background coding agent called Inspect. **75% of merged PRs at Ramp are now raised by Inspect**, up from ~60% two months after launch, and the system crossed **one million total sessions** in July. Engineers are free to use anything they want, so that share is a revealed preference rather than a mandate. Ramp is not alone: Block has Goose (open source), Stripe has Minions, Shopify has River. Orosz's framing is the one that matters for this wiki: the "buy, don't build" convention that governs almost all developer tooling **appears not to apply to AI harnesses**, and a non-frontier-lab company was able to build tooling more effective for its own engineers than what the frontier labs ship.

---

## What Inspect actually is, and why they built it

Inspect is a background coding agent running on **remote sandboxes** with access to most of Ramp's internal data sources, which verifies its own backend and frontend changes on the remote machine before handing them over. Stack: React/Vite front end, Cloudflare Durable Objects, SQLite, Cloudflare Agents SDK, Modal sandboxes. Inside each sandbox: OpenCode, real development services (Postgres, Redis, RabbitMQ, Temporal), Chromium, and VS Code Server — with enough engineering on cold-start that sandboxes spin up in **five seconds or less**.

Three reasons they did not just use Claude Code, Codex or Cursor:

1. **Local machines cap concurrency.** They liked Claude Code on day one but could only run one or two sessions locally. They wanted many agents in parallel, which needs remote execution.
2. **Frontend tooling was inadequate**, and the original goal was letting designers make small UI changes themselves.
3. **They needed remote dev environments anyway** as system complexity grew, for work at the intersection of services: backward-compatibility debugging, broken API contracts.

The differentiators Orosz identifies are both about closing the loop rather than about the model. **Internal integrations**: Inspect has the same tools and context a Ramp engineer has, so "the only constraint on agents' ability is model intelligence, not missing tools or access." **Verification**: it runs tests, reads telemetry, and queries feature flags for backend work, and for frontend work it visually verifies by producing screenshots and live previews. Ramp shipped screenshot verification nearly a year before third-party vendors supported it. Third-party harnesses still largely cannot do telemetry- or feature-flag-based verification out of the box, because they have no path to a specific company's internal systems.

One organizational detail is unusual enough to note: **all Inspect sessions are public and open to collaboration, with no opt-outs allowed**, and more than 150 people at Ramp have contributed to the project.

---

## Relation to prior wiki pages

**This is the industrial confirmation of the periodization [agent-harness-engineering](../agentic-systems/agent-harness-engineering.md) recorded from Ken Huang on 08-14: model as product → wrapper as product → harness as product boundary.** Ramp is what the third phase looks like from the buyer's side. The company is not building a model or reselling a wrapper; it is treating the harness as the thing that has to be owned, because the harness is where its proprietary context lives. That is a stronger version of the claim than the salary evidence that page currently leans on (Forward Deployed Engineers at ~$1M/year, Anthropic at $750k+ for harness and loop skill). Salaries show the market pricing the skill. Ramp shows the market deciding the artifact cannot be bought.

**It supplies the missing explanation for why the harness is not a commodity, and the answer is verification, not orchestration.** [agent-harness-engineering](../agentic-systems/agent-harness-engineering.md) records the *Agent Safety Should Be a Runtime Contract* argument (arXiv 2608.11274, 08-13) that a harness has a preventive face and an **evidential** face: no task-complete claim without checkable proof — test runs, log captures, file diffs, citation grounding. Ramp's entire competitive advantage over Claude Code, in Orosz's telling, is exactly this evidential face: telemetry reads, feature-flag queries, screenshot verification. A vendor harness cannot supply evidence about a system it cannot see. So the part of the harness that is genuinely non-portable is the verification layer, and the parts research has shown to be highly portable — [Meta-Harness's (08-25)](../agentic-systems/2026-08-25-meta-harness-code-space-optimization.md) discovered math-retrieval harness adding 4.7 points across five held-out frontier models zero-shot, [AutoDesign's (08-14)](../agentic-systems/2026-08-14-autodesign-meta-harness-optimization.md) DesignHarness lifting seven other code-agent-model configurations from 54.99 to 67.39 — are the context and control-logic parts. **That is a clean split the wiki did not have: harness structure is portable, harness evidence is not.** It predicts the market shape, which is vendors selling optimizable structure and companies building their own verification.

**It confirms rules 1 through 4 of [today's Gradient Flow essay](../agentic-systems/2026-08-26-nine-rules-for-agents.md) with a production instance.** Lorica's rule 4 says design for recovery and verification rather than a flawless first pass, and measure recovery separately from first-attempt accuracy. Inspect's design is that rule taken literally: the agent's job is not to be right, it is to be able to check. Lorica also reports an 18 percentage point spread between the best and worst harness configuration for the same open model. Ramp's 60% → 75% PR share across two quarters, on a harness they kept improving, is the longitudinal version of that spread inside one organization.

**On the cost axis it is a gap, not a data point.** [compute-economics](../hardware/compute-economics.md) argues cost-per-completed-task is the only unit in which efficiency effects are commensurable, and [agent-harness-engineering](../agentic-systems/agent-harness-engineering.md) has carried open problem 0 since its creation: nobody has put harness optimization and fine-tuning on one cost axis for equal capability gain. Ramp reports one million sessions, 75% of merged PRs, and five-second sandbox spin-up, and reports no dollar figure for any of it. The most valuable number in this story is the one not in it: **what a merged PR costs at Ramp, against what it cost before Inspect.** A company with a million sessions of telemetry certainly knows.

---

## Related pages

- [Agent harness engineering](../agentic-systems/agent-harness-engineering.md)
- [Nine practical rules for agents (08-26)](../agentic-systems/2026-08-26-nine-rules-for-agents.md)
- [Compute economics](../hardware/compute-economics.md)
- [Token price is not task cost (08-14)](2026-08-14-alphasense-token-price-vs-task-cost.md)
