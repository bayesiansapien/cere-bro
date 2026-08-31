---
source: farmer/huggingface
farmed: 2026-08-31T10:31:04.593371+05:30
arxiv_id: 2608.27906
url: https://huggingface.co/papers/2608.27906
arxiv_url: https://arxiv.org/abs/2608.27906
date: 2026-08-31
---

# Rubric-to-Code Credit Assignment for Reinforcement Learning

Interactive web application generation requires models to produce usable HTML, CSS, and JavaScript applications from natural language requests. Unlike conventional code generation, application quality depends on multiple user-facing functional requirements, each often tied to localized code regions such as event handlers, state updates, DOM fragments, or CSS selectors. Standard GRPO collapses these structured outcomes into a single sequence-level reward and applies the resulting advantage uniformly to all tokens, weakening credit assignment. We propose Rubric-to-Code Credit Assignment (RCCA), a reinforcement learning framework that converts rubric-level functional feedback into localized optimization signals over generated code. RCCA builds training tasks around explicit functional rubrics, uses a hierarchical reward to separate format, source-code, runtime, and functional failures, and aligns evaluator-generated textual attributions with responsible code spans and generated tokens. The resulting model, Ling-RCCA-Flash, scores 41.25 on MiniAppBench, improving Ling-3.0-Flash by 32.20 points and slightly surpassing Claude Opus 4.5. It also reaches 76.19 on ArtifactsBench, improving the SFT model by 4.48 points and establishing a new top score under the official ArtifactsBench leaderboard setting by surpassing the GPT-5 score by 3.64 points, suggesting transferable implementation-level gains.
