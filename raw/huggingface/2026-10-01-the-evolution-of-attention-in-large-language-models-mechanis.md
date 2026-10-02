---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350241+05:30
arxiv_id: 2609.39661
url: https://huggingface.co/papers/2609.39661
arxiv_url: https://arxiv.org/abs/2609.39661
date: 2026-10-01
---

# The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends

Self-attention gives LLMs fine-grained, query-dependent access to context, but dense token interactions incur quadratic prefill cost and a key--value cache growing with context length. Research thus spans explicit-memory compression, sparse access, recurrent state construction, structured state dynamics, and heterogeneous mechanism composition. This survey analyzes these developments as model-internal contextual memory. We introduce a five-dimensional lens---Memory Representation, Memory Update, Access, Readout, and Integration---describing what is represented, how it changes, what is query-eligible, how it is read, and how readouts form outputs. This lens compares overlapping research lines without imposing one computational model.
  We reconstruct mechanism-level developments and architectural adoption using 59 release-level records from 14 major model lineages and 11 high-performing open-weight endpoints. First, explicit-memory and recurrent-state methods retain distinct interfaces but increasingly control overlapping memory functions. Second, heterogeneous architectures increasingly coordinate across network depth: layer-wise composition distributes complementary memory processing across representational stages, while cross-layer reuse carries selected memory and routing artifacts forward. Depth thus becomes a dimension along which contextual memory is constructed and managed. Third, these developments motivate a stateful multidimensional memory-routing hypothesis: persistent memory is organized across temporal scope, network depth, substrate type, and representation granularity, while coordinated Sparse Write and Sparse Read determine what is maintained and what contributes to each query. Overall, efficient sequence architecture design increasingly concerns the organization, lifecycle, and selective use of contextual memory rather than an isolated Attention operator.
