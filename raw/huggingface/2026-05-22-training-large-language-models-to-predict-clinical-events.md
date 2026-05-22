---
source: farmer/huggingface
farmed: 2026-05-22T00:00:00+00:00
arxiv_id: 2605.12817
url: https://huggingface.co/papers/2605.12817
arxiv_url: https://arxiv.org/abs/2605.12817
date: 2026-05-22
---

# Training Large Language Models to Predict Clinical Events

Longitudinal clinical notes contain rich evidence of how patients evolve over time, but converting this signal into training supervision for clinical prediction remains challenging. We extend Foresight Learning to clinical prediction by converting time-ordered MIMIC-III notes into examples consisting of past patient context, a natural-language question about a possible future event, and a label resolved from later documentation. This process yields 6,900 prediction examples from 702 admissions across medications, procedures, organ support, microbiology, and mortality. A small LoRA adapter trained on these examples improves over the prompted base model, reducing ECE from 0.1269 to 0.0398 and Brier score from 0.199 to 0.145, and slightly outperforming GPT-5 point estimates on held-out questions. The approach enables reusable clinical prediction supervision from longitudinal notes without hand-engineered structured features or endpoint-specific classifiers.
