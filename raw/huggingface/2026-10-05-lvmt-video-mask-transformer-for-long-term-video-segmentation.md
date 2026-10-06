---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.34895
url: https://huggingface.co/papers/2609.34895
arxiv_url: https://arxiv.org/abs/2609.34895
date: 2026-10-05
---

# LVMT: Video Mask Transformer for Long-term Video Segmentation

Existing online video segmentation methods struggle to track objects in long, complex videos with long-term occlusions. We hypothesize that this limitation is caused by (i) the inability of their temporal propagation mechanism to adaptively select the object information that is propagated across time, and (ii) their inability to be trained on long videos due to memory requirements and vanishing gradients. To address the first limitation, we propose to use a lightweight GRU-based temporal propagation module that can learn to select which information it keeps in memory and propagates across time. Second, to allow training on long videos, we introduce Truncated Query Propagation (TQP), a training strategy in which the model processes a video in chunks of frames, where information about tracked objects is propagated between chunks but backpropagation is only conducted in individual chunks, enabling longer temporal supervision without out-of-memory issues, inference overhead, or vanishing gradients. The resulting model is called the Long-term Video Mask Transformer (LVMT). Extensive experiments on six benchmarks show that LVMT sets a new state of the art across a range of video segmentation tasks, while retaining the speed of the highly efficient model it is based on, making it 10X faster than the prior state of the art. Code: https://www.tue-mps.org/lvmt
