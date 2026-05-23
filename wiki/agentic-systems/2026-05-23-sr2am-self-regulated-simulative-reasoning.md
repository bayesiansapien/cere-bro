# SR^2AM: Self-Regulated Simulative Reasoning for Efficient Agents

**Date:** 2026-05-23
**Arxiv:** [2605.22138](https://arxiv.org/abs/2605.22138)
**HF papers:** [https://huggingface.co/papers/2605.22138](https://huggingface.co/papers/2605.22138)
**Raw source:** [farmer/huggingface](../../raw/huggingface/2026-05-23-efficient-agentic-reasoning-through-self-regulated-simulativ.md)

## TL;DR

SR^2AM (Self-Regulated Simulative Reasoning Agentic LLM) argues that efficient agents need three subsystems, not a single reactive chain-of-thought: System I (reactive execution), System II (simulative reasoning grounded in a world model), and a new System III (a learned configurator deciding when and how deeply to plan). The two reported instantiations both run as distinct stages inside a single LLM's chain-of-thought. v0.1-8B matches 120-355B systems on Pass@1 across math, science, tabular analysis and web information seeking. v1.0-30B matches 685B-1T systems while using 25.8-95.3% fewer reasoning tokens. RL increases average planning horizon by 22.8% while planning frequency rises only 2.0%: the model learns to plan further, not more often.

## Why this matters

The agentic-systems thread of the wiki has had a tension since the 04-17 paper "Model Capability Dominates Inference-Time Optimization": more tokens does not buy more capability past a ceiling. SR^2AM gives a complementary structural answer: spending more tokens on every step is the wrong axis, the right axis is *deciding when to plan at all* and *how far ahead when you do*. The learned-configurator framing turns inference-time compute from a slider into a policy.

## Mechanism

Three loops nested inside the same LLM CoT:

1. **System I**: produce the next action directly from current state.
2. **System II**: simulate future states using the LLM-as-world-model, then choose an action based on the rolled-out trajectory.
3. **System III**: learned policy that decides whether the current step needs II or I, and at what horizon to simulate.

Two implementations: v0.1 records decisions from a prompted multi-module system; v1.0 reconstructs structured plans from traces of pretrained reasoning LLMs, then trains via supervised fine-tuning followed by RL.

The RL outcome is the headline mechanism finding. The policy does not learn to plan more often (frequency rises only 2.0% from initial behaviour). It learns to plan further ahead when it does plan (horizon grows 22.8%). This is the opposite of what naive chain-of-thought scaling does, which is to make every step longer regardless of need.

## Key takeaways

- v0.1-8B matches 120-355B agentic LLMs on Pass@1.
- v1.0-30B matches 685B-1T systems while using **25.8-95.3% fewer reasoning tokens**.
- After RL: planning horizon +22.8%, planning frequency +2.0%.
- Tested on math, science, tabular analysis, web information seeking.

## Gaps

The "learns to plan further not more often" pattern is the most interesting claim and wants explicit ablation against a frequency-only policy. The world-model fidelity question is unaddressed: when System II rollouts mispredict future states (a known LLM-as-world-model failure mode), does the policy detect and downweight them? Composition with the 04-17 KV Packet / 05-19 LongLive-2 efficiency stack is open; if System II rollouts blow up the KV footprint, the token savings are partly illusory.

## Related wiki pages

- [Model Capability Dominates Inference-Time Optimization (2026-04-17)](../inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md) — the ceiling-on-inference-compute argument SR^2AM works around.
- [Tool Calling](./tool-calling.md) — adjacent concept page.
- [Agent Memory](./agent-memory.md).

## Research angle

If System-III configurators generalize across task families (which the paper claims but does not exhaust), the next bottleneck is the inverse: a *meta-policy* that picks the configurator. The paper's broader claim is that learned self-regulation extends beyond planning, to how agents govern their own learning and adaptation. That is exactly the move that would turn current agent stacks (fixed harness, learned policy inside) into self-modifying systems. The falsifiable prediction worth tracking: within two quarters, a paper appears that lets the configurator itself be updated online from task feedback.
