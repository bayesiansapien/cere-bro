---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.19790
url: https://huggingface.co/papers/2607.19790
arxiv_url: https://arxiv.org/abs/2607.19790
date: 2026-07-23
---

# Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning

Reinforcement learning with verifiable rewards (RLVR) has substantially improved language-model reasoning, yet its extension to vision-language models remains constrained by the lack of training data that are simultaneously broad, exactly verifiable, and reproducible. We introduce Trace, a taxonomy-guided environment for multidomain visual reasoning. Trace factorizes task construction into a scene grammar and an executable task program, separating visual realization from answer computation. A shared semantic state determines the rendered image, prompt, typed answer, verifier state, and replayable instance trace. The resulting environment comprises 1,000 tasks over 277 scene grammars and 11 visual domains, with controlled semantic and visual variation. RLVR on 64,000 Trace instances improves the macro-average across 24 external benchmarks by 3.51 percentage points for Qwen2.5-VL-3B and 4.06 points for Qwen2.5-VL-7B, providing evidence that broad procedural training can transfer beyond the generated task distributions. Project page: https://maveryn.github.io/trace/.
