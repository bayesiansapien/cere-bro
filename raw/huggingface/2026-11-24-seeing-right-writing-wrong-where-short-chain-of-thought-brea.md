---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.931096+00:00
arxiv_id: 2611.28665
url: https://huggingface.co/papers/2611.28665
arxiv_url: https://arxiv.org/abs/2611.28665
date: 2026-11-24
---

# Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA

Asking a vision-language model (VLM) to think step by step often makes it worse at spatial questions, even though the image stays in context. We show that short chain-of-thought (CoT) turns a perception problem into a transcription problem. Once a VLM writes a spatial relation, its answer follows that sentence instead of the image, so whether CoT helps or hurts depends largely on whether the written relation is more accurate than answering directly. Studying 15 open VLMs (2B-38B) and six frontier closed models, we rule out token count, turn format, and visual forgetting in open models and trace the failure through three stages. First, writing re-weights visual cues, weakening a "lower is closer" shortcut in all 13 open models tested but also discarding valid cues, which produces false relations. Second, the written text takes over. With the model's own conclusion-removed rationale held fixed, swapping in an opposite-depth image moves the answer by 2-9 points on rendered twins (vs. up to 77 for direct answers) and by 3.0-3.4 points on average on natural photographs (vs. 20.5-69.6). Third, the concluding sentence can invert even a true relation, mainly on converse questions. Together, false relations and conclusion mis-mapping account for four in five CoT losses. Scale does not remove this bottleneck: Qwen3-VL-32B shows the same pattern. Frontier closed models are not hurt: they write relations as accurately as they answer, and three of six re-check the image after writing. The three queried with reasoning off lock in like open models, so re-grounding co-occurs with answer-turn reasoning; we identify answer-step re-grounding as the step open VLMs lack. In a single-model pilot, fine-tuning on fixed rationales with image-determined labels restores it on natural photographs. We open-sourced all our datasets and code at https://ming-zch.github.io/seeing-right-writing-wrong.
