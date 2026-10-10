---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.417353+00:00
arxiv_id: 2610.12459
url: https://huggingface.co/papers/2610.12459
arxiv_url: https://arxiv.org/abs/2610.12459
date: 2026-10-09
---

# WorldGuide: Goal-Directed Video World Model for Procedural Task Execution

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely on pretrained executors or indirect verification. This leaves a gap between deciding an action and successfully realizing it. We formulate procedural video generation as closed-loop task execution in visual world space and introduce WorldGuide. Given only an initial image and a task goal, WorldGuide predicts an atomic action, generates its corresponding video clip, and uses the generated result to select the next action or terminate. The Planner and Executor are trained on the same step-level procedural demonstrations: the Planner learns to predict the next atomic action or task completion from visual progress, while the Executor is directly trained to realize the predicted actions. Hierarchical visual memory maintains state across long-horizon execution with bounded history token cost. Due to the lack of step-level action-video supervision for joint planner-executor training, we introduce WorldGuide Bench: approximately 59K step-annotated videos across 245 tasks and 27 procedural categories. WorldGuide achieves a 33.33\% Task Success on WorldGuide-Bench, compared with 29.90\% for the strong recent video model MiniMax-H3, even though MiniMax-H3 receives reference action plans, and achieves 47.69\% on VideoCraft-Bench compared with 32.73\% for MiniMax-H3 under goal-only conditioning. These results demonstrate the importance of coupling planning with learned execution for goal-directed procedural video generation.
