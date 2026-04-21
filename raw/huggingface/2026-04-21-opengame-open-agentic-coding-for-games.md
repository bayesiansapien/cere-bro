---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.18394"
url: https://huggingface.co/papers/2604.18394
arxiv_url: https://arxiv.org/abs/2604.18394
date: 2026-04-21
---

# OpenGame: Open Agentic Coding for Games

Game development sits at the intersection of creative design and intricate software engineering, demanding the joint orchestration of game engines, real-time loops, and tightly coupled state across many files. While Large Language Models (LLMs) and code agents now solve isolated programming tasks with ease, they consistently stumble when asked to produce a fully playable game from a high-level design, collapsing under cross-file inconsistencies, broken scene wiring, and logical incoherence. We bridge this gap with OpenGame, the first open-source agentic framework explicitly designed for end-to-end web game creation. At its core lies Game Skill, a reusable, evolving capability composed of a Template Skill that grows a library of project skeletons from experience and a Debug Skill that maintains a living protocol of verified fixes-together enabling the agent to scaffold stable architectures and systematically repair integration errors rather than patch isolated syntax bugs. Powering this framework is GameCoder-27B, a code LLM specialized for game engine mastery through a three-stage pipeline of continual pre-training, supervised fine-tuning, and execution-grounded reinforcement learning. Since verifying interactive playability is fundamentally harder than checking static code, we further introduce OpenGame-Bench, an evaluation pipeline that scores agentic game generation along Build Health, Visual Coherence, and Interaction Quality axes.

**Authors:** Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, Jiaming Han, Tianshuo Peng, Kaixuan Fan, Manyuan Zhang, Xiangyu Yue (CUHK MMLab)

**Project Page:** https://www.opengame-project-page.com/

**Code:** https://github.com/leigest519/OpenGame
