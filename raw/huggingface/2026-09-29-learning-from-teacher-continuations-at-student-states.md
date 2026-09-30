---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930270+00:00
arxiv_id: 2609.36246
url: https://huggingface.co/papers/2609.36246
arxiv_url: https://arxiv.org/abs/2609.36246
date: 2026-09-29
---

# Learning from Teacher Continuations at Student States

We present OLIVE (OnLine InterVEntion). At each iteration, the evolving student policy generates a new prefix, the teacher continues it autoregressively, and the student is updated using cross-entropy computed on the teacher-generated tokens. Each design choice targets a corresponding limitation of existing distillation methods: (1) sequential covariate shift in offline supervised fine-tuning (SFT) on fixed teacher trajectories, (2) fragmented supervision under prefix failure in token-level on-policy distillation (OPD), and (3) the need for access to teacher token probabilities in distribution-matching distillation. OLIVE achieves higher reasoning performance than OPD (with a top-16 KL approximation) at comparable GPU-hour cost. Our asynchronous implementation further reduces OLIVE's total training time by 23.8\%. We evaluate OLIVE on both hard reasoning tasks and agentic tasks which reflects modern post-training scenarios, and it consistently outperforms existing distillation methods under the same training budget. By regenerating prefixes from the evolving student, OLIVE continues improving after offline distillation plateaus while better preserving the general capabilities and plasticity of the student. Using only text from GPT-5.4-mini, continuously training with OLIVE outperforms offline SFT from the same teacher by 13\% on ScienceWorld. These results support OLIVE as an effective and efficient approach to online language-model distillation.
