# SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills

**Source:** [arXiv:2605.24117](https://arxiv.org/abs/2605.24117), via HuggingFace Daily Papers 2026-05-26.
**Topic:** Agent skills / procedural knowledge / experience reuse.

## TL;DR

LLM agents accumulate rich episodic trajectories solving tasks, but it remains unclear whether that experience can be distilled into reusable procedural skills that survive context shift. SkillEvolBench is a diagnostic benchmark for exactly this step. 180 tasks across six real-world agent environments, organized into role-conditioned task families with shared latent procedures. Agents learn on acquisition tasks, update an external skill library from compacted trajectories plus verifier feedback, then face frozen deployment tasks under context shift, adversarial shortcuts, and composition. Verdict across 10 model configurations and 3 agent harnesses: current agents adapt locally but rarely form robust reusable skills. Raw-trajectory reuse frequently outperforms distilled skills, suggesting current abstraction procedures discard contextual cues that future tasks still need. Writing more skills or larger libraries does not help: additional updates improve coverage at the cost of episode-specific drift and procedural clutter.

## Why this matters

This is the empirical-validation paper sitting directly next to SkillOpt (2026-05-25, the deep-learning-style optimizer for the skill document with a held-out validation gate that hit +24.8 on GPT-5.5 inside Codex). SkillOpt said: train the skill artifact like a weight tensor and the gains are real. SkillEvolBench says: but the natural baseline (raw-trajectory reuse, no skill abstraction at all) often wins, and naively scaling skill libraries hurts. The two papers together define the open problem precisely: skill abstraction is not free, and the current SkillOpt-style optimization works on a subset of cases the wiki should not yet take as universal.

## Key findings

- **180 tasks** across six environments. Role-conditioned task families with shared latent procedures (so a learned skill should generalize within family).
- **Acquisition / deployment split**: agents update a skill library on acquisition tasks, then face frozen deployment tasks that test context shift, adversarial shortcuts, and composition.
- **Headline result**: agents adapt locally but rarely form robust reusable skills. Skill-based conditions can improve acquisition or replay, but gains are unstable under frozen deployment.
- **Negative result**: raw-trajectory reuse frequently outperforms distilled skills. The current abstraction procedures (used by Trace2Skill, EvoSkill, Skill1, SkillOS, GEPA, SkillOpt) discard contextual and procedural cues that the deployment task still needs.
- **Scaling result**: writing more skills or making the library larger is not sufficient. Additional updates introduce episode-specific drift and procedural clutter that degrades downstream use.

## How this relates to prior wiki pages

The wiki has been tracking the skill-evolution thread closely:

- **2026-04-18 Corpus2Skill** (knowledge navigation, the original "distill trajectories into skills" instance)
- **2026-05-05 Ctx2Skill** (self-evolving skills, the iteration that added context conditioning)
- **2026-05-07 MedSkillAudit** (domain-specific audit showing skill quality degrades fast)
- **2026-05-09 Skill curation cluster** (Strata, Skill1, SkillOS, the cluster of skill-management systems)
- **2026-05-25 SkillOpt** (deep-learning-style optimizer with validation gate, the best result yet)

SkillEvolBench is the benchmark this cluster needed. It validates that SkillOpt's approach works on some cases (Codex coding-agent setting), and exposes that the broader claim "agents can distill experience into reusable procedural skills" is much weaker than the field has assumed. Specifically: the wiki's own thread synthesis from 2026-05-25 ("portable harness + portable skill + portable prompt + stable model is the new agent architecture") needs the qualifier that "portable skill" is not yet universally portable, only situationally so.

The companion lifecycle paper from 2026-05-25 (the skill lifecycle study that showed extractor strength and consumer strength decouple) already pointed at this: skill distillation is a routing problem, not just an optimization problem. SkillEvolBench makes the same point at the deployment side: distilled skills under-transfer because the abstraction step discards context the deployment task needs.

## Research angle

The natural reading is that current skill abstractions over-abstract. The fix is not better optimization of the skill text (SkillOpt has already pushed hard on that surface); it is better representation of what context to preserve in the skill itself. A skill that carries its conditioning cleanly (when it applies, what assumptions it makes, what failure modes it has) is what the benchmark is implicitly asking for. The next paper in this thread should treat skill conditioning as the load-bearing design surface.

## Industrial implication

Production agent stacks that have invested heavily in skill libraries (Microsoft Copilot's portable skill catalog, Anthropic's Claude Skills) should treat this benchmark as an audit tool, not a leaderboard. The result that more skills makes things worse will land hard with any team that has been measuring success by skill-library growth.
