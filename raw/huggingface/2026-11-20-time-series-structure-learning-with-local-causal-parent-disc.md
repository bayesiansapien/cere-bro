---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.392225+00:00
arxiv_id: 2611.26232
url: https://huggingface.co/papers/2611.26232
arxiv_url: https://arxiv.org/abs/2611.26232
date: 2026-11-20
---

# Time Series Structure Learning with Local Causal Parent Discovery

Learning and inference on time series can pose significant statistical challenges, including autocorrelated observations, distribution shift over time, and the curse of dimensionality. These challenges complicate the practical application of causal discovery algorithms, which already suffer from high computational and sample complexity in the general case. To mitigate these issues, this work introduces Iterative Temporal Parent Discovery (ITPD): a sound and complete constraint-based procedure for causal structure learning on multivariate time series with causal nonstationarity. ITPD takes a local-to-global learning approach that discovers the global graph by sequentially discovering the parent set for each variable. ITPD exploits temporal structural priors, graph partitioning, and the local Markov condition to swap higher-order conditional independence tests for lower-order alternatives. With an exact oracle, ITPD performed the least number of tests and used the smallest average conditioning set sizes relative to baselines. In benchmarking simulations, ITPD sat on the Pareto frontier with respect to F1 and wall-clock time and was faster than baselines on large graphs (geq 1000 nodes). For graphs with 2000 nodes, ITPD ran 2.3times, 9.1times, and 40.9times faster than iterative IAMB, DF-PC, and PCMCI, respectively.
