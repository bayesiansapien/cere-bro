---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.09269
url: https://huggingface.co/papers/2605.09269
arxiv_url: https://arxiv.org/abs/2605.09269
date: 2026-05-12
---

# DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification

Aligning Multimodal Large Language Models (MLLMs) requires reliable reward models, yet existing single-step evaluators can suffer from lazy judging, exploiting language priors over fine-grained visual verification. While rubric-based evaluation mitigates these biases in text-only settings, extending it to multimodal tasks is bottlenecked by the complexity of visual reasoning. The critical differences between responses often depend on instance-specific visual details. Robust evaluation requires dynamically synthesizing rubrics that isolate spatial and factual discrepancies. To address this, we introduce DeltaRubric, an approach that reformulates multimodal preference evaluation as a plan-and-execute process within a single MLLM. DeltaRubric operates in two steps: acting first as a Disagreement Planner, the model generates a neutral, instance-specific verification checklist. Transitioning into a Checklist Verifier, it executes these self-generated checks against the image and question to produce the final grounded judgment. We formulate DeltaRubric as a multi-role reinforcement learning problem, jointly optimizing planning and verification capabilities. Validated on Qwen3-VL 4B and 8B Instruct models, DeltaRubric achieves solid empirical gains. For instance, on VL-RewardBench, it improves base model overall accuracy by +22.6 (4B) and +18.8 (8B) points, largely outperforming standard no-rubric baselines. The results demonstrate that decomposing evaluation into structured, verifiable steps leads to substantially more reliable reward modeling for multimodal alignment.
