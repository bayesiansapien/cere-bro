---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.10538
url: https://huggingface.co/papers/2608.10538
arxiv_url: https://arxiv.org/abs/2608.10538
date: 2026-08-14
---

# SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models

Agent skills represent a standardized format for packaging procedural knowledge and domain expertise, serving within agent harness systems as an essential mechanism to continually constrain a language model's behavior space for repeatable, high-quality task execution. However, because strong closed-source models entail high inference costs, current popular agent harnesses, such as Codex and OpenClaw, remain prohibitively expensive when deploying these skills to accomplish real-world tasks. The rapid capability enhancement of open-source models deployable on consumer-grade GPUs presents a compelling opportunity to drastically reduce these costs by leveraging skill-based behavioral constraints. Nevertheless, automatically generating effective skills tailored specifically for such compact models remains a significant practical challenge. To address this, we propose SKILLER, a natural-language-driven reinforcement learning framework designed to automatically generate executor-specific skills for small models, which employs a strong model as the actor and critic, treats the small-model agent system as the environment, and propagates all reinforcement learning signals entirely via natural language. Extensive experimental evaluations across five relevant benchmarks using Qwen3.5-9B and Qwen3.5-4B demonstrate that SKILLER outperforms three open-source and one closed-source skill generation or evolution methods, achieving absolute gains ranging from 4.3 to 20.4 percentage points for the 9B model and 1.8 to 13.3 points for the 4B model, while remarkably matching the performance of strong closed-source models on single-skill tasks in SkillsBench. The project is available at https://github.com/DANG-ai/SKILLER.
