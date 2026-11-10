# Your KV Cache Can Spot Attacks on Your AI Agents (Ari Azarafrooz, Intrinsec AI)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=1NWnSwCB4NM

## TL;DR
The KV cache is a record of the model's computation on every input, and serving stacks already keep it, page it and move it around. Azarafrooz proposes mining it as a security signal. You learn a baseline distribution of KV pages for your workload, flag rare pages as anomalies, then classify or explain them. This complements input/output judge models, catches whatever slips past them (it still becomes computation), and needs no access to plaintext, which helps in privacy-constrained deployments. Short vendor pitch with promising but thin evidence.

## Key Takeaways
- **Recipe:** (1) baseline the KV page distribution of normal traffic, (2) detect pages that are rare relative to the baseline, (3) classify or explain them with a model that takes KV pages as features.
- **Two integration points:**
  - **Inline in the engine** (vLLM, SGLang and similar): real time. Alerts can be attached to later tool calls so downstream policy hardens on the fly.
  - **Offline over the KV store** (LMCache tier, or the routing layer in llm-d or NVIDIA Dynamo): threat discovery over pages already persisted from GPU to remote storage.
- **Voice agent demo:** used a Gemma-class "4B" audio model. Baseline: 72 benign clips in 4 voices, 16-token pages. A clip with a hidden spoken instruction was flagged, and the anomaly was localized to specific pages. A KV-feature explainer that was never trained on audio still tagged PII categories (home address, location, travel destination).
- **Text agent demo:** a ~14B model served live on vLLM with LMCache. On an agent-failure benchmark from Hugging Face (benign traces plus 8 failure types, such as injected tool descriptions and misinformation), 7 to 8 of the top 10 anomaly alerts were real, meaningful failures (precision@10 of about 0.7 to 0.8).
- **Hard production problems the speaker admits:**
  - **Model heterogeneity:** fine-tunes, multi-model agents and routers that pick a specialist per request each write KV in their own coordinate space. You either keep one baseline per model (expensive) or learn a shared representation across models.
  - **Data movement:** one 256-token chunk is about 40 MB of KV on a mid-size model. Even with CacheGen-style compression, streaming it out for real-time analysis is slow.

## Architecture & Optimization Mechanics
- **Why it might work:** an injected instruction changes attention patterns and key/value statistics in ways a surface classifier can miss, especially for audio or obfuscated text. Page-level granularity (vLLM's PagedAttention block) gives a natural unit for localizing the anomaly.
- **The cost problem lands on infra people:** KV is the largest transient object in serving. Anything that reads it competes with decode bandwidth. A practical design would compute cheap per-page sketches on GPU at prefill time (norms, low-rank projections, attention entropy) and ship only kilobytes, not raw pages.
- **Tension with compression:** KV quantization (FP8/INT4), eviction (H2O, SnapKV) and cross-layer sharing all perturb the very statistics this method baselines. The baseline must be learned under the same compression config, and switching quantization schemes invalidates it.
- **Routing link:** the shared-representation problem is the same one a cross-model router faces. A model-agnostic KV embedding would be a reusable asset for both security and routing (for example as a difficulty or uncertainty signal).

## Grounded Context (Web Enrichment)
I found no public footprint for "Intrinsec AI" or a paper behind these numbers, so the results are vendor-reported, with tiny baselines (72 clips) and precision@10 as the only metric. That is not enough to judge false-positive rates at production traffic volumes. Adjacent academic work supports the premise. RedVisor (February 2026) defends against prompt injection with a lightweight adapter and reuses the KV cache to avoid a second prefill ([arXiv 2602.01795](https://arxiv.org/abs/2602.01795)). "Latent Introspection" shows models can detect earlier concept injections from information encoded in their cached representations ([arXiv 2602.20031](https://arxiv.org/pdf/2602.20031)).

The flip side matters too. Work on Malicious Token Injection treats the KV cache itself as an attack surface: perturbing cached keys changes model behavior even when prompts and weights are secure ([arXiv 2510.17098](https://arxiv.org/html/2510.17098v2)). HiddenLayer has described backdoors that hold state in KV positions and fire on tool-call triggers ([HiddenLayer](https://hiddenlayer.com/innovation-hub/research)). With KV now persisted and shared across workers (LMCache, llm-d, Dynamo), cache integrity is as much a security question as cache observability.

## Real-World Application / Actionable Step
- **Cheap experiment:** on your vLLM setup, hook prefill to log per-block summary statistics (per-head key norm, value norm, attention entropy) for a benign corpus. Then run a prompt-injection set (for example from AgentDojo or InjecAgent) and measure AUROC with a simple Isolation Forest. A day of work tells you whether the signal is real for your models.
- **Test robustness to compression:** repeat the experiment under FP8 and INT4 KV quantization and with an eviction policy. If detection survives aggressive KV compression, that is a publishable result connecting your compression work to security.
- **For routing:** test whether the same KV-sketch features predict "this query needs the big model". One feature pipeline could serve both anomaly detection and routing decisions.
