---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.926935+05:30
arxiv_id: 2610.33645
url: https://huggingface.co/papers/2610.33645
arxiv_url: https://arxiv.org/abs/2610.33645
date: 2026-10-29
---

# PreView: Enhancing GUI Grounding with Preprocessed Views and Cues

GUI grounding requires locating small controls in cluttered screenshots and identifying which control a natural-language instruction refers to. Cropping and enlargement can expose local detail, but the resulting image may still leave ambiguity about the intended target. We propose PreView, an auxiliary preprocessor that improves the inputs to an existing grounding model without further training that model. PreView prepares two complementary types of input features: task-relevant views for localization and candidate-specific cues for target understanding. A trained lightweight auxiliary model predicts and refines a center, crops the screenshot into a local view, and enlarges that view for zoomed-in grounding. It also prepares a visual cue (i.e., a red-circle marker with a location hint) and a textual cue describing the candidate's identity or function. The frozen grounding model uses the prepared inputs to predict the final click. Across five benchmarks, PreView improves the average grounding accuracy of Qwen3-VL-2B, OS-Atlas-4B, and Qwen3-VL-4B without further training these grounding models. Extensive analyses examine the contributions of views and cues, center refinement, and visual input budgets.
