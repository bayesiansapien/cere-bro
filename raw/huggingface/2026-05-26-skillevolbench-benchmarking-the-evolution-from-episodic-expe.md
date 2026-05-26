---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.24117
url: https://huggingface.co/papers/2605.24117
arxiv_url: https://arxiv.org/abs/2605.24117
date: 2026-05-26
---

# SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills

Large language model (LLM) agents accumulate rich episodic trajectories while solving real-world tasks, but it remains unclear whether such experience can be distilled into reusable procedural skills. We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation. It contains 180 tasks across six real-world agent environments, organized into role-conditioned task families with shared latent procedures. Agents learn from acquisition tasks, update an external skill library using compacted trajectories and verifier feedback, and then face frozen deployment tasks testing context shift, adversarial shortcuts, and composition. By comparing self-generated and curated-start skill evolution against no-skill and raw-trajectory controls, SkillEvolBench separates procedural abstraction from base capability, curated prior knowledge, and direct reuse of episodic traces. Across ten model configurations and three agent harnesses, we find that current agents often adapt locally but rarely form robust reusable skills. Skill-based conditions can improve acquisition or replay, and individual models sometimes gain on specific deployment axes, but these gains are unstable under frozen deployment. Raw-trajectory reuse frequently outperforms distilled skills, suggesting that current abstraction procedures discard contextual and procedural cues that remain useful for future tasks. Capacity and cost analyses further show that writing more skills or larger Tier-3 resource libraries is not sufficient: additional updates can improve coverage while introducing episode-specific drift and procedural clutter. These findings position SkillEvolBench as a testbed for measuring when one-off experience becomes durable procedural knowledge rather than task-local memory.
