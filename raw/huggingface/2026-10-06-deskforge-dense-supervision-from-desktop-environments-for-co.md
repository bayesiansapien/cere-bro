---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02320
url: https://huggingface.co/papers/2610.02320
arxiv_url: https://arxiv.org/abs/2610.02320
date: 2026-10-06
---

# DeskForge: Dense Supervision from Desktop Environments for Computer-Use Agents

Computer-use agents need to reliably ground action targets in complex desktop scenes, where multiple applications, overlapping windows, and visually similar controls compete for attention. Existing training data rarely pair such scenes with dense annotations or vary them in a controlled way. We introduce DeskForge, a controllable desktop environment that composes and explores real applications to generate large-scale supervision for computer-use agents. It varies application states, content, window layout, appearance, and resolution, and fuses screenshots, accessibility trees, and window geometry into dense element annotations while recording the outcome of each executed action. Using this environment, we construct DeskForge-1M, a corpus of 1.2M annotated desktop observations containing 159.7M element instances. We fine-tune four vision-language models on 200K grounding examples drawn from DeskForge-1M. All four improve across held-out desktop conditions and on all five external GUI grounding benchmarks; for Qwen3.5-4B, accuracy increases by 11.51 percentage points on ScreenSpot-Pro and 10.11 points on OSWorld-G. The gains also translate to long-horizon task completion: under a fixed planner, the fine-tuned action models solve more WebArena-Infinity and OpenApps tasks, with Qwen3.5-4B increasing from 31 to 50 of 119 tasks and from 3 to 15 of 100 tasks, respectively. These results show that controllable composition of real desktop environments provides a scalable source of supervision for improving both GUI grounding and long-horizon computer use. The framework code, the dataset, and the fine-tuned model are available from the project page: https://saidgurbuz.github.io/deskforge/
