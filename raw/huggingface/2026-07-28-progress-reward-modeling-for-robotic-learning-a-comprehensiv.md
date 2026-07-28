---
source: farmer/huggingface
farmed: 2026-07-28T03:19:32Z
arxiv_id: 2607.21655
url: https://huggingface.co/papers/2607.21655
arxiv_url: https://arxiv.org/abs/2607.21655
date: 2026-07-28
---

# Progress Reward Modeling for Robotic Learning: A Comprehensive Survey

Robotic learning takes place in dynamic environments with large behavior spaces. A terminal success signal only tells the robot whether the task is completed. It does not explain whether the current behavior is making progress, remaining unchanged, or undoing earlier progress. For this reason, recent studies have increasingly explored progress rewards that provide feedback during task execution. However, the current literature lacks a shared framework. Existing methods use different observations, goal specifications, output signals, supervision sources, and evaluation protocols. This makes it difficult to compare them and understand what their results actually validate. In this survey, we provide a unified view of progress reward modeling for robotic learning. We organize the field in three connected steps. We first study the interface of a progress model. This defines the problem from the outside by asking what information the model receives and what form of progress signal it produces. We then move inside the model and study the methods used to construct this signal. This reveals the different assumptions and mechanisms behind progress estimation and reward generation. Finally, we examine the data and benchmarks that support these methods. This shows how progress supervision is obtained and what different evaluations actually measure. Together, these three perspectives connect what a progress model is, how it is built, and how its quality is validated. We further summarize the main limitations of current approaches and discuss future research directions.
