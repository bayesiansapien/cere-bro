# Monitoring shorts: reasoning as computation, portable probes, behavior maps

**Sources:** Kurate cs.LG weekly · raw: `raw/kurate/2026-10-25-cs-lg.md`
**Topic:** CoT monitoring, white-box monitoring, agent evaluation

## Computation, Not Memory ([2610.25760](https://arxiv.org/abs/2610.25760), Kurate cs.LG #5)

In a file-system task where background events toggle file locks without saying the new value, Qwen3-8B and Qwen3.5-9B must reconstruct lock state from history. Most of the drop in lock-violating commands comes from reasoning written *at the moment of action*; keeping earlier reasoning in the prompt adds little. Filler text, reasoning for a different history, or an accurate state table do not reproduce the benefit. Given reasoning written for a history that differs in one lock, the agent follows the reasoning against its own history. Linear probes decode the state from activations without reasoning, but decoding accuracy does not predict which interventions change actions. **Implication:** CoT here is load-bearing computation, which supports CoT monitoring, and it also means dropping old reasoning from context (a token saving) costs little.

## Portable white-box monitoring ([2610.28366](https://arxiv.org/abs/2610.28366), Kurate cs.LG #20)

Express each activation by its angular distances to a shared anchor set, pooled across all layers ("global anchoring"). A frozen probe trained on one model then transfers to another without labelled target data, keeping at least 85% of same-model AUROC over chance on trivia, safety and math monitoring, and holding up better than standard probes after model updates. Transfer can fail even when the property is decodable in the target. **Implication:** probes become reusable across model upgrades, which lowers the cost of white-box monitoring.

## Agent Behavior Maps ([2610.30014](https://arxiv.org/abs/2610.30014), Kurate cs.LG #16)

Place each LLM-plus-harness pair by its centered action log-likelihoods on shared reference trajectories, with no new rollouts. Coordinate distances track trajectory KL in rank order (with error bounds); across 100 LLMs and four environments, ALFWorld coordinates predict performance and show behavioral similarity beyond success rate and size. Harness-component displacements roughly compose. **Implication:** a cheap pre-screen for routing or harness selection.

## Relation to prior wiki pages

Feeds [responsible AI](responsible-ai.md). The CoT result is consistent with the containment-week thread (10-24) that monitors must read live reasoning; the probe result is the first portability evidence for activation monitors in the wiki.
