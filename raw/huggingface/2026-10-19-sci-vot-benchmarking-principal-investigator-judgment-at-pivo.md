---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.21082
url: https://huggingface.co/papers/2610.21082
arxiv_url: https://arxiv.org/abs/2610.21082
date: 2026-10-19
---

# SciΠvot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents

Large language model (LLM) agents can keep scientific experiments running for months with little human supervision, but reliable autonomous research also requires scientific judgment. Evaluating scientific judgment is difficult because research decisions are open-ended and depend on project context. We construct SciΠvot, a 248-case benchmark of scientific judgment based on human corrections. The benchmark draws on records from six months of research in which senior researchers ran LLM agents on 26 projects across six scientific fields and repeatedly intervened to correct the agents' research judgments. In each case, an agent chooses between the original LLM plan and the human-corrected alternative, using only the project record available before the correction as context. We compare LLM and human performance and examine the effects of reasoning effort, access to the project record, and reconsideration. At medium reasoning effort with the project record, models systematically prefer the original LLM plan over the human-corrected alternative. Four of five frontier models perform below chance on the selected cases. The highest accuracy in the project condition across the tested models and reasoning effort settings is 63.5%, compared with 73.4% for fresh researchers. At medium effort, every model achieves lower accuracy with the project record than without it, and reconsideration does not consistently improve overall accuracy. Even with a human-corrected alternative available, frontier models struggle with the selected research decisions, while SciΠvot supports systematic evaluation of scientific judgment for LLM agents.
