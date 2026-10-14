---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.05637
url: https://huggingface.co/papers/2610.05637
arxiv_url: https://arxiv.org/abs/2610.05637
date: 2026-10-13
---

# Visual Grounding Safety in Vision-Language Models

Vision-language models (VLMs) are increasingly trained to generate structured outputs like points and bounding boxes that downstream interfaces, agents, and robots can act on, yet safety alignment of this output channel has not been systematically analyzed. We study visual grounding safety by repurposing three safety benchmarks spanning direct harm (VLSU), social bias (BBQ-V), and situational safety (Asimov-2.0) into 15,401 matched pairs of harmful requests that differ only in the requested output: a free-text answer (VQA) or a grounding (point or bounding box). Across five VLMs, models that refuse a harmful request posed as a question often comply when the same request asks for a grounding: averaged over models, grounding refusal trails VQA refusal by 31-59 percentage points, depending on the domain, and safety system prompts do not close this gap. We propose a fine-tuning approach that combines grounding-form refusals with capability grounding data and self-distilled benign data to counter over-refusal. For Qwen3-VL-8B and VisionReasoner-7B, it improves grounding refusal by 77-95 percentage points on VLSU and BBQ-V and by 64-85 points on the held-out Asimov-2.0 domain, while also improving VQA refusal, preserving grounding capability, and keeping over-refusal limited. Representation analysis shows that fine-tuning moves harmful requests toward each model's refusal direction, most strongly for grounding, while leaving benign requests near the harmless reference.
