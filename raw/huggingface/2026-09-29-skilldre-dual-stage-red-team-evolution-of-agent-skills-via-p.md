---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935622+00:00
arxiv_id: 2609.32400
url: https://huggingface.co/papers/2609.32400
arxiv_url: https://arxiv.org/abs/2609.32400
date: 2026-09-29
---

# SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution and Runtime Feedback

Agent skills package instructions, executable code, and task-specific resources into reusable artifacts that agents can improve using execution feedback. The same mechanism also enables attackers to evolve malicious skills, making them more effective and less detectable. However, a candidate skill may pass pre-execution scanning yet fail to realize its target under runtime defenses, while a revision that repairs execution may introduce new scanner findings. We introduce SkillDRE, a fully automated framework for evolving complete malicious skill packages through a dual-stage feedback loop. Given a benign task and its associated skills, SkillDRE autonomously constructs and validates a task-conditioned malicious objective and a verifiable judge rule. It then holds both fixed while evolving the skill implementation, with preservation of legitimate task capability. SkillDRE combines scanner-guided evolution with runtime-guided refinement informed by execution outcomes observed under runtime defense. Each runtime-guided revision returns to the pre-execution stage for rescanning and further optimization before re-execution, forming a cross-stage closed loop. Evaluated on SkillsBench across four victim models, SkillDRE achieves an average attack success rate of 45.28%, exceeding the strongest baseline by 40.3%, while its final submitted skills receive no SkillScan findings and largely preserve benign-task performance. These results show that two-stage defense feedback can serve as a useful learning signal for adaptive red teaming and that evaluating either defense stage in isolation can miss the resulting attack capability. Codes is available at https://github.com/whfeLingYu/SkillDRE
