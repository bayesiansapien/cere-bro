---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.324712+00:00
arxiv_id: 2611.10592
url: https://huggingface.co/papers/2611.10592
arxiv_url: https://arxiv.org/abs/2611.10592
date: 2026-11-10
---

# MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification

Large language models can generate motion graphics from static images and natural language requests, but it remains difficult to evaluate how well models can follow requests that combine spatial, appearance, and temporal requirements. We introduce MotionGraphicsBench, an expert-curated benchmark of 100 instances for animating an input static SVG with a motion edit prompt. By supplying all required visual elements, our editing task reflects a designer-like workflow and isolates motion generation from graphic generation. Derived from real-world Lottie motion designs, our benchmark contains diverse combinations of spatio-temporal animation behaviors. Each benchmark instance pairs its model input with a deterministic, human-readable verification program that accepts different valid implementations and reports which prompt requirements pass or fail, rather than comparing against a reference animation or using a VLM judge. We construct these programs with a multi-agent pipeline using human-labeled animations and synthesized test cases. On a balanced test set of 180 animations, our programs achieve 93.3% raw agreement with human judgments, compared with 83.3% for a GPT-6 Astra VLM baseline, and outperform the baseline in both approval and rejection recall. Across 47 configurations from 32 LLMs and 12 providers, pass@1 ranges from 6.0% to 67.7%. Across 15 models evaluated at their highest available reasoning effort with 32 attempts per instance, additional attempts improve every model, but pass@32 still ranges from 38.0% to 95.0%. Our analysis of verification programs reveals that generated animations often fail to match reference poses, follow requested motion trajectories, or coordinate related events. We release our benchmark at https://huggingface.co/datasets/figma-ai/motion-graphics-bench.
