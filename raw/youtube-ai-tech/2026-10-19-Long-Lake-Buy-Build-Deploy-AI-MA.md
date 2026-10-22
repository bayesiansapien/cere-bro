# Buy, Build, Deploy: Using M&A to Drive AI Transformation (Prathik Naidu, Long Lake)

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=J7n3WJnFTto
**Domains:** ai-tech (primary), finance (secondary)

## TL;DR
Long Lake, a $7.5B-backed "applied AI holding company," argues that selling AI agents into enterprises is a losing game because the vendor eats all the deployment pain while the customer's P&L captures nearly all the value. Their alternative: acquire mission-critical services businesses outright, embed engineers inside them, and use AI to break the labor-scales-with-revenue curse so service margins start to look like software margins. Forty acquisitions in three years, capped by the $6.3B Amex GBT take-private.

## Key Takeaways
- **Three walls of outside-in deployment:** security review and legacy integration, driving adoption (whose job is it?), and monetization (tokens vs seats, ROI measurement). None of these are model problems. The models are fine.
- **The value capture asymmetry:** a $1M/yr agent contract that delivers $5M/yr EBITDA impact creates roughly $50M of enterprise value at a 10x multiple. The vendor sees $1M. The owner sees $50M. Ownership fixes this arithmetic.
- **Why not build from scratch:** no customers, no brand, no 20-year relationships. A hospital system hands a new surgery building to the firm it has trusted for two decades, not an AI architecture startup.
- **Five compounding advantages of ownership:** access to veterans with tacit knowledge, live task data with ground-truth labels, aligned incentives, inherited trust, and cash flow to reinvest. Together these form a flywheel: agents plus people act in live operations, generate real-world data, improve outcomes, repeat.
- **The services math:** software keeps ~$80 of every incremental $100; services keep ~$20 because delivery and overhead scale with headcount. That is an 80% marginal tax on growth. AI breaks the link between labor cost and revenue.
- **Target filter:** customer base that trusts the firm with end-to-end outcomes, real human judgment in the service, and regulatory accountability. Not "draft the HOA newsletter" but "own the urgent leak." Long Lake screens ~5,000 deals/year.
- **J-curve of transformation:** heavy upfront investment, then capacity unlock (same output, fewer hours), then the hard part: redeploying that capacity into growth, NPS, and revenue per employee. Stopping at "time saved" leaves the value on the table.
- **Playbook compounds:** the same platform and deployment ops team get faster at each new acquisition.

## Architecture & Optimization Mechanics
- **Data flywheel as the real asset:** each acquired business is a live RL environment with real tasks, real edge cases, and real correctness signals. This is the same argument Jediah Katz makes about harnesses feeding labs, but Long Lake keeps the data private. For an optimization researcher the implication is clear: proprietary trajectory data from a real operating business is worth more than any public benchmark for fine-tuning or distilling a domain-specific small model.
- **Capacity unlock is a routing problem:** "same output, fewer hours" means the agent handles the routine 80% and escalates the exception 20% to the veteran. Designing that escalation boundary is the same confidence-threshold routing problem as cheap-model vs frontier-model routing, just with a human as the expensive fallback.
- **Cheap intelligence, expensive accountability:** Naidu's framing that "the price of intelligence is rapidly declining, so what remains expensive?" is the services version of the inference cost curve. The scarce resource is no longer tokens, it is liability and trust.

## Grounded Context (Web Enrichment)
The Amex GBT deal is real and has closed. Long Lake agreed in May 2026 to pay $9.50/share in cash (about 60% premium), roughly $6.3B, with equity from existing investors plus Koch Equity Development and debt from JPMorgan, BofA, Citi, and MUFG. Shareholders holding ~69% (including American Express, Expedia, QIA, BlackRock) pre-committed. Approval came in August and the stock has delisted from the NYSE. Amex GBT called it "the world's first AI take-private deal" and it was Long Lake's 35th acquisition at the time; Naidu's "40 businesses" figure is consistent with subsequent deals. Long Lake was founded in 2023, matching the "about 3 years ago" claim.

The weak spot in the talk is the unstated assumption that AI-driven margin expansion survives contact with regulated, judgment-heavy services. The pitch deck J-curve has no numbers attached, and no portfolio company P&L was shown. The thesis is directionally sound (YC and others have been pushing "AI-native services" for a year), but Long Lake is levered on bank debt against a services business whose labor it intends to compress. If the capacity unlock stalls at "time saved" rather than converting to revenue, the leverage cuts the other way.

## Real-World Application / Actionable Step
- **For compression/distillation work:** the most valuable distillation target is not a public benchmark but a captured operating workflow with ground-truth outcomes. If you can get access to a services-business trace dataset (even synthetic, modeled on one), distill a small model against it and measure how the escalation rate to the "veteran" falls as the student improves. That escalation rate is the business metric.
- **For routing:** model the human expert as the most expensive tier in a routing cascade. The confidence threshold that triggers escalation is the knob that converts "time saved" into "revenue per employee." Instrument it.
- **Investment angle:** watch for Long Lake's next leveraged deals and any portfolio disclosures. The AI-services roll-up thesis will either print margin expansion in 2027 or show up as distressed debt. Either outcome is informative.
