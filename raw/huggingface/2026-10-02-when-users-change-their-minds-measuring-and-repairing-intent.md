---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820224+00:00
arxiv_id: 2609.32520
url: https://huggingface.co/papers/2609.32520
arxiv_url: https://arxiv.org/abs/2609.32520
date: 2026-10-02
---

# When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM Agents

LLM agents often operate over multi-turn interactions in which user intent changes before execution. We study intent drift: the failure mode in which superseded parts of the user's intent continue to influence the final answer or tool action. We introduce IntentFlux, an executable benchmark that converts verifiable tasks into dialogues with controlled intent changes while preserving their original graders. In a 627-case calibration, mean task score falls from 0.476 to 0.384 as dialogues contain more superseded and withdrawn information. Across eight models, the rate of fully correct solutions is significantly lower when the same final task must be recovered from an evolving dialogue rather than given directly in a single turn. We further introduce StateForge, which explicitly maintains the active requirements before generation. On General-Test, it improves mean task score from 0.367 to 0.467. Providing the ground-truth final state improves performance further but still does not recover single-turn performance, indicating that state-estimation errors explain only part of the gap. These results establish intent drift as a measurable multi-turn failure mode and explicit state maintenance as a partial mitigation.
