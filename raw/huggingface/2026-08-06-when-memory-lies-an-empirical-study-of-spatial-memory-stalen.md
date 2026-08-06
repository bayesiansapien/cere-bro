---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04574
url: https://huggingface.co/papers/2608.04574
arxiv_url: https://arxiv.org/abs/2608.04574
date: 2026-08-06
---

# When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents

Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs under both text and image inputs (1,800 detection runs, and 12,000 text-mode navigation episodes over four LLM navigators at a shared 50-seed scale). Three findings emerge. First, text solvability does not imply visual grounding: models that flag stale entries reliably from text nonetheless span vision F1 from 0.887 down to 0.067 on the identical grids, and the weakest keeps making fluent, confident decisions that ignore the image. Second, consuming stale memory without an audit is a safety liability: in our primary GPT-4o setting, an agent that trusts raw memory dies more than twice as often as the same agent given no memory at all. Third, auditing helps but does not close the gap: a transparent read-time filter removes much of the safety cost in text mode, yet even oracle stale labels bring no further significant gain on the current grid size, and when visual auditing is unreliable, filtering yields no consistent benefit. Together these results frame spatial-memory staleness as a safety failure mode and isolate reliable visual grounding and action selection under memory--observation conflict as the central open challenges for memory-augmented agents.
