---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.503062+00:00
arxiv_id: 2610.14609
url: https://huggingface.co/papers/2610.14609
arxiv_url: https://arxiv.org/abs/2610.14609
date: 2026-10-14
---

# EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment

Determining whether an image is AI-generated does not establish whether the situation it depicts is factually supported. We formulate Image Factuality Assessment: given an image and a generic verification instruction, a system returns a supported or refuted verdict with an evidence-grounded explanation. Without a supplied textual claim, the system must progressively refine factual questions during investigation and align external evidence with the specific situation depicted. We introduce EviLens, an expert-reviewed benchmark of 10,174 supported and refuted images from controlled construction and web collection, covering twelve factual error types and evaluating both verdict accuracy and evidence sufficiency. We develop EviScene, a multimodal ReAct agent that interleaves visual inspection, external retrieval, and evidence analysis, using new findings to refine its questions and revisit relevant image details. We train a compact policy with supervised fine-tuning on reviewed teacher trajectories, followed by privileged on-policy self-distillation applied to verified decisions from the policy's own investigations. On the 1,527-image test set, the trained Qwen3.5-9B agent achieves 79.05% balanced accuracy and a Strict Evidence Sufficiency Rate (SESR) of 52.26%, improving over the same-backbone base agent by 6.71 and 9.37 percentage points, respectively. Its SESR is the highest among the evaluated agents.Code, models, and data will be released at https://github.com/wangzian828/EVISCENE and https://huggingface.co/ZiAnwang/EviScene.
