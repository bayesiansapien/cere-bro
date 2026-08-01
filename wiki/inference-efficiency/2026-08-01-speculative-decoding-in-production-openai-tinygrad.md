# Speculative Decoding Leaves the Lab: OpenAI's 13x Price Move and tinygrad's 245 tok/s

**Date ingested:** 2026-08-01
**Sources:** [AI Breakfast, 07-31](../../raw/gmail/2026-08-01-starred.md) citing [OpenAI's price-performance post](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) · [@__tinygrad__ benchmark, 08-01](https://x.com/__tinygrad__/status/2083452143319896210) · [The Decoder on the Luna cut](https://the-decoder.com/openai-goes-full-china-pricing-mode-with-an-80-percent-cut-to-its-most-affordable-gpt-5-6-model/)
**Raw:** [Gmail starred](../../raw/gmail/2026-08-01-starred.md) · [Twitter afternoon](../../raw/twitter/2026-08-01-afternoon.md) · [tinybox benchmark image](../../raw/twitter/images/2026-08-01/2083452143319896210-0.jpg)

---

## TL;DR

Two independent data points landed within a day of each other showing speculative decoding is now the load-bearing component of production inference economics rather than a research technique. OpenAI attributes its GPT-5.6 price cuts to internal infrastructure work rather than a new model: **speculative decoding raising token generation 15% and cutting GPU serving cost 20%**, which cascaded into an **80% price cut on GPT-5.6 Luna** (to $0.20 per million input, $1.20 per million output), a 20% cut on Terra, and moving Auto-review in ChatGPT and Codex CLI onto Luna for a **10x cost reduction**. AI Breakfast's framing of the whole set is a **13x** drop in the cost of the same intelligence, since Luna now matches March's full GPT-5.4 flagship at one-thirteenth the token price. On the same day tinygrad published a full serving profile for **DeepSeek-V4-Flash-0731 on two RTX Pro 6000 Blackwell GPUs**: **~245 tok/s sustained single-user**, median TPOT ~2.8 ms, TTFT ~0.4 s, using **DSpark K5 fixed-depth speculative decode**, W4A8 kernels and an **fp8 KV cache** at 131k max context. That single-user number **beats the runbook's own validated 217 to 220 tok/s**.

The two together are the answer to a question yesterday's [lossy verification audit](2026-07-31-lossy-verification-speculative-decoding.md) raised and could not answer: how much of the current price collapse is riding on speculative decoding, and therefore how much is exposed to the audit's finding that relaxed verification silently rewrites the output distribution.

---

## The tinygrad numbers in full

| Scenario | Output tok/s | Notes |
|---|---|---|
| Single user (CC1, 128→512) | **~245 sustained** | median TPOT ~2.8 ms → ~300–350 tok/s instantaneous; TTFT ~0.4 s |
| Concurrent ×16 (128→512) | **608 total** | TPOT ~17 ms per stream; **DSpark accept 63.8%** |
| Concurrent ×16, long ctx (8192→512) | **499 decode** | **8,477 tok/s total including prefill** (~10.6k prefill tok/s); **DSpark accept 90.5%, accept-len 5.52** |

Settings: vLLM "Gilded Gnosis" r16, B12X W4A8 kernels, DSpark K5 fixed-depth speculative decode, fp8 KV cache, 131k max context, temp 0, random-token prompts. Running on **2 of 4 GPUs** (TP=2, ~95 GB used each, GPUs 2 and 3 idle), which is why tiny corp simultaneously launched a **2-GPU tinybox variant**.

The honest caveat is in tinygrad's own footnote and is the most valuable line in the post: **long-context acceptance is inflated by repetitive random tokens, and real code is approximately 64%.** So the headline 90.5% acceptance is a synthetic-prompt artifact and the deployable number is the 63.8% figure. Very few vendors publish the deflated number next to the inflated one.

---

## Why this pairs with yesterday's audit

[Revisiting Lossy Verification in Speculative Decoding (07-31)](2026-07-31-lossy-verification-speculative-decoding.md) found that every published relaxation of speculative decoding's exact rejection sampling falls into two families, **truncation-based** and **collaborative**; that truncation-based methods can perform *worse* than the true truncation-sampling baseline they approximate; and that collaborative verification's single controlling quantity is **how far draft probabilities overshoot target probabilities**. Its conclusion was that relaxed verification silently rewrites the decoding distribution and nobody measures the object that changed.

Today supplies the deployment context that makes that finding urgent rather than academic. When speculative decoding was a 1.5x nice-to-have, a quality tax hidden in the tails was tolerable. When it is the stated mechanism behind an 80% price cut on a frontier-lab endpoint, and the stated mechanism behind a practitioner beating a vendor runbook by 12%, the distribution being rewritten is the distribution most production traffic is now sampled from. **Neither OpenAI nor tinygrad states whether its verifier is lossless.** OpenAI's post frames the change as pure infrastructure efficiency, which implies lossless rejection sampling, but does not say so. DSpark K5 is a fixed-depth scheme whose family membership is not public.

The checklist the audit implies is two questions long and neither party has answered it.

---

## What is actually new here

Three things, none of them a technique:

1. **Speculative decoding is now priced.** A 15% generation increase and 20% serving-cost reduction converting into an 80% list-price cut is the first public mapping from a serving-stack optimisation to an endpoint price. It also tells you the margin structure: a 20% cost improvement supporting an 80% price cut means the cut is competitive rather than cost-driven, and the speculative decoding gain is the cover story that makes it survivable.
2. **A four-bit weight, eight-bit activation, fp8 KV cache, speculative decode stack is a single configuration a hobbyist can run.** Every one of those was a separate research line eighteen months ago. tinygrad's profile is all four composed, on two consumer-adjacent workstation GPUs, serving a 304B-parameter model.
3. **Acceptance rate is workload-dependent by 27 points.** 90.5% on repetitive synthetic tokens against ~64% on real code, on the same model and the same scheme. Any speculative-decoding speedup quoted without the prompt distribution is unfalsifiable.

---

## How this relates to prior wiki pages

**It closes the loop on the [speculative-decoding](speculative-decoding.md) page's central open question.** That page has tracked whether speculative decoding's gains survive contact with production serving, and has been carrying [VIA-SD (06-12)](../ai-routing/2026-06-12-via-sd-intra-model-routing-speculative-decoding.md), which carves a slim verifier out of the full verifier so medium-confidence tokens get cheaply regenerated, with an open note asking whether its regeneration path is exactly lossless. Today's answer is that production is not waiting for the question to be settled.

**It is the industrial half of the pattern [Memory Decoder (07-31)](2026-07-31-memory-decoder-at-scale.md) opened.** That paper argued the parameter budget contains a separable memory component nobody prices. tinygrad's profile shows the serving budget contains four separable components (weight precision, activation precision, KV precision, draft depth) that practitioners now tune jointly and that no model card reports. Both are versions of the same complaint: the published spec of a model tells you almost nothing about what it costs to run.

**It contradicts nothing and confirms one thing about [DeepSeek V4-Flash](../daily-digest/2026-07/2026-07-31.md).** Yesterday the wiki logged V4-Flash jumping ten points to 50 on the Artificial Analysis Intelligence Index at roughly 60% lower cost per task than GPT-5.6 Luna, from the vendor's own pricing. tinygrad's numbers are the first independent confirmation that the model is genuinely cheap to *serve*, not just cheap to buy, which are different claims and only the second one is a durable property.

---

## Research angle

The measurement nobody is publishing: **acceptance rate as a function of prompt distribution, reported alongside every speculative-decoding speedup.** tinygrad's 90.5% versus 64% split is a 27-point gap discovered by one honest footnote, and it implies most published speculative-decoding speedups are quoted at an acceptance rate their deployment will not see. A standard reporting convention (acceptance on synthetic, on code, on natural prose, on multi-turn chat) would cost nothing and would make the literature comparable for the first time.

Second, the composition question. W4A8 weights, fp8 KV cache and a speculative draft all perturb the output distribution, and every paper studies one at a time. Nobody has measured whether the perturbations compose additively or interact, and the interaction that matters is between quantisation error in the draft model and the verifier's acceptance test, because a quantised draft is systematically *miscalibrated* rather than merely noisy, which is exactly the overshoot condition yesterday's audit named as the failure mode for collaborative verification.

---

## Related pages

- [Speculative Decoding](speculative-decoding.md)
- [Lossy Verification in Speculative Decoding (07-31)](2026-07-31-lossy-verification-speculative-decoding.md)
- [KV Cache](kv-cache.md)
- [GPU Kernels](../hardware/gpu-kernels.md)
- [MXAttention (08-01)](2026-08-01-mxattention-mxfp4-attention-quantization.md)
