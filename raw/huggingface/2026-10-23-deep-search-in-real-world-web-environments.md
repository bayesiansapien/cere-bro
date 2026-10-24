---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.875627+00:00
arxiv_id: 2610.30181
url: https://huggingface.co/papers/2610.30181
arxiv_url: https://arxiv.org/abs/2610.30181
date: 2026-10-23
---

# Deep Search in Real-World Web Environments

Despite substantial progress in Deep Search agents, their ability to conduct end-to-end research in real-world open Web environments remains insufficiently evaluated. Unlike static retrieval settings, information on the real-world Web is distributed across diverse sources, modalities, and heterogeneous formats, often involving complex interaction mechanisms that require agents to autonomously search for, access, and integrate relevant evidence during execution. To address this gap, we introduce the OpenDS task, designed to evaluate agents' ability to perform multi-step deep search in the live, open Web. This task requires agents to autonomously explore the real Web, discover and connect relevant evidence from multiple independent sources through Web search, browser interaction, and evidence processing, and ultimately determine a unique factual answer. Building on this task formulation, we construct OpenDS-World, a benchmark comprising 200 challenging tasks spanning diverse information modalities, heterogeneous file formats, and interactive access requirements, with independent human verification to ensure evidence validity and answer uniqueness. We evaluate 12 frontier models under a unified tool environment and execution protocol. The best-performing model achieves 39.0% accuracy, while human evaluation across 1,000 independent attempts yields 21.1% accuracy. Further analyses of tool usage, search cost, termination behavior, and failure recovery reveal substantial differences in research strategies across models, as well as persistent challenges in tool coordination and long-horizon search management. OpenDS-World provides a unified evaluation platform for systematically assessing and advancing agents' autonomous deep search capabilities in real-world open Web environments.
