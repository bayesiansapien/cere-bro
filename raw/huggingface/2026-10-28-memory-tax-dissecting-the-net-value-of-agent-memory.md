---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993530+05:30
arxiv_id: 2610.34073
url: https://huggingface.co/papers/2610.34073
arxiv_url: https://arxiv.org/abs/2610.34073
date: 2026-10-28
---

# Memory Tax: Dissecting the Net Value of Agent Memory

Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underperform naive RAG in many cases, indicating a negative net value. Taking RAG as a reference, we dissect the net value of memory into the gains and losses over direct retrieval, termed memory benefit and memory tax. These gains and losses arise because memory process changes how the raw information is organized and accessed. We view such changes as the double-edged deviations from the raw history. They are originally designed and introduced to benefit the task, for example by reorganizing facts or distilling preferences, but some may also remove or obscure evidence, giving rise to memory tax. Since memory benefit reflects the expected gains of its design, we then focus more on the overlooked memory tax, study how it arises from the system and evaluation side, and generalize the concept to more application scenarios of memory. We hope the notion of memory tax can provide a new lens and shift more attention from standalone performance to the net value of memory, informing more reliable memory designs and evaluations. We will open-source the code and results to the community. Project Page: https://hexuan21.github.io/MemoryTax/
