---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.03312
url: https://huggingface.co/papers/2606.03312
arxiv_url: https://arxiv.org/abs/2606.03312
date: 2026-06-07
---

# RobotValues: Evaluating Household Robots When Human Values Conflict

While household robots are often evaluated based on task completion, everyday domestic environments involve value-conflicting situations in which robots are expected to choose actions that prioritize other values than task success, such as human autonomy, efficiency, or social appropriateness. Yet, there are no benchmarks for evaluating robots' value preferences in such scenarios. We introduce RobotValues, a benchmark to evaluate household robot planners in 10K value-conflict scenarios. Each instance consists of a realistic household image with multiple plausible robot actions that prioritize different human values. We construct RobotValues through LLM-assisted scenario generation, stakeholder-grounded value extraction, image generation and automatic quality control. Using RobotValues we evaluate VLMs used in robotics and find that models exhibit default value preferences, including safety and accommodation, while underselecting privacy-prioritizing actions. When the models are instructed to prioritize specific values that conflict with their own preferences, they often fail to override their default actions, choosing incorrect actions for 80% of the time. These findings suggest that household robot evaluation should measure not only task completion or safety compliance, but also whether robots can choose among plausible actions when human values conflict.
