---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.325591+00:00
arxiv_id: 2611.01112
url: https://huggingface.co/papers/2611.01112
arxiv_url: https://arxiv.org/abs/2611.01112
date: 2026-11-10
---

# Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation

Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's success rate from 22.5% under the reference control interface to 76.2%. We present Auriga, a task-agnostic agent harness that closes 68.3% of this gap in zero-shot manipulation without target-task trials or resets. In Auriga, the model makes all task decisions over an explicit task belief and acts through either direct tool calls or synthesized multi-step Python programs, while the harness supplies calibrated 3D measurements, finger-referenced dual-arm control, and a single admission gateway to the robot. Before motion, the model inspects a visual trajectory preview while simulation is paused; during execution, the harness checks declared stage tolerances and grasp bounds, stopping the robot on divergence and returning the measured discrepancy for in-place recovery. Developed across 13 cross-task capability iterations and frozen for evaluation, Auriga ranks first on the RoboDojo leaderboard with a 57.7% success rate (64.0 Score), more than doubling the reference harness on the same model, and remains first under scene randomization while learned policies drop by up to 33.9%. On RoboCasa365, the same frozen harness reaches a 73.2% success rate, outperforming VLA-assisted agents by up to 23.1% on composite tasks.
  Project page: https://auriga.stelledge.com/ Code: https://github.com/lose4578/Auriga
