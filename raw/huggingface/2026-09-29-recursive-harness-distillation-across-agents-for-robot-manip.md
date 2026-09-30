---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929116+00:00
arxiv_id: 2609.33378
url: https://huggingface.co/papers/2609.33378
arxiv_url: https://arxiv.org/abs/2609.33378
date: 2026-09-29
---

# Recursive Harness Distillation across Agents for Robot Manipulation

A central goal in robotics is to enable manipulation across changing tasks and environments. Vision-language-action (VLA) models provide broad manipulation capabilities but can struggle when execution requires diagnosing failures and adapting behavior. Strong agents can discover effective interventions through interaction with these policies. We propose Recursive Harness Distillation to accumulate this experience as reusable guidance across agents. A strong agent distills its experience into a playbook for a light agent, then recursively refines the playbook using the light agent's execution feedback. The resulting playbook enables agents to reuse accumulated intervention knowledge in new task instances without updating model parameters. In real-world manipulation, the harness improves success from 37.3% to 64.0%. On SimplerEnv Bridge, the light agent with the playbook achieves 66.7% success, compared with 41.7% for the GR00T-only baseline, and outperforms the strong agent without a playbook. The same playbook also benefits the strong agent, which reaches 79.2% success. These results demonstrate the feasibility of harness distillation for robotics: intervention experience can be accumulated, refined through execution, and reused across agents to improve manipulation.
