# Salesforce: 231-Day Migration Done in 13 Days, 79% More PRs, 5% Fewer Incidents

**Source:** The Decoder (2026-05-30), Salesforce Engineering blog, @bcherny thread
**Raw:** [raw/rss/2026-05-30-the-decoder-salesforce-claims-ai-agents-cut-a-231-day-migration-to.md](../../raw/rss/2026-05-30-the-decoder-salesforce-claims-ai-agents-cut-a-231-day-migration-to.md) · [raw/twitter/2026-05-29-evening.md](../../raw/twitter/2026-05-29-evening.md) · [Salesforce blog](https://www.salesforce.com/news/stories/how-engineering-became-agentic/) · [The Decoder coverage](https://the-decoder.com/salesforce-claims-ai-agents-cut-a-231-day-migration-to-13-days-with-fewer-incidents/)

## TL;DR

Salesforce moved its entire engineering org to Anthropic's Claude Code with no token limits and published April 2026 numbers: **79% more pull requests per developer, 5% fewer incidents, one 231-person-day migration completed in 13 days (18x faster)**. One PR is reported to have delivered 21 endpoints at 100% test coverage. Boris Cherny (Anthropic, Claude Code lead) amplified the writeup as the canonical example of "the teams seeing the biggest wins from AI are completely changing how they work, not speeding up what they already do." The numbers cannot be independently verified — this is a vendor case study with a vendor partner amplification — but it is the first concrete enterprise-scale validation of yesterday's Dynamic Workflows release.

## Why this matters

Yesterday's digest treated Anthropic's Dynamic Workflows release (Claude writes a JavaScript orchestration script that fans out to up to 1,000 subagents with adversarial verification) as the production-grade realization of the "routing IS the policy" thread the wiki has been tracking through Conductor (Sakana), CaRE, MISA, and Cloud-Device. Today, Salesforce is the first large enterprise case study attaching a 79%-PRs / 18x-migration number to that release. The two posts compose: the runtime shipped on 05-28, and the customer case shipped on 05-30. The interesting claim is **simultaneous productivity AND quality gains** (incident rate dropped 5% while PR throughput rose 79%) — productivity-vs-quality has historically been framed as a tradeoff in engineering management, and the Salesforce framing rejects that.

## What is missing

- Independent verification. The numbers are Salesforce-reported on a Salesforce blog, amplified by Anthropic. Both have skin in the game.
- Selection bias: which teams adopted Claude Code first and whether those teams already shipped more PRs than the org median.
- Time horizon. April-2026 numbers are roughly the first full month of unlimited-token Claude Code deployment. Sustained behavior over 6-12 months is not in the writeup.
- The 231-day → 13-day migration is presented as one project. The class of migrations where the same speedup transfers is not characterized.
- The 21-endpoints-in-one-PR claim is the headline anecdote; the failure-mode distribution across PRs that *didn't* hit 100% coverage is not reported.

## Connections

- **Yesterday's Anthropic Dynamic Workflows release**: this is its first published customer case.
- **Marcus tokenmaxxing critique (05-29)**: Salesforce's "no token limits" policy is exactly the kind of consumption that the critique calls financially unsustainable in the long run. The case study is one data point on the productivity side of that ledger.
- **Cursor input-tokens-dominate report (05-29)**: as agents consume more context, input tokens become the majority cost. Salesforce's unlimited-token policy implies it absorbed that cost shift internally.
- **Bcherny on workflow target**: "big migrations and refactors are some of a team's most important work, and the easiest to push off to a better time." Salesforce's 231-day migration is exactly the workload profile Dynamic Workflows was advertised for.

## Industrial implication

If the numbers hold across other large enterprises, the migration backlog every large engineering org has been deferring becomes addressable. That changes who pays whom: Anthropic's revenue path (per yesterday's $47B run-rate figure) depends on enterprises spending more, not less, on per-developer tokens, and migration-backlog clearance is the workload that justifies that spend. Expect competitor labs (OpenAI Codex, Google Gemini Code Assist) to publish migration-velocity case studies within a quarter to defend the budget category.

## Related pages

- [Anthropic Opus 4.8 / Dynamic Workflows / Series H — 2026-05-29](2026-05-29-anthropic-opus-4-8-dynamic-workflows-65b-raise.md)
