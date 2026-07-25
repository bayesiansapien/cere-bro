# NVIDIA's $500B SK Partnership: Buying the Memory Supply, Not Just Selling Chips

**TL;DR.** NVIDIA announced a $500 billion partnership with SK Group, the conglomerate that owns SK hynix, on 2026-07-24. The stated aim is to help NVIDIA access more high-bandwidth memory and fill more datacenters with its servers. The concrete pieces: SK Telecom builds a 2-gigawatt Vera Rubin DSX AI factory in Korea, **SK hynix co-develops next-generation AI memory including HBM with NVIDIA**, NAVER and Brookfield expand Korea's national AI factory buildout to gigawatt scale, and KAIST launches a joint AI research lab with NVIDIA in Seoul. President Lee Jae Myung met Jensen Huang ahead of the San Francisco AI Summit.

The number is the headline; the HBM co-development line is the signal. NVIDIA is moving upstream into memory design because memory, not compute, is what constrains it.

## Why this is a memory story, not a datacenter story

Read alongside today's [SemiAnalysis AMD analysis](2026-07-25-semianalysis-amd-cuda-moat.md), the strategic logic is unambiguous. AMD's MI455X ships **12 HBM4 stacks for 432GB at 23.3 TB/s** against Rubin's 8 stacks for 288GB. NVIDIA's answer was not more stacks but faster ones: it raised its HBM4 pin-speed target to **10.7 Gbps**, well above the original JEDEC HBM4 spec and 40% faster than AMD's 7.6 Gbps, specifically to erase AMD's bandwidth advantage and land Rubin at 22 TB/s from a 33% narrower bus. Memory suppliers had to rework their HBM4 to deliver a spec NVIDIA set unilaterally, which pushed out upstream output and delayed Rubin.

That is the context for a $500B partnership with the company that has to build those parts. NVIDIA needs bins that AMD does not need (a 10.7 Gbps part is a much higher-quality bin than a 7.6 Gbps part), it needs them in volume, and it just discovered what happens when the supplier cannot keep up. Co-developing the next generation rather than specifying it after the fact is the obvious correction.

The [memory hierarchy](memory-hierarchy.md) page has held since 06-07 that the binding constraint on AI infrastructure shifted from FLOPS to memory, and that the shortage is structural (Micron's roughly 3:1 HBM-to-DDR5 wafer trade ratio rising per generation, plus the advanced-packaging bottleneck, keeping top-end HBM allocation-driven into 2030). A $500B vertical arrangement between the largest buyer and one of three suppliers is what a structural shortage looks like when it reaches the balance sheet. The corroborating detail from the AMD piece: **AMD quietly dropped the up-to-1TB of direct-attached LPDDR from the MI455X EAM module**, which SemiAnalysis attributes to tight memory supply. One vendor signs a half-trillion-dollar supply partnership; the other deletes a memory tier from its roadmap.

## Market reaction context

The same 24 hours carried a sharp divergence in how markets are pricing the buildout. Alphabet fell 7% on Thursday after disclosing a further capex increase, all but wiping out its year-to-date gain, and Tesla fell 15% on its own capex jump. The Information's read: big tech firms need to do a better job explaining their AI investment strategies. Meanwhile NVIDIA itself is up only 10% year to date against AMD's 142%, Micron's 213%, and the Philadelphia semiconductor index's 71%, despite revenue expected to rise 83% this year, which The Information argues means NVIDIA is "priced as though everything that could go wrong in the next couple of years will go wrong."

The read that ties these together: the market is rewarding the *memory* supply chain (Micron +213%) and the credible second source (AMD +142%) far more than the incumbent whose revenue is actually growing 83%, while punishing the hyperscalers doing the spending. Capital is pricing in exactly the constraint NVIDIA just spent $500B to secure.

## What to watch

- Whether the SK hynix co-development produces an HBM5 spec that NVIDIA sets jointly rather than unilaterally. The 10.7 Gbps episode was costly for both sides.
- Whether AMD can restore the cancelled LPDDR tier on MI500, or whether the second tier of accelerator-attached memory stays a casualty of allocation.
- Whether a 2GW single-country Vera Rubin DSX deployment shifts where inference capacity physically sits, given that Korea also hosts the fabs and packaging.

## Relation to prior wiki

- **Extends** [memory-hierarchy](memory-hierarchy.md): the structural-shortage thesis now has a half-trillion-dollar vertical-integration datapoint.
- **Pairs with** [the SemiAnalysis AMD piece (07-25)](2026-07-25-semianalysis-amd-cuda-moat.md), which supplies the technical reason this deal exists.
- **Follows** [Vera Rubin gigascale ramp (07-22)](2026-07-22-nvidia-vera-rubin-gigascale-ramp.md), where CoreWeave measured 10x tokens per megawatt over Grace Blackwell. The 2GW Korean DSX factory is that rack going into volume deployment.

## Sources

- [Nvidia Forms $500 Billion AI 'Partnership' With Memory Chip Giant SK (The Information)](https://www.theinformation.com/briefings/nvidia-forms-500-billion-ai-partnership-memory-chip-giant-sk)
- [Nvidia Shares Are Priced For Everything To Go Wrong (The Information)](https://www.theinformation.com/articles/nvidia-shares-priced-everything-go-wrong-makes-sense) · [Wall Street Sends Google a Message (The Information)](https://www.theinformation.com/articles/wall-street-sends-google-message)
- [@nvidia on the Korea partnership](https://x.com/nvidia/status/2080833379197477226) · [KAIST-NVIDIA joint lab](https://x.com/nvidia/status/2080663854447804796)
- Raw: `raw/rss/2026-07-25-the-information-nvidia-forms-500-billion-ai-partnership-with-memory-chi.md`, `raw/twitter/2026-07-25-morning.md`, `raw/twitter/2026-07-25-afternoon.md`
