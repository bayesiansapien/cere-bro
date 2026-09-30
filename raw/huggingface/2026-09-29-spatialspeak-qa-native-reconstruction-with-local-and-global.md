---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930565+00:00
arxiv_id: 2609.33616
url: https://huggingface.co/papers/2609.33616
arxiv_url: https://arxiv.org/abs/2609.33616
date: 2026-09-29
---

# SpatialSpeak: QA-Native Reconstruction with Local and Global Context for Spatial Chain-of-Thought Reasoning

Vision-language models (VLMs) can benefit from geometric priors for multi-view spatial reasoning, yet answer-only training does not directly supervise the intermediate geometric estimates and their use in deriving quantitative spatial answers. We hypothesize that spatial chain-of-thought (CoT) supervision becomes more effective when the VLM first jointly learns complementary local geometry and global scene context through multi-view reconstruction. We introduce SpatialSpeak, a two-stage framework that connects QA-native reconstruction pretraining with spatial CoT learning. In Stage I, QA-Native Reconstruction Pretraining (QA-RP) combines marked-point 3D queries for fine-grained local geometry with object-center queries for global scene context across views. Both tasks are formulated as text-based question answering, allowing geometric estimation and subsequent reasoning to share the same autoregressive output interface. In Stage II, spatial CoT with Visual Compensation (CoT-VC) trains the model to express question-relevant geometric estimates and use them to derive answers, with reliability assessment and visual compensation supporting answer refinement when needed. On ReVSI, QA-RP increases the gain from CoT-VC from 2.6 to 6.9 points, and ablations show that both local and global reconstruction supervision are beneficial. SpatialSpeak achieves state-of-the-art results on ReVSI, VSI-Bench, and SPAR-Bench, with a ReVSI score of 62.8 that exceeds the strongest compared baseline by 8.7 points.
