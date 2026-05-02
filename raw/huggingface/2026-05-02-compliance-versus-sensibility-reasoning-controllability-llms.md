---
source: farmer/huggingface
farmed: 2026-05-02T00:00:00Z
arxiv_id: "2604.27251"
url: https://huggingface.co/papers/2604.27251
arxiv_url: https://arxiv.org/abs/2604.27251
date: 2026-05-02
---

# Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models

Large Language Models acquire reasoning capabilities through shared inference patterns in pre-training data, further enhanced via Chain-of-Thought practices. This research investigates whether fundamental reasoning patterns—induction, deduction, and abduction—can be separated from specific problem instances, which is crucial for model controllability.

The authors examine this through "reasoning conflicts," which occur when mandated logical approaches contradict those naturally expected for a task. Their findings reveal that LLMs consistently favor task-appropriate reasoning patterns over conflicting instructions. Notably, models maintain high performance even when using conflicting patterns, indicating reliance on internalized parametric memory that scales with model size.

The researchers demonstrate that reasoning conflicts produce detectable drops in confidence scores and that reasoning types are linearly encoded in middle-to-late layers. Using mechanistic interventions, they increased instruction-following compliance by up to 29%. The study concludes that while LLM reasoning is grounded in concrete instances, active intervention can effectively decouple logical patterns from data, enabling improved controllability, faithfulness, and generalizability.
