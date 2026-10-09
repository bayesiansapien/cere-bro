---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.314376+05:30
arxiv_id: 2610.09228
url: https://huggingface.co/papers/2610.09228
arxiv_url: https://arxiv.org/abs/2610.09228
date: 2026-10-08
---

# Co-Evolving Robot Orchestrators and Policies through Deployment

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because the harness is built around a frozen policy that has limited language steerability, the orchestrator can avoid the policy's failures but never overcome them. The policy becomes the bottleneck of the whole system. Fine-tuning the policy can remove this bottleneck, but updating it alone decouples it from an orchestrator tuned to its old behavior. We propose Robo-COP, in which the orchestrator and policy co-evolve during deployment. Robo-COP curates skill demonstrations from its own executions, fine-tunes the policy when this data can address recurring failures, and adopts each new policy only after it improves the skills it was trained for. Across ten simulated RoboLab tasks, Robo-COP raises mean held-out success from 64.8% to 73.8% over the same harness with a frozen policy, while fine-tuning on a fixed schedule without verification reaches only 65.8%. On three real-world tasks, Robo-COP raises held-out success from 38.3% to 50.0%. Robo-COP turns deployment into a self-improving flywheel in which robots learn by doing, with each improvement in execution producing better data for the next round of learning. Videos and code are available at https://robo-cop.pages.dev/.
