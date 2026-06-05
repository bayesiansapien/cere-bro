---
source: farmer/huggingface
farmed: 2026-06-05T08:18:05.247595+00:00
arxiv_id: 2606.06021
url: https://huggingface.co/papers/2606.06021
arxiv_url: https://arxiv.org/abs/2606.06021
date: 2026-06-05
upvotes: 2
---

# OPRD: On-Policy Representation Distillation

On-policy distillation (OPD) supervises the student only in output space by matching next-token probabilities. This output-only paradigm has two limits: (1) sampling variance from Monte Carlo KL estimates over large vocabularies (e.g., Qwen's ~150k tokens) persists throughout training, and (2) it treats the teacher as a black-box, discarding all intermediate hidden states after the LM head. We propose On-Policy Representation Distillation (OPRD), which lifts distillation into hidden-state space by aligning student and teacher representations across selected layers on the same rollouts, bypassing the LM head entirely. Theoretically, OPRD eliminates sampling variance and provides richer per-layer structural information. Empirically, OPRD closes the student-teacher gap on AIME 2024/2025 and AIMO, while output-space OPD baselines plateau below the teacher. OPRD also trains 1.44x faster and uses 54% less memory than top-k OPD. Code: https://github.com/ShenzhiYang2000/OPRD.
