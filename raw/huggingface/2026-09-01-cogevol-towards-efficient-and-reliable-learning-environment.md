---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.30968
url: https://huggingface.co/papers/2608.30968
arxiv_url: https://arxiv.org/abs/2608.30968
date: 2026-09-01
---

# CogEvol: Towards Efficient and Reliable Learning Environment Generation

We present CogEvol, a family of models trained specifically for Learning Environment Generation: turning a course brief into a finished learning artifact (structured-JSON slides or self-contained interactive HTML pages) in a single pass. Across 220k production requests, CogEvol completes a slide in a median of 17 seconds and an interactive page in 59, replacing minutes-long multi-turn agent scaffolding. Reliability is enforced rather than hoped for: a production-grounded data pipeline turns real failures into 53,687 verified SFT samples, and a hybrid rule-plus-VLM reward drives GRPO-based RL, hardened after we caught and fixed a reward-hacking episode that produced visually convincing but unplayable games. CogEvol-27B scores 83.7 on slide quality and 63.7 on a 500-case interactive-HTML benchmark with 26.9x fewer parameters than flagship coding models, and, in collaboration with the OpenMAIC team, serves their live production traffic. CogEvol-4B is released openly under the Apache 2.0 license at https://github.com/CogEvol/CogEvol-4B; external flagships are measured on the same suites under the identical harness. Scaffold editing cuts interactive-page generation cost by a further ~76%, and the full stack runs on domestic Ascend accelerators at application-level parity with A800 GPUs, lowering the unit cost of AI-native education at scale.
