---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.389336+00:00
arxiv_id: 2611.23835
url: https://huggingface.co/papers/2611.23835
arxiv_url: https://arxiv.org/abs/2611.23835
date: 2026-11-20
---

# NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding

Speculative decoding is widely used to speed up generation in large language models (LLMs), with a small draft model proposing tokens that one forward pass of the target model verifies. Draft models that read the target's hidden states, such as DFlash and EAGLE-3, typically inherit the target's hidden width. We show that the draft's whole residual stream can run at half or a quarter of that width while largely preserving acceptance. For DFlash, which borrows the target's vocabulary projection, the trained output adapter folds into it, giving one narrower projection with logits unchanged up to floating-point rounding. We test two drafter families, DFlash and EAGLE-3, on two targets, Qwen3-8B (NVFP4) and GPT-OSS-20B (MXFP4), in SGLang on a B200 and a DGX Spark (GB10). At batch size 1 and temperature 0, narrowing the draft to half or a quarter width speeds up end-to-end decoding by 1.06-1.12x on B200 and 1.13-1.44x on GB10. The speedup holds at larger batch sizes. From batch 32 to the largest batch each GPU fits, narrowing reaches up to 1.21x on both GPUs, and no narrow draft is slower than full width.
