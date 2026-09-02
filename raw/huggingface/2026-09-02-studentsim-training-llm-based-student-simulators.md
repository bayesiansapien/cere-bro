---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2609.01591
url: https://huggingface.co/papers/2609.01591
arxiv_url: https://arxiv.org/abs/2609.01591
date: 2026-09-02
---

# StudentSim: Training LLM-based Student Simulators

AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to collect from real learners. Student simulators can provide this signal as a proxy, yet existing approaches are limited: state-tracking models fit student behavior but struggle to process explanations or corrections, while LLM role-play follows guidance fluently but does not reliably match the competence of the student being imitated. We present StudentSim, a training framework that turns sparse per-student data into individualized simulators through pooled training followed by per-student specialization. The resulting simulators both mirror a student's own responses and update them under tutor guidance. We also introduce StudentSimEval, a standardized protocol covering 60 students across chess, second-language English writing, and mathematics, using public learner datasets with de-identified records shared for research. StudentSimEval measures behavioral fidelity (F), or how well a simulator matches a student's responses, and guidance responsiveness (R), or how readily it updates under tutor guidance, with all methods fit and evaluated on the same records. Across all three domains, StudentSim outperforms GPT-5.4 on both metrics. In chess, StudentSim reaches F=0.51 and R=0.91, compared with 0.23 and 0.72 for GPT-5.4 and 0.45 and 0.27 for Maia2. As a proof of concept, using StudentSim as a reward model for tutor reinforcement learning produces a chess tutor that expert humans rate as more accurate, better-guided, and more personalized than a no-RL baseline and a tutor trained against a GPT-5.4 simulator reward. Code is available at https://github.com/microsoft/StudentSim.
