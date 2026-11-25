---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.929877+00:00
arxiv_id: 2611.30075
url: https://huggingface.co/papers/2611.30075
arxiv_url: https://arxiv.org/abs/2611.30075
date: 2026-11-24
---

# Context-Grounded Skill Internalization for Vision-Language Agents

Skill internalization offers a way for agents to learn useful behaviors from skills and use them without explicit guidance in context at inference time. A common approach is to generate demonstration trajectories with the skill in context and then fine-tune the same model on its own trajectories with the skill removed. However, this leads to the problem that the model may learn to reference the removed skill, which we named as context misalignment (CoMi). In this work, we first analyze agent behaviors related to CoMi under this common pipeline. Across ALFWorld, WebShop, and ARC-AGI-1, skill-removed fine-tuning consistently results in CoMi: 12.2-46.0% of test trajectories reference the removed skill. To address this problem, we develop Context-Grounded Skill Internalization (CGSI). CGSI uses a sentence detector to identify unsupported references and then masks or rewrites the selected sentences before fine-tuning. Experimental results demonstrate the effectiveness of CGSI and reveal two key findings. (i) Compared with directly fine-tuning with the skill removed, CGSI reduces CoMi at test time by 72.5-94.6% while preserving task success. (ii) Compared with existing reinforcement learning-based skill-internalization baselines, CGSI achieves comparable performance with substantially less training time. CGSI also significantly reduces processing costs compared with large-scale trajectory auditing and correction.
