---
source: farmer/huggingface
farmed: 2026-08-31T10:31:04.593371+05:30
arxiv_id: 2608.25697
url: https://huggingface.co/papers/2608.25697
arxiv_url: https://arxiv.org/abs/2608.25697
date: 2026-08-31
---

# LMSM: LLM Security Framework Inspired by Linux Security Modules

Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals are not security controls by themselves. Deployments that adapt them for safety typically couple each signal to its own calibration, policy logic, and intervention code, so each new artifact creates integration work instead of strengthening a shared defense. We present Language Model Security Modules (LMSM), a security framework that adapts the separation behind Linux Security Modules (LSM) to LLM serving. In LMSM, a selected security backend exposes calibrated evidence, a versioned policy evaluates active rules over trusted per-request context, and a separate gate authorizes buffered output release. This design separates mediation correctness from policy effectiveness, and it allows backend, rule, or schedule changes without rebuilding request handling or enforcement. Our prototype shows the separation working in practice: with Hugging Face Transformers and continuously batched vLLM, the same substrate hosts artifact-backed sparse autoencoder (SAE) and transcoder deployments and task-fitted dense probes, preserves request-specific decisions under scheduler churn, and selectively enforces and composes multiple rules per request. On Qwen3-4B, LMSM-Checkpoint reduces HarmBench attack success rate from 39.20% to 3.32%, with XSTest false refusals rising from 2.40% to 4.40%, while retaining 98.14% of the throughput of a matched serving path that performs no monitoring work at 32 active sequences. LMSM gives advances in interpretability and model-internal analysis a common path to runtime enforcement.
