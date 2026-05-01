---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.27419"
url: https://huggingface.co/papers/2604.27419
arxiv_url: https://arxiv.org/abs/2604.27419
date: 2026-05-01
---

# InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?

With the advancement of multimodal large language models (MLLMs) and coding agents, the website development has shifted from manual programming to agent-based project-level code synthesis. Existing benchmarks rely on idealized assumptions, especially for well-structured, information-rich inputs and static execution settings. In contrast, real-world development is constrained by a critical bottleneck: the semantic misalignment between ambiguous, low-quality instructions from non-expert users and model understanding, which results in a failure mode that we term blind execution. To address this gap, we introduce InteractWeb-Bench, the first multimodal interactive benchmark for website generation under non-expert low-code user conditions. InteractWeb-Bench introduces four types of user agents and persona-driven instruction perturbations to systematically simulate diverse user behaviors, including ambiguity, redundancy, and contradiction, grounded in requirement engineering defect taxonomies. We develop an interactive execution environment for agents, featuring a unified action space comprising Clarify, Implement, Verify, and Submit, enabling iterative intent refinement, code synthesis, and visual feedback-based validation. Extensive experiments and analysis reveal that frontier MLLM-based agents remain trapped in blind execution, exposing limitations in intent recognition and adaptive interaction.
