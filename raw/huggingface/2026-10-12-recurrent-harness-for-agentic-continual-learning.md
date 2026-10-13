---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.220194+05:30
arxiv_id: 2610.12668
url: https://huggingface.co/papers/2610.12668
arxiv_url: https://arxiv.org/abs/2610.12668
date: 2026-10-12
---

# Recurrent Harness for Agentic Continual Learning

Language model agents increasingly operate over long interaction streams, requiring online adaptation to distribution shifts through continual learning. However, existing agent harnesses typically either evolve their states only through forward information flow or rely on additional replay or validation data for harness optimization. To address this, we propose ReHarness, a recurrent harness framework for agentic continual learning that complements forward read and write with backward revision under a strictly online streaming protocol. We ask what information could have been captured differently in the harness state to better inform the current instance in the stream. Specifically, after each instance, we leverage the resulting trajectory as feedback to revise the reflections retrieved for that instance, thereby propagating feedback backward through the textual harness state. Across three continual learning benchmarks and three language model backbones, ReHarness consistently outperforms strong raw-context baselines, memory- and reflection-based methods, and prompt optimization approaches. Further analysis shows that ReHarness produces source-grounded and meaningful revisions, corrects overgeneralized or outdated experience under distribution shifts, and improves both stability and plasticity during continual learning.
