---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.818952+00:00
arxiv_id: 2609.39378
url: https://huggingface.co/papers/2609.39378
arxiv_url: https://arxiv.org/abs/2609.39378
date: 2026-10-02
---

# EgoTools: Towards Tool-Centric Reasoning in Real-World Egocentric Videos

Real-world embodied tasks, from everyday activities to professional procedures, require agents to act under physical constraints while tracking evolving object and task states. Tool use sits at the heart of such tasks, as many everyday and professional activities are tool-mediated. Understanding them requires reasoning about affordances, hand-tool-object geometry, procedural progress, and causal effects on target objects. Yet despite strong performance on perception-oriented video tasks such as captioning and general video QA, current multimodal video models remain limited in this form of tool-centric embodied reasoning. Progress in this direction has been limited by the lack of real-world egocentric data and diagnostic benchmarks. To address this gap, we introduce EgoTools, the first comprehensive suite for egocentric tool-use understanding. It consists of two complementary components: EgoTools-Data, a large-scale corpus of 100 hours of tool-centric egocentric recordings with synchronized audio, dense captions, reasoning-heavy narrations, and supplementary 3D information; and EgoTools-Bench, a diagnostic benchmark of 1,000 QA pairs across four tracks that cover tool-use understanding from perception and geometry to procedure and causal reasoning. Experimental results show that current models still struggle to ground tool use in visual evidence: Gemini-3.1-Pro achieves 66.9% overall accuracy but only 51.7% on Perception & Grounding. Beyond evaluation, we validate EgoTools-Data as a training resource. On the full 1,000-question benchmark, full supervised fine-tuning improves Qwen3-VL-8B-Instruct from 50.0% to 60.9%, under strict source-video separation. Together, these results establish EgoTools as a unified resource for both training and diagnostic evaluation of real-world egocentric tool-use understanding.
