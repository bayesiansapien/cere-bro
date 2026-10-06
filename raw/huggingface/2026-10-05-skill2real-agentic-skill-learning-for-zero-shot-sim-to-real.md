---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.02788
url: https://huggingface.co/papers/2610.02788
arxiv_url: https://arxiv.org/abs/2610.02788
date: 2026-10-05
---

# Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation

Transferring robotic skills from simulation to reality requires task knowledge that remains usable across differences in perception, dynamics, and embodiment. We introduce Skill2Real, an agentic policy framework that learns executable skills through a shared application programming interface (API). A Proposer-Verifier-Governor (PVG) loop uses privileged simulation evidence to diagnose outcomes and validate updates, while keeping learned skills grounded in public observations and API semantics. The Cerebellum first acquires local manipulation skills; the Brain then learns task-level composition with the Cerebellum frozen. Both memories transfer to the real robot without task-policy fine-tuning or skill-memory updates. As GPT-5.6 Sol learns skills on LIBERO-90, evaluating each frozen checkpoint with GPT-6 Astra raises LIBERO-Pro Long success from 2.0% to 56.3%, without training on Pro Long. Independent Robosuite training reaches 85.1% and 89.4% mean success with Sol and Opus 5 across seven tasks, respectively. Frozen Sol-trained LIBERO-90 skills achieve 78.75% mean completion across four real-world manipulation tasks with Astra. Removing the Verifier or Governor during LIBERO-90 training lowers final Pro Long success by 17.3 and 13.3 percentage points, respectively. These results support learning and transferring a hierarchy of executable skills through a common robot interface.
