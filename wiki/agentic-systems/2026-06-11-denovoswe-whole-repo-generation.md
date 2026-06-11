# DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch

**TL;DR.** Code agents are moving past localized bug fixes toward building whole repositories from a high-level spec. Training for that is hard because verifiable whole-repo-generation data barely exists. DeNovoSWE is a 4,818-instance dataset where each instance requires generating a complete repository from documentation, built automatically through a sandboxed agentic workflow (no human annotation) using a divide-and-conquer plus critic-repair philosophy and difficulty-aware trajectory filtering. Fine-tuning Qwen3-30B-A3B on it raises the BeyondSWE-Doc2Repo score from 5.8% to 47.2%.

**Source:** HuggingFace Daily Papers · arxiv [2606.10728](https://arxiv.org/abs/2606.10728)

## Key findings

- **Whole-repo, not patch-level.** Each instance is "generate a complete repository from its documentation," a genuinely long-horizon task, versus SWE-bench's single-issue patch contract.
- **Automatic construction.** A sandboxed agentic workflow curates instances without human labels, using divide-and-conquer decomposition and a critic-repair loop; difficulty-aware filtering balances quality against diversity.
- **Large effect.** Qwen3-30B-A3B on BeyondSWE-Doc2Repo goes 5.8% → 47.2%, an 8x relative jump, showing the data bottleneck (not the model) was limiting long-horizon SWE.

## How this relates to prior wiki knowledge

DeNovoSWE is the **data-substrate** member of the 06-11 self-improvement cluster alongside [Arbor](2026-06-11-arbor-hypothesis-tree-refinement.md) (research over a hypothesis tree) and [RACES](../llms-foundation-models/2026-06-11-races-composable-verifiable-environments.md) (composable verified environments). Where RACES manufactures RL environments and Arbor manufactures research strategy, DeNovoSWE manufactures *training data* for long-horizon coding. All three answer the [self-evolving agents](self-evolving-agents.md) page's standing question of where long-horizon training signal comes from. It also pairs with [Claw-SWE-Bench](2026-06-11-claw-swe-bench-harness-evaluation.md) (06-11, the harness-aware SWE benchmark): DeNovoSWE builds the training data, Claw-SWE-Bench measures whether the resulting harness uses it well.

→ Raw: [`raw/huggingface/2026-06-11-denovoswe-scaling-long-horizon-environments-for-generating-e.md`](../../raw/huggingface/2026-06-11-denovoswe-scaling-long-horizon-environments-for-generating-e.md)
