---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350408+05:30
arxiv_id: 2609.34736
url: https://huggingface.co/papers/2609.34736
arxiv_url: https://arxiv.org/abs/2609.34736
date: 2026-10-01
---

# SeLMRoute: Probabilistic Semantic Evidence for Large Language Model Routing

Large language model (LLM) routing aims to select the most suitable model for each incoming query. Most existing routers learn this decision directly from query embeddings, model representations, preference data, or clusters of similar examples. Such approaches can be effective, yet the representation used for routing rarely states what a query actually requires. We introduce SeLMRoute, a routing framework that separates the extraction of candidate-independent semantic evidence from the learning of candidate performance and the application of deployment objectives. A decision model first evaluates a set of interpretable questions about the query, such as its reasoning requirements and use of external knowledge, with each judgment retained as a probability distribution. The resulting probabilistic semantic state is used by a lightweight supervised router to estimate candidate model performance. Routing objectives are applied after performance estimation, which allows the same semantic state to support performance-oriented and cost-aware decisions. On the LLMRouterBench (15 datasets, 20 candidate models, 11,481 queries), SeLMRoute achieves an average accuracy of 72.08% pm 0.45, while grouped five-fold out-of-fold evaluation reaches 72.64%, compared with 69.23% for the strongest fixed candidate. The representation achieves the highest mean performance among the evaluated semantic, dense, lexical, and domain-level representations. In a separate 13-model performance-cost setting, SeLMRoute improves performance in all five grouped splits, with a mean PerfGain of 2.66%. Our code is available at https://github.com/Indigma-Innovations/SeLMRoute.
