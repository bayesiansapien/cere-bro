# Why Buying Companies Beats Selling Them AI | Prathik Naidu, Long Lake

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=J7n3WJnFTto

*Conference talk. Long Lake is an applied-AI holding company (~3 years old, 55 staff, 40 acquired businesses). Secondary domain: finance.*

## TL;DR
Selling AI into enterprises hits three walls: deployment (security, legacy integrations), adoption (whose job is it?), and value capture (a $1M/year AI contract may create $5M/year EBITDA for the client, worth ~$50M at 10x, almost none of which the vendor keeps). Building an AI-native services firm from scratch solves value capture but lacks customers, brand and domain experts. Long Lake's answer is to buy mature services businesses (HOA management, architecture, HR, now corporate travel via the $6.3B Amex GBT take-private) and deploy AI from the inside. Services keep about $20 of every $100 of new revenue versus about $80 for software; AI breaks the link between revenue and headcount so services economics start to look like software. The value shows up as a J-curve: investment, then capacity, then P&L only once freed capacity is redirected into growth.

## Key Takeaways
- **Org charts lie.** Real decisions sit in webs of veterans with decades of tacit knowledge; outside vendors cannot see them.
- **Systems of record are not enough.** CRMs, ticketing and SOPs miss exceptions, edge cases and the quick questions asked to the expert. That is where the work actually happens.
- **Value capture math:** $1M contract, $5M EBITDA uplift, ~$50M enterprise value at 10x, all accruing to the client.
- **Why ownership works:** access to the people doing the work; live environment data with real outcomes for training agents; incentive alignment; inherited trust and brand; scale and cash flow from day one. These compound into a flywheel.
- **Market size:** software sells tools to people doing the work; services (roughly $70T globally) sell the work. Owning outcomes is the bigger prize.
- **Services margin tax:** ~80% of incremental revenue goes to delivery and overhead, so many founders stop chasing growth.
- **Selection filter:** customers trust the firm with end-to-end outcomes; real human judgment in the service; regulatory accountability. Intelligence gets cheap; accountability stays expensive. Examples: handling an urgent leak (not drafting an HOA newsletter), taking responsibility for a tax decision (not extracting data), handling flight disruptions (not booking).
- **Funnel:** ~5,000 deals screened per year, tight filter.
- **J-curve:** build platform and capture workflows, then adoption and time savings, then convert capacity into growth, NPS and revenue per employee. Stopping at time savings creates no P&L.
- **Capital:** $7.5B raised (Elad Gil, General Catalyst, Alpha Wave, D1 and others).

## Architecture & Optimization Mechanics
- **The owned business is an RL environment.** Real tasks, real edge cases, ground-truth outcomes. This is the data moat outside vendors lack, and it is the same insight behind labs paying for expert-curated environments.
- **Capacity is not savings.** Efficiency gains (faster inference, cheaper models, pruning) only show up in a P&L if someone redeploys the freed capacity. True for internal ML infra teams too.
- **Platform reuse:** a shared agent platform across 40 companies cuts time-to-deploy for each new acquisition, the same amortization logic as a shared inference stack.

## Grounded Context (Web Enrichment)
The Amex GBT deal is real but not recent: announced 4 May 2026, all cash at $9.50 per share (a 60.2% premium), valued at about $6.3B, financed by Long Lake equity plus Koch Equity Development and committed debt from JPMorgan, BofA, Citi and MUFG (JPMorgan marketed about $6B of debt). Holders of ~69% of shares, including American Express (~30% stake, $1.5B cash and a $975M pre-tax gain), Expedia, QIA and BlackRock, signed voting agreements; close is targeted for H2 2026. It is Long Lake's first take-private ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/amex-gbt-agrees-6-3-163512714.html), [Financier Worldwide](https://www.financierworldwide.com/long-lake-agrees-63bn-take-private-acquisition-of-amex-gbt), [Skift](https://skift.com/2026/05/04/amex-gbt-deals-ownership-saga-winners-losers/), [KuCoin/Bloomberg](https://www.kucoin.com/news/flash/jpmorgan-markets-6b-debt-for-american-express-global-business-travel-take-private-deal)).

The thesis is a rebrand of the roll-up model (Constellation Software, Danaher) with AI as the operating lever. The talk shows no P&L results from the 40 businesses, only the J-curve shape. The risks it skips: roll-ups often fail on integration and overpaying, and a debt-funded $6.3B travel deal is a leveraged bet that AI can cut servicing costs faster than interest accrues. If model costs keep falling, competitors without the acquisition debt get the same AI at lower cost.

## Real-World Application / Actionable Step
- **Value-capture lens for your own work:** when proposing a routing or compression project internally, frame ROI as capacity redeployed (more queries served, new products enabled), not just GPU cost saved. That is what shows up in the P&L.
- **Investing:** the "AI-enabled roll-up" model is investable in public markets via serial acquirers of services and vertical software (e.g. Constellation, Topicus, Indian IT services firms with platform plays). Track revenue per employee, not AI announcements; it is the single number that tests this thesis.
- **Career optionality:** applied-AI holdcos (Long Lake, General Catalyst's roll-up vehicles) are hiring engineers to deploy inside owned businesses. This gives access to real outcome data, which is rare for model-efficiency research.
