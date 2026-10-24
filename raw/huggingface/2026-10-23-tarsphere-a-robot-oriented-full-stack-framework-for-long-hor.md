---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.888163+00:00
arxiv_id: 2610.30043
url: https://huggingface.co/papers/2610.30043
arxiv_url: https://arxiv.org/abs/2610.30043
date: 2026-10-23
---

# TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments

Robots must act under physical and social constraints while adapting to changes in their environment and human needs. Existing embodied-agent systems often focus on specified goals or abstract execution into symbolic actions, limiting evaluation in an evolving world. We introduce TARSphere, a robot-oriented full-stack framework for physically and socially grounded long-horizon embodied agents. TARSphere-Infra runs robot policies in a physics simulator with embodied NPCs and constrained dialogue. An event-driven finite-state machine (FSM) uses completed actions and delivered information to update task states and evaluate outcomes. TARSphere-Harness, its embodied brain harness, lets a frozen multimodal large language model (MLLM) act through multi-level executable skills, using observations, hierarchical memory, and execution feedback to revise its decisions. On this foundation, agent-in-the-loop curation aligns task semantics, causal dependencies, and scene geometry to construct TARSphere-Bench: 360 episodes across 30 indoor scenes. Five paired conditions assess perceptual robustness, disruption adaptation, task update, human coordination, and intent understanding for navigate-and-report and fetch-and-deliver tasks. Our evaluation of 8 MLLMs shows that general-purpose models can outperform embodied models, while task updates and human interaction remain difficult. Frequent collisions and falls further motivate evaluating execution safety alongside task success, even with a shared action interface and decision budget.
