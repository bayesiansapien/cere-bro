# How 21 People Built a $100M+ Agent Company | Quinn Slack, Amp

**Channel:** AI Engineer
**Published:** 2026-11-25
**Source:** https://www.youtube.com/watch?v=Xyb1Bn_L2U4

## TL;DR
Amp spun out of Sourcegraph with 21 people and, because of the legal spin-off, **couldn't hire or grant options for a year**. Slack says that constraint pushed them into an agent-native operating model: no PMs, no Jira, no support desk, no mandatory PR review, one meeting a week, and everyone talks to customers. He claims **>$100M ARR, profitable, and 40 to 50x more revenue per dollar of cost** than traditional software companies. The product is "basically 100% built with AI." The thesis: feature-level differentiation is dead because competitors' agents copy features in weeks. SaaS's sales-led, 10-year-renewal model is breaking, and teams two orders of magnitude smaller, where everyone has large equity, will win.

## Key Takeaways
- **Enterprise-readiness is a trap.** Optimizing for the median enterprise buyer's checklist makes the product obsolete in about 3 months. Stay on the frontier and win developers' love.
- **No sustainable feature moat.** Orbs (cloud agents) and multiplayer threads can be copied once proven. Adam Wathan's praise ("you can't understand why it's good until you use it") is the only real marketing.
- **Everything happens in the agent.** Threads replace tickets, support and chat. A shared thread lets you pull in a teammate mid-task, which local agents can't do.
- **Risk reduction by pushing *more*:** tiny increments, add logging first to check the agent's model of the system, let the agent monitor for an hour, then push again. Run shadow systems side by side to diff outputs.
- **Agent-provable correctness:** frame-by-frame visual diffs to kill UI jitter (no human would have that patience), and lots of parallel variants (for example 9 waveform designs) instead of serial one-change requests.
- **Closed-loop bug handling:** Fix with an agent, email an apology plus free credits, then mine logs for *everyone else* who hit the same error (the "17 others") and proactively notify them. That builds a feedback flywheel.
- **Dictation** is the highest-bandwidth path from brain to agent (and an argument for remote work).
- **Build-vs-buy flips.** They built their own CRM. You use about 2% of Salesforce, and an agent can build that 2% plus perfect integrations. An SDR built their ACH wire-payment flow himself.
- **Org design:** 1/21 equity "skin in the game," "follow your energy," with weekends included. His closing advice: "Get out of the cage."

## Architecture & Optimization Mechanics
- **Shadow systems are the production analog of differential testing.** The pattern shows up in three talks this week (Sumner's three-way JIT/AOT diff, Lance Martin's Lean oracle, Slack's shadow runs). For a routing system: shadow-route 100% of traffic through a candidate cheap model, diff against the incumbent's outputs offline, and promote per query class only when divergence is below threshold. Nothing user-visible ships until the shadow diff is clean.
- **Parallel variant generation is a throughput and latency trade:** fire N cheap generations and choose, instead of serial expensive turns. That's best-of-N at the product level and a natural fit for routing to cheap models.
- **Unit economics:** A 40 to 50x efficiency claim at >$100M ARR implies an inference bill that dominates COGS. Any reseller-of-tokens agent company lives or dies on routing and caching margin.

## Grounded Context (Web Enrichment)
Verified: Amp announced its spin-out from Sourcegraph on **Dec 2, 2025** as an "independent research lab." Dan Adler became Sourcegraph CEO, Slack and Beyang Liu stayed on Sourcegraph's board and co-founded Amp Inc., and Amp stated it was **profitable** at the split, with about 20 people. Slack has previously argued publicly against mandatory code review. **Not verified:** the ">$100M ARR" and "40 to 50x" figures. I found no independent or reported Amp ARR number, only an aggregator estimate of about $50M 2025 revenue for Sourcegraph as a whole. Treat the headline as the CEO's own claim at a recruiting-flavored talk. Also note survivorship bias: no-review, push-constantly works with 21 high-equity senior people on a dev-tool product. It's unproven for regulated or safety-critical software.

## Real-World Application / Actionable Step
- **Steal the shadow-route pattern for your LLM router this week.** Log 100% of production queries to a shadow path on the cheap candidate model, auto-diff with an LLM judge plus exact-match checks per query cluster, and publish a daily per-cluster "safe-to-route" table. Promote a cluster only after 7 days below the divergence threshold. That turns routing rollout from a risky bulk switch into an agent-monitored incremental push.
- Personally: start dictating to agents for design and spec prompts. It's the cheapest bandwidth gain available.

Sources: [Amp: Amp Inc. announcement](https://ampcode.com/news/amp-inc), [Sourcegraph: why Sourcegraph and Amp are becoming independent](https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies), [Tessl: Sourcegraph spins out Amp](https://tessl.io/blog/sourcegraph-spins-out-ai-coding-agent-amp-as-a-standalone-company/), [StartupHub: Amp killed mandatory code review](https://www.startuphub.ai/news/quinn-slack-amp-killed-mandatory-code-review), [Contrary Research: Quinn Slack](https://research.contrary.com/report/quinn-slack-everything-downstream-of-the-coding-agent), [Amp Frontier Corporation](https://ampcode.com/news/amp-frontier-corporation)
