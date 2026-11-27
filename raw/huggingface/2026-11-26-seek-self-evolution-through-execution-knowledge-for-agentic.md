---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.906086+00:00
arxiv_id: 2611.33915
url: https://huggingface.co/papers/2611.33915
arxiv_url: https://arxiv.org/abs/2611.33915
date: 2026-11-26
---

# SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation

General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working context. Once the task ends, it loses this execution knowledge, such as how to carry a bowl between two grippers. On the next attempt at the task, the robot may take just as long and repeat the same mistakes. To avoid this repetition, robots must retain execution knowledge across attempts. Yet replaying past actions is insufficient, because their effects depend on the current conditions. Procedures that determine actions from the current scene address this, but when they meet conditions that earlier attempts did not cover, revising them requires the measured effects of earlier actions. We therefore propose SEEK, an agentic framework that retains both, enabling robots to improve across attempts while keeping the underlying model fixed. To adapt retained knowledge to the current scene, SEEK adopts a Self-Evolving Programmatic Policy (SEPP) that encodes manipulation as executable procedures and determines each action from current observations. As the robot executes these procedures, SEEK records the measured effects of its actions, including those from failed attempts, in a Persistent Action-Effect Bank (PAEB). Where a retained procedure applies, it acts without a model request; where it meets a condition it does not cover, this evidence guides its revision. On RoboDojo, knowledge retained over ten attempts raises SEEK's average task score from 27.0 to 54.4 and its success rate from 19.7% to 48.0% across all 42 tasks. On 34 of these tasks with GPT-6.2 Astra, SEEK reaches 80.1 after five attempts, against 49.6 for the same model acting directly, and uses 77.6% fewer model requests. https://zeyangguan.github.io/SEEK-Agentic-Robot-Manipulation/
