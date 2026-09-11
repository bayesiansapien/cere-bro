---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11561
url: https://huggingface.co/papers/2609.11561
arxiv_url: https://arxiv.org/abs/2609.11561
date: 2026-09-11
---

# Memory as Plans: World-Action Modeling with Memory-Grounded Planning

Mainstream robotic policies often adopt a Markovian formulation, but many complex real-world manipulation tasks are inherently non-Markovian, requiring long-horizon memory beyond the current observation. Existing memory mechanisms often rely on language summaries, growing visual windows, or their combinations, and may therefore lose fine-grained visual evidence or face a trade-off between history coverage and execution efficiency. We introduce MaP-WAM, a Memory-as-Plans framework that decomposes memory-dependent world-action modeling into memory-grounded planning and plan-conditioned execution, and uses long-term multimodal episodic context as planning-time evidence rather than repeatedly conditioning the executor on the full history. MaP-WAM represents memory as completed segment records containing language instructions and sparse visual context, and converts this episodic memory into compact plans comprising the next segment-level language plan and corresponding visual guidance. A World-Action-Progress (WAP) model executes each plan over an unknown duration by jointly predicting action chunks and corresponding execution progress at inference time, calibrating predicted progress through plan-observation alignment for adaptive segment transitions and closed-loop context updates. MaP-WAM keeps the executor context length fixed, while structured attention further enables key-value caching in both planning and execution. MaP-WAM achieves state-of-the-art performance on RMBench with an 83.3% success rate and attains 78.0% success on real-robot tasks, while maintaining approximately constant executor inference latency as task history grows.
