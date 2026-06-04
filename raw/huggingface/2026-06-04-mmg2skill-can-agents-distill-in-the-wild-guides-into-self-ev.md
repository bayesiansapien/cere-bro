---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.01993
url: https://huggingface.co/papers/2606.01993
arxiv_url: https://arxiv.org/abs/2606.01993
date: 2026-06-04
---

# MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?

Abundant procedural knowledge on the Web holds great potential for helping agents solve long-horizon tasks. However, such knowledge is often multimodal, heterogeneous, noisy, and implicitly assumes human executors, making it difficult to use directly as the skills required by agents. To bridge the gap between human-oriented guides and agent-executable skills, we formalize this problem as guide-to-skill learning: converting in-the-wild guides into executable skills and continuously improving them from trajectories observable to the agent. To evaluate the capability of existing agents on this task, we introduce MMG2Skill-Bench, the first benchmark designed for this problem. We further propose MMG2Skill, a closed-loop framework that compiles guides into editable skills, conditions a fixed vision-language model (VLM) agent on these skills during execution, and revises the skills from trajectory-level root-cause feedback without using benchmark scores. Across GUI control, open-ended gameplay, and strategic card play with six VLM backbones, MMG2Skill consistently outperforms vanilla baseline agents in every model-domain setting, achieving macro-average gains of +12.8 to +25.3 percentage points across backbones. Ablation studies show that directly prompting agents with raw guides can degrade performance, while both structured skill construction and trajectory-driven revision are necessary for the observed improvements. On success-inferable tasks, analyzer-based early stopping further prevents late-stage performance regressions and saves 25%-53% of attempts when the success signal is properly calibrated.
