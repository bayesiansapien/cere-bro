---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.04527
url: https://huggingface.co/papers/2606.04527
arxiv_url: https://arxiv.org/abs/2606.04527
date: 2026-06-04
---

# Echo-Infinity: Learning Evolving Memory for Real-Time Infinite Video Generation

We present Echo Infinity, an autoregressive (AR) framework towards real-time infinite video generation that employs a learnable evolving memory to dynamically filter, abstract, and compress any-length history at constant cost. Existing methods mainly curate memory with predefined KV-cache schedules, fixed-ratio heuristic compression, or inference-time RoPE adaptation. These designs inevitably lose historical information and amplify compounding errors due to their limited cache window and ignorance of autoregressive generation noise. Inspired by human memory consolidation, Echo-Infinity replaces handcrafted memory curation with learnable Memory Query, which are updated by attention and a gating mechanism when past frames are evicted from the local window. The queries are optimized end-to-end with the video diffusion transformers (DiTs), forming an evolving memory that supports arbitrary compression ratios with constant computation independent of video length. They also act as a generalizable generation prior, improving quality even when only the optimized initial state is used. We further introduce Unified Relative RoPE Recipe, which anchors the sink frames to start from id 0 and lets the newest frame id grow at most to the DiTs' pretrained maximum temporal RoPE id throughout training and inference, freeing the model from the finite RoPE constraint and closing the train-test RoPE extrapolation gap. In long and short video generation, Echo-Infinity achieves state-of-the-art performance, and, to our knowledge, demonstrates promising 24-hour (>1.3 M frames) real-time rollouts for the first time, suggesting a practical path toward infinite video generation.
