---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.146540+00:00
arxiv_id: 2611.22673
url: https://huggingface.co/papers/2611.22673
arxiv_url: https://arxiv.org/abs/2611.22673
date: 2026-11-19
---

# FVScore: Specification-Driven Neuro-Symbolic Video Evaluation

We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to specific temporal violations remain open challenges. FVSCORE addresses these limitations by compiling each video into explicit propositions capturing prompt requirements and implicit propositions capturing unstated physical, temporal, and cross-modal constraints. It grounds each proposition using specialized perceptual tools and evaluates the resulting confidence traces with soft temporal operators inspired by Linear Temporal Logic. A Significance-Aware Calibration step then aligns verification with human perception by retaining only perceptually significant violations before producing a timestamp- and evidence-grounded report. We conduct extensive experiments across public and complex multi-event benchmarks with the strongest video models to date, demonstrating that FVSCORE outperforms holistic and agent-based evaluators in human correlation while providing highly accurate and interpretable feedback.
