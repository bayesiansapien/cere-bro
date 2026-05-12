---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.09996
url: https://huggingface.co/papers/2605.09996
arxiv_url: https://arxiv.org/abs/2605.09996
date: 2026-05-12
---

# Omni-Persona: Systematic Benchmarking and Improving Omnimodal Personalization

While multimodal large language models have advanced across text, image, and audio, personalization research has remained primarily vision-language, with unified omnimodal benchmarking that jointly covers text, image, and audio still limited, and lacking the methodological rigor to account for absent-persona scenarios or systematic grounding studies. We introduce Omni-Persona, the first comprehensive benchmark for omnimodal personalization. We formalize the task as cross-modal routing over the Persona Modality Graph, encompassing 4 task groups and 18 fine-grained tasks across ~750 items. To rigorously diagnose grounding behavior, we propose Calibrated Accuracy (Cal), which jointly rewards correct grounding and appropriate abstention, incorporating absent-persona queries within a unified evaluation framework. On our dedicated experiments, three diagnostic findings emerge: (i) open-source models show a consistent audio-vs-visual grounding gap that RLVR partially narrows via dense rule-based supervision; (ii) answerable recall and parameter scale are incomplete diagnostics, since strong recall can coexist with absent-persona hallucination and larger models do not always achieve higher Cal, exposing calibration as a separate evaluation axis; and (iii) SFT is bounded by the difficulty of constructing annotated ground-truth supervision at scale, while RLVR generalizes more consistently through outcome-level verifiable feedback yet drifts toward conservative behavior and lower generation quality under our reward design. Omni-Persona thus serves as a diagnostic framework that surfaces the pitfalls of omnimodal personalization, guiding future post-training and reward design.
