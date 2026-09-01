---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.31075
url: https://huggingface.co/papers/2608.31075
arxiv_url: https://arxiv.org/abs/2608.31075
date: 2026-09-01
---

# Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence

Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to improve as human supervision gradually recedes from the learning loop. We examine two connected dimensions of this problem. The reward axis traces the development from per-instance human judgments to reusable verifiers and rewards that operate even without human feedback. The experience axis examines how learning can progress from human-curated tasks and environments toward self-generated curricula, constructed environments, and autonomous co-evolution. We connect these dimensions through a five-level ladder from L0 to L4 that identifies which parts of the learning process remain under continued human control. Our analysis further highlights the risks introduced by increasingly autonomous rewards and experience generation, including reward hacking, feedback drift, curriculum collapse, and environment errors. Consequently, we also provide the evaluation around three complementary objects: policy capability, feedback fidelity, and experience quality. This analysis provides a structured account of current approaches to scaling LRMs beyond human supervision and the open problems involved in developing self-sustaining learning systems toward superintelligence. Furthermore, we maintain a continuously updated https://github.com/visitworld123/Awesome-Scaling-LRM-Beyond-Human-Supervision{GitHub repository} to track the latest advances.
