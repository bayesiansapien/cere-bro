---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35025
url: https://huggingface.co/papers/2609.35025
arxiv_url: https://arxiv.org/abs/2609.35025
date: 2026-09-30
---

# AutoDataBench: Can Agents Write the Data That Feeds the Self-Improvement Loop?

Recent gains in language model capability have come more from data than from architecture. Frontier labs and data companies produce verifiable agentic tasks, which supervised finetuning and reinforcement learning then turn into capability.This production line still rests on human labour and on human-in-the-loop collaboration. Automating task creation would let data production scale with compute rather than with expert headcount, would extend to more domains, and would enable a key step in recursive self-improvement (RSI). Current evaluations of an agent's ability to write such tasks measure how a model performs after training on what the agent produced. That does not match common practice in the data industry, where data is delivered sample by sample and each sample is accepted against a set of criteria rather than put straight into training. No existing evaluation asks whether an individual task meets the acceptance criteria of a data pipeline. We therefore introduce AutoDataBench. Given an original benchmark task and a record of the target model attempting it, an agent must write a new task for the same suite that meets practical acceptance standards on validity, novelty, difficulty and behavioural coverage. Across three benchmarks of executable agent tasks, no agent we evaluate scores above 20 out of 100 at the default time budget of 45 minutes. Giving the strongest agent four times as long improves its score substantially, while the cost of one usable task stays almost unchanged. Current agents can write training tasks of the required quality, but not efficiently. AutoDataBench provides a direct measure of an agent's capacity for autonomous data synthesis: one artifact at a time, judged against the criteria a production pipeline would apply, and without a training run. Code and data are available at https://github.com/StarDewXXX/AutoDataBench.
