---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.11924
url: https://huggingface.co/papers/2608.11924
arxiv_url: https://arxiv.org/abs/2608.11924
date: 2026-08-13
---

# Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill

Turning a research idea into a complete paper requires more than text generation: the system must retrieve literature, design and execute experiments, revise claims according to evidence, produce publication-ready figures, and maintain consistency across a long generation process. We present Spark-to-Paper, an end-to-end research paper generation system implemented as thirteen composable skills inside an existing coding assistant, without requiring a separate agent platform or orchestration service. Spark-to-Paper separates model-based judgment from deterministic operations that can be directly executed and checked. It further separates experiment planning from reporting, so that required evidence is specified before results are observed and manuscript claims are revised according to measured outcomes. To improve reliability over long research trajectories, the system combines deterministic integrity checks with self-critique and bounds a failure mode we call the Self-Refutation Loop, in which repeated experiments continue to reject the original research objective. Spark-to-Paper also produces editable vector figures through programmatic plotting for experimental results and code-based reconstruction for generated method diagrams. Across eight controlled research topics, Spark-to-Paper achieves 99.5% citation validity and 96.4% figure editability. A controlled ablation increases fabrication detection from 14% for a single-pass draft to 92% with the full integrity and review stack, while adversarial review achieves 74% precision. The full system uses 11.9M tokens, costs $8.1 per manuscript, and requires 3.2 hours on average. These results show that end-to-end research paper generation can be implemented as a lightweight, composable workflow inside existing coding assistants while keeping experimental evidence central to how claims are accepted, revised, or abandoned.
