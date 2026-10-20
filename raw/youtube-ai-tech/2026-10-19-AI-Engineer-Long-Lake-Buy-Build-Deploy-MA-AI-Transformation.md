# Buy, Build, Deploy: Using M&A to Drive AI Transformation (Prathik Naidu, Long Lake)

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=J7n3WJnFTto
**Domains:** ai-tech (primary), finance (secondary)

## TL;DR
Selling AI agents into enterprises from the outside is structurally bad business: the vendor eats the integration pain, fights for adoption, and then captures maybe a million a year while the client books five million in EBITDA that gets capitalized at 10x into 50 million of enterprise value. Long Lake's answer is to skip the vendor relationship entirely and buy the services business, then deploy AI as the owner. Ownership gives access to tacit knowledge, live task data with ground-truth labels, aligned incentives, inherited trust, and cash flow. Applied to a 70 trillion dollar services economy where every 100 dollars of new revenue normally costs 80 in labor, AI converts service economics toward software margins.

## Key Takeaways
- The three "walls" for outside-in AI vendors: security and legacy-integration review, driving adoption (whose job is it?), and monetization (tokens vs seats, price sensitivity as models commoditize).
- Value capture asymmetry is the core argument: a 1M/year contract that generates 5M/year EBITDA for the client creates roughly 50M in enterprise value for the client, not the vendor.
- Building an AI-native services firm from scratch avoids the capture problem but has no customers, no brand, and cannot hire niche expertise. Hospitals hand surgery-building design to the 20-year architecture partner, not an AI startup.
- Ownership flywheel: access to veterans with tacit knowledge, every business is a live RL environment with real edge cases and correctness signals, incentive alignment, inherited trust, and scale from existing cash flow.
- Services marginal economics: software keeps ~80 of every incremental 100 dollars, services keep ~20. AI breaks the labor-to-revenue coupling, producing operating leverage.
- Acquisition filter: customers trust the firm with end-to-end outcomes, human judgment is in the loop, and regulation imposes accountability. Not "draft a newsletter" but "own the urgent leak," not "extract data" but "own the tax decision," not "book a flight" but "handle the disruption."
- Deal funnel: ~5,000 deals seen per year, very tight filter. 40+ portfolio businesses, 55-person team, 7.5B raised (Elad Gil, General Catalyst, Alpha Wave, D1), 3 years old.
- Transformation follows a J-curve: upfront platform and workflow capture, then capacity unlock (same output, fewer hours), then the hard part of redeploying that capacity into growth and NPS. A reusable platform plus playbook compounds time-to-P&L across each new acquisition.

## Architecture & Optimization Mechanics
- **Deployment pattern, not a model story.** Naidu explicitly says the model is not the bottleneck. The bottleneck is organizational embedding, tacit knowledge, and accountability. This is the strongest version of the "last mile" thesis: intelligence is cheap, judgment and trust are expensive.
- **Owned businesses as RL environments.** Each acquired firm is a live environment with real tasks, real exceptions, and real answers on whether an agent got it right. That is a labeled dataset generated as a byproduct of operations, which outside vendors never see at full fidelity.
- **Platform plus playbook as the compounding asset.** The Nexus platform is reused across 40+ businesses, so each new acquisition inherits the agent deployment stack and the change-management playbook. The marginal cost of transforming business N+1 falls.
- **Monetization question dissolves.** Tokens vs seats, pricing erosion as alternatives cheapen, and ROI measurement all vanish when the vendor and the client are the same P&L.

## Grounded Context (Web Enrichment)
The Amex GBT deal mentioned as "recently announced" has already closed. Long Lake completed the all-cash take-private of Global Business Travel Group at 9.50 dollars per share (about 6.3B) around September 29, 2026. American Express sold its roughly 30 percent stake for about 1.5B, booking a pre-tax gain near 975M. Paul Abbott stepped down as Amex GBT CEO and moved to an operating partner role at Long Lake, with Drew Crawley taking over. Long Lake says customer contracts and service continue unchanged while its Nexus AI platform rolls out "behind the scenes," which commentators note is an ambition rather than a shipped capability at close.

The broader "AI roll-up" category is a deliberate General Catalyst program. GC allocated 1.5B from its fund for AI-enabled roll-ups starting late 2023 and has co-created at least ten such vehicles, including Eudia (legal), Titan (IT services), and Long Lake, which it calls the first expression of the concept. Lightspeed and Khosla are running similar plays in engineering services and healthcare. The 7.5B figure in the talk is capital raised across the platform; earlier PitchBook data (2025) showed 670M, so the scale-up has been fast and is driven heavily by deal-specific financing like Amex GBT. Treat the "services economics start to look like software" claim as a thesis, not a demonstrated result: no public margin data from Long Lake portfolio companies exists yet.

## Real-World Application / Actionable Step
- **For routing and inference work:** the "owned business as live environment" idea is directly usable. If you have any production agent, log the ground-truth correctness signal per task and treat it as a router training set. Cheap model first, escalate on failure, and let the operational data label which queries actually needed the expensive model.
- **For career and investment thinking:** the value-capture argument is a warning about being an AI vendor. If you build optimization tooling, the EBITDA lands in the customer's P&L. Either price on outcomes or own the outcome.
- **Finance angle:** AI roll-ups of services businesses (HOA management, architecture, corporate travel, legal) are now a venture-backed asset class with PE-style leverage. Watch for public comps and for whether Amex GBT margins actually move over the next 4 to 6 quarters before believing the "software margins for services" thesis.
