---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.365204+05:30
arxiv_id: 2611.03806
url: https://huggingface.co/papers/2611.03806
arxiv_url: https://arxiv.org/abs/2611.03806
date: 2026-11-04
---

# BEND 2.0: Benchmarking the Capabilities Needed to Design DNA

Genomic foundation models are increasingly used to propose DNA sequences and edits. But successful design requires capabilities that current benchmarks do not measure. Here we introduce BEND 2.0 (BENchmark for DNA language models), which tests how well models predict the effects of DNA changes and whether these predictions can guide sequence design. Across eight tasks built on five experimental datasets, we find that model choice and how representations are accessed both affect performance. Linear readouts fitted to frozen representations can match or exceed models' native outputs, and functional post-training substantially improves the models' capabilities. Linear readouts transfer well across experimental assays and genes, suggesting that models capture functional patterns beyond the data used to fit individual predictors. At the same time, strong prediction of average effects can conceal weaker prediction of context-specific effects, and accurate prediction of combined mutation effects does not imply accurate prediction of their interactions. In design tasks, model predictions can reduce the number of candidates needed to find a desired response, but still leave substantial room for better design choices, particularly for context-specific and multi-cell objectives. Our benchmark reveals that genomic models now display signs of general utility but have yet to saturate on performance in even simple tasks.
