# Nvidia's Backstop Universe: $530B of off-balance-sheet guarantees

**Source:** [SemiAnalysis, "Nvidia's Backstop Universe – Heads I Win, Tails Who Loses?"](https://newsletter.semianalysis.com/p/nvidias-backstop-universe-heads-i) (2026-09-11)
**Raw:** [starred Gmail 2026-09-12](../../raw/gmail/2026-09-12-starred.md)

## TL;DR

Nvidia's most recent 10-Q discloses **$530 billion of gross off-balance-sheet guarantees**, up from $184 billion one quarter earlier. Its on-balance-sheet liabilities are $91 billion. The gap is the story. Nvidia is not just selling GPUs; it is manufacturing credit. It floors Neocloud revenue, guarantees their landlords, and signs datacenter leases itself, so that operators without investment-grade ratings can borrow at investment-grade pricing. SemiAnalysis's read is that the risk is **asymmetric in Nvidia's favor** and that Nvidia can and should keep expanding these commitments. The tail risk is narrow but real, and it is correlated.

## The numbers, because they are the argument

The quarter-over-quarter jump from $184B to $530B comes mostly from three line items:

- **Supply and capacity commitments: $119B → $279B**, primarily **memory** per the CFO, with 96% due by fiscal 2029. Nvidia is pre-buying the HBM supply chain.
- **Guarantees and LPS Guarantees: $3.5B → $108.5B**, essentially all of it on SB Energy's PORTS-Pike campus in Ohio: **4.25 GW leased to OpenAI for twenty years**, with Nvidia guaranteeing the land, the power and the shell.
- **Two line items appearing for the first time:** $36B of **AI cloud agreements**, the take-or-pay floors under Neocloud capacity from the AI Cloud Partner program, and **$20B of datacenter leases Nvidia has signed as a tenant** but expects to reassign to third parties.

Against that: $91B of on-balance-sheet liabilities including $33.4B of debt ($25B of senior notes issued last quarter), a cash balance that grew $12B to $22B, and an investment book that went from **$45B to $128B in four quarters**, with the $99B equity portion generating $23.7B of gains in the first half alone and $25B more committed. Consensus has Nvidia generating roughly **$441B of EBITDA in fiscal 2028**. SemiAnalysis models the cash balance reaching **$1.4 trillion by fiscal 2031**, against an estimated **$11 trillion of cumulative industry capex from CY24 through CY29**.

## The mechanism, and why it exists

The reason these guarantees exist is a fight over who controls the cost of capital. SemiAnalysis's framing: the **Gigascalers** (Amazon, Microsoft, Google, Meta, Oracle) have been gatekeeping the investment-grade capital the buildout runs on, and profiting from the spread between the offtake price they are charged and the spot price they resell at, plus the services layered on top. **Nvidia's response is to manufacture alternative credit anchors** so that Neoclouds and smaller labs can raise money without going through the Gigascalers.

The payoff structure is the title. **Heads:** demand holds, and Nvidia wins twice, once on the GPU sale at full day-one margin and again on the revenue share above the contractual floor. **Tails:** demand falls, the Neocloud earns nothing but stays solvent because the revenue floor is set high enough to repay lenders, and the guarantee acts as a breakwater stopping contagion from reaching those lenders. Nvidia only loses if backstopped operators miss their lease and offtake commitments *at the same time* as Nvidia's own cash generation deteriorates. Those two are correlated by construction, since a Neocloud that cannot pay its lease is a Neocloud that has stopped buying GPUs.

The scale check that deflates the panic: Nvidia backstops roughly **6.5 GW**, most of it unbuilt. SemiAnalysis's datacenter model has Microsoft, Meta, AWS and Oracle leasing about **15 GW of third-party capacity in 2026 and more than 35 GW by 2028**, on fifteen-to-twenty-year leases that developers borrow against at investment-grade pricing. **The Gigascalers are the far larger implicit backstop of the buildout.** Nvidia's program draws attention because it is new and because, in their phrase, many investors have "Cisco PTSD."

## How this relates to the rest of the wiki

**It adds the financing layer to a thesis the [compute economics page](compute-economics.md) has built entirely out of unit economics.** That page has recorded Anthropic signing $517B of compute contracts in eleven months against OpenAI's ~$750B through 2030, and noted that both CEOs are on record calling the buildout excessive while participating in it, which the page read as evidence the commitments are defensive rather than demand-driven. This piece explains **how those commitments get funded at all**: not from the buyers' balance sheets, but from a credit structure the chip vendor is underwriting. That materially changes the interpretation. A defensive commitment financed by the seller is a different object from a defensive commitment financed by the buyer, because the seller has an incentive to keep extending it.

**The memory line is the one this reader should watch.** $119B to $279B of supply commitments, "primarily memory," is the largest single move in the disclosure and it is a direct claim on HBM capacity through fiscal 2029. Put that beside the same day's note from AI Breakfast that **DeepSeek open-sourcing a 552B model knocked three percent off Korean memory stocks**, and you have both sides of the same trade: Nvidia locking in multi-year memory supply while the market prices open-weight efficiency gains as demand destruction for that same memory. **Both cannot be right about 2029.**

**The power guarantee is the item that connects to the day's research.** Nvidia guaranteeing land, power and shell for 4.25 GW leased to OpenAI for twenty years is a bet that power is the binding constraint and worth owning the risk on. That is the same premise the [Jalapeño ASIC entry (08-26)](2026-08-26-openai-jalapeno-inference-asic.md) recorded from OpenAI's side, that it is limited by datacenter power rather than budget or floorspace, and it is the premise today's [job power elasticity paper](2026-09-12-job-power-elasticity-pfi.md) makes measurable.

## Gaps and how to read it

SemiAnalysis is explicit that its projection "does not represent our base case or a definitive forecast," which is the right disclaimer and should be honored. The analysis is also not neutral: SemiAnalysis sells the AI Compute, Capital and Markets model that the dollar figures depend on, and advertises it twice in the piece. The load-bearing assumption is the **$441B EBITDA consensus for fiscal 2028**, and every conclusion about capacity to support obligations scales linearly with it; if that number is wrong the whole firepower argument moves with it. Finally, the piece argues Nvidia *should* keep expanding these commitments, which is an editorial position and not a finding.

## Industrial implication

The practical consequence is that **Neocloud credit quality is now partly a derivative of Nvidia's balance sheet**, and anyone contracting for capacity should price it that way. The correlated-failure scenario SemiAnalysis identifies is narrow but it is exactly the scenario in which a buyer would most want their capacity contract to hold. For the smaller trainers this page has repeatedly flagged as the ones squeezed hardest by a scarcity market, the near-term effect is positive and real: Nvidia's credit manufacturing is the reason non-investment-grade operators can offer capacity at all.

**Related:** [compute economics](compute-economics.md) · [OpenAI Jalapeño (08-26)](2026-08-26-openai-jalapeno-inference-asic.md) · [job power elasticity (09-12)](2026-09-12-job-power-elasticity-pfi.md) · [behind-the-meter power (09-10)](2026-09-10-behind-the-meter-power-datacenters.md)
