---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.221394+05:30
arxiv_id: 2609.39566
url: https://huggingface.co/papers/2609.39566
arxiv_url: https://arxiv.org/abs/2609.39566
date: 2026-10-12
---

# From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical Reasoning

Foundation models can serve as clinical agents through tool-use harnesses. However, conventional medical benchmarks assess reasoning over preselected evidence rather than the ability to seek it across clinical records and longitudinal imaging. We propose CASE: a series of role-specific Clinical Agents for Seeking Evidence, together with a tool-use harness and an agentic post-training framework for compact vision-language policy models. We further introduce a longitudinal multimodal benchmark built on UK Biobank, comprising 50,401 clinical questions derived from real-world ICD-10-coded diagnoses of 4,739 participants. Each question links to a patient-specific environment containing clinical context and multi-sequence MRI from baseline and follow-up visits, where agents autonomously select which visits, organs, modalities, slices, and specialist tools to inspect and compare. Supervised fine-tuning transfers evidence-seeking workflows from 14,734 frontier-model interaction trajectories, followed by agentic reinforcement learning on the learner's own environment interactions. Privileged on-policy self-distillation and rubric-based LLM feedback refine evidence-to-conclusion reasoning without prescribing tool sequences. Experiments show that CASE moves beyond question-answer imitation toward transferable investigation policies, strengthening evidence-grounded longitudinal reasoning. Under matched evaluation conditions, our Qwen3-VL-8B based agent achieves over 16% and 10% relative improvements in answer accuracy over GPT-5.4 and Claude Opus 4.8. Code will be available at https://github.com/VinyehShaw/CASE.
