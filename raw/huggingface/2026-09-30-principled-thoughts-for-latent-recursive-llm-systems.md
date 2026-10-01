---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36159
url: https://huggingface.co/papers/2609.36159
arxiv_url: https://arxiv.org/abs/2609.36159
date: 2026-09-30
---

# Principled Thoughts for Latent Recursive LLM Systems

Large language models can reason in continuous space instead of decoded text, by recurring on their own hidden states or by passing those states between agents, while training supervises only the Cross-Entropy (CE) of the final decoded answer and does not constrain the thought. Theoretical and empirical analyses establish and confirm four failures of CE-only training that lead to a lower probability of the correct answer such as collapsing thoughts across distinct questions and retaining irrelevant information. We introduce REST (REpresentation-Supervised Thoughts), a training objective that turns four properties of a valid thought representation (causality, minimality, separability, and stability) into differentiable losses added to CE. We instantiate it in latent single-agent and multi-agent systems, without architectural changes or added parameters at inference. Across 7 benchmarks spanning mathematics, science, medicine, and code generation, with the same training data, compute, and latent budget, REST increases accuracy over CE-only training across agent settings and model sizes by up to 7.5 percentage points and convergence on a final answer by 30\%. Furthermore, REST thoughts encode more of what is required to achieve the correct answer, and decoding them better recovers the intended output of the agent, which makes latent communication easier to interpret. Project Website: https://fard-lab.github.io/REST
