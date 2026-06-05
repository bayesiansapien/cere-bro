# SePO: Self-Evolving Prompt Agent for System Prompt Optimization

**TL;DR.** System-prompt optimization improves agent behavior without touching model weights, yielding human-readable, model-agnostic instructions. Existing methods build a prompt agent that refines *task* agents' prompts but leave the prompt agent's *own* system prompt hand-engineered and fixed. SePO makes the prompt agent's own prompt an optimization target too, in a self-referential design: one prompt agent improves both task agents' prompts and its own, under an open-ended evolutionary search that keeps an archive of candidate prompts as stepping stones. It pre-trains on a multi-task pool, then fine-tunes on a target task. Across five benchmarks (AIME'25, ARC-AGI-1, GPQA, MBPP, Sudoku) it beats Manual-CoT, TextGrad, and MetaSPO, +4.49 average points over Manual-CoT, and the learned skill generalizes beyond the pre-training mixture rather than memorizing per-task prompts.

**Source:** HuggingFace Daily Papers (upvotes: 1)
**arxiv:** [2606.04465](https://arxiv.org/abs/2606.04465)
**Raw:** [raw/huggingface/2026-06-05-sepo-self-evolving-prompt-agent-for-system-prompt-optimizati.md](../../raw/huggingface/2026-06-05-sepo-self-evolving-prompt-agent-for-system-prompt-optimizati.md)

## Key points

- **Self-reference:** the prompt agent optimizes its own system prompt alongside the task agents' prompts, closing the loop that prior methods left hand-engineered.
- **Open-ended evolutionary search** with a candidate archive used as stepping stones (a quality-diversity flavor), rather than greedy refinement.
- **Two-stage:** pre-train the prompt-optimization skill on a multi-task pool, then fine-tune on the target task.
- **Generalization:** the pre-trained skill transfers to tasks outside the pre-training mixture, so it learns *how to optimize prompts* rather than memorizing specific prompts, the same principle-vs-instance distinction the cluster keystone draws.

## Relation to prior wiki

Part of today's self-evolving-agents cluster ([Continual Experience Internalization](2026-06-05-continual-experience-internalization.md)). SePO is the prompt-space instance of "make the optimizer self-improving," and its finding that the *skill* generalizes while per-task prompts would not is the exact principle-level-beats-instance-level result the keystone paper formalizes. It also rhymes with the broader self-referential trend the wiki has tracked in [self-evolving environments (EvoEnv, 05-15)](2026-05-15-evoenv-self-evolving-rl-via-environment-synthesis.md): the system evolves the thing that shapes its own learning.

## Related pages
- [2026-06-05-continual-experience-internalization.md](2026-06-05-continual-experience-internalization.md)
- [multi-agent-systems.md](multi-agent-systems.md)
