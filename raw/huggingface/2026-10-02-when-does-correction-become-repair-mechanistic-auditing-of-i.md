---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.822109+00:00
arxiv_id: 2609.36138
url: https://huggingface.co/papers/2609.36138
arxiv_url: https://arxiv.org/abs/2609.36138
date: 2026-10-02
---

# When Does Correction Become Repair? Mechanistic Auditing of Internal Interventions in Tool-Using LLMs

Before invoking external tools, an agentic LLM must select among a K-way action space: executing a call, seeking clarification, answering directly, or declining. While internal activation steering can alter these pre-execution decisions, conventional aggregate metrics obscure where altered states land and what collateral damage they inflict. We present SAKIKO, an auditing framework that formalizes representation repair via directional error discovery, router-conditioned intervention, destination-resolved verification, and prospectively frozen statistical licensing. Across seven LLMs on When2Call and MetaTool, channel-keyed interventions induce direction-specific net gains in five models; across three sealed evaluations, none of 59 budget-matched random directions matches calibrated target gain. Crucially, destination auditing shows that behavioral movement does not equal repair: an intervention achieving +55 net gain corrupts over half of the baseline-correct decisions it touches, and promising point estimates on Qwen3-4B and Gemma-2-9B are formally declined due to finite-sample uncertainty. SAKIKO establishes the necessity of outcome-resolved adjudication before claiming internal repair. Code: https://github.com/ruizheliUOA/mechanistic-tool-use-llm.
