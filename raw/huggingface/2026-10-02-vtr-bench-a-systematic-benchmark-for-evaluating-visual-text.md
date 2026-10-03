---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820974+00:00
arxiv_id: 2610.01499
url: https://huggingface.co/papers/2610.01499
arxiv_url: https://arxiv.org/abs/2610.01499
date: 2026-10-02
---

# VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation

Recent video generation models can produce highly realistic videos from natural language instructions, with visual quality approaching cinematic standards. Existing evaluation benchmarks, however, predominantly assess visual quality, aesthetic appeal and physical plausibility, while paying limited attention to text, an essential medium for conveying information in everyday scenes. A generated video may appear visually compelling and feature lifelike subjects, yet still render the text within the scene incorrectly. To address this overlooked dimension, we introduce VTR-Bench, a systematic benchmark for evaluating the Visual Text Rendering capabilities of video generation models. VTR-Bench situates text within concrete application scenarios, such as advertisements and scientific videos, with 300 carefully constructed prompts spanning five scenario categories. We develop an automated evaluation pipeline with human alignments that separately assesses text fidelity through carrier-specific transcription and scene and motion requirements through a prompt-specific chain of query. Beyond evaluation, we introduce a Keyframe-Guided Agentic Framework in which a Director agent coordinates image and video generation with visual evaluation, guiding iterative refinement and candidate selection through visual feedback. Experiments on 11 state-of-the-art models reveal widespread difficulties in accurately rendering scene text, with the best-performing model recording an overall word error rate (WER) of 0.250. We further analyze text rendering failures to characterize the challenges faced by current video generation models. These findings highlight visual text rendering as a key challenge for video generation and demonstrate a practical path toward improvement. Code is available at https://github.com/hardenyu21/VTR-Bench.
