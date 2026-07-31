---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28374
url: https://huggingface.co/papers/2607.28374
arxiv_url: https://arxiv.org/abs/2607.28374
date: 2026-07-31
---

# LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger

Multimodal agents for visual question answering increasingly operate as multi-step trajectories that interleave perception, retrieval, and reasoning, yet evaluation still largely reduces to final-answer accuracy. This aggregate signal cannot tell whether a correct answer was reached through grounded evidence, language priors, or accidental error cancellation. We propose to treat a multimodal agent trajectory as a provenance-constrained state machine: tool outputs are normalized into a Structured Evidence Ledger that serves as the trajectory state, downstream reasoning and decision claims may cite only active ledger entries, grounding is checked at the entity and numeric level, and repair is realized as typed state transitions that cannot introduce content without tool-produced provenance. We instantiate this design as LedgerMind (Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger), augmented by a Three-Layer Grounding Protocol, an Adaptive Dual-Path Dispatcher that matches reasoning depth to question complexity, and an Event-Triggered Verification-and-Repair engine with a formal provenance non-amplification guarantee. We use LedgerMind to target four recurring failure patterns that final-answer accuracy tends to obscure: unsupported intermediate reasoning, citation-backed entity hallucination (Phantom Grounding), over-reasoning on simple queries, and repair-time amplification. Experiments across multiple multimodal reasoning benchmarks and backbone MLLMs show that LedgerMind improves both answer accuracy and trajectory-level faithfulness.
