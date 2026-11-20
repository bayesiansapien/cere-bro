---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.140645+00:00
arxiv_id: 2611.24789
url: https://huggingface.co/papers/2611.24789
arxiv_url: https://arxiv.org/abs/2611.24789
date: 2026-11-19
---

# HINT-WAM: Hindsight-Informed Training for World Action Models

World action models (WAMs) have shown promising generalization and data efficiency in robot manipulation by coupling action generation with predictions of future visual dynamics. Translating these capabilities into reliable task execution, however, remains a challenge for existing post-training methods. Offline supervised fine-tuning provides dense supervision on expert trajectories, but its flow-matching action expert is trained only on noised demonstration actions and never on the intermediate states produced by its own sampler; task-specific adaptation can also compromise pretrained capabilities. On-policy reinforcement learning trains on the policy's own behavior, yet sparse task rewards make exploration and credit assignment difficult, while dense reward shaping still provides scalar evaluations rather than direct action targets. We introduce HINT-WAM, the first on-policy self-distillation framework that supervises the action expert on its own sampling trajectories using hindsight, the future video of the demonstration, as privileged information available to the WAM itself. For each demonstration observation, the student generates its action through its own denoising trajectory, and at the states along this trajectory the same model acts as a teacher conditioned additionally on this hindsight, providing a conditional action distribution as a dense training target, while the student sees only deployment-time inputs and needs no environmental rewards or simulator interaction. To transfer this supervision to a flow-matching action expert, HINT-WAM distills the teacher into the student with an energy score, a distribution-level objective that matches the teacher's action distribution from the student's own samples rather than regressing its velocity field. The project web is available in https://tuandattt.github.io/hintwam/.
