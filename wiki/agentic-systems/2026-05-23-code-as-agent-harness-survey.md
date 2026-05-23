# Code as Agent Harness: A Survey

**Source:** Twitter (curated retweet from @bayesiansapien → @burkov), 2026-05-21. arxiv link from retweet article.
**arxiv:** [2605.18747](https://arxiv.org/abs/2605.18747) · [ChapterPal walkthrough](https://www.chapterpal.com/s/3c994f49/code-as-agent-harness)

## TL;DR

LLMs have moved from producing standalone code to powering AI agents that plan over many steps, call external tools, keep track of changing state, and recover from their own errors during long-running tasks. Inside these systems, code has become the working material for almost everything: agents write small programs to reason through math, to drive a browser, to query a database, to test their own outputs, and to share intermediate work with other agents through files in a repository. This survey reframes "code as final answer" as the wrong frame: code is the agent harness, the substrate the agent reasons over and modifies.

## Why this matters

The wiki has tracked the harness-engineering thread independently in three places: the Ken Huang Compound Orchestrator article (Gmail starred today), the @_vmlops "Harness Engineering" tutorial repository (Twitter retweet today), and the Dive-into-Claude-Code design-space paper (04-17). The community has been converging on the same vocabulary — *harness* as the durable, project-local scaffolding that makes agent behavior reproducible. This survey ties the academic literature to that vocabulary.

The strongest framing in the abstract: "Existing surveys still treat code mainly as the final answer that a model produces." That is precisely the inversion the agentic-systems thread of the wiki has been making for the past month. Code is not output; it is the manipulation surface.

## Connections to prior wiki state

- [Dive-into-Claude-Code design space (2026-04-17)](2026-04-17-dive-into-claude-code.md) — first explicit wiki entry on harness as design surface.
- Ken Huang Compound Orchestrator (Gmail 2026-05-23, also covered in Daily-Digest agentic-ai feed) — practical recipe.
- @_vmlops harness-engineering retweet (2026-05-23 morning Twitter) — community tutorial.
- [SaaSBench (2026-05-21)](2026-05-21-saasbench-enterprise-saas-coding-agents.md) — testing harnesses against enterprise patterns.

This survey is the first published academic catalog of the design space that practitioners have been building in parallel.

## Gaps

A survey can only summarize. The interesting question (which harness primitives compose, and which don't) is necessarily empirical. The survey notes the categories: instructions agents read before touching anything, persistent state, verification gates that cannot be skipped, ownership tracking, review gates, README maintenance, compound learning folders. Whether the *order* of these primitives matters for reliability is the open empirical question.

## Research angle

If code is the agent's harness, then the harness itself is a learnable artifact. The next paper worth watching is one that lets an agent modify its own harness based on task feedback (the System-III self-regulation move from [SR^2AM (today)](./2026-05-23-sr2am-efficient-agentic-reasoning-self-regulated.md), applied at the harness level rather than the planning level).

## Raw source

[raw/twitter/2026-05-23-morning.json](../../raw/twitter/2026-05-23-morning.json) — article content captured via Twitter farmer.
