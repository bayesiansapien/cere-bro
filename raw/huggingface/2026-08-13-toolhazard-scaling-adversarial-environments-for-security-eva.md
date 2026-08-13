---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.11878
url: https://huggingface.co/papers/2608.11878
arxiv_url: https://arxiv.org/abs/2608.11878
date: 2026-08-13
---

# ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents

Large language model (LLM) agents integrated with external tools are vulnerable to indirect prompt injections embedded in environmental states. However, existing studies largely rely on manually implemented or reused environments, stochastic LLM-based tool simulation, and predefined injection locations, limiting scalable security research across broader domains. To bridge this gap, we propose **ToolHazard**, a scalable adversarial environment synthesis framework that reduces human engineering and supports expansion with additional seed domains and compute. Through an Environment Simulator, an Attacker Agent, and a User Simulator, ToolHazard synthesizes executable stateful environments, discovers viable injection points and generates environment-specific payloads, and constructs state-grounded long-horizon tasks. Based on ToolHazard, we build **ToolHazard-Bench** for stress-testing agents under complex workflows and diverse environmental attacks. Experiments reveal substantial agent vulnerabilities and show that injection timing and placement affect attack effectiveness. Moreover, ToolHazard-generated alignment data improves security on both ToolHazard-Bench and AgentDojo while preserving benign task utility.
