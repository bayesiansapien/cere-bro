---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07348
url: https://huggingface.co/papers/2610.07348
arxiv_url: https://arxiv.org/abs/2610.07348
date: 2026-10-07
---

# Stepped MoE: Segment-Level Routing with Configurable Inference Complexity

Training large language models (LLMs) is resource-intensive, and adapting them for diverse deployment scenarios with varying computational constraints remains challenging. While elastic architectures enable flexible model deployment and sparsely activated models allow input-adaptive computation, existing approaches treat these dimensions independently. Moreover, models catered towards on-device edge inference need to conform to the memory and compute limitations of the serving devices. In this paper, we introduce a unified framework that combines elastic structures with sparsely gated architectures to create models that adapt simultaneously to both deployment constraints and task requirements. Our approach employs a model backbone that conditions on both the context and target efficiency specifications, enabling fine-grained control over the accuracy-efficiency trade-off at inference time. The model learns to activate task-relevant parameters within elastically-nested sub-networks, allowing a single model to span multiple capacity points while maintaining input-adaptive routing. Through experiments we demonstrate that we can create a model that allows the flexibility to use 1,2,3,4 billion parameters while being more accurate than their dense counter-parts (2-5\% on knowledge-intensive benchmarks) and at par with their static versions while delivering similar latency metrics as dense models. Overall, we save on device disk space by sharing the model parameters, allow flexibility of serving based on DRAM and compute available while delivering more accurate results.
