---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04926
url: https://huggingface.co/papers/2608.04926
arxiv_url: https://arxiv.org/abs/2608.04926
date: 2026-08-06
---

# Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation Learning

As chart images, tabular data, and visualization code play increasingly important roles across diverse domains, cross-representation understanding across these modalities poses fundamental challenges for AI systems: the relationships across representations are inherently one-to-many, supervision is ambiguous and costly, and model optimization lacks a principled signal that is both direction-adaptive and representation-generalizable beyond task-specific objectives. We introduce CoCoEvolve to improve consistency across chart, table, and code representations. Instead of treating cross-representation mapping as a one-to-many problem, we define explicit one-to-one correspondences and optimize models using agreement between representations, without additional annotations. During training, CoCoEvolve@Train performs co-evolution across the chart-table-code cycle, while CoCoEvolve@Test applies the same consistency objective at inference time for test-time co-optimization. We also present CoCoEvolve@Eval, an evaluation suite covering all six cross-representation tasks. Across four benchmarks, CoCoEvolve improves performance in both training-time and test-time settings. Our project page: https://xhguo7.github.io/CoCoEvolve/.
