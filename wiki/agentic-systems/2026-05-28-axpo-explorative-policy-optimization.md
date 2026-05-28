# AXPO: Agent Explorative Policy Optimization for Multimodal Agentic Reasoning

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28774](https://arxiv.org/abs/2605.28774) · [HuggingFace](https://huggingface.co/papers/2605.28774) · [raw](../../raw/huggingface/2026-05-28-agent-explorative-policy-optimization-for-multimodal-agentic.md)

## TL;DR

Vision-language reasoning models that interleave thinking with tool use have an asymmetry: thinking is the safe default, tool calling is high-variance and risky. Under standard GRPO (Group Relative Policy Optimization, the RL setup where rollouts in a group are scored relatively), the asymmetry kills learning: tool use is attempted on only ~30% of rollouts, and when attempted, the entire tool-using subgroup is all-wrong on ~40% of questions, which zeros out the gradient for exactly the tool calls that need to improve. AXPO fixes this by freezing the thinking prefix and resampling only the tool call and its continuation in the all-wrong subgroups, paired with uncertainty-based prefix selection. SFT+AXPO outperforms SFT+GRPO by +1.8pp Pass@1 and Pass@4 on average across nine multimodal benchmarks, and 8B SFT+AXPO beats 32B base on Pass@4.

```
Standard GRPO on a tool-call question:
  thinking-only rollouts: [✓ ✓ ✗]   ← gradient flows
  tool-using rollouts:    [✗ ✗ ✗]   ← all-wrong subgroup, NO GRADIENT on tool tokens

AXPO:
  freeze thinking prefix, resample tool-call branch only:
    prefix  →  tool call (resample N times)
                   └─ now subgroup has variance → gradient on tool calls again
  + uncertainty-based prefix selection to focus on rollouts where the tool call mattered
```

## Key findings

- Tool calls attempted in only ~30% of GRPO rollouts and the tool-using subgroup is all-wrong on ~40% of questions, suppressing the very gradient the agent needs.
- SFT+AXPO outperforms SFT+GRPO by +1.8pp Pass@1 and +1.8pp Pass@4 averaged across nine multimodal benchmarks at 8B.
- 8B with SFT+AXPO beats 32B base on Pass@4 with 4x fewer parameters.
- Tested on three scales of Qwen3-VL-Thinking, so the result is not specific to one model size.

## How this fits prior wiki state

The "all-wrong group" problem is essentially a credit-assignment failure. It connects to two prior threads:
- AKBE (2026-05-27, knowledge-boundary tool use), also a tool-call discipline problem, but framed as "don't call the tool when intrinsic knowledge suffices." AXPO and AKBE attack from opposite ends: AKBE reduces the rate of low-signal tool calls, AXPO improves the gradient when tool calls do happen.
- T2PO (2026-05-05, uncertainty multi-turn RL), also uses uncertainty for sample selection. AXPO's uncertainty-based prefix selection extends the same idea to the tool-call setting.

The bigger pattern: across yesterday's CPT/DarkForest/AKBE plus today's AXPO, the field is converging on the same diagnosis. The current RL training stack wastes gradient on rollouts that look bad but had no chance of being useful. The remedies all involve some form of selective resampling or selective trust.

## Related pages

- [[2026-05-27-akbe-knowledge-boundary-tool-use]], opposite-end tool-call discipline
- [[2026-05-05-t2po-uncertainty-multi-turn-rl]], uncertainty for sample selection
- [[2026-05-27-cpt-collaborative-parallel-thinking]], share findings across parallel branches
- [[tool-calling]], concept page

## Research angle

The thinking-acting asymmetry AXPO identifies is a structural property of the agent itself, not of any particular benchmark. If the same asymmetry is present in non-multimodal coding agents, the same intervention should work there. A clean ablation would be SFT+AXPO on a non-vision SWE-Bench harness to see if the +1.8pp gain transfers. The frame to watch is whether "freeze prefix, resample acting step" becomes a default RL recipe for agentic post-training.
