---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.417485+00:00
arxiv_id: 2610.11570
url: https://huggingface.co/papers/2610.11570
arxiv_url: https://arxiv.org/abs/2610.11570
date: 2026-10-09
---

# Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention Residuals

In this paper, we argue that looped Transformers need their own residual connections to prevent performance degradation as the number of iterations grows. We observe that increasing loop iterations can reduce reasoning accuracy: noisy state updates overwrite correct intermediate deductions and even undo completed solutions. This leaves subsequent iterations to recover lost information from an already degraded representation: once an error arises in an earlier loop, often as a result of long-range propagation through the recurrence, later loops find it difficult to correct. In this paper, we introduce InfiLoop, a loop-native residual connection that learns which past computations to retain and how much to accept from each new update. InfiLoop combines content-based weighting with learned temporal decay to maintain a running summary of recurrent states. An exact streaming recurrence keeps its persistent aggregation memory constant as the loop count grows. The resulting adaptive update suppresses unreliable proposals and preserves useful intermediate states. Across extensive reasoning tasks, a 7M-parameter InfiLoop model outperforms existing recursive architectures, reaching 97.9% exact accuracy on Sudoku-Extreme, and 13.6% pass@2 on ARC-AGI-2. Notably, on Sudoku-Extreme, InfiLoop continues to improve with test-time looping beyond 20,000 effective steps, showing that added depth translates directly into stronger reasoning. Our code is available at https://github.com/pixeli99/InfiLoop.
