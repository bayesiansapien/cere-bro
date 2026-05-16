---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.14068"
url: "https://huggingface.co/papers/2605.14068"
arxiv_url: "https://arxiv.org/abs/2605.14068"
date: 2026-05-16
---

# CurveBench: A Benchmark for Exact Topological Reasoning over Nested Jordan Curves

We introduce CurveBench, a benchmark for hierarchical topological reasoning from visual input. CurveBench consists of 756 images of pairwise non-intersecting Jordan curves across easy, polygonal, topographic-inspired, maze-like, and dense counting configurations. Each image is annotated with a rooted tree encoding the containment relations between planar regions. We formulate the task as structured prediction: given an image, a model must recover the full rooted containment tree induced by the curves. Despite the visual simplicity of the task, the strongest evaluated model, Gemini 3.1 Pro, achieves only 71.1\% tree-generation accuracy on CurveBench-Easy and 19.1\% on CurveBench-Hard. We further demonstrate benchmark utility through RLVR-style fine-tuning of open-weight vision-language models. Our trained Qwen3-VL-8B model improves over Qwen-3-VL-8B-Thinking from 2.8\% to 33.3\% tree-generation accuracy on CurveBench-Easy, exceeding GPT-5.4 and Claude Opus 4.5 under our evaluation protocol. The remaining gap, especially on CurveBench-Hard, shows that exact topology-aware visual reasoning remains far from solved.
