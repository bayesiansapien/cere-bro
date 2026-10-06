---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.03240
url: https://huggingface.co/papers/2610.03240
arxiv_url: https://arxiv.org/abs/2610.03240
date: 2026-10-05
---

# Collective Bias Mitigation via Model Routing and Collaboration

Large language models (LLMs) are increasingly deployed in public health, finance, and governance, requiring both accuracy and societal value alignment. Despite recent advances, LLMs often perpetuate or amplify bias embedded in their training data, posing challenges to fairness. While self-debiasing encourages an LLM to identify and correct its own biases, relying on a single model's intrinsic knowledge may be insufficient to address deeply ingrained stereotypes. To address this limitation, we introduce Collective Bias Mitigation (CBM), a framework that alleviates bias by learning fine-grained model behavior and fostering knowledge sharing among diverse LLMs. This work is the first to systematically explore the effective selection and organization of distinct LLMs to cultivate fairer LLM responses. Experiments show CBM substantially outperforms standalone baselines (e.g., in the top-7 setting, Committee lowers the age bias score from 0.25 to 0.10). Our Debating and Committee topologies achieve substantial bias reduction, with the latter balancing mitigation effectiveness and inference cost, highlighting the potential of CBM for fairer LLMs.
