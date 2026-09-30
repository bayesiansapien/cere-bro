---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929529+00:00
arxiv_id: 2609.28236
url: https://huggingface.co/papers/2609.28236
arxiv_url: https://arxiv.org/abs/2609.28236
date: 2026-09-29
---

# EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks

Long-horizon embodied interaction requires agents to retain and continually update information about the environment as they observe, act, and encounter change. Yet current agents struggle to maintain such memory reliably. Our analysis traces this limitation to four key deficiencies: weak fine-grained visual memory, unreliable dynamic world-state tracking, failing to record world state revealed by interaction outcomes, and limited generalization from prior experience. However, existing benchmarks do not directly assess these memory capabilities during long-horizon embodied interaction. To address this gap, we introduce EmbodiedMemory-Bench (EMem-Bench), comprising 2,554 interactive episodes across four task families. EMem-Bench requires agents to build and update memory from interaction history, then use it to complete a later task by acting in the environment. We further present Embodied-Memorizer (EMem), an external memory system that organizes embodied experience into spatial, event, and scene memories. We also train EMem-8B, an 8B policy that manages and uses these memories. We evaluate a diverse range of open-source and proprietary MLLMs and representative multimodal memory systems. Results show that current models remain weak and uneven across the four challenges. Under matched backbones, EMem achieves the best overall performance among the evaluated memory systems and improves both open-source and proprietary models, while EMem-8B further improves over its backbone. Project page: https://zju-omniai.github.io/EmbodiedMemoryBench/
