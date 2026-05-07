---
source: farmer/huggingface
farmed: 2026-05-07T00:00:00Z
arxiv_id: 2605.03848
url: https://huggingface.co/papers/2605.03848
arxiv_url: https://arxiv.org/abs/2605.03848
date: 2026-05-07
---

# Parameter-Efficient Multi-View Proficiency Estimation: From Discriminative Classification to Generative Feedback

Estimating how well a person performs an action, rather than which action is performed, is central to coaching, rehabilitation, and talent identification. This task is challenging because proficiency is encoded in subtle differences in timing, balance, body mechanics, and execution, often distributed across multiple views and short temporal events. We discuss three recent contributions to multi-view proficiency estimation on Ego-Exo4D. SkillFormer introduces a parameter-efficient discriminative architecture for selective multi-view fusion; PATS improves temporal sampling by preserving locally dense excerpts of fundamental movements; and ProfVLM reformulates proficiency estimation as conditional language generation, producing both a proficiency label and expert-style feedback through a gated cross-view projector and a compact language backbone. Together, these methods achieve state-of-the-art accuracy on Ego-Exo4D with up to 20x fewer trainable parameters and up to 3x fewer training epochs than video-transformer baselines, while moving from closed-set classification toward interpretable feedback generation. These results highlight a shift toward efficient, multi-view systems that combine selective fusion, proficiency-aware sampling, and actionable generative feedback.
