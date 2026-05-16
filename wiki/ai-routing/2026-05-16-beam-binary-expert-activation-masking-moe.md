# BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE

**Source:** HuggingFace Daily Papers · [arXiv 2605.14438](https://arxiv.org/abs/2605.14438)
**Raw:** [farmer file](../../raw/huggingface/2026-05-16-beam-binary-expert-activation-masking-for-dynamic-routing-in.md)
**Tier:** 1 — MoE routing, dynamic sparsity, inference efficiency, vLLM-integrated CUDA kernel

## TL;DR

BEAM (Binary Expert Activation Masking) replaces fixed Top-K MoE routing with **token-adaptive trainable binary masks** trained via straight-through estimator plus an auxiliary regularization on activation count. End-to-end training induces dynamic sparsity instead of bolting it on after the fact, which is what prior acceleration methods do at high sparsity with severe quality drops from train-inference mismatch. A custom CUDA kernel ships with vLLM integration. The result: >98% of original model performance, up to 85% MoE-layer FLOP reduction, 2.5x faster decoding, 1.4x higher throughput. Plug-and-play.

## Why it matters

Fixed Top-K is the wrong abstraction. Some tokens need three experts, some need one, some need zero, but every token gets exactly K. BEAM lets each token learn its own expert count subject to a budget. This is the third paper in the wiki proposing a per-token expert-routing reform after **CaRE** (bi-level routing across tasks, [2026-05-11](../ai-routing/2026-05-11-care-bi-level-routing-moe-continual-learning.md)) and **DLR** (training-time joint code-policy-parameter learning, [2026-05-15](../ai-routing/2026-05-15-dlr-dynamic-latent-routing-post-training.md)). Each operates at a different granularity: CaRE selects task routers above experts, DLR learns latent codes alongside model parameters, BEAM masks expert activations per token. Three different mechanisms, one shared diagnosis: routing was the wrong unit of analysis when it was modeled as a switch.

The vLLM kernel is the deployment-side detail that makes this paper actionable rather than theoretical. Most MoE-acceleration work in the literature reports flop savings on paper and dies at the kernel. BEAM ships the kernel.

## Connections to prior wiki state

- **CaRE Bi-Level Routing MoE** ([2026-05-11](2026-05-11-care-bi-level-routing-moe-continual-learning.md)) added the task-axis routing layer above experts. BEAM adds dynamic per-token sparsity below experts. Stacked, they describe a full routing surface: task router selects expert routers, expert router activates a learned token-adaptive subset of experts. Neither paper composes with the other; the composition has not been written.
- **DLR Dynamic Latent Routing** ([2026-05-15](2026-05-15-dlr-dynamic-latent-routing-post-training.md)) made routing a training-time concern. BEAM makes the expert activation mask a training-time concern. Both papers shift the "where is the routing decision actually learned" question from deployment to training. The composition (DLR latent codes as the input to BEAM's mask network) is a one-paper extension.
- **MISA** (2026-05-11, head-axis routing) extends to sparse attention indexer heads. With BEAM, two of the four obvious "routing inside the model" axes (expert axis, head axis) now have published mechanisms.
- **Make Each Token Count** ([2026-05-12](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md)) treated the KV cache as a programmable substrate with token-level eviction policies. BEAM is the MoE-expert analogue: an expert-set-per-token policy learned at training time, not heuristic.
- **NVFP4 Kimi-K2.6** (NVIDIA release, 2026-05-15 digest) and **TurboQuant** (vLLM blog) are the per-token-bytes axis. BEAM is the per-token-experts axis. The two compose multiplicatively: NVFP4 reduces bytes-per-expert; BEAM reduces experts-per-token. For Kimi-K2 family on Blackwell, a >4x throughput stack is now buildable from public components.

## How it works

For each token at each MoE layer, BEAM computes a binary mask over experts. The mask is parameterized by a trainable gating head; straight-through estimator carries gradients through the binarization. An auxiliary regularization loss penalizes deviation from a target average activation count, which is what gives the model headroom to drop experts on easy tokens and add them on hard ones. Train end-to-end, ship the trained mask network, run inference with the custom kernel.

The vLLM kernel exploits the binary mask structure: instead of indexing into K specific experts as in Top-K, it iterates only over the experts that the mask selects, with a contiguous-memory layout that avoids the gather-scatter overhead that has historically killed dynamic-K MoE inference.

## Open problems / Research angle

- **BEAM + DLR composition.** DLR's discrete latent codes are causally distinct routing signals. If they drive BEAM's mask network, the activation count becomes a function of the model's own internal task representation. One-paper extension, untested.
- **Quality-vs-sparsity Pareto under verifier-graded eval.** WildClawBench (2026-05-15) showed harness shifts can move scores by 18 points. Whether BEAM's >98% retention holds under native-runtime grading is unmeasured. Falsifiable: a 60-day follow-up measuring BEAM at multiple sparsity levels on WildClawBench-style native eval.
- **BEAM for the indexer-head axis.** MISA (2026-05-11) routes 64 indexer heads in sparse attention. Same mechanism (binary mask, STE, regularized activation count) should transfer directly. Falsifiable: a paper that ships this and reports >98% retention at >50% head-FLOP reduction.
- **Train-side cost.** Auxiliary regularization + STE typically costs training time. The paper does not quantify the training-time hit, only the inference-time win. If pre-training cost goes up by >20%, the deployment story changes for frontier-scale runs.

## Concept tags

`mixture-of-experts` · `dynamic-routing` · `binary-mask` · `straight-through-estimator` · `vllm-kernel` · `inference-efficiency`
