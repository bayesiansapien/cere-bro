---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.21450
url: https://huggingface.co/papers/2608.21450
arxiv_url: https://arxiv.org/abs/2608.21450
date: 2026-09-03
---

# Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering

Knowledge-Based Visual Question Answering (KB-VQA) relies on retrieving external information to answer queries involving long-tail entities. However, existing retrieval pipelines predominantly employ CLIP-style dual encoders, which prioritize surface-level visual similarity over entity-level semantic alignment. This paradigm often fails when semantically identical concepts exhibit large visual variations or when distinct entities appear visually similar. To address this, we propose KBMR, the first MLLM-based embedding retriever tailored for KB-VQA. Leveraging the robust autoregressive capabilities of MLLMs, KBMR maps images into a semantic space that better preserves concept identity. To tackle the challenge of noisy supervision in Wikipedia-scale retrieval, we introduce an MLLM-based semantic discriminator that generates continuous entity-consistency weights. These weights guide a novel continuous semantic distillation objective, enabling effective hard negative sampling and soft supervision beyond rigid binary labels. Extensive experiments demonstrate that KBMR significantly outperforms CLIP baselines, yielding up to a 14.7% improvement in retrieval Recall@1 and a 9.4% gain in end-to-end VQA accuracy. Code is available at https://github.com/realHarryX/KBMR.
