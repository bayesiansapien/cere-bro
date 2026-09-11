# SAEScientist-Bench: agents can find the right feature but cannot steer with it

**Source:** HuggingFace Daily Papers (14 upvotes) · [Paper](https://arxiv.org/abs/2609.09113) · [Code](https://github.com/Trae1ounG/SAEScientist) · [raw](../../raw/huggingface/2026-09-10-saescientist-bench-can-ai-agents-conduct-autonomous-sae-inte.md)

## TL;DR

Research on recursive self-improvement has mostly automated the *training* pipeline. The missing pillar is post-hoc monitoring: understanding what a model learned and confirming it is safe. Sparse autoencoders (SAEs) are the main mechanistic-interpretability tool for that job, isolating individually interpretable features from a model's internal activations. SAEScientist-Bench asks whether an agent can use them like a scientist. Given a target concept, an agent must design contrastive probes and navigate a **Gemma Scope dictionary of 131K+ features** in Gemma-2-9B-IT to find the best feature, scored against curated expert references anchored on Neuronpedia across three axes: activation rank, concept selectivity on contrastive texts, and **causal steering**. Across 10 agent configurations and 20 tasks, frontier agents show genuine discovery ability and different configurations lead on different axes, but all remain well behind the expert baseline. The split is the finding: agents **approach expert level at separating a target concept from contrastive controls** and **lag substantially at causal generation steering**. Further analysis shows agents can design contrasts that rule out spurious candidates but **frequently misinterpret their own experimental measurements**.

## Key points

- **Selectivity is discrimination, steering is intervention, and only the second one proves you found the mechanism.** An agent that ranks features by how well they separate contrastive texts is doing correlational science. Steering asks whether clamping that feature actually changes generation. Agents are good at the first and bad at the second, which is the classic failure of confusing a correlate for a cause.
- **Misreading measurements, not designing bad experiments, is the bottleneck.** That is a more tractable defect than it sounds, and it points at verification scaffolding rather than at model capability.
- **The framing matters as much as the benchmark.** Positioning interpretability as the *auditing* half of autonomous AI R&D, rather than as a separate research programme, makes "can agents audit models" a measurable capability with a number attached.

## How this relates to prior wiki pages

**It is the interpretability instance of the pattern [Φ-Bench (09-10)](../hardware/2026-09-10-phi-bench-llm-infrastructure-engineering.md) found for systems engineering: models are competent at well-posed sub-tasks and weak at the open-ended judgement that decides which sub-task matters.** Φ-Bench's gap is between writing a kernel and deciding which kernel is worth writing. SAEScientist-Bench's gap is between finding a candidate feature and establishing that it is causal. **Two benchmarks published the same day, two different domains, the same shape of deficit.**

**It gives an empirical floor to the recursive-self-improvement anxiety that dominated the day's industry coverage.** An Anthropic researcher resigned publicly citing unmanaged risk from self-improving systems and another put p(catastrophe) above 10%. This paper's contribution to that argument is a measurement rather than a position: **the auditing capability that would make an RSI loop safe is currently the weaker half.** Anyone arguing that interpretability will keep pace with capability now has a benchmark to be wrong about.

**It also constrains the reading of [WMRL (09-10)](../agentic-systems/2026-09-10-wmrl-world-model-rl-research-agents.md), which makes automated-research RL 3-4x cheaper by replacing environment execution with a learned world model.** Cheaper research loops raise the value of a working audit step, and this benchmark says the audit step is where agents misread their own results.

## Gaps

One SAE dictionary on one model (Gemma Scope on Gemma-2-9B-IT), 20 tasks, and expert references curated from Neuronpedia, which encodes a particular community's interpretive conventions as ground truth. Whether "the expert feature" is the right target at all is contested inside interpretability.

## Related

- [Φ-Bench](../hardware/2026-09-10-phi-bench-llm-infrastructure-engineering.md) · [Self-evolving agents](../agentic-systems/self-evolving-agents.md) · [Agent benchmarks](../agentic-systems/agent-benchmarks.md)
