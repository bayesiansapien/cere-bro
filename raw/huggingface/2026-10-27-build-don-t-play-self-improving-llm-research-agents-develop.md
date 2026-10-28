---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33845
url: https://huggingface.co/papers/2610.33845
arxiv_url: https://arxiv.org/abs/2610.33845
date: 2026-10-27
---

# Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players

Can LLM agents carry a hard real-world problem from raw data to a system that holds its own against people? We study this in Hearthstone Battlegrounds, an eight-player auto-battler with stochastic shops and battles, hidden information and nearly a thousand interacting cards. We present AutoTavern, a self-improving research system: specialised LLM research agents share a typed research memory, every claim passes verification gates, and live games close the loop, so the agents improve the simulator, opponents and policy and, from the same feedback, their own research process; a human sets goals and rules on ambiguous mechanics. In 20 days AutoTavern built TavernGym, the first faithful, full-content reproduction of the live game, and delivered 23 versions of TavernAgent, trained with PPO against opponents calibrated to real games. TavernAgent plays complete games on the live ladder by itself: its rating rose from 6,000 to about 15,000 and, on the public leaderboard's measure, its last 20 records average a placement of 1.60 with 80% first places, better than the server's ten highest-rated players on every statistic (2.34, 59%). TavernBench, 960 tasks in 40 scenarios, shows that the system the agents built is the strongest player: TavernAgent answers 91% of the play tasks against at most 63% for frontier LLMs, and decides in 0.03 s where they need up to 26 s; within the second a live turn allows, it keeps 90% and no LLM more than 26%. LLM agents build far better than they play. We will open-source TavernBench and TavernGym at https://github.com/MCG-NJU/AutoTavern.
