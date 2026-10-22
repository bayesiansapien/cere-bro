---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.22636
url: https://huggingface.co/papers/2610.22636
arxiv_url: https://arxiv.org/abs/2610.22636
date: 2026-10-20
---

# Measuring Mechanistic Uncertainty in Large Language Models via Causal Robustness

Large language models (LLMs) are increasingly used in critical domains, where their susceptibility to hallucinations makes reliable and interpretable uncertainty quantification essential. We introduce the concept of mechanistic uncertainty, which characterizes uncertainty through the stability of the internal mechanisms supporting a model's response. We propose the causal robustness margin, defined as the minimum internal intervention required to deviate the model's output, and operationalize it using Jacobian Lens (Jlens) concept steering vectors. Across three open-source models and five question-answering datasets, we show incorrect and uncertain responses exhibit smaller margins, indicating greater sensitivity to internal interventions, and the causal robustness margin complements conventional output-based uncertainty methods. Finally, in a controlled knowledge injection experiment, correctly learned facts show increased margins after training, suggesting that causal robustness provides a mechanistically grounded signal of uncertainty.
