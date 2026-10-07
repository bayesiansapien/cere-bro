---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02480
url: https://huggingface.co/papers/2610.02480
arxiv_url: https://arxiv.org/abs/2610.02480
date: 2026-10-06
---

# MEA: A Reward-Driven Multi-Agent System for Faithful Model Explanations

Recent years have seen the employment of a plethora of machine learning (ML) models in high-stakes domains, but they remain largely opaque to the practitioners who act on their predictions. While post-hoc explanation methods offer a lens into this model behavior, wielding them effectively demands expertise most domain experts lack: navigating high-dimensional outputs, selecting the best explanations, and synthesizing evidence across disparate tools. To this end, we present MEA, a multi-agent framework that removes the explanation knowledge barrier entirely: a Proposer agent selects and configures explanation tools based on the question and modality, while an Actor agent is optimized end-to-end against faithfulness, transforming the outputs into natural language explanations grounded in model behavior across tabular, text, and vision modalities. Further, we introduce diverse question types spanning feature attribution, counterfactual reasoning, and spurious feature detection, each paired with a perturbation-based faithfulness metric. We find that frontier LLMs systematically produce unfaithful explanations. By optimizing against faithfulness rewards augmented with a modality-adaptive penalty, MEA consistently outperforms post hoc explainers, agentic, and closed-source baselines across six datasets, with reward-driven optimization yielding faithfulness gains of +28% (tabular), +21% (text), and +34% (vision) over the untrained backbone. More broadly, our findings suggest that AI agents themselves can serve as a scalable, adaptable interface to ML explainability, opening a path toward natural-language explainability that generalizes beyond the fixed, single-purpose tools that have long defined the field.
