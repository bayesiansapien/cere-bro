---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.21833
url: https://huggingface.co/papers/2608.21833
arxiv_url: https://arxiv.org/abs/2608.21833
date: 2026-08-25
upvotes: 7
authors: ["Kun Chen", "Haorong Hong", "Peizhong Gao", "Jianfeng Lin", "Tongxu Luo", "Yuxuan Xie", "Chenxu Liu", "Jieling He", "Zhongyuan Liu", "Zeno Zeng"]
---

# GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?

**Upvotes:** 7
**Authors:** Kun Chen, Haorong Hong, Peizhong Gao, Jianfeng Lin, Tongxu Luo, Yuxuan Xie, Chenxu Liu, Jieling He, Zhongyuan Liu, Zeno Zeng

Recent large language models (LLMs) can operate as coding agents that build complete games from natural language requests. Game development is especially demanding because program logic, visual and audio content, interfaces, interaction and playability must function together in one executable artifact. Measuring this capability therefore requires evaluation of both game product and the development process. Existing benchmarks often assess the game development capabilities of LLMs by evaluating the final artifact or an isolated development stage. Our analysis of complete human-agent development trajectories identifies three stages that together span the lifecycle of game development with a coding agent: initial game generation, bug diagnosis and repair, and optimization over multiple turns. Therefore, we introduce GameXpert-Bench, which operationalizes the three lifecycle stages as three complementary benchmark tracks. GameGen evaluates complete game creation from a single request in an empty workspace. GameFix evaluates diagnosis and repair when defects are reported or left for the agent to discover. GameOpt evaluates cumulative optimization through request chains seeded by real development trajectories between users and agents. We evaluate each track using live game interaction, deterministic behavioral tests, or final product criteria with regression checks. The suite contains 97 generation tasks across 11 genres; 100 repair tasks from 50 game levels verified by humans, each with 19-27 injected bugs; and 17 optimization chains with six turns and 102 requests. Across the three tracks, current agents are more reliable at producing playable foundations and implementing explicit requirements than at discovering defects, verifying runtime behavior, and preserving functionality across changes.
