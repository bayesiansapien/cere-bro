---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.391801+00:00
arxiv_id: 2611.26624
url: https://huggingface.co/papers/2611.26624
arxiv_url: https://arxiv.org/abs/2611.26624
date: 2026-11-20
---

# PlayCraft: Designing Engaging Games from Agent Play Experience

Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.
