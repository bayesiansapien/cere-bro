---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.223152+05:30
arxiv_id: 2610.19789
url: https://huggingface.co/papers/2610.19789
arxiv_url: https://arxiv.org/abs/2610.19789
date: 2026-10-15
---

# More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning

Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to training stability and computational cost. These limitations obscure the source of reported gains and the practical strengths and weaknesses of competing methods. Costly agent training further motivates a common basis for comparison. To address these gaps, we compare ten representative methods against GRPO on ALFWorld, ScienceWorld, Search-QA, and WebShop across three model sizes. Our study comprises 132 training runs totaling 12,124.4 recorded H800 GPU-hours, with repeated evaluations over eight rollout seeds for the pretrained backbones and all eleven trained methods. Beyond final task performance, we examine training progress, stability, and measured computational cost. Our evaluation yields three key findings. First, gains over GRPO remain limited in scope, with no method consistently outperforming it across settings. Second, strong final performance can mask unstable training. Third, additional training cost does not consistently translate into better performance. We establish this benchmark to support fair, comprehensive comparison and guide future research toward reliable and cost-effective improvements in agent training. Project page: https://aim-uofa.github.io/Self-Distillation-AgentRL/
