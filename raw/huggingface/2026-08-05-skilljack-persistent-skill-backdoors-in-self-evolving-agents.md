---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.03509
url: https://huggingface.co/papers/2608.03509
arxiv_url: https://arxiv.org/abs/2608.03509
date: 2026-08-05
---

# SkillJack: Persistent Skill Backdoors in Self-Evolving Agents

Self-evolving agents increasingly convert interaction histories into reusable skills that persist beyond individual tasks. While prior work studies memory and retrieval poisoning, such attacks only affect agents when poisoned records are retrieved as context. We uncover a new and more fundamental risk: poisoned experiences can be transformed by the agent itself into durable behavioral artifacts. We present SkillJack, the first attack that exploits the experience-to-skill pipeline of self-evolving agents. Instead of directly manipulating runtime context, SkillJack hijacks the agent's own learning process to implant malicious behaviors into its reusable skill repertoire. We identify three key properties of this transformation: sanitization whitewashing, where malicious intent is obscured during skill extraction; cross-layer promotion, where transient experiences become persistent capabilities; and persistence isolation, where the attack survives removal of its original source records. We evaluate SkillJack on two representative systems, SkillX and Anything2Skill, using a shared dataset of 150 trajectories across four policy-risk categories. Results show that skill extraction substantially reduces attack detectability: in SkillX, safety detection drops from 98.5\% for poisoned trajectories to 11.4\% for extracted skills, while Anything2Skill shows a similar effect. Meanwhile, the implanted skills remain effective, achieving attack success rates of 56.2\% and 89.2\% on the two systems, respectively. Furthermore, 80.0\% of skill-mediated attacks persist after deleting the original poisoned records, and some skills unintentionally activate on benign queries. Our findings reveal skill evolution as a new attack surface and motivate provenance-aware skill lifecycle protection. Our code is available at https://github.com/Tencent/AI-Infra-Guard/research/skilljack.
