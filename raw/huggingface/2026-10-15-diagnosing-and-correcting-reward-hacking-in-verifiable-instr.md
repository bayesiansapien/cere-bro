---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.227810+05:30
arxiv_id: 2610.19525
url: https://huggingface.co/papers/2610.19525
arxiv_url: https://arxiv.org/abs/2610.19525
date: 2026-10-15
---

# Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following

Verifiable instruction-following benchmarks emphasize output-constraint satisfaction but can overlook whether responses meaningfully answer the underlying request, creating an evaluation blind spot. We show that frontier models can receive full credit for responses with little substantive answer content. Using the same verifier-based criterion as a training reward can induce reward hacking, as publicly released checkpoints exhibit higher constraint satisfaction but lower response quality after reinforcement learning with verifiable rewards. To address this reward hacking, we introduce CALIF, a lightweight method that augments verifier rewards with a calibrated likelihood-based bonus to preserve response quality. CALIF evaluates response likelihood under the request alone using the existing frozen reference policy, requiring no additional judge or learned reward model. Across models ranging from 1.7B to 8B in reasoning and non-reasoning modes, CALIF improves constraint satisfaction on IFBench while maintaining response quality near or above pre-RL levels. It also outperforms corresponding base policies in 40 of 45 model-metric comparisons across three rubric-based instruction-following benchmarks, demonstrating gains beyond training verifiers.
