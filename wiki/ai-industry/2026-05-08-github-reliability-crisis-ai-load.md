# GitHub Reliability Crisis: AI Load Breaks the Platform

**Source:** [The Pulse: AI load breaks GitHub, why not other vendors? — Pragmatic Engineer (Gergely Orosz)](https://newsletter.pragmaticengineer.com/p/the-pulse-ai-load-breaks-github-why) — Gmail starred 2026-05-07
**Tier:** 1 — AI industry / infrastructure / developer-platform reliability

## TL;DR

GitHub's reliability has collapsed to **86% uptime over 90 days** (third-party tracker), with multiple data-integrity incidents, a 6-hour Elasticsearch outage that hid pull requests and issues, a critical security disclosure (Wiz: any actor could git-push to all repos via a single command before the patch), and Mitchell Hashimoto (HashiCorp founder, Ghostty maintainer) publicly leaving GitHub after 18 years citing daily outages blocking his work. CTO Vlad Fedorov blames "AI agent-fuelled load spike." This is the second AI-infrastructure stress story of the week alongside Anthropic's [Colossus 1 capacity-crunch](2026-05-08-anthropic-colossus-deal-capacity.md) deal.

## The reliability collapse

| Metric | Value |
|---|---|
| Third-party tracker, 90-day average | **85.51% uptime** ("zero nines") |
| Last month, third-party measurement | 90% (one nine) |
| Effective downtime per day | 2-3 hours (averaged over 90 days) |

Concrete incidents in the past week alone:

- **Thursday 23 April: Data integrity incident.** PRs merged via the merge queue using squash merge produced incorrect merge commits when the merge group contained more than one PR. Commits were silently *lost* in the merged code. **2,092 pull requests affected**, including at Modal and Zipline. Customers had to manually untangle and recover lost commits with zero help from GitHub. The integrity-promise broke.
- **Monday 27 April: 6-hour Elasticsearch outage.** PRs and issues disappeared from the web UI for 6 hours. The cluster overloaded.
- **Tuesday 28 April: Wiz critical security disclosure.** Bad actor could get access to all repositories on GitHub and GitHub Enterprise via a single `git push`. GitHub fixed `github.com` in 6 hours; Enterprise servers that didn't update remain vulnerable.
- **Tuesday 28 April: GitHub Actions problems.**
- **Wednesday 29 April: Incomplete pull requests in repositories.**

Direct quote from Can Duruk (Modal engineer):
> "The COO going out of their way to find a huge denominator to make the impact appear small feels very dishonest; versus a sincere apology about how this invalidates their entire promise to their customers. We had to dig into their status page about this to even realize they just casually f***ed up our repo."

## Mitchell Hashimoto leaving

> "The past month I've kept a journal where I put an 'X' next to every date where a GitHub outage has negatively impacted my ability to work. Almost every day has an X... I want to be there, but it doesn't want me to be there. I want to get work done and it doesn't want me to get work done... After 18 years, I've got to go."

Hashimoto is moving Ghostty (his current main project) off GitHub. The cultural-influence weight of the HashiCorp founder publicly quitting GitHub for reliability reasons is the signal Pragmatic Engineer is foregrounding.

## CTO's explanation: AI agent-fuelled load

Vlad Fedorov (GitHub CTO) attributes the load spike to **AI coding agents** as a class. The implicit thesis is that Codex, Claude Code, Cursor, Aider, and the broader agent-coding ecosystem are pushing read+write traffic at a rate the platform's existing capacity cannot absorb.

This is **the same root cause** as the [Anthropic-Colossus capacity-crunch](2026-05-08-anthropic-colossus-deal-capacity.md): AI workloads are stressing the underlying infrastructure faster than the providers can scale. Anthropic responded by leasing the worst-environmental-record data center in the industry. GitHub responded by... not yet visibly. The two stories together are the wiki's first cluster on AI-infrastructure-under-stress.

## How this relates to prior wiki work

- **Direct continuation** of [Pragmatic Engineer GitHub-Anthropic trust](2026-05-01-pragmatic-engineer-github-anthropic-trust.md) (05-01). Pragmatic Engineer has been tracking GitHub-trust signals for two weeks.
- **Cross-source cluster** with today's [Anthropic-Colossus capacity-crunch](2026-05-08-anthropic-colossus-deal-capacity.md). Both are AI-load stress stories, both are this week, both are sourced from Pragmatic Engineer.
- **Lateral to the [Pulse: did capacity shortages turn Anthropic hostile](https://newsletter.pragmaticengineer.com/p/the-pulse-did-capacity-shortages)** (also Pragmatic Engineer, also today's RSS). Two Pragmatic Engineer pieces in one week, both on AI-infrastructure stress at major platforms. One pattern, two vendors.

## What's surprising

The GitHub CTO **named AI agents as the cause publicly**. That is unusual candor for an outage post-mortem. It implicates the entire developer-AI-tools market as the load source, not specific bad actors. The implicit claim is that the platform's capacity-planning model assumed human-rate request volume, and agents have invalidated that assumption.

## Worth Watching

- **Will GitHub introduce per-agent rate limits?** Falsifiable in 60 days. If yes, it changes the cost structure for every coding-agent product.
- **Will any major customer move to GitLab / Forgejo / Codeberg?** Hashimoto is the first publicly-named departure. If a Fortune-500 follows within 90 days, the platform-trust story is real, not anecdotal.
- **Will the GitHub-vs-Anthropic-Colossus pattern extend to a third platform?** If a third major AI-infrastructure provider (Vercel, Cloudflare, AWS) reports similar stress within 30 days, the wiki should treat AI-infrastructure-saturation as a Tier 1 industry trend, not isolated incidents.

## Action

Surface this in today's digest as a Tier 1 industry Deep Dive paired with the Anthropic-Colossus story. The two together are the cluster.
