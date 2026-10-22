---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25736
url: https://huggingface.co/papers/2610.25736
arxiv_url: https://arxiv.org/abs/2610.25736
date: 2026-10-20
---

# Learning from Fleet Experience: A Collective Learning Paradigm for Robots

Experience generated during deployment offers an opportunity for robots to improve policy reliability through learning from their own executions. However, learning through human corrections requires teleoperators to monitor execution and intervene when policies fail, a demand that is difficult to meet as robot fleets grow. We introduce collective experience learning (CEL), a learning paradigm in which deployed robots share their execution experience to improve a common policy. We realize CEL through failure-guided experience retrieval fine-tuning (FERT), which uses failure contexts from robot executions to retrieve relevant trajectory segments from the fleet's shared successful experience and uses their actions as supervision for policy updates, without collecting additional expert demonstrations or corrective actions. A fault-tolerant asynchronous training system (FATS) coordinates experience collection, policy optimization and policy distribution despite local interruptions within the robot fleet. Across five real-world manipulation tasks, the resulting policies achieve success rates of 93.3-99.2%, evaluated over 120 trials per task on robots excluded from training data collection. With collection time per robot held fixed, larger fleets provide more experience and FERT generally achieves higher success rates across the evaluated sizes. On multi-stage phone packaging, learning with 96 robots increases success from 79.2% to 98.3%. These results support collective experience as a practical basis for scalable robot learning and a path towards improving policy reliability during deployment without collecting additional expert corrective actions.
