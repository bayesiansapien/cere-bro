# Behind-the-meter power: 75GW of binding orders, and the execution risk nobody prices

**Source:** SemiAnalysis, 2026-09-10 · [Post](https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the) · [raw](../../raw/rss/2026-09-10-semianalysis-what-is-so-hard-about-behind-the-meter-power-for-datace.md)

## TL;DR

Behind-the-meter power means generating electricity on the datacenter site rather than drawing it from the grid, and a year ago SemiAnalysis was close to alone in calling onsite gas generation the primary way AI labs would solve their power constraint. Critics called it "science experiments," "Dark Gigawatts," and "literally the dumbest thing that human beings have ever attempted to do." The scoreboard now: their Energy Model tracks **75 GW of firm, binding orders** for behind-the-meter AI compute, of which roughly **20 GW were ordered in Q2 2026 alone**. This counts binding OEM orders tracked at project level, explicitly excluding the speculative announcements other analysts fold in. By end of 2026, about **3 GW of operational US datacenter IT capacity will be powered behind the meter**, with multiple straight years of triple-digit growth to follow. Part 1 focuses on the execution risk between a firm order and a delivered project, which is where the remaining uncertainty actually lives.

## Who has committed what

- **Microsoft**: over 5 GW of behind-the-meter nameplate capacity signed year-to-date in 2026, including 2.7 GW with Joulent and Chevron and well over 2 GW through turnkey leases with firms like Crusoe.
- **Google**, historically the most reluctant on onsite gas: 930 MW of off-grid aeroderivative turbines at an Armstrong County flagship campus, plus 900 MW of Bloom Energy fuel cells in Wyoming paired with more than 1 GW of Mitsubishi J-class turbines.
- **Anthropic and Meta**: each 300-500 MW with Enchanted Rock, whose product is 0.5 MW gensets built around a 21.9-litre V12 gas engine. Anthropic's Texas flagship, backstopped by Google, adds over 1.5 GW of off-grid generation.
- **OpenAI**: imminent operations at a 1.4 GW IT-capacity off-grid campus in Shackelford County, Texas, running **over five hundred 4.25 MW Jenbacher J624 engines**. Combined with a 1.3 GW New Mexico site, that underpins over **$150B of contracted spending signed with Oracle** that depends on behind-the-meter power.

## Key points

- **The consensus flipped inside twelve months**, which is the piece of information with the most forward value. A technique dismissed as an Elon Musk eccentricity is now standard practice at every hyperscaler and frontier lab.
- **Binding orders are a different data class from announcements.** The discipline of counting only project-level OEM commitments is what makes 75 GW meaningful rather than a press-release aggregation.
- **Execution risk, not demand risk, is the live question.** The supply chain accelerated faster than the buildout capability, and Part 1's subject is the gap between an order and a running turbine.
- **$150B of OpenAI-Oracle contracted spend is load-bearing on this working.** That is a concentration of counterparty risk on a power-delivery assumption.

## How this relates to prior wiki pages

**It supplies the electricity term that [compute-economics.md](compute-economics.md) has been missing.** That page tracks GPU pricing, utilization and the durability of the buildout, and it has treated power as a constraint named but not quantified. 75 GW of binding orders is the quantification, and it reframes the constraint: the labs are not waiting for grid interconnection queues, they are routing around them with capital.

**It composes with the same day's supply-side story in an uncomfortable way.** [DeepSeek V4.1 Flash (09-10)](../llms-foundation-models/2026-09-10-deepseek-v41-flash-architecture.md) responds to HBM scarcity by moving nearly half its parameters onto host LPDDR, and [Chapter 4 on extreme quantization (09-10)](../inference-efficiency/2026-09-10-extreme-quantization-blackwell-fp4-native-fp8.md) responds to the same scarcity with sub-byte numerics. Those are demand-reduction answers to a memory shortage. Behind-the-meter gas is a supply-expansion answer to a power shortage. **Two of the three physical inputs to AI, memory and electricity, are simultaneously binding, and the industry is attacking them with opposite strategies.** The third, and the one The Pulse flagged the same day, is [CPUs](2026-09-10-cpu-shortage-agentic-tool-use.md).

**It confirms the direction of [modular datacenters (07-30)](2026-07-30-semianalysis-lego-datacenters-modular.md), which argued that prefabricated, repeatable datacenter units were becoming the build pattern because they compress schedule risk.** Five hundred identical 4.25 MW engines at one OpenAI site is the power-generation instance of exactly that logic: standardize the unit, parallelize the deployment, accept lower per-unit efficiency for schedule certainty.

## Gaps

This is Part 1 and the execution-risk analysis is the promised content, so the delivery-rate figures that would let a reader convert 75 GW of orders into a capacity forecast are not yet published. Emissions and local permitting exposure are unaddressed. And the report's own methodology, counting only binding orders, is a floor rather than an estimate.

## Related

- [Compute economics](compute-economics.md) · [Memory hierarchy](memory-hierarchy.md) · [Modular datacenters](2026-07-30-semianalysis-lego-datacenters-modular.md)
