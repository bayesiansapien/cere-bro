---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821978+00:00
arxiv_id: 2609.38593
url: https://huggingface.co/papers/2609.38593
arxiv_url: https://arxiv.org/abs/2609.38593
date: 2026-10-02
---

# Prompt2Skill: Unsupervised Skill Optimization From Natural Language Instructions

Skills are external artifacts that Large Language Models (LLMs) consume at inference time to improve their performance on specialized domains by incorporating relevant procedural and domain knowledge. Expert-authored skills are expensive to produce, and the resulting artifacts are not optimized for the specific model that consumes them, whose failure modes can vary with version, scale and training. In addition, emerging tasks may fall outside the scope of existing skill libraries, creating a need to develop new skills before curated training data become available. Recent works have explored automated skill optimization through reflection, but they require a curated, in-distribution training set, which users might not always have. To address these limitations, we present Prompt2Skill, a framework that builds skills from natural-language task description alone. From the prompt, the system derives a task specification, discovers or synthesizes datasets, and refines the skill in a closed loop of reflective editing. Across four domains spanning question answering, reading comprehension, spreadsheet manipulation, and mathematical reasoning, Prompt2Skill consistently outperforms the direct prompting baseline, achieving an average improvement of 10.8 across open-source and frontier models.
