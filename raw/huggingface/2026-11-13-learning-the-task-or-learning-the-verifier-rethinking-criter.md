---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.530131+00:00
arxiv_id: 2611.08318
url: https://huggingface.co/papers/2611.08318
arxiv_url: https://arxiv.org/abs/2611.08318
date: 2026-11-13
---

# Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the corresponding language instructions, so a score from such a verifier may not faithfully reflect whether the instructed task was completed, especially for robot-control programs written by an agent. As embodied coding agents report ever higher benchmark scores, a natural question arises: when a coding agent is exposed to the benchmark's criteria, does it generate code that better performs the instructed task, or code that simply overfits to the verification criteria? We conduct controlled experiments with a self-improving agent with and without CE, and find that with CE the agent quickly produces code with a higher success rate under the given criteria, but this advantage disappears when the criteria are changed slightly without departing from the original instructions. More importantly, the skills the agent develops under CE transfer poorly across tasks. We further propose instruction-faithful criteria and show that they better reflect the performance of agent-generated programs.
