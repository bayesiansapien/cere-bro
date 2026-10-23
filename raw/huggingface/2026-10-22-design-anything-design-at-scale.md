---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.196864+00:00
arxiv_id: 2610.24771
url: https://huggingface.co/papers/2610.24771
arxiv_url: https://arxiv.org/abs/2610.24771
date: 2026-10-22
---

# Design Anything, Design at Scale

As multimodal resources are transformed into media outputs, agentic AI is expected to stay aligned with design intent over long horizons. Designers follow briefs specifying goals, constraints, and deliverables, with later work building on earlier decisions. Recent work reuses design experience across tasks, yet alignment among artifacts within one project remains challenging. Agents therefore need to preserve and apply this intent across domains and as projects grow. We introduce Design Anything, a graph-based harness that preserves design intent outside the model and binds deliverables to the workflow steps that produce them through an intent-execution graph. A task contract retains constraints and decisions, selected designs become explicit inputs to later generations, and a deterministic controller uses bindings and execution records to check output types and counts, identify outstanding deliverables, and guide subsequent turns. We also introduce DesignAnything-Bench, with 228 tasks across 19 design domains, including 38 project families at scales of 6, 14, and 24 artifacts. With the LLM held fixed, Design Anything satisfies 85.0% and 92.5% of the brief's factual constraints with DeepSeek V4.1 Flash High and GPT-5.6 Sol High, respectively, exceeding the strongest same-model baselines by 15.4% and 14.4%. These gains reach 25.1% and 23.0% on 24-artifact tasks. Under each model, Design Anything leads or ties in constraint satisfaction in 18 of 19 domains. Professional designers also prefer its complete deliverable sets over those of same-model baselines in a blind evaluation.
