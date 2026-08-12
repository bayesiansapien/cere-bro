---
source: farmer/huggingface
farmed: 2026-08-12T03:35:42Z
arxiv_id: 2608.11079
url: https://huggingface.co/papers/2608.11079
arxiv_url: https://arxiv.org/abs/2608.11079
date: 2026-08-12
---

# SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure

Self-evolving agents accumulate reusable skills by appending successful procedures and failure fixes. Over time, the same requirement is often restated in several branches, examples, and warnings, while common action sequences are copied rather than reused. The resulting skill becomes expensive to inject and difficult to maintain. Generic prompt compression is ill-suited to this setting because a skill is not a flat passage: its name and description define when it applies, its workflow controls execution, its tool and output contracts constrain validity, and rare exceptions may remain essential even when no sampled task activates them. Evaluation-guided compression can test these behaviors, but it introduces rollouts, cost, and dependence on the compression-time evaluation set. We present SkillZip, an evaluation-free method that compresses a skill by finding its shortest faithful structural explanation. The intuition is explain once, reference many: state a repeated rule once at the scope where it applies, factor a repeated action sequence into a shared procedure, and keep only the differences as explicit exceptions. We formalize this intuition as a typed minimum description-length objective over a skill contract and a residual, subject to a hard coverage constraint for every extracted trigger, workflow edge, tool requirement, obligation, and output field. The formulation provides simple sharing thresholds, preserves unique rare rules by construction, and supports efficient local updates. SkillZip has a one-shot mode with one structured extraction call and deterministic optimization, and a continual Zip-on-Write mode that integrates each self-evolution patch without replaying tasks or reparsing the full history. Through comprehensive experimental evaluations, we demonstrate the effectiveness and superiority of SkillZip in compression performance, generalizability, and cost overhead.
