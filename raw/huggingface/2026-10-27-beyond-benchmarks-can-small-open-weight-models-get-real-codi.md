---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34241
url: https://huggingface.co/papers/2610.34241
arxiv_url: https://arxiv.org/abs/2610.34241
date: 2026-10-27
---

# Beyond Benchmarks: Can Small Open-Weight Models Get Real Coding Work Done?

Making an open-weight language model generate text is not the same as making it finish coding work. This retrospective empirical systems experience report follows my engineering work from July to October 2026 across coding clients, model-specific serving recipes, vLLM, SGLang, llama.cpp, and MLX. Models behind a nominally compatible endpoint still differed in tool-call formatting, turn control, context behavior, cache reuse, and reliability. A served model, coherent text, executed tool calls, and code that passes independent behavioral checks proved to be distinct levels of progress. The evidence includes 4,165 coding-agent gateway turns from my own sessions, 623 debug jobs, and three separate delegation studies with hidden behavioral checks and a fixed Claude Opus 5.5 parent. Saved cold-prefix requests had a median time to first token of about 69.4 s, versus 2.8 s for high-reuse requests (observational). In a 45-trial study, direct coding passed 15/15 and delegation to a quantized Qwen3-Coder 30B-A3B worker passed 12/15 and 14/15. On a second 15-task suite under a fixed artifact contract, the completed replacement cohort had 45/45 for direct coding and 12/45 for a Nemotron Cascade 2 worker (11 worker substitutions). Sixteen sessions stopped by a subscription limit before any model call were replaced; counting them as failures gives 37/45 and 8/45. A Qwen3-Coder worker passed 0/45. In both studies with a direct arm, direct coding had lower API list-price-equivalent frontier cost per verified success. A post-hoc diagnostic found that 19 of 36 artifacts rejected only for renamed parameters passed the hidden checks unchanged; they are not counted as successes.
  The contribution is an evidence-qualified account of serving, agent protocol, session continuity, artifact validation, and verification in practice. The studies are not pooled and do not rank models or runtimes.
