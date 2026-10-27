# Research shorts: reward-model scaling, rationale supervision, proved-faster code, team distillation

**Date:** 2026-10-27 · **Sources:** DAIR picks [Scaling Laws for Generative Reward Models (2610.30765)](https://arxiv.org/abs/2610.30765), [Agentic Verified Optimization of Real-World Software (2610.30188)](https://arxiv.org/abs/2610.30188) · HuggingFace 10-26: [DeCert (2610.27528)](https://arxiv.org/abs/2610.27528), [MultiAgent-OPD (2610.23234)](https://arxiv.org/abs/2610.23234), [On-Policy Self-Training (2610.32770)](https://arxiv.org/abs/2610.32770), [CoRE (2610.14465)](https://arxiv.org/abs/2610.14465) · X: [Principia (2610.32195)](https://arxiv.org/abs/2610.32195), [Flow Reasoning Models (2606.29150)](https://arxiv.org/abs/2606.29150)
**Raw:** `raw/dair/2026-10-26-230504-dair-academy.md`, `raw/huggingface/2026-10-26-*.md`, `raw/twitter/feed/`

## Reward models: the best judge is not the best teacher

- **Scaling laws for generative reward models** (SynthLabs, Stanford, Thinking Machines). Qwen3 judges from 0.6B to 14B supply preferences for online DPO on creative writing; a fixed 32B evaluator scores the policies. "Thinking" judges trained with GRPO have higher static accuracy, yet "Answer-Only" judges trained with SFT give higher peak policy Elo in 7 of 8 matched settings. Intermediate checkpoints of a thinking judge can train better policies than later, more accurate ones. Static judge accuracy is a poor proxy for reward quality.
- **DeCert** supervises the judge's justification, not only its verdict: when several sampled judgments share a correct verdict, differences in certificate quality build rationale preference pairs. Beats strong generative-judge baselines and raises position-consistent accuracy by up to 14.8 points.
- **Read together:** both say the reward model's job is to give a useful gradient, and accuracy on a static label set does not measure that. This echoes the 10-26 agentic-OPD trio (SPOD, R2S, minimal-edit), where a teacher that can solve the task still scores tokens in a way that hurts the student.

## Agentic verified optimization

Ye, Song (Berkeley) and AWS ask an agent for a faster program plus a Lean 4 proof that it equals the original. Using the existing implementation as the spec removes the spec-writing step. Their Aqueduct framework ports C, C++, Go and Rust into native Lean and validates each port by differential testing. On 189 Verina reference implementations, agents produce proved faster rewrites for 156, including algorithmic changes such as replacing exponential recursion with dynamic programming. Relevant to kernel and systems optimization agents: "passes tests" is not "equivalent", and proofs close that gap.

## Distillation and self-training

- **MultiAgent-OPD:** a frozen teacher (trained on a Searcher-Answerer workflow) scores student search and summary tokens to give Searchers local process supervision, while the Leader learns from team success. Reaches 38.68% macro avg@4 across seven datasets, +4.06 over a prompted critic and +2.61 over a trained cascaded system. On-policy distillation moves from single agents to teams.
- **On-Policy Self-Training:** the model writes its own curriculum and privileged reasoning traces from coarse topic descriptions only, then self-distills. Improves across text and VQA while keeping off-target skills. No external teacher, no curated prompts.

## Other

- **CoRE** (routing for retrieval): an RL routing policy picks a reasoning rule per query and a contrastively trained retriever searches under that rule; the two co-adapt without query-rule labels (STaRK-QA). A routing paper in the retrieval layer.
- **Principia** (KAIST): LLMs build comparative causal hypotheses from observations, generalize them into principles at test time, and revise both as new observations arrive.
- **Flow Reasoning Models:** a flow model conditioned on its own previous outputs revises all decisions in parallel; Fixed-Point Forcing trains it on its own inference states. 99.5% on Sudoku-Extreme, matching the next-best 98.7% at 44x fewer inference FLOPs (per the media-zone draft read of the paper). Puzzles only.

Concept pages: [rl-for-llms](rl-for-llms.md), [knowledge-distillation](../inference-efficiency/knowledge-distillation.md), [llm-routing](../ai-routing/llm-routing.md).
