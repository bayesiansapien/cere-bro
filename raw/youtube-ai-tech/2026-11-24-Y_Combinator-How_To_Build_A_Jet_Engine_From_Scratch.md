# How To Build A Jet Engine From Scratch

**Channel:** Y Combinator
**Published:** 2026-11-24
**Source:** https://www.youtube.com/watch?v=-ieJwYq4j-o

## TL;DR
A YC documentary on Boom Supersonic. After Rolls-Royce walked away in Sep 2022 (which founder Blake Scholl calls a "stage-four cancer diagnosis"), Boom built its own engine. In 2025 Scholl realized the core could become a **42 MW natural-gas turbine for AI data centers** ("Superpower"). Sam Altman's reply was "as many as you can make." The first full-scale engine core **fired on Nov 21, 2026**, and turbine shipments target **mid-2027**. The strategy: turbine profits fund the Overture airliner (Scholl says two units a month makes Boom cash-flow positive), and fleet run-hours (a million instead of 5,000) de-risk FAA certification. The method: extreme vertical integration (85% in-house by weight, its own single-crystal blade foundry), software-first hardware engineering, and a cap of 250 non-manufacturing staff.

## Key Takeaways
- **Demand side:** The grid interconnect queue is 5 to 10 years long, and GE gas turbines are sold out through about 2030. The US needs about 100 GW of new generation in 10 years, about $300B of turbines. One prospective customer wants **1.6 GW every 30 days**. Boom's plan is 1 GW a year.
- **Incumbent critique:** Turbine OEMs have tripled prices, and they won't add capacity that Wall Street might punish. Scholl traces the stagnation to 1973 (the supersonic ban plus flattening electricity per capita, now declining since 2000).
- **The blade bottleneck:** The supply-chain quote for 3D-printed blades was 18 months and $1.3M per shipset. The printer cost $1.1M with 2-week delivery, so they bought it. Single-crystal superalloy blades (about 3,000°F, 10K RPM, 3 years continuous) were reportedly a 3-company capability. Boom aims to "design Monday, cast Tuesday."
- **Software-first hardware:** a software engineer on every hardware team. **Bladerunner**: an in-house CAD kernel plus an in-house GPU cluster running real-time aero and structural simulation as you drag a slider, so one engineer does what took 100 people 6 months. The fastest full engine iteration industry-wide is 3 months, 6 is typical.
- **Org:** 165 people (40 in manufacturing). XB-1 was built by about 50.
- **Same core, two products:** 40,000 lbf at Mach 1.7 for Overture, or remove the fan and add a generator for 42 MW.

## Architecture & Optimization Mechanics
- **Power is now the binding constraint on inference capacity, which raises the value of efficiency work.** If behind-the-meter gas turbines are the marginal power source, every joule per token saved by quantization, sparsity or routing turns directly into fewer turbines, less gas and less capex. At about 42 MW per unit, a 2x efficiency gain from INT4 plus speculative decoding across a cluster is worth about one turbine per 42 MW of IT load.
- **Bladerunner is the GPU-accelerated-simulation thesis in practice:** real-time CFD and FEA inside the design loop compresses iteration cycles by 100x. It's another case where an inference-speed (latency) win changes what is *designable*, not just the cost.
- **Lesson for agent-era orgs:** "Most hardware engineering is actually software engineering," and now "the receptionist is a coder." That's the same small-team thesis as Amp's 21 people (see the 2026-11-25 page).

## Grounded Context (Web Enrichment)
The video leaves out a major fact. Boom announced **Crusoe as the Superpower launch customer in Dec 2025: 29 units, 1.21 GW, about $1.25B**, alongside a $300M raise. But **TechCrunch and TechRepublic reported on Sep 28, 2026 that Crusoe walked away from that deal.** So the "firm customer demand as far as the eye can see" pitch currently rests on *prospective* customers (the unnamed 1.6 GW-a-month buyer), not a signed launch order. The first-fire claim (Nov 21) comes from Boom and YC, and I found no independent confirmation yet. The macro demand is real: turbine backlogs at GE Vernova, Siemens Energy and Mitsubishi run multiple years, and behind-the-meter gas has become the default bridge for AI campuses. The open questions are Boom's ability to hit industrial reliability (aeroderivative turbines usually take years of field validation) and emissions permitting. The XB-1 supersonic flight (Jan 2025) and the self-built engine program announcement (Dec 2022) are both accurate.

## Real-World Application / Actionable Step
- **Investment:** The constraint is real, so the durable trade is the turbine incumbents and the grid supply chain (GE Vernova, Siemens Energy, Mitsubishi Heavy, plus transformer and switchgear names), not Boom. Boom is private and pre-revenue on turbines, and just lost its launch customer. If you hold incumbents, watch Boom's mid-2027 first shipment as the first credible new-entrant pricing pressure.
- **Research framing:** Lead your next compression or routing write-up with energy per token (J/token) alongside latency. In a power-constrained world that's the metric buyers care about.

Sources: [Boom press release: Superpower, $300M](https://boomsupersonic.com/press-release/boom-supersonic-to-power-ai-data-centers), [DCD: Crusoe orders 1.21GW](https://datacenterdynamics.com/en/news/crusoe-orders-121gw-of-natural-gas-turbines-from-prototype-airliner-co-boom-supersonic), [TechRepublic: Crusoe walks away from $1.25B deal](https://www.techrepublic.com/article/news-crusoe-boom-turbine-deal/), [Tom's Hardware: 42 MW Superpower](https://www.tomshardware.com/tech-industry/supersonic-airline-outfit-boom-unveils-turbine-for-ai-data-centers-42-mw-superpower-turbine-uses-the-same-tech-designed-to-power-concorde-successor-to-mach-1-7-at-60-000-ft), [Turbomachinery Magazine](https://www.turbomachinerymag.com/view/boom-supersonic-s-superpower-gas-turbines-drive-data-centers-obtain-funding), [Quartz: Boom pivots to AI power](https://qz.com/boom-supersonic-jet-startup-ai-data-center-power)
