---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.348115+05:30
arxiv_id: 2609.38541
url: https://huggingface.co/papers/2609.38541
arxiv_url: https://arxiv.org/abs/2609.38541
date: 2026-10-01
---

# ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing

Instruction-guided video editing has made significant progress, yet existing methods use multimodal large language models (MLLMs) primarily as semantic encoders, so they often fall short in working with implicit edits that require causal or semantic reasoning. To bridge this fundamental gap in video editing, we propose ThinkV2V, a reasoning-driven framework for complex instruction-guided video editing, explicitly activating MLLM thinking before visual generation. At its core, ThinkV2V builds on a practical MLLM-to-DiT architecture to turn explicit thinking over the source video and instruction into refined conditioning signals for video editing. Further, we equip it with a dedicated training and inference recipe, combining Progressive Curriculum Training, which gradually cultivates the model from basic editing to reasoning-intensive cases, with Inference-Time Thinking Scaling, which iteratively refines candidate prompts and selects the most reliable one, to better elicit reasoning in challenging editing scenarios. We also curate the ThinkV2V-150K dataset and introduce ThinkV2V-Bench to support training and evaluation of video editing with implicit intent and causal reasoning. Experimental results demonstrate the state-of-the-art performance of ThinkV2V on both complex and standard editing scenarios, in which our 5B-scale DiT model substantially outperforms larger 10B-scale baselines.
