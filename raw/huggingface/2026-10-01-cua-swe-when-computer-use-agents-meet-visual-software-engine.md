---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349099+05:30
arxiv_id: 2609.32600
url: https://huggingface.co/papers/2609.32600
arxiv_url: https://arxiv.org/abs/2609.32600
date: 2026-10-01
---

# CUA-SWE: When Computer-Use Agents Meet Visual Software Engineering

Software development requires more than editing code: developers repeatedly run software, interact with its interfaces, visually inspect its behavior, and use these observations to decide what to change next and whether a change works. Existing coding agents and computer-use agents are largely studied in isolation, leaving this integrated development process underexplored. Diagnosing a runtime interaction failure requires agents to connect visual observations with the responsible code, then use the application again to verify the repair. We introduce CUA-SWE, a benchmark, environment, and evaluation pipeline for software engineering with computer use. Beyond studying how GUI feedback supports diagnosis and repair, we ask whether agents can complete software engineering tasks when required specification or operational information is available only through the running application's visual interface. CUA-SWE spans four software engineering domains and requires agents to modify code and configuration, execute commands, interact with running software, and inspect visual feedback within the same task. Each task includes deterministic, task-specific tests that verify whether the resulting software satisfies the requirements and preserves specified behavior. Our evaluation characterizes how frontier agents combine source-level execution with application screenshots and graphical interaction to produce verified software changes. We examine performance across domains and task information requirements, alongside the development behaviors associated with successful repairs. CUA-SWE provides a unified testbed for studying how agents use visual feedback and interaction to guide software engineering, with executable correctness criteria for the resulting software.
