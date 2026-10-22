---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.17816
url: https://huggingface.co/papers/2610.17816
arxiv_url: https://arxiv.org/abs/2610.17816
date: 2026-10-20
---

# Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution

Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved throughout execution rather than a one-shot decision for each query. Such interleaved participation introduces trajectory-level effects that remain insufficiently understood. To address this gap, we introduce EC2-Bench, a benchmark for evaluating edge-cloud collaboration in long-horizon agent execution. It provides executable digital-workspace agent tasks and a unified evaluation framework covering task performance, resource usage, and privacy exposure. Using this benchmark, we empirically study diverse forms of edge-cloud collaboration. Our study reveals three findings. First, collaboration achieves a favorable balance among task performance, resource usage, and privacy exposure compared with edge-only and cloud-only execution. Second, as edge models become stronger, collaborative execution approaches cloud-only performance, and performance differences across strategies shrink, while privacy exposure remains strongly strategy-dependent. Third, stronger edge capability shifts preferred collaboration from externally controlled cloud participation and direct cloud execution toward more edge-controlled collaboration. Further analyses identify cloud-invocation decision-making and instruction following as important edge-side abilities for effective collaboration. These findings provide a systematic understanding of edge-cloud collaboration in long-horizon agent execution and insights for designing future edge agents that effectively collaborate with cloud models. Code and resources are available at https://github.com/OpenBMB/EC2-Bench.
