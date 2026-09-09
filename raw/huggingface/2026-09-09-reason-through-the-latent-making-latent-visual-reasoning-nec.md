---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06746
url: https://huggingface.co/papers/2609.06746
arxiv_url: https://arxiv.org/abs/2609.06746
date: 2026-09-09
---

# Reason Through the Latent! Making Latent Visual Reasoning Necessary

Latent visual reasoning aims to perform multimodal reasoning through hidden-state computation rather than explicit textual chains of thought. However, visual information being present in a latent state does not imply that the model actually relies on that state when producing its answer, especially when alternative image-conditioned paths remain available. We introduce Causal Visual Recurrent Reasoning (CVRR), which preserves pretrained visual competence while making recurrent computation the required image-conditioned path to prediction. CVRR initializes recurrence from the question hidden state after the pretrained vision-language model has incorporated the image, then repeatedly updates this state while re-reading the same fixed visual evidence. Before decoding, visual states and the original multimodal KV cache are removed so that only the final recurrent state carries image-conditioned information to the answer. Across the V^*, MMVP, BLINK, and MME-RealWorld-Lite benchmarks, CVRR retains strong performance under this strict interface, while compatible latent reasoners fail to recover comparable visual competence even when retrained under the same constraint. Causal interventions further show that predictions remain sensitive to recurrent content when the question is held fixed, and that persistent visual evidence causally revises the recurrent trajectory. These results distinguish latent informativeness from latent computation that is actually used for prediction.
