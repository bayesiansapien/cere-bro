---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.06221
url: https://huggingface.co/papers/2605.06221
arxiv_url: https://arxiv.org/abs/2605.06221
date: 2026-05-11
---

# UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification

As large language models (LLMs) continue to advance rapidly, they are becoming increasingly capable while simultaneously demanding ever-longer context lengths. To improve the inference efficiency of long-context processing, several novel low-complexity hybrid architectures have recently been proposed, effectively alleviating the computational burden of long-context inference. However, existing research on long-context prefill acceleration remains predominantly focused on sparse attention mechanisms, which achieve their maximum speedup only on full-attention models. When transferred to emerging architectures - such as linear/full attention hybrids or sliding window/full attention hybrids - these prefill acceleration approaches suffer significant performance degradation. Furthermore, such methods are generally incompatible with continuous batching, making them difficult to integrate into modern inference engines such as vLLM. To this end, we propose UniPrefill, a prefill acceleration framework applicable to virtually any model architecture, which directly accelerates the model's computation at the token level. We further implement UniPrefill as a continuous batching operator and extend vLLM's scheduling strategy to natively support prefill-decode co-processing and tensor parallel for UniPrefill, enabling its seamless integration into vLLM. UniPrefill achieves up to 2.1x speedup in Time-To-First-Token (TTFT), with the acceleration becoming increasingly pronounced as the number of concurrent requests grows.
