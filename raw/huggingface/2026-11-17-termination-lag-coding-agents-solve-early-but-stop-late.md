---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.112443+00:00
arxiv_id: 2611.14960
url: https://huggingface.co/papers/2611.14960
arxiv_url: https://arxiv.org/abs/2611.14960
date: 2026-11-17
---

# Termination Lag: Coding Agents Solve Early but Stop Late

Coding agents can solve a task well before they stop working on it. We characterize termination lag--the number of steps between an agent's first correct patch and the end of its run--across five models, two agent frameworks, and three SWE-bench datasets by recording and testing every distinct repository patch generated during execution. Our analysis reveals that 38--82% of successful runs achieve a correct solution on their initial source-code edit. However, agents continue to expend substantial effort after correct patches, with post-solution steps accounting for a median of 35--37% for Qwen3-Coder and 54--60% for Laguna-XS.2 in successful runs on SWE-bench Verified and Multilingual. Agents spend most of these additional steps verifying their work and exploring the repository. In a small fraction of cases (1--8%), this continued activity leads agents to undo their earlier correct patch, leaving the final solution incorrect.
