---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.21392
url: https://huggingface.co/papers/2611.21392
arxiv_url: https://arxiv.org/abs/2611.21392
date: 2026-11-18
---

# VideoNexus: Video Perception Beyond the Reasoning Context

Understanding long videos requires locating evidence, resolving visual details, and integrating observations into an answer. Even when relevant evidence is present, performing these operations within long, dense visual sequences burdens both perception and reasoning. Video agents enable selective inspection, but returning frames to the planner still accumulates visual information in its reasoning context. Delegating perception reduces this burden, yet sparse sampling can miss decisive details, and per-frame descriptions can preserve context growth. We introduce VideoNexus, a training-free framework that separates detailed video perception from evidence-driven planning and reasoning. The planner controls where to inspect, what to resolve, and how densely to sample. Perception sub-agents process native audio-video in independent contexts and return compact, temporally grounded evidence for iterative search and verification. Using Gemini 3.8 Flash for both planning and perception, VideoNexus achieves 88.6% accuracy on full LVBench, exceeding same-backbone static ingestion and built-in agentic processing by 3.6 and 1.1 points, respectively, at 44% of the latter's measured API cost. A paired LVBench subset ablation shows lower planner input and higher accuracy. With Kimi K3 as the shared backbone, VideoNexus improves over the official Video-GAIA ReAct harness by 8.5 points in our evaluation. These results support compact evidence exchange for combining detailed observation with efficient planning and reasoning.
