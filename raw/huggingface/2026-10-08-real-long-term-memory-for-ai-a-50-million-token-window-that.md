---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.311112+05:30
arxiv_id: 2610.10845
url: https://huggingface.co/papers/2610.10845
arxiv_url: https://arxiv.org/abs/2610.10845
date: 2026-10-08
---

# Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and Cheaper Than Recompute

A large language model can only use the text that fits in its context window, and it recomputes its internal key-value (KV) state for a prompt every time the prompt is sent. We test a memory layer, the public package galahad-kv, that saves the KV state of each block of about 16,000 tokens to encrypted local NVMe disk and loads it back later, byte-exact, without recomputing it. We ran it on 50,000,000 tokens of real public text, served through vLLM on one NVIDIA H100, with Gemma 4 12B and Gemma 4 31B. Every block we probed was loaded back from the encrypted store with no recompute (100 of 100, at depths from 0 to 50M tokens) on both models. Loading a block was 2.8x to 4.3x faster than recomputing it and used 8.8x to 12.3x less GPU energy, and GPU memory stayed flat over the whole 50M-token stream. Asked about facts planted millions of tokens earlier, the 12B model gave the right answer 82 times out of 100 and the 31B model 98 times out of 100. Neither model made up an answer. The limits are as follows. This is reuse of stored state, not a wider attention window: one block is loaded at a time, and how well a question is answered depends on the model. Writing the memory is a one-time cost, and the store takes terabytes of local NVMe disk. We describe the test protocol, which is built to resist common ways of gaming long-context benchmarks, and give a single-GPU reproduction that uses public software and a free licence for the package.
