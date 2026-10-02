---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.344602+05:30
arxiv_id: 2609.38143
url: https://huggingface.co/papers/2609.38143
arxiv_url: https://arxiv.org/abs/2609.38143
date: 2026-10-01
---

# Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI

Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the frozen skill bank to construct harnesses for unseen tasks. Across Harness-Bench and NewtonBench, full-bank meta-skills improve macro-average performance by 8.95 percentage points over no-skill construction, and 12.02 points over direct delivery of the same bank to the Target. These results highlight the value of translating experience into executable support. Gains when the same model serves both roles further suggest a path to system level self-improvement through learning to build better environments.
