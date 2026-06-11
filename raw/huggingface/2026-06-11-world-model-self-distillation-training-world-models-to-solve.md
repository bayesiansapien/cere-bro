---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.12072
url: https://huggingface.co/papers/2606.12072
arxiv_url: https://arxiv.org/abs/2606.12072
date: 2026-06-11
---

# World Model Self-Distillation: Training World Models to Solve General Tasks

Pretrained video generators are promising visual world models that exhibit emergent task-solving abilities; however, their reliance on detailed textual descriptions limits their direct use for planning and decision-making. Existing approaches either outsource this reasoning to language or vision-language models, or rely on supervised fine-tuning with paired task-execution videos, which are costly to collect and difficult to scale. We propose a scalable framework that elicits task-solving ability in such models by combining self-distillation with reinforcement learning. Given an unlabeled scene image, a vision-language model generates a candidate task and a detailed step-by-step solution. The solution conditions a pretrained video diffusion model, the Demonstrator; we distill its behavior into an Executor conditioned only on the image and a short task prompt. This transfers execution knowledge from caption-guided generation to instruction-conditioned task solving without curated task-video supervision. We further improve the Executor with reinforcement learning from VLM feedback, exploiting the asymmetry between judging whether a sampled video satisfies a task and generating the solution. Experiments on our proposed WorldTasks-Benchmark and the DreamGen robotics benchmark show that the Executor surpasses the Demonstrator under our VLM-based evaluation protocol and transfers competitively to robotic tasks.
