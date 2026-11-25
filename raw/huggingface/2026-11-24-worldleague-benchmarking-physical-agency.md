---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.917671+00:00
arxiv_id: 2611.30989
url: https://huggingface.co/papers/2611.30989
arxiv_url: https://arxiv.org/abs/2611.30989
date: 2026-11-24
---

# WorldLeague: Benchmarking Physical Agency

AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms. What range of physical goals can today's AI systems achieve autonomously? Answering this question requires testing systems on tasks that demand different combinations of perception, memory, planning, and action. We introduce WorldLeague, a benchmark that compares AI systems on a common set of 60 simulated robot tasks by measuring progress toward each task's physical goal from the robot's trajectory. Robots explore scenes to gather evidence in WorldSeek, rearrange objects in WorldShape, and adapt to changes in WorldShift. Tying these goals to a single control interface limits which AI systems can be compared. In WorldLeague, vision-language models (VLMs) choose targets and motions, while vision-language-action models (VLAs) and world-action models (WAMs) use their native controls. For each of six capability dimensions, we measure how much progress a system makes toward its goals (Interactive Score) and how often it achieves them (physical success rate). Together, these measures form the system's Physical Agency Profile. Among 13 representative AI systems, Claude Fable 5.2 achieves 13 of the 60 goals and earns the highest mean Interactive Score (28.58/100). Fable leads in four dimensions, while GPT-6.1-Sol and GPT-6-Astra tie for first on rule-following tasks. Even when VLMs answer every final question correctly, they receive an Interactive Score of zero in 71.8\% of those episodes. WorldLeague gives Embodied AI, Physical AI, and Agentic AI a shared basis for comparing what AI systems achieve autonomously, from partial progress toward a physical goal to full goal completion. Project Webpage: https://xyangzhou.github.io/WorldLeague
