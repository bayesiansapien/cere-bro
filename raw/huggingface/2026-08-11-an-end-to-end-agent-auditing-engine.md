---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.07346
url: https://huggingface.co/papers/2608.07346
arxiv_url: https://arxiv.org/abs/2608.07346
date: 2026-08-11
---

# An End-to-End Agent Auditing Engine

With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important. However, efficiently building an end-to-end, systematic, and comprehensive evaluation pipeline remains a significant challenge. To address this challenge, we introduce A^2E (Agent Auditing Engine), an end-to-end evaluation engine designed for agent harnesses. A^2E leverages our newly proposed Agent Task Protocol (ATP) to enable the rapid integration of evaluation tasks with different harnesses. Through an automatically instrumented Monitor, it captures and generates standardized execution traces during experiments. In the Evaluation stage, A^2E systematically assesses harness capabilities using a suite of multidimensional metrics. Compared with correctness alone, these metrics provide a more fine-grained characterization of differences among harnesses in execution efficiency, tool use, task planning, and error recovery. Experiments conducted with A^2E further reveal that model-harness combinations exhibit substantial performance variation across different types of tasks, and that no single combination consistently outperforms all others across every task. These findings not only demonstrate the necessity of systematic evaluation but also provide useful guidance for the co-evolving of models and harnesses. Our code is available at https://github.com/datamllab/A2E.
