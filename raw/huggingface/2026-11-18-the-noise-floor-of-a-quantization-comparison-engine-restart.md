---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.15671
url: https://huggingface.co/papers/2611.15671
arxiv_url: https://arxiv.org/abs/2611.15671
date: 2026-11-18
---

# The Noise Floor of a Quantization Comparison: Engine, restart, batch and kernel drift, measured against 8-bit and 4-bit effects in two decision models

A quantized model is usually judged by comparing it with its BF16 original, but that comparison changes more than the weights. It often changes the serving engine, it always runs on a different server instance, it may change how requests are batched, and on some stacks the library selects a different kernel depending only on which packages import. We measure each of these sources on the same 2,400 public decisions for two of Cloudflare's decision models, Clef-flash (9B) and Clef (27B), on an NVIDIA GB10, and state every quantization effect as the excess over them. Sources that are not quantization move between 0 and 0.92% of decisions. llama.cpp restarts are bit-identical on every record for both models. vLLM restarts flip 0, 5 and 20 decisions at BF16, FP8 and NVFP4 on Clef-flash and 4, 0 and 22 on Clef; a third instance of Clef's quantized builds (exploratory) leaves FP8 at 0 and puts NVFP4 at 4 to 22, depending on which two instances are compared. An engine change at BF16 flips 6 to 16, a batch-size change 8 to 15, and the Gated DeltaNet kernel transformers selects unasked 10 to 14. Quantization inside one engine moves more: for Clef-flash and Clef, 0.88% and 1.04% at Q8_0, 2.12% and 1.62% at FP8, 5.79% and 3.50% at Q4_K_M, and 5.79% and 5.67% at NVFP4. On both models, every 4-bit interval excludes every non-quantization source. Two of our five pre-registered predictions failed, and the same two fail when the tests are rerun on the 27B: FP8 is not inside restart noise, and changing engine moves fewer decisions than 8-bit quantization does. Accuracy hides most of this. Over the full 31,275 public questions, Clef's Q4_K_M build moves accuracy by a net six questions (-0.02 points [-0.20, +0.16]) while 436 of its decisions get worse (exploratory), and NVFP4 costs Clef-flash 0.95 points and Clef 0.65. We release the code, quantization recipes, per-record outputs and the pre-registration.
