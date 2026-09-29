---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.593894+00:00
arxiv_id: 2609.26333
url: https://huggingface.co/papers/2609.26333
arxiv_url: https://arxiv.org/abs/2609.26333
date: 2026-09-28
---

# Disaggregated Quantization: Specializing LLM Prefill and Decode

Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation. We propose "disaggregated quantization" (DQ), which specializes computation formats, weights and storage placement to both of these phases. On Qwen 3 and Gemma 3, removing activation quantization specifically on decode improves accuracy on decode-heavy tasks without increasing inference cost. Training separate compute-native prefill weights accelerates prompt processing relative to weight-only inference while matching or exceeding its accuracy at 2-3-bit decode on both decode-heavy and prefill-heavy tasks. With released Qwen3.8-27B GGUF decoders, training an NVFP4 prefiller improves 1-bit accuracy by 32.5 points on MMLU-Pro and 35.3 on MMMU-Pro without modifying the decode checkpoint. To accommodate the additional checkpoint on a single device, offloaded disaggregated prefill (ODP) streams its weights from SSD, amortizing loading over prompt length. On the same 27B model, ODP delivers a 1.78x time-to-first-token speedup over the weight-only baseline at 8K prompt length in llama.cpp. We evaluate accuracy under disaggregated serving in vLLM and further validate shared-weight format disaggregation through post-training quantization on models up to 2.8T parameters.
