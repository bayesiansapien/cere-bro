# Compression and architecture-efficiency shorts (2026-10-16)

**Date:** 2026-10-16 · **Source:** HuggingFace Daily Papers (15 Oct) + X following feed
**Raw:** `raw/huggingface/2026-10-15-*.md`

Six papers that each cut cost on a different axis: pruning for reasoning models, elastic sizing, looped-MoE compute, host-memory n-grams, linear-time sparse attention, and non-autoregressive decoding.

## LayerTrim: structured pruning that does not break long reasoning ([arXiv 2610.19121](https://arxiv.org/abs/2610.19121))

Structured pruning (removing whole components to get a smaller dense model) usually collapses long-form reasoning such as AIME. LayerTrim finds redundant decoder layers and trims only their **MLP features**, keeping every attention block and the full depth. Training-free, no gradients, no recovery fine-tuning. Up to **+21.4 points** average over RESP across three reasoning models and five benchmarks. On Qwen3-14B: **1.24x faster prefill, 19.7% lower peak memory**, and the shortest generations among pruned models. The win is partly that a pruned model that still reasons well also *thinks shorter*. Relation: matches the [model pruning page](model-pruning-sparsity.md) thread that attention is the fragile component and MLPs carry the slack.

## Your Transformer Is Secretly Elastic ([arXiv 2610.20588](https://arxiv.org/abs/2610.20588))

Turns one pretrained transformer into a model that runs at any compute budget, without retraining. It ranks every MLP neuron and attention head jointly on one scale by minimizing loss under soft pruning across many sparsity targets at once. Across 27 encoders (22M-8B), smooth degradation to 60% sparsity; DINOv3 ViT-H+/16 at 50% sparsity loses 0.8% ImageNet linear-probe accuracy; ViT-B/16 at 60% gets 1.80x throughput on A100. Built in minutes. Encoders only, so not yet a decoder-LLM result. Relation: the post-hoc counterpart to ShellElastic (10-15), which trains all sizes in one pretraining run.

## LatentLoop: spend less on the first loop of a looped MoE ([arXiv 2610.19975](https://arxiv.org/abs/2610.19975))

In a looped MoE (one shared block applied twice), learned residual scales show the first visit matters less. LatentLoop compresses the sequence on the first visit, keeps full resolution on the second, and spends the savings on a wider hidden size. MoE weights are shared across visits; attention is separate. Across 15 configs (1.3B-7B, up to 10^21 FLOPs): **19.0% predicted compute savings vs vanilla MoE, 7.9% vs the looped baseline**. Relation: [looped transformers](../llms-foundation-models/looped-transformers.md); joins ELR (10-13, loop count as a per-request dial) and ResidualQuant (10-14, per-loop KV redundancy).

## The COUNT: n-gram memory from counts, stored on cheap host RAM ([arXiv 2610.20456](https://arxiv.org/abs/2610.20456))

N-gram embedding tables scale memory separately from compute, but training them needs fast GPU memory. COUNT builds n-gram embeddings with **no learned parameters**: it stores precomputed corpus counts on host memory and weights the model's own unembeddings of the tokens that most often follow the current n-gram. At fixed compute, adding it to a 1B pretraining run improves validation loss **as much as 57% more compute**. Swap in a domain corpus's count table at inference to adapt without training. Relation: a third answer to the [conditional memory](conditional-memory-embeddings.md) page's open disagreement. Engram addresses by token ID (prefetchable), MoME by hidden state (not prefetchable); COUNT addresses by token ID and has nothing to train, so the table lives in DRAM by design.

## FreeSolo: linear-time sparse attention that extrapolates ([arXiv 2610.17191](https://arxiv.org/abs/2610.17191))

A sliding-window branch plus a long-range branch that picks "keypoint cells" for direct token attention. FS-L learns to prune the prefix before selection with short continued pretraining; FS-B searches balanced trees at O(N log² N). Better zero-shot length extrapolation than baselines, no long-context fine-tuning. Abstract gives no throughput numbers.

## Next-Concept Modeling: coarse-to-fine parallel text generation ([arXiv 2610.14162](https://arxiv.org/abs/2610.14162)) (cross-source confirmed via social: HF + @Azaliamirh thread)

A multiscale residual VQ-VAE encodes text into a hierarchy of discrete codes. A transformer generates one level at a time, all codes in a level in parallel. Versus the strongest diffusion LM: better perplexity on LM1B at **21x speed**, competitive on OpenWebText at **10x**, matches ROUGE-L on XSum at **31x**. Beats AR and diffusion baselines on Sudoku. Small scale only; the open question is whether the VQ-VAE bottleneck holds at frontier quality. Relation: a decode-bound alternative to [speculative decoding](speculative-decoding.md).

## Also

- **Continuum Attention** ([2610.20586](https://arxiv.org/abs/2610.20586)): attention as integration over a continuous piecewise-linear memory curve, closed-form; -0.020 nats/byte vs softmax. Still quadratic.
- **History Replays Itself** ([2610.15715](https://arxiv.org/abs/2610.15715)): long-context recall in linear attention.
- **Long-Horizon RL Needs Muon** ([2610.20256](https://arxiv.org/abs/2610.20256)): a single-rollout async recipe (Muon optimizer, token-averaged loss, TIS, length and tool-error penalties) trains repo-level issue resolution better than baselines.
