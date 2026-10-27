---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800276+00:00
arxiv_id: 2610.21109
url: https://huggingface.co/papers/2610.21109
arxiv_url: https://arxiv.org/abs/2610.21109
date: 2026-10-26
---

# Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows

When humans collaborate with AI agents on long-horizon tasks, what happens to the agents' contributions? For solving long-horizon tasks, humans place greater importance on ongoing interaction with AI agents (e.g., revising plans) than on an agent's ability to complete the task in a single attempt. However, most agentic benchmarks have focused more on automation. Strong performance on such benchmarks does not imply effective real-world collaboration. Professional workflows offer a useful setting, as they often involve interdependent steps. To address this gap, we introduce Kolab, a new dataset of 115+ hours of screen recordings of 50 professionals from 40 occupations collaborating with agents on realistic, long-horizon problems. Kolab also contains participants' collaboration and output quality judgments. Our analysis reveals diverse collaboration patterns, highlighting the importance of when and how professionals coordinate with agents. A collaborative agent must do two things that automation benchmarks never test: anticipate whether experts will adopt, modify, or reject its contribution once it leaves the chat window to guide its next steps, and assess collaboration quality from the unfolding workflow without constant expert feedback. Our benchmark operationalizes both: (1) forecasting how professionals use agent contributions at diverse workflows, and (2) verifying their judgments of collaboration satisfaction and output quality. Findings show that frontier models, both agentic and non-agentic, overestimate collaboration with experts and struggle to distinguish between high- and low-quality collaboration. Longer workflow context does not consistently improve these predictions. As frontier agents cannot yet understand long-horizon collaboration with experts, we position Kolab as a valuable dataset for studying human-agent collaboration grounded in real professional workflows.
