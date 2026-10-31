---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.162593+00:00
arxiv_id: 2610.34298
url: https://huggingface.co/papers/2610.34298
arxiv_url: https://arxiv.org/abs/2610.34298
date: 2026-10-30
---

# Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents

Language agents increasingly act through external tools and interactive environments, making the interface between the model and its executable capabilities part of the decision process. Model Context Protocol (MCP) and command-line interfaces (CLI) can expose the same semantic operations through markedly different model-facing representations. We study whether these representational differences change agent behavior when executable capabilities are matched. We introduce Matched Interface Comparison and Analysis (MICA), which renders MCP and CLI from a shared semantic action contract and routes decoded actions through the same runtime. Across six models and three interactive environments, matched interfaces produce substantial differences in task performance and interaction cost. These effects extend beyond surface validity to semantic action selection, failure pathways, and recovery. Matched-state probes localize sensitivity to capability presentation, realization, and feedback. Paired natural trajectories reveal structured divergence in 94.3% of 2,004 episodes and show that early differences propagate through subsequent interaction. This analysis identifies interface realization as a direct intervention boundary. We therefore introduce Decoupled Action Realization and Targeted Repair (DART), which preserves validated semantic commitments while repairing interface-specific realization. DART improves benchmark score in all six evaluated settings by up to 9.0 points and reduces MCP token cost in all three environments by up to 27.1k tokens per task. Together, these results establish interface representation as part of the closed-loop decision environment shaping agent behavior.
