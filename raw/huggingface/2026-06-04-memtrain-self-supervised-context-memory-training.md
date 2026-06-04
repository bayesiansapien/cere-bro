---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.03197
url: https://huggingface.co/papers/2606.03197
arxiv_url: https://arxiv.org/abs/2606.03197
date: 2026-06-04
---

# MemTrain: Self-Supervised Context Memory Training

Memory is an indispensable capability for long-horizon LLM agents, enabling them to preserve and utilize information accumulated across extended interactions. Existing memory-agent approaches are typically trained end-to-end with reinforcement learning on downstream tasks. However, collecting high-quality annotated problems for memory-intensive scenarios is costly, and the resulting training data often lack sufficient diversity to cover general memory behaviors. In this work, we propose MemTrain, a self-supervised training framework for generally enhancing the context-memory capability of LLM agents for more effective downstream post-training. MemTrain introduces two coupled proxy tasks over unlabeled Wikipedia corpora: (1) an end-to-end masked reconstruction objective, which requires the model to recover masked entities after multiple rounds of memory updates, thereby encouraging memory maintenance from the final outcome perspective; and (2) an intermediate memory recall objective, which requires the model to reconstruct masked historical information using intermediate memory states, encouraging faithful compression and memory completeness throughout the interaction process. The two objectives are jointly optimized using GRPO. Extensive experiments on long-text QA and search-based QA benchmarks demonstrate that MemTrain consistently improves downstream memory-intensive reasoning performance across different models, achieving gains of up to 17.67 points over direct task-specific post-training.
