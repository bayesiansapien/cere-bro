---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.27951
url: https://huggingface.co/papers/2607.27951
arxiv_url: https://arxiv.org/abs/2607.27951
date: 2026-08-03
---

# Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs

Large language model safeguards decide whether to answer before seeing how an answer will be used. This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history. We separate the capability released by the model from the evidence available about downstream use. When that evidence is copyable, we derive the exact worst-case floor on attacker assistance while preserving useful answers. The result yields a safety trilemma: Useful Capability, Reliable Safety, and Open Access cannot coexist. We then show how a trusted credential can complement existing safeguards by adding hard-to-copy information that predicts actual downstream use, and identify the stronger condition needed to eliminate the floor. Evidence from dual-use evaluations, adaptive attacks, and deployed trusted-access programs supports the practical relevance of these conditions.
