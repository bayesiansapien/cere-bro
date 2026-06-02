---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.30852
url: https://huggingface.co/papers/2605.30852
arxiv_url: https://arxiv.org/abs/2605.30852
date: 2026-06-02
---

# Speculative Pipeline Decoding: Higher-Accruacy and Zero-Bubble Speculation via Pipeline Parallelism

Speculative Decoding (SD) accelerates low-concurrency LLM inference by employing a draft-then-verify paradigm. However, mainstream methods typically rely on multi-token prediction, which introduces escalating prediction difficulty and serial drafting latency. To address these, we propose Speculative Pipeline Decoding (SPD), a groundbreaking framework that unlocks the true potential of pipeline parallelism. By partitioning the target LLM into n pipeline stages, SPD allows LLM to process n tokens in parallel to accelerate decoding. To continuous fill the pipeline in single sequence decoding, a speculation module aggregates intermediate features across different pipeline depths to predict the next token, executing strictly in parallel with the target model's pipeline step, to realize bounded difficulty, higher acceptance rates, and zero latency bubbles. Our experiments demonstrate that SPD achieves a significantly higher theoretical speedup compared to mainstream baselines, offering a highly scalable solution for LLM decoding acceleration. Our code is available at https://github.com/yuyijiong/speculative_pipeline_decoding
