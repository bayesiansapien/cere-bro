---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352817+05:30
arxiv_id: 2609.40195
url: https://huggingface.co/papers/2609.40195
arxiv_url: https://arxiv.org/abs/2609.40195
date: 2026-10-01
---

# MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories

Long-term egocentric video enables personalized AI assistants to reason about daily life. However, as video histories grow to hundreds of hours spanning months or years, reprocessing raw clips for every query becomes computationally prohibitive. Memory systems offer a scalable alternative by compacting videos into text representations, but often fail on practical benchmarks: either the memory does not preserve key evidence, or the retriever fails to locate relevant entries due to retrieval competition in growing search spaces. To address these challenges, we introduce MemLife, a multimodal memory system that constructs entity-grounded, first-person text episodes and retrieves them via a time-indexed agentic reader. Without training or query-time video access, MemLife improves over the strongest training-free baseline by 4.6--12.0% across four long-horizon benchmarks. To further improve memory quality, we propose MemOpt, a reinforcement learning framework that optimizes the memory writer to produce faithful, informative, and retrievable memories. MemOpt consistently improves MemLife by 2.7--5.0% across different video and question distributions, with gains that generalize across writer and reader backbones and memory systems.
