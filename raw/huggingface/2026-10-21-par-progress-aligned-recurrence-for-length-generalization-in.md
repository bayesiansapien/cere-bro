---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.638813
arxiv_id: 2610.27628
url: https://huggingface.co/papers/2610.27628
arxiv_url: https://arxiv.org/abs/2610.27628
date: 2026-10-21
---

# PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking

Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent state. We introduce Progress-Aligned Recurrence (PAR), which trains the prediction at iteration k to match the state after the first k operations and rescales recurrent states to their first-iteration norms. On swap-S_5, a Qwen2.5-0.5B model trained on at most 32 moves achieves 95.5\% mean full-state accuracy at 512 moves, or 16times the training length, compared with 55.7\% reported for RLT and 0.8\% for explicit chain of thought on the same backbone. Controlled S_5 ablations show that removing norm anchoring reduces the extrapolation factor from 16times to below 2.2times, and replacing progress-aligned targets with final-answer supervision reduces it to at most 8times. A learned completion readout selects when to answer without a supplied stopping depth. When intermediate labels are unavailable, prefix self-distillation induces the correspondence from shorter problem prefixes using only final answers. The gains apply across sequential state-tracking tasks, establishing the task structure required for depth extrapolation. These findings support training intermediate predictions and state scale together to make additional recurrent depth useful for longer problems.
