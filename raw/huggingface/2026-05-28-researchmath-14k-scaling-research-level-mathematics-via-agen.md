---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.28003
url: https://huggingface.co/papers/2605.28003
arxiv_url: https://arxiv.org/abs/2605.28003
date: 2026-05-28
---

# ResearchMath-14K: Scaling Research-Level Mathematics via Agents

The frontier of mathematics is defined by problems whose solutions are not yet known, yet it remains unclear whether language models can meaningfully engage with such problems without human intervention. A major obstacle is the lack of large-scale research-level math datasets. To this end, we introduce ResearchMath-14k, a set of 14{,}056 problems curated from academic sources via a multi-agent pipeline, making it the largest collection of research-level mathematical problems to date. We further generate ResearchMath-Reasoning, 220K teacher trajectories from two open models, where we observe recurring avoidance behaviors such as non-attempts and fabricated references. Interestingly, across eight open-weight models, newer generations produce 5.6times more references and 5.0times more fake references per trace. After agentic filtering of ResearchMath-Reasoning, fine-tuning Qwen3 models from 4B to 30B parameters improves over base models by 9.2 points on average. This shows that filtered open-problem attempts can provide useful supervision even without fully correct reasoning traces. We make ResearchMath-14k publicly available for future works on research-level mathematical reasoning.
