---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821307+00:00
arxiv_id: 2609.40222
url: https://huggingface.co/papers/2609.40222
arxiv_url: https://arxiv.org/abs/2609.40222
date: 2026-10-02
---

# LOCI: Spatial Linear Memory for Streaming World Models

When a camera revisits a previously observed region, a video world model should reproduce what was there before. This requires both remembering past observations and retrieving the right one for the current viewpoint. Key-value caches preserve visual detail but grow with video length; recurrent memory is compact but compresses history into a fixed-size state, so individual past observations are no longer directly accessible. We introduce LOCI, a hybrid spatial-memory architecture that keeps both representations. In half of the transformer blocks, main attention keeps a key-value cache of past observations; in the other half, it is restricted to the current chunk and complemented by a recurrent linear-attention memory whose reads and writes are conditioned on projective camera geometry, so viewpoint enters both memory addressing and stored content. Recurrent readouts flow into subsequent cache-backed blocks and supply their queries with accumulated scene context. On the public MIND memory benchmark and on held-out recorded trajectories, LOCI reproduces revisited content more faithfully than representative world models and a same-recipe full-softmax model; with full history, it lowers peak memory at equal length by about 30% relative to full softmax. With a bounded bank of retained observations, it streams long videos at constant memory and remains more faithful than full softmax under the same budget.
