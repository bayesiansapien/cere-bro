---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.499550+05:30
arxiv_id: 2610.40945
url: https://huggingface.co/papers/2610.40945
arxiv_url: https://arxiv.org/abs/2610.40945
date: 2026-11-02
---

# On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning

On-policy reinforcement learning for large language models assumes that training responses are sampled from the current policy. In practice, an inference engine samples the responses and a separate trainer computes the gradients, and the training-inference mismatch between the two makes the training data off-policy. The mismatch has two sources, the numerics of the engine and the stale weights of asynchronous sampling, and a correction that stabilizes training under one source can fail under the other. We ask which property of a mismatch source decides the correction it needs. Evaluating the trainer at the sampler's weights splits each sampled-token error exactly into a numerical discrepancy of the engine and a policy lag of the trainer, and we follow both through training. The numerical discrepancy stays approximately constant, so it biases the updates by a nearly fixed amount, and centering the score at each prefix removes its leading bias. The policy lag is produced by the trainer's own updates: the bias it leaves enters the next update, which enlarges the next lag and closes a feedback loop. Importance weighting cuts this loop only while the lag ratio stays concentrated, and on Qwen3-1.7B it fails at the step where the effective sample size of the ratio falls below one half. From this account we derive the discrepancy-lag correction (DLC), which centers the numerical discrepancy, clips the lag ratio against the sampler's weights and resynchronizes the sampler when this effective sample size falls below one half. Under a stale sampler, DLC keeps the KL divergence from on-policy training within twice the KL between two independent on-policy trainings on Qwen3-0.6B and Qwen3-1.7B, and its resynchronization prevents collapses that the per-token corrections leave and that a KL measured on the sampler's prefixes does not detect.
