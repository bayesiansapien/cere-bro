---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2606.13610
url: https://huggingface.co/papers/2606.13610
arxiv_url: https://arxiv.org/abs/2606.13610
date: 2026-08-25
upvotes: 2
authors: ["Minghao Luo", "Liang Chen"]
---

# One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders

**Upvotes:** 2
**Authors:** Minghao Luo, Liang Chen

Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: LLM recommenders may consume web content that Generative Engine Optimization (GEO) operators have polluted to mislead them. We ask: to what extent do they become unwitting promoters of fake products? We introduce FORGE (Fake Online Recommendations in Generative Environments), which locally rewrites real products in a frozen set of retrieved web pages into fake ones and measures how often the LLM recommends the fake product, across 225 real products in 15 categories and 5 consumer scenarios. Across 12 commercial and open-weights LLMs, all models are vulnerable: a single polluted page yields fooled rates of up to 27%, while the full top-3 replacement raises this to 73.8%. Vulnerability varies across categories, increasing when models lack stable prior knowledge of the products. Reasoning does not mitigate this vulnerability; instead, it often generates spurious social proof to justify false recommendations. None of the four defenses is adequate: the skepticism prompt can exacerbate vulnerability much like reasoning, the two consensus filters risk suppressing legitimate products, and credibility re-ranking helps every model but removes only a sixth of the fakes. We release the FORGE benchmark and the evaluation code at https://github.com/leoluolol/forge-benchmark.
