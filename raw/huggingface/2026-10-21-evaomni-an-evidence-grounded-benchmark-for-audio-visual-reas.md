---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.641950
arxiv_id: 2610.28444
url: https://huggingface.co/papers/2610.28444
arxiv_url: https://arxiv.org/abs/2610.28444
date: 2026-10-21
---

# EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning

Omni LLMs can naturally locate key audio and visual evidence and integrate information across modalities for audiovisual reasoning. Existing audio-visual reasoning benchmarks that mainly rely on multiple-choice questions usually score models solely based on answer correctness, making it difficult to assess whether a model truly forms a reasoning chain from evidence to the correct answer. In addition, textual or unimodal shortcuts may allow models to answer correctly without analyzing the necessary audio-visual evidence, further weakening the reliability of evaluation benchmarks. To address these issues, we introduce EvaOmni, an evidence-grounded benchmark containing 392 videos and 1,027 purely human-annotated question-answer pairs, covering 15 capabilities and three levels: retrieval and localization, basic understanding, and complex reasoning. We design a series of rigorous annotation procedures in which experts annotate audio and visual evidence and construct video-based distractors; humans review whether questions meet strict inspection criteria, and finally models filter textual and unimodal shortcuts. Beyond high-quality question-answer pairs, we require models to simultaneously return the answer and supporting evidence intervals in order to evaluate the complete reasoning chain. We propose the Coverage Grounded Score (C.G.) to measure how much annotated evidence a model identifies, and the Bottleneck Grounded Score (B.G.) to penalize poor temporal localization in either modality; both are incorporated into answer correctness. Across 7 open-weight and 17 proprietary Omni LLMs, Gemini3.7-Flash achieved the highest overall accuracy (79.4%), C.G. (70.8%), and B.G. (35.1%). At Level 3, it reached 79.1% accuracy, but its B.G. was only 12.3%. These results show that even the most advanced models still have room for development in grounded audio-visual reasoning.
