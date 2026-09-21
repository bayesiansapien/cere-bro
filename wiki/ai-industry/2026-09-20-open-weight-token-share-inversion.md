# The token/revenue split: open weights took 78.4% of the volume and 5% of the money

**Date:** 2026-09-20
**Topic:** ai-industry
**Source:** Vercel AI Gateway data, reported on the X home feed ([@MelvinInvests](https://x.com/MelvinInvests/status/2101363203381006778), [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2101432372923363367))
**Raw:** `raw/twitter/feed/2026-09-20-morning-ranked.json`

---

## TL;DR

Usage data from Vercel's AI Gateway, a router that sits in front of many model providers and
therefore sees a real cross-vendor traffic mix, shows a split that has gone from notable to
structural in three months.

**By token volume:** open-weight models **78.4%**, closed models **21.6%**. In June the open share
was roughly 40%, so it has nearly doubled in one quarter. **DeepSeek V4.1 Flash alone is 59.3% of all
tokens crossing the gateway.** Claude Opus 4.8 and Claude Sonnet 5 are 1.7% each.

**By spend, the picture inverts.** Claude Opus 4.8 takes **13.7% of dollars on 1.7% of tokens**.
Anthropic's five listed models together take **36.9% of total spending**. DeepSeek V4.1 Flash moves
most of the tokens and collects **5.1% of the spending**.

So the two businesses are no longer the same business. Open weights own the volume tier; closed
models own the revenue tier by charging roughly an order of magnitude more per token for the work
people will not delegate downward.

---

## Why this is a routing result, not just a market result

This is the clearest production-scale confirmation to date of the premise every paper on
[the routing page](../ai-routing/llm-routing.md) assumes and none of them measures: **that real
traffic is sharply separable into a large cheap tier and a small expensive tier, and that operators
will act on the separation once the cheap tier is good enough.** A gateway is a router. The 78.4/21.6
volume split against the 5.1/36.9 spend split is an empirical picture of what a large population of
developers decided the value-of-information trade actually is, without anyone writing the objective
down.

It also sharpens a distinction the wiki has been sloppy about. Most routing papers optimise
accuracy per dollar on a benchmark. This data says the deployed behaviour is closer to a **floor**
than an optimum: send everything to the cheap model unless the task is one you have already decided
needs the expensive one. That is a much coarser policy than any router in the literature, and it is
capturing most of the available saving. The marginal value of a sophisticated router is whatever is
left after the coarse policy runs, and nobody has measured that residual.

**One vendor at 59.3% of volume is its own risk finding.** A gateway whose traffic is majority one
open model is not a diversified open ecosystem, it is a single point of dependence with a permissive
licence. The usual argument for open weights is that you can self-host, fine-tune and move clouds.
That argument holds for the licence and not for the concentration.

---

## What it does to the industry thread

**It gives Lambert's compute-allocation worry a mechanism.** [The RSI entry
(09-20)](../agentic-systems/2026-09-20-scientisttwo-recursive-self-improvement.md) records Nathan
Lambert arguing that frontier labs may not be able to hold a constant share of compute on internal
R&D as volume grows, especially under IPO scrutiny. If the volume tier is migrating to open weights
while the revenue tier holds, then the labs' revenue is increasingly concentrated in a narrow band of
hard tasks. That is a higher-margin business and a smaller one, and it is more exposed to the open
models improving by one notch than a volume business would be.

**It reframes the week's regulation fight.** Today also brought a class action in California federal
court alleging that the September 12 call for industry-wide coordination to limit AI progress, plus
same-day supportive statements from three rival labs, constitutes a Section 1 Sherman Act restraint
on output. The most-shared framing on the feed connects the two directly: the argument runs that a
slowdown pact conveniently freezes the capability gap at the moment open models are closing it from
below. That is a motive claim and not evidence, and it should be labelled as such. The gateway data
is evidence about market structure; the inference about intent is commentary.

**It is consistent with the decision-model story.** The other dominant thread today,
[the Jev ecosystem census (09-20)](../ai-routing/2026-09-20-jev-ecosystem-census-72h.md), is 160
projects built in 72 hours around pushing the cheapest class of decisions off the frontier model
entirely. Same direction, one tier further down: first the bulk generation moves to open weights,
then the bulk *decisions* move to a model that does not generate at all.

---

## Gaps

One gateway is one population. Vercel's users skew toward web and agent developers building
cost-sensitive products, which is exactly the population most likely to route downward, so the 78.4%
is an upper bound on the general market rather than an estimate of it. Token volume is also a poor
proxy for work done: reasoning models emit many internal thinking tokens per unit of output, so a
share measured in tokens flatters whichever models think longest. No per-task or per-request
breakdown is published. And the June comparison point is quoted without a source, so the doubling
claim rests on the same single report.

---

## Related pages

- [LLM routing](../ai-routing/llm-routing.md)
- [Compute economics](../hardware/compute-economics.md)
- [Jev ecosystem census (09-20)](../ai-routing/2026-09-20-jev-ecosystem-census-72h.md)
- [ScientistTwo and the RSI argument (09-20)](../agentic-systems/2026-09-20-scientisttwo-recursive-self-improvement.md)
