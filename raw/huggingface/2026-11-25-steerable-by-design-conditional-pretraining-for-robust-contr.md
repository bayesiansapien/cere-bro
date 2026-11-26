---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32199
url: https://huggingface.co/papers/2611.32199
arxiv_url: https://arxiv.org/abs/2611.32199
date: 2026-11-25
---

# Steerable by Design: Conditional Pretraining for Robust Control of Language Models

Our goal is to build language models that are steerable by design. Today's language models are pretrained with next-token prediction, which relegates alignment and control to the final 1% of training tokens or inference-time interventions. These models repurpose a single input channel for both instructions and data, leading to common failure modes where the model mistakenly treats data as instructions such as intentional jailbreaks and unintentional in-context alignment drift. To correct this, we propose a pretraining method and architecture that separates the two from the very start, producing Mancelle-3B. An encoder processes high-level semantic features of upcoming text with cross-attention that prevents the token stream from writing back into this control channel. During pretraining, the model learns to rely on these features to predict the next token, turning the channel into an effective handle for steering the model. Mancelle-3B steers more strongly than prompt- and activation-based methods on comparable open models while maintaining fluency, and it withstands adversarial black-box and soft-prompt counter-steering that defeats those baselines. We reproduce this against a more controlled baseline with Mancelle-400M. Our results show that robust control can be built into language models if we do so early and intentionally.
