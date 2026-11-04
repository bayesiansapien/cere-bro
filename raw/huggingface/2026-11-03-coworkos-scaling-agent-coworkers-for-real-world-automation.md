---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.03178
url: https://huggingface.co/papers/2611.03178
arxiv_url: https://arxiv.org/abs/2611.03178
date: 2026-11-03
---

# CoworkOS:Scaling Agent Coworkers for Real-world Automation

Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decision-making over long horizons, a combination that remains an open challenge. We introduce CoworkOS, a general-purpose harness for long-horizon work that separates task strategy from execution management: the model decides actions, delegation, and acceptance, while the runtime maintains state and feedback. Its three-layer architecture enables direct execution or delegation to Subagents, synchronously or asynchronously, under stable responsibilities. Through a shared application layer, humans and agents inspect and revise the same evolving documents, presentations, CAD models, and Blender scenes, so human-in-the-loop participation can enter both through conversation and through direct modification of the work itself. To sustain continuity across agents and sessions, CoworkOS further introduces hierarchical workspaces and persistent semantic memory, so working files, key decisions, and long-running Job logs remain shareable, reusable, and resumable after interruption. Across 12 benchmarks and 6 categories of real-world applications, CoworkOS proves highly competitive with frontier agent applications such as Codex and DeepSeek Harness. As a sustained-work case study, CoworkOS uses GLM-5.3 as its backbone to conduct RSI-driven automated post-training on Qwen3.6-35B-A3B. Over five rounds, the model's average score across eight benchmarks rose from 33.19 to 42.95 (+9.76). Looking ahead, we believe CoworkOS opens a meaningful path toward general cowork-agent intelligence.
