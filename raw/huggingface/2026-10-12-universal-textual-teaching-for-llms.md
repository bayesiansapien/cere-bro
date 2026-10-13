---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.222078+05:30
arxiv_id: 2610.12114
url: https://huggingface.co/papers/2610.12114
arxiv_url: https://arxiv.org/abs/2610.12114
date: 2026-10-12
---

# Universal Textual Teaching for LLMs

Knowledge distillation (KD) transfers knowledge from stronger Teacher models to weaker Student models, but most methods require training the Student parameters, thereby binding the distilled knowledge to a specific architecture and checkpoint. This implicit representation is difficult to interpret or reuse across models and limits KD for API-only or costly-to-train models. This paper studies knowledge transfer for large language models (LLMs). We introduce Universal Textual Teaching (UTT), a parameter-update-free framework that distills observed Teacher-Student knowledge gaps into a textual, interpretable, and reusable natural-language artifact called Primer. Specifically, UTT first identifies representative gap cases through paired evaluations, and iteratively updates the Primer via multi-role interactions: the Student attempts each task, the Prompter turns evaluation feedback into a teaching instruction, the Teacher provides a targeted demonstration, and the Synthesizer consolidates validated lessons. Empirically, on the challenging math (Omni-MATH-2) and code generation (KernelBench) tasks, extensive results confirm the effectiveness of the method: UTT remarkably raises the Student's accuracy from 9.4% to 48.6% and Fast1 accuracy from 9% to 35% on KernelBench, while increasing mathematical reasoning accuracy from 27.6% to 51.7%. UTT also performs better than representative prompt engineering and parameter-based KD methods. Of note, UTT is shown to be generalizable across different Teachers and Students: a Primer synthesized for one Teacher-Student pair can generalize to other Students that do not participate in the synthesis.
