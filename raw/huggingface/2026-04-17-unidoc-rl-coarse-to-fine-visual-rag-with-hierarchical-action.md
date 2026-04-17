---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2604.14967
url: https://huggingface.co/papers/2604.14967
arxiv_url: https://arxiv.org/abs/2604.14967
date: 2026-04-17
---

# UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards

Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.
