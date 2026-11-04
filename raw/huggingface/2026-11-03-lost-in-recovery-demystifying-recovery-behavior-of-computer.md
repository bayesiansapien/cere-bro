---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.27954
url: https://huggingface.co/papers/2610.27954
arxiv_url: https://arxiv.org/abs/2610.27954
date: 2026-11-03
---

# Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay

Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unintended side effects, making the ability to recover from failures critical. Yet, existing remedies remain inadequate: environment resets are infeasible in proprietary settings, action replay is prohibitively expensive over long horizons, and API-based rollback is limited to web environments, leaving model-based recovery largely unexplored. To address this gap, we present ReTrace, a scalable evaluation framework for systematically studying recovery behavior in computer-use agents. We formalize Transition-Consistent Recovery: identical downstream actions from the recovered and target states must yield identical outcomes. We operationalize this criterion through goal-oriented action replay following controlled error injection. Using ReTrace, we present the first systematic study of autonomous, model-based recovery, revealing that (i) ideal recovery can unlock model's latent task completion capabilities, (ii) current computer-use agents fail to exploit their latent recovery capabilities, and (iii) accurate model-based recovery yields measurable end-to-end gains. Together, these findings establish recovery as a fundamental capability for building reliable computer-use agents. Our code and dataset is available at https://github.com/BangProx/ReTRACE.
