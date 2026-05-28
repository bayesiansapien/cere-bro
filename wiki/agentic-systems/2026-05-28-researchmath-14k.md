# ResearchMath-14K: Scaling Research-Level Math via Agents

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28003](https://arxiv.org/abs/2605.28003) · [HuggingFace](https://huggingface.co/papers/2605.28003) · [raw](../../raw/huggingface/2026-05-28-researchmath-14k-scaling-research-level-mathematics-via-agen.md)

## TL;DR

ResearchMath-14k is a 14,056-problem dataset of research-level mathematics curated from academic sources by a multi-agent pipeline — the largest such collection to date. The authors generate 220K teacher trajectories from two open models on these problems and observe that newer-generation models produce 5.6x more references and 5.0x more fake references per trace than older ones. After agentic filtering, fine-tuning Qwen3 models from 4B to 30B parameters improves base models by 9.2 points on average. Useful supervision can therefore come from imperfect attempts at open problems, not only from fully correct reasoning chains.

## Key findings

- 14,056 problems, the largest research-level math collection so far.
- 220K teacher trajectories generated from two open models, with recurring avoidance behaviors (non-attempts, fabricated references) cataloged.
- Across eight open-weight models, newer generations produce 5.6x more references and 5.0x more fake references per trace.
- Agentic filtering produces useful supervision even from incorrect reasoning traces.
- Fine-tuning improves Qwen3-4B through 30B by 9.2 points on average.

## How this fits prior wiki state

The fabricated-reference scaling result is striking. It is a measurement of model honesty (or its absence) on a hard mathematical task, parallel to the LLM-honesty thread from the past week (Google's uncertainty paper, the sycophancy-lying circuit work, the gentle-prompting hallucination study). The "useful supervision from imperfect traces" finding connects to PEAM's failure-correction objective (today) and to LearnWeak's targeted-weakness training (today). A cross-paper theme: training signal can be reconstructed from agent failures if you process them deliberately.

## Related pages

- [[2026-05-09-ai-co-mathematician]] — co-mathematician agent
- [[2026-05-28-peam-parametric-embodied-memory]] — failure as training signal
- [[2026-05-13-llm-agents-already-know-when-to-call-tools]] — model self-awareness

## Research angle

The 5x fabricated-reference rate in newer models is the most concerning piece. Tooling that auto-verifies citations during chain-of-thought should be a default in any research-agent pipeline; otherwise the fabricated-reference rate scales with model capability. A study that decomposes which fabricated references are introduced during search vs during generation would clarify whether retrieval is the right intervention point.
