---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.08244
url: https://huggingface.co/papers/2610.08244
arxiv_url: https://arxiv.org/abs/2610.08244
date: 2026-10-07
---

# Sensor-Language-Action Models

Sensors are useful not only for understanding the world but also for deciding what to do next. Existing sensor models however largely stop at perception: they recognize states or predict outcomes, leaving actions modeled separately through task-specific and often closed label spaces. We introduce Sensor-Language-Action (SLA) modeling, a framework that connects multimodal sensor observations, natural language, and actions within a unified model. SLA uses language as a semantic interface between sensing and acting, allowing heterogeneous actions to be represented, predicted, and explained while remaining grounded in the underlying sensor evidence. We build a large-scale SLA benchmark consisting of datasets that span more than 116,000 individuals, 79 sensor modalities, and 60 action groups, together with a multi-faceted captioning pipeline that aligns user context, sensor dynamics, and action evidence. Building on this framework, we present OpenSLA, a unified SLA model for hierarchical action prediction, state understanding, and action explanation. Extensive experiments on real-world tasks in clinical prediction, operating rooms, and metabolic health verify its superior performance over the state-of-the-art. OpenSLA also demonstrates intriguing capabilities including language-guided evidence grounding and zero-shot generalization to unseen actions and cohorts.
