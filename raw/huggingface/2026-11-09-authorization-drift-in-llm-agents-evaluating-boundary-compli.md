---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.205634+00:00
arxiv_id: 2611.09113
url: https://huggingface.co/papers/2611.09113
arxiv_url: https://arxiv.org/abs/2611.09113
date: 2026-11-09
---

# Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use

LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis (SERS) grounds benchmark validation in real agent rollouts rather than LLM self-critique. Across 13 LLMs and three frameworks (25,207 trajectories), greater capability accompanies greater drift, with frontier-capable models exhibiting drift rates of 0.43 to 0.61. Yet 86.18% of tasks admit an observed clean-success trajectory, showing that drift is avoidable. Drift is persistent and dominated by early data over-collection; apparent improvements under agentic scaffolds coincide with collapsing clean-completion performance. To understand potential harms to individuals and society, we map drift points to legal provisions across four jurisdictions, connecting overreach to privacy and information-security concerns. Data minimisation is the most frequently implicated provision, and 93.5% of legally grounded drifting runs map to multiple jurisdictions, making the potential consequences of authorization drift more interpretable.
