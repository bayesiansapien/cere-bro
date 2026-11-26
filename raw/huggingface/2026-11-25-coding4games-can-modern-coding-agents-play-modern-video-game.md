---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.31974
url: https://huggingface.co/papers/2611.31974
arxiv_url: https://arxiv.org/abs/2611.31974
date: 2026-11-25
---

# Coding4Games: Can Modern Coding Agents Play Modern Video Games?

Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring repeated inference cost and, in real-time games, acting while the environment continues to evolve. We ask whether coding agents can learn from game interaction to develop standalone game-playing programs that run without language model inference. We thus introduce Coding4Games, a benchmark for evaluating whether coding agents can develop standalone programs that play modern games through visual observations and standard game inputs. Coding4Games has three defining features: 1) Diverse Modern Games, covering 15 games with diverse visual, strategic, and control demands; 2) Development-Test Separation, in which a coding agent uses a sandbox and the standard player interface to iteratively develop a program, after which the selected program is frozen and independently tested without language-model inference; and 3) Outcome and Process Evaluation, which measures not only game performance and reliability but also how agents use feedback, revise programs, and resolve problems during development. Across 15 games, the best program per game outscores the strongest GUI baseline on 13 and ties it on one. The human player outscores all agents on 10 games. We additionally examine the effects of development budgets. Coding4Games evaluates whether coding agents can turn their understanding of complex interactive environments into programs that work reliably on their own.
