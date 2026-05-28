# Simon Willison: Anthropic and OpenAI Have Found Product-Market Fit

**Date ingested:** 2026-05-28
**Source:** Simon Willison's blog (RSS)
**Links:** [Post](https://simonwillison.net/2026/May/27/product-market-fit/) · [raw](../../raw/rss/2026-05-27-simon-willison-i-think-anthropic-and-openai-have-found-product-market.md)

## TL;DR

The wave of "Uber's AI budget blew up" stories is, on closer reading, the opposite story. Willison argues that Anthropic and OpenAI have found product-market fit through enterprise coding agents, and the price-shock stories are the predictable consequence of switching enterprise pricing from heavily-discounted seats to API-token costs. Anthropic flipped to $20/seat plus API usage in November 2025 (existing customers learning about it as they renew); OpenAI Codex moved Plus/Pro/Enterprise to per-token billing on April 2 2026. GPT-5.5 (April 23 release) is 2x the API price of GPT-5.4, Opus 4.7 is roughly 1.4x Opus 4.6 once you correct for the new tokenizer. Willison's own ccusage tool shows his personal $200/month spend would have been $2,180 at API prices for one month of Claude Code + Codex. He calls April 2026 a new inflection point and pegs the moment as the start of the labs making real revenue rather than the burn-the-stockpile previous regime.

## Key findings

- Anthropic Enterprise switched to $20/seat + API pricing in November 2025 per their spokesperson, surfacing at renewal time.
- OpenAI Codex moved Plus/Pro/Enterprise plans to per-token (in "credits" that match API prices) on April 2 and April 23 2026.
- GPT-5.5 is 2x the API price of GPT-5.4; Opus 4.7 is roughly 1.4x Opus 4.6 after the tokenizer change.
- Willison's ccusage shows $2,180/month equivalent API usage for $200 paid out-of-pocket: heavy users are massively subsidized at the consumer plans.
- "Uber maxed out its annual AI budget in months" looks like product-market fit working: the customer sucked air through their teeth and said yes anyway.
- The SpaceX S-1 shows Anthropic committing $1.25B per month through May 2029 for Colossus compute, likely inference, not training.
- OpenAI is hiring 32.6% enterprise-sales roles (229 of 703 openings); Anthropic 26.9% (105 of 390). Both labs are shifting headcount mix toward enterprise revenue.

## How this fits prior wiki state

This is the cost-discipline cluster's industry-side counterweight. Yesterday's TL;DR opened with "the bill came due" and listed five papers about agent waste plus Gary Marcus's bubble piece on Uber. Willison's response on the same Uber data is that the bill is the product working. Both stories can be true: agents waste 50% of their tokens AND companies are paying anyway because the marginal value beats the cost. The April 2026 inflection point Willison flags is the moment those two facts started showing up in lab P&L.

Also strengthens the Anthropic/AWS/Colossus thread from earlier this month ([[2026-05-08-anthropic-colossus-deal-capacity]], [[2026-05-21-anthropic-profitability-spacex-deal-ipo]]). The new $15B/yr Colossus commitment is the largest single-vendor compute spend on record.

## Related pages

- [[2026-05-27-agent-token-consumption]], token economics paper from yesterday
- [[2026-05-21-anthropic-profitability-spacex-deal-ipo]], Anthropic profitability + Colossus
- [[2026-05-23-anthropic-glasswing-mythos-vulnerabilities]], Anthropic frontier model

## Research angle

The relevant research question for the next quarter is whether the per-token enterprise pricing creates a strong incentive for customer-side cost-discipline tooling (ESR-style trajectory truncation, AKBE-style tool-call discipline, Efficiency-Frontier-style strategy switching). If yes, the cost-research papers from this week are not academic curiosities; they are pre-production tooling that enterprises will pay for to bring their token bills down. That implies a near-term enterprise market for "AI cost governance" tools, parallel to the existing FinOps market for cloud.
