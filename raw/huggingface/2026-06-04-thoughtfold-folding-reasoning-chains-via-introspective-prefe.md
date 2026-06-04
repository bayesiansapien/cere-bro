---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.03503
url: https://huggingface.co/papers/2606.03503
arxiv_url: https://arxiv.org/abs/2606.03503
date: 2026-06-04
---

# ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning

Large Reasoning Models (LRMs) have achieved remarkable progress thanks to Reinforcement Learning with Verifiable Rewards (RLVR) on Chain-of-Thoughts (CoTs). However, since long CoTs naturally contain trial and errors and mainstream RLVR approaches choose outcome-correct CoT trajectories for memorization, the redundant explorations in long CoTs are inevitably reinforced, which results in the over-thinking issues of LRMs. Previous attempts to resolve this issue mainly give more advantage to shorter trajectories, yet their learning signals are still outcome-based and cannot reduce the memorization of redundant explorations in long CoTs. Therefore, we propose ThoughtFold, a framework that leverages fine-grained preference learning to mitigate redundant explorations for efficient reasoning. ThoughtFold employs an introspective strategy to identify redundancy within each correct trajectory, which yields a spectrum of candidate sub-trajectories. Leveraging this spectrum, we introduce a masked preference optimization objective that explicitly penalizes redundant explorations and encourages the model to directly bridge essential reasoning segments, effectively folding its reasoning chains into a more concise path. Extensive experiments show that ThoughtFold significantly enhances efficiency. It reduces the token usage of DeepSeek-R1-Distill-Qwen-7B by approximately 56% while maintaining state-of-the-art accuracy.
