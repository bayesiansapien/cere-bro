---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934293+00:00
arxiv_id: 2609.33391
url: https://huggingface.co/papers/2609.33391
arxiv_url: https://arxiv.org/abs/2609.33391
date: 2026-09-29
---

# Beyond Timestamps: Decision-Aligned On-Policy Distillation for Long-Horizon Agents

Reinforcement learning with verifiable rewards (RLVR) often relies on sparse outcome rewards, providing coarse supervision for long-horizon agents. On-policy self-distillation (OPSD) complements this signal with dense privileged feedback. However, we identify Decision--Timestamp Mismatch: privileged guidance may be misaligned with the student's functional decision because the corresponding decision can occur at a different timestep, while the student's decision itself may span multiple timesteps rather than being tied to a single timestamp. Thus, timestamp-local supervision can misalign both the context and the temporal scope of credit. To address this mismatch, we introduce AlignOPSD, following the principle of aligning supervision before assigning credit. Decision-Aligned Supervision Rectification re-scores the same student-sampled response in functionally matched contexts across sibling rollouts to calibrate local teacher evidence. Semi-Markov Hierarchical Credit Assignment then derives variable-duration decision spans from correspondence changes and uses rectified evidence to allocate outcome-grounded credit across spans and their constituent turns. We evaluate AlignOPSD with Qwen2.5-3B and Qwen2.5-7B on ALFWorld, WebShop, and Search-QA against representative baselines. AlignOPSD outperforms both GRPO and StepOPSD across all eight backbone--aggregate-metric comparisons, improving on GRPO by 5.5--8.7 \% and ranking first in six. Additional analyzes examine the two alignment stages and hyperparameter sensitivity between tasks. Our code is avaliable at https://github.com/mingju-c/Align-OPSD
