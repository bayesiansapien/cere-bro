---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.202436+00:00
arxiv_id: 2611.09124
url: https://huggingface.co/papers/2611.09124
arxiv_url: https://arxiv.org/abs/2611.09124
date: 2026-11-09
---

# Toward the Era of Agentic Embodied Intelligence

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery. We introduce A2-MEAS, an embodied multi-agent framework built around code as a scaling interface. Learned correction codes combine corrective language, spatial evidence, execution history, and action proposals. MetaBrain provides training supervision and runtime guidance. A correction encoder and adapter absorb this knowledge into policy weights during training, while fresh codes adapt behavior with frozen weights at deployment. The action model, A2-WLA, adds motion-aware history and a latent world model to a vision-language-action policy. Surprisingly, this simple design with action pretraining and task specialization reaches 0.5755 Q-score on the 50-task BEHAVIOR 2026 public subset before online correction, 2.21x the 2025 winner's reported 0.2605 across different benchmark editions and training configurations. On all 100 BEHAVIOR 2026 public tasks, A2-MEAS achieves 0.6411 Q-score and 45.40% task success. On RoboTwin 2.0, A2-WLA achieves 93.98% average success, rising to 95.05% with the complete system. Across 12 real-robot tasks in five household settings, A2-WLA achieves 57.92% average success versus 26.67% for pi0.5. In long-horizon pour-over coffee preparation, a history-conditioned adapter raises post-failure completion at two filter-handling steps from 14% to 94% and from 8% to 82%, compared with A2-WLA retries. Our training infrastructure delivers 427.1 samples per second, 4.03x the throughput of a pi0.5 reference implementation on matched hardware. We will release the system, models, training scripts, and infrastructure to support efficient embodied learning.
