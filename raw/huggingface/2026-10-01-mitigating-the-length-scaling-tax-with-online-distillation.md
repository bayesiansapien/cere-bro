---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352899+05:30
arxiv_id: 2609.38854
url: https://huggingface.co/papers/2609.38854
arxiv_url: https://arxiv.org/abs/2609.38854
date: 2026-10-01
---

# Mitigating the Length-Scaling Tax with Online Distillation

Length scaling during reinforcement-learning (RL) post-training is often viewed as a sign of improved reasoning ability, especially on difficult problems, but may also make responses to already-solved problems unnecessarily verbose. We quantify this side effect as the length-scaling tax (LST): excess response length on already-solved queries without a commensurate accuracy gain. To mitigate LST, we propose Length Self-Distillation (LSD), which routes solved prompts to on-policy distillation and retains the original RL objective for unsolved prompts. LSD uses an exponential moving average of the online policy as its teacher, requiring no external model. We find that LSD achieves comparable or better performance than RL across multiple variants, while substantially curbing response-length growth on easy queries. LSD reduces LST from 19.0% to -3.7% on single-turn reasoning and from 31.4% to 13.7% on multi-turn agentic tasks, demonstrating that LSD effectively preserves concise response patterns on easy queries while supporting efficient exploration on difficult queries during RL post-training.
