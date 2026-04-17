---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2509.25843
url: https://huggingface.co/papers/2509.25843
arxiv_url: https://arxiv.org/abs/2509.25843
date: 2026-04-17
---

# ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack

Large language models (LLMs), despite being safety-aligned, exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes. As tense jailbreaking demonstrates that models refusing harmful requests often comply when rephrased in past tense, a critical generalization gap is revealed in current alignment methods whose underlying mechanisms are poorly understood. In this work, we introduce Activation-Scaling Guard (ASGuard), an insightful, mechanistically-informed framework that surgically mitigates this specific vulnerability. In the first step, we use circuit analysis to identify the specific attention heads causally linked to the targeted jailbreaking such as a tense-changing attack. Second, we train a precise, channel-wise scaling vector to recalibrate the activation of tense vulnerable heads. Lastly, we apply it into a preventative fine-tuning, forcing the model to learn a more robust refusal mechanism. Across four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility. Our findings underscore how adversarial suffixes suppress the propagation of the refusal-mediating direction, based on mechanistic analysis.
