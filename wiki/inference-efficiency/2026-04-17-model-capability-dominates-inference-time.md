---
source: raw/huggingface/2026-04-17-model-capability-dominates-inference-time-optimization-lesso.md
arxiv: https://arxiv.org/abs/2603.27844
date: 2026-04-17
---

# Model Capability Dominates: Lessons from AIMO 3 Inference-Time Optimization

## TL;DR

Prompt-level inference-time tricks (diverse prompts, different reasoning strategies, temperature tuning) were tested exhaustively on 50 IMO-level math problems. Every single intervention failed to close the gap with a better model. Model capability is 4x more impactful than any prompt-level optimization.

## Key Findings

- **Setup**: 3 models, 23+ experiments, 50 IMO-level problems, one H100 80GB, 5-hour limit
- **Diverse Prompt Mixer**: assigns different reasoning strategies to different voters in majority voting — natural fix for correlated errors
- **Result**: every prompt-level intervention failed. High-temperature sampling already decorrelates errors sufficiently; weaker strategies reduce accuracy more than they reduce correlation
- **The gap**: best majority-vote score was 42/50 vs pass@20 of ~45.5 — a 3.5-point selection loss, not a prompt loss
- **Conclusion**: a verifier-based selector could close the gap; prompt engineering cannot

## Why It Matters for Routing

This is a direct input to routing research. If you're routing between models, the 4x capability advantage of a better model swamps any prompt-level optimization you could apply to a cheaper model. The implication: **routing should focus on capability matching, not on prompt-level tricks applied to weak models**.

The selection loss finding is also interesting — the right answers exist in the sample but the selector can't find them. A better verifier/router that selects the best answer from candidates (not just majority vote) could close ~3.5 points at the same compute budget.

## Related Pages

- [LLM Routing](../ai-routing/llm-routing.md)
- [Knowledge Distillation](knowledge-distillation.md)
