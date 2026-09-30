---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.928776+00:00
arxiv_id: 2609.32704
url: https://huggingface.co/papers/2609.32704
arxiv_url: https://arxiv.org/abs/2609.32704
date: 2026-09-29
---

# CoWindow Attention: Full Causal Coverage Is a Collective Property

FullAttn repeatedly exposes the complete causal history to every attention head, creating substantial redundant computation and memory traffic even with IO-efficient dense kernels. We introduce CoWA, a structured attention architecture that distributes access to the causal history across KV heads. All heads share near-diagonal and prefix-sink windows, while complementary long-range windows partition the remaining history. Their union provides full causal coverage although each head attends sparsely to distant tokens. This position-defined attention pattern requires no learned router or indexer, is used consistently during training and inference, and aligns with KV-head tensor parallelism. A window-matched ablation at 8K isolates the effect of complementary long-range allocation: CoWA with 100% collective coverage reaches 89.73% accuracy, compared with 89.97% for FullAttn, while duplicated long-range windows perform substantially worse. Across a broader controlled associative-recall comparison with matched token budgets, CoWA closely tracks FullAttn as the context grows, whereas other sparse patterns lose a substantial fraction of the associations. In an attention-operator benchmark at 128K tokens with tensor parallelism, CoWA reduces forward and backward latency during training by 7.4x and 8.6x and decoding latency during inference by 3.0x over FullAttn. Its per-rank peak operator memory matches FullAttn during training and is 7.6x lower during decoding. Across scaling-law training from 0.6B to 14B parameters, CoWA closely tracks FullAttn in perplexity while reducing total training FLOPs. The resulting 14B models and 32B models from separate continued training achieve comparable knowledge, reasoning, and long-context retrieval scores to FullAttn. These results show that full causal coverage can be a collective property of the head ensemble rather than a duplicated property of every head.
