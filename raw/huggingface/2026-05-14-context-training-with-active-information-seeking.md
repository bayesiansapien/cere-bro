---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13050
url: https://huggingface.co/papers/2605.13050
arxiv_url: https://arxiv.org/abs/2605.13050
date: 2026-05-14
---

# Context Training with Active Information Seeking

Most existing large language models (LLMs) are expensive to adapt after deployment, especially when a task requires newly produced information or niche domain knowledge. Recent work has shown that, by manipulating and optimizing their context, LLMs can be tailored to downstream tasks without updating their weights. However, most existing methods remain closed-loop, relying solely on the model's intrinsic knowledge. In this paper, we equip these context optimizers with Wikipedia search and browser tools for active information seeking. We show that naively adding these tools to a standard sequential context optimization pipeline can actually degrade performance compared to baselines. However, when paired with a search-based training procedure that maintains and prunes multiple candidate contexts, active information seeking delivers consistent and substantial gains. We demonstrate these improvements across diverse domains, including low-resource translation (Flores+), health scenarios (HealthBench), and reasoning-heavy tasks (LiveCodeBench and Humanity's Last Exam). Furthermore, our method proves to be data-efficient, robust across different hyperparameters, and capable of generating effective textual contexts that generalize well across different models.
