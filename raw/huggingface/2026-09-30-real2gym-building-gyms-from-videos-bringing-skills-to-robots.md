---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37089
url: https://huggingface.co/papers/2609.37089
arxiv_url: https://arxiv.org/abs/2609.37089
date: 2026-09-30
---

# Real2Gym: Building Gyms from Videos, Bringing Skills to Robots

Real-world videos provide rich demonstrations of manipulation, but turning them into reusable robot skills requires visually aligned environments, executable physical interactions, and mechanisms for learning from experience. We introduce Real2Gym, an agentic Real2Sim2Real framework that turns human and robot demonstrations into interactive simulation gyms and brings skills acquired in simulation to physical robots. The Real2Sim module reconstructs editable scenes, aligns objects and cameras with the input, validates demonstrated or retargeted actions through native physics execution, and generates task-conditioned variations with action-feasibility checks. Within these environments, the agent generates executable code for manipulation stages, observes their outcomes, and distills successful attempts and failures into reusable task procedures, object-relative motions, and recovery strategies. Through a shared perception-and-control interface, these skills guide subsequent execution in simulation and on real robots, with motions adapted to current observations and no updates to the underlying model weights. Extensive evaluations demonstrate that Real2Gym enables high-fidelity simulation environment reconstruction, outperforming GPT-6 Astra Direct Mode by 16.7% in success rate with approximately 74.9% fewer policy-execution tokens across these environments, while exceeding it by 33.3% in physical robot execution success rate across four tasks on a real Franka robot.
