---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.391379+00:00
arxiv_id: 2611.25005
url: https://huggingface.co/papers/2611.25005
arxiv_url: https://arxiv.org/abs/2611.25005
date: 2026-11-20
---

# Inhabitant: An Agent Framework for Long-Horizon Human-Scene Interaction with Spatial Control and Quantitative Feedback

Recent work on human-scene interaction (HSI) generation moves from single interactions to long-horizon interaction, where a language-model agent plans and executes a sequence of interactions in a 3D scene under one instruction. However, existing agents struggle in challenging everyday scenarios (e.g., picking up a toy and throwing it into a basket) because they lack spatial control over the motion and quantitative feedback on its execution, and they often fail to complete the interaction sequence. To address these gaps, we present Inhabitant, a training-free agent framework in which the agent specifies each motion through positions, paths and poses, measures how the executed interaction deviates from its intent, and revises the control specification accordingly. For an extensive evaluation in such scenarios, we build Inhabit, a benchmark of 75 household tasks in 31 furniture layouts of an apartment, in which every task chains one to three goals on movable objects and is carried out by the whole body, excluding fingers. On Inhabit, Inhabitant completes 98.7\% of the tasks with Claude Opus 5.5, and 93.3\% and 82.7\% with Claude Sonnet 5.5 and Gemini 4 Argon, respectively. Ablations confirm that without spatial control the agent fails most tasks, and without quantitative feedback its motion becomes less precise. Code is available on the project page.
