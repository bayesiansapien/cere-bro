---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.387481+00:00
arxiv_id: 2611.26248
url: https://huggingface.co/papers/2611.26248
arxiv_url: https://arxiv.org/abs/2611.26248
date: 2026-11-20
---

# TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs

AI agents are increasingly expected to act as AI scientists, which requires three increasingly open abilities: carrying out a given computational workflow correctly, choosing the next measurements from a given design space, and designing their own experiments. Existing benchmarks mainly evaluate the first two abilities, in a terminal or in a closed loop that selects from predefined candidates. Evaluating the third ability requires reliably executing an experiment that an agent designs, with readings grounded in a real laboratory. We introduce TwinLab-Bench, which evaluates AI scientists on self-designed experiments in 52 tasks from laboratories in the physical sciences, the life sciences, and engineering. The benchmark supports more than 100 experimental action types, and the agent's report is scored by comparison with a hidden answer taken from real laboratory records. Each task has its own TwinLab agent, an agent that serves as the environment and executes the experiments that the tested agent designs, reading the raw materials of the laboratory and calling calculators that are built from its records. Compared with a language model that sees only the task description, the TwinLab agent almost eliminates readings that deviate from the real records and inconsistent answers to a repeated request, and closed-book probes control for answers recalled from memory. We find that these tasks remain hard for frontier models: the strongest, Claude Fable 5.2, averages a score of only 45.0, and we conduct an empirical study of where it fails.
