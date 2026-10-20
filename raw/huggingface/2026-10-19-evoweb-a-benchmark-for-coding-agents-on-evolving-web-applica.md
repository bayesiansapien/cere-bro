---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.16402
url: https://huggingface.co/papers/2610.16402
arxiv_url: https://arxiv.org/abs/2610.16402
date: 2026-10-19
---

# EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications

Web application development often proceeds through successive requests that extend an existing implementation. Yet web-generation benchmarks primarily evaluate development toward fixed specifications. We introduce EvoWeb, a novel benchmark comprising 320 cumulative requests over 32 web applications, grounded in real-world product features and structured by functional dependency graphs. Agents iteratively modify a persistent codebase, while a multimodal web agent tests each intermediate application in a live browser, assessing newly requested functionality, cross-request integration, and previously requested functionality. To characterize reliability throughout development, we integrate trajectory performance across user-tolerance thresholds rather than impose a fixed stopping criterion. Experiments across open- and closed-source frontier models show that EvoWeb reveals clear performance differences between models, with cross-request integration emerging as a key challenge. Further analysis shows that later requests with deeper or more numerous dependencies are solved less accurately, while runtime errors become more frequent over successive requests. EvoWeb provides a testbed for evaluating and improving coding agents in long-horizon, multi-request development.
