---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.928610+00:00
arxiv_id: 2609.32712
url: https://huggingface.co/papers/2609.32712
arxiv_url: https://arxiv.org/abs/2609.32712
date: 2026-09-29
---

# MassAlloc Attention: Let Attention Allocate Its Own Compute

FullAttn often assigns negligible normalized mass to much of the causal score space, yet dense kernels execute the complete post-score path after forming each QK tile. We introduce MALA, a fused attention primitive that preserves score access to every legal causal interaction and uses normalized contribution to allocate post-score computation. Forward uses its evolving online-softmax normalizer, while backward reuses the finalized normalizer to derive nested retained support using only standard attention state. A common tolerance governs training and inference, allowing for adaptive retention of the work. MALA reduces low-contribution post-score computation. A matched-work study at 8K isolates the benefit of distribution-adaptive allocation: under exactly matched total post-score work, MALA approaches a per-instance reference-mass oracle, with mean omitted mass of 0.0188% versus 0.0182%. Across context lengths from 1K to 32K tokens, the same tolerance maintains low output and gradient errors relative to the reference. Across a broader controlled associative-recall comparison, MALA closely tracks FullAttn as context grows, reaching 89.67% accuracy at 8K compared with 89.97% for FullAttn. In an attention-operator benchmark at 128K tokens with tensor parallelism, MALA reduces forward and backward latency during training by 2.2x and 3.0x and decoding latency during inference by 1.6x relative to FullAttn. Across scaling-law training from 0.6B to 14B parameters, MALA closely tracks FullAttn in perplexity while reducing total training FLOPs. The resulting 14B models and 32B models from separate continued training achieve comparable knowledge, reasoning, and long-context retrieval scores to FullAttn. These results indicate that allocating post-score computation according to normalized attention contributions can retain the evaluated capabilities of FullAttn while reducing attention computation.
