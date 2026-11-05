---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.361337+05:30
arxiv_id: 2611.02501
url: https://huggingface.co/papers/2611.02501
arxiv_url: https://arxiv.org/abs/2611.02501
date: 2026-11-04
---

# SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding

Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass. However, it remains unclear whether their released systems (stock) attain the full speedup that parallel drafting permits. We identify three challenges. First, with one request, each step accepts few tokens but reads every target weight. Second, with batching, per-request verification work roughly halves the speedup over autoregressive (AR) decoding. Third, speculative decoding is deployment-specific, and no universal optimization fits every serving regime, drafter, target model and GPU. To address these challenges, we present SpecPilot, an autonomous agentic loop that discovers algorithms and systems optimizations for each deployment. In each round, a cost model locates the largest gaps between the current system and its ceiling. Parallel agents explore directions and integrate the successful ones. Token forcing checks every output token against stock to detect reward hacking. A structured memory carries validated mechanisms to new rounds and deployments. SpecPilot discovered a general lossless 12-bit weight format, tree verification for hybrid recurrent targets, two-level verification and three batching mechanisms. We evaluate it across four target models, three drafters, two GPU platforms and five benchmarks. Without training or quality loss, it raises the speedup over AR from stock's 4.46times to 10.87times with one request, and from 1.94times to 3.93times with batching.
