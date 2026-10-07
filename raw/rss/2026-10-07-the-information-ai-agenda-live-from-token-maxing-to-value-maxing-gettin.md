---
source: farmer/rss
feed: the-information
farmed: 2026-10-07T15:45:24.796171+00:00
title: "AI Agenda Live: From Token Maxing to Value maxing: Getting More From Every Unit of Compute"
url: https://www.theinformation.com/articles/ai-agenda-live-token-maxing-value-maxing-getting-every-unit-compute
published: 2026-10-07
author: The Information Partnerships
---

# AI Agenda Live: From Token Maxing to Value maxing: Getting More From Every Unit of Compute

<p>In AI circles, conversations about compute shortages are as common as talk of the weather. As agentic workflows threaten to multiply token consumption further, it’s little wonder that talk has shifted from securing GPUs to optimizing them.</p>

<p>At a recent panel, The Information’s Phoebe Liu sat down with three AI leaders—from chipmakers and AI clouds to Fortune 500s—to discuss how they’re squeezing more tokens from every unit of compute. Those on the panel were:</p> <ul>
<li>Marc Boroditsky, Chief Revenue Officer, Nebius</li> <li>Mattie Toia, VP, Infrastructure, Uber</li> <li>Dion Harris, Sr. Director, HPC &amp; AI Hyperscale Infrastructure Solutions, NVIDIA</li> </ul> <h3><strong>Optimizing to the customer’s KPI</strong></h3> <p>Nebius was recently rated Platinum, the top tier, in SemiAnalysis’ ClusterMAX rating, which puts GPU cloud providers through a suite of hands-on tests on the compute they supply. This distinction, said Chief Revenue Officer Marc Boroditsky, reflects the company’s ability to deliver high performance at high efficiency.</p>

<p>“Not only are we a well-regarded supplier for neolabs, but we’re also enterprise-grade, so ready to supply the entire market,” he said.</p>

<p>He noted that Nebius tailors optimizations in Nebius Token Factory, its inference platform, to specific customer’s specific goals, whether speed, reliability, quality or price.</p>

<p>One recent example of how they do this is speculative decoding, which allows smaller models to predict likely next tokens that a larger model verifies in bulk, rather than generating one token at a time. Nebius uses each customer’s own traffic to improve the result.</p>

<p>NVIDIA, meanwhile, is helping companies avoid unnecessary compute altogether. A feature in its Dynamo platform locates already-computed data sitting in a cluster’s KV cache so teams don’t waste compute recalculating it.</p>

<p>“We’re seeing a lot of bang for the buck in terms of driving performance, efficiency and overall effectiveness,” noted NVIDIA’s Dion Harris.</p>

<p>Uber has seen its token costs stabilize in recent months even as its use of agentic workflows has grown, said Mattie Toia. She credited caching pushed down to individual sub-agents, plus a simpler shift: giving engineers visibility into their own usage.</p>

<p>“It starts by giving visibility to individual users—how many tokens they’re spending, the relative cost of them. That gives people context to think about how they’re optimizing,” she said.</p>

<p>Boroditsky described the shift as moving from “token maxing” to “value maxing”: measuring how many agent turns, tokens and dollars it takes to reach an outcome, whether that’s a document or a completed form.</p>

<p>“What you’re looking for is, how do I actually optimize the value that I’m creating for the cost that I’m spending?” he said.</p> <h3><strong>The ecosystem at work</strong></h3> <p>Improving the economics of compute is a job for the whole industry, not any one company, the panel agreed. “It takes a lot more than a chip to deliver AI at scale,” Harris said.</p>

<p>He pointed to compounding gains from pairing new hardware with better software—kernel tuning, smarter frameworks, and tools built across NVIDIA’s ecosystem. Over a chip’s lifetime, this can drive 3-5X performance gains from day zero to year five.</p>

<p>Boroditsky added that no single model wins every use case.</p>

<p>“Models matter a lot, but by themselves, they don’t solve a problem,” he said. “It’s the entire end-to-end solution.”</p> <h3><strong>Data discipline</strong></h3> <p>One thing companies can do today, Toia said, is get their own data in order.</p>

<p>“There is a lot of valuable data that most organizations have that is really important to grounding your models,” she said. Uber built an internal “context graph”—roughly 24 million nodes pulled from Jira tickets, system design docs and code reviews—to feed its AI agents better context, cutting query times from 20 minutes to 30 seconds while using fewer tokens.</p>

<p>Boroditsky agreed with this approach, noting that the companies that build centralized resources get better results. His five-year prediction: “The leading companies in the market will have taken control of their intelligence.”</p> <h3><strong>The future of pricing</strong></h3> <p>Asked whether Nebius would consider outcome-based pricing, Boroditsky said the company was open to the idea.</p>

<p>“I don’t think we’ve figured out yet the right economic model between the supplier and the customer,” he said.</p>

<p>Nebius already runs capacity auctions and recently launched spot pricing. As the applications built on Nebius move toward outcome-based models, Boroditsky noted that vendors will have to adapt. Looking ahead, he expects managed services to route workloads intelligently on customers’ behalf.</p>

<p>“In the coming quarters, you’re going to see a lot more managed services that are doing more of the heavy lifting,” he said.</p>
