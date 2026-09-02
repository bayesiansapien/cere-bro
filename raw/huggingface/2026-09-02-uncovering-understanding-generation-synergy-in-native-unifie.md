---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2609.01607
url: https://huggingface.co/papers/2609.01607
arxiv_url: https://arxiv.org/abs/2609.01607
date: 2026-09-02
---

# Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System

While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors. At the representation level, we find that each objective provides useful signal to the other: generation enriches the visual features learned for understanding, while understanding strengthens vision--language alignment for generation. However, when both objectives are forced through the same computation path, one tends to dominate. A task-decoupled architecture that specializes conflicting visual computation while preserving semantic interaction avoids this asymmetric degradation. At the task level, through three case studies, we find positive bidirectional transfer when understanding and generation tasks rely on shared knowledge. At the system level, we show that an end-to-end UMM outperforms a matched planner--executor pipeline on complex tasks that explicitly require both image understanding and generation. Together, these results show that the value of UMMs extends beyond a unified interface: appropriate specialization, shared task knowledge, and end-to-end optimization can turn coexistence into synergy.
