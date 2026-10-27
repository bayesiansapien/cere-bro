---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801997+00:00
arxiv_id: 2610.14253
url: https://huggingface.co/papers/2610.14253
arxiv_url: https://arxiv.org/abs/2610.14253
date: 2026-10-26
---

# SliderEdit++: Improved Slider Trajectories in Instruction-Based Image Editing

Slider-based control aims to give users continuous, fine-grained control over the intensity of individual edits in instruction-based image editing. However, existing approaches fail to deliver reliable continuous controllability: traversing a slider can produce abrupt visual jumps and non-monotonic changes, while jointly controlled sliders can interfere with one another. To systematically study these limitations, we introduce SlideBench, a comprehensive benchmark for continuous image editing spanning diverse editing categories and equipped with a unified suite of metrics quantifying monotonic progression, perceptual continuity, and inter-slider disentanglement. Building on these observations, we propose SliderEdit++, which explicitly regularizes the intermediate editing trajectory rather than supervising only its endpoints. Our method combines velocity- and semantic-space trajectory regularization with spectral control to encourage smooth, predictable slider traversal, together with a disentanglement objective that reduces interference between independently controlled edits. On SlideBench, SliderEdit++ achieves state-of-the-art performance, improving the overall score by 18.5% relative to the strongest baseline. At the same time, using a few-step editing backbone makes our method approximately 3x to 20x faster than existing slider-based approaches, enabling substantially more responsive interactive editing.
