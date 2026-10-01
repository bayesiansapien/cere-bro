---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.32522
url: https://huggingface.co/papers/2609.32522
arxiv_url: https://arxiv.org/abs/2609.32522
date: 2026-09-30
---

# Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations

Long-term memory enables agents to accumulate information and reason across sessions, yet existing research primarily focuses on dyadic text or image-text conversations, leaving long-term memory for multi-party spoken conversations underexplored. This setting requires preserving conversational content, identifying participants across sessions, and retaining who speaks to whom. To this end, we propose VoxPolyMem, an interaction-aware multimodal memory framework combining incremental speaker identification with a memory hierarchy comprising interaction memory, fact memory, and participant profiles. We formulate retrieval as sequential decision-making, where an agent rewrites queries and selects retrieval tools and memory layers based on accumulated evidence to address information gaps. We further introduce Evidence-Gain GRPO (EG-GRPO), which uses round-wise credit assignment to encourage complementary evidence acquisition. We also construct VoxPolyBench to evaluate memory evolution, personalized answering, memory retrieval and reasoning, and interaction reasoning and attribution in multi-party spoken conversations. VoxPolyMem achieves an overall score of 85.0 on VoxPolyBench, surpassing the strongest evaluated baseline by 23.6 points. On Mem-Gallery and H2HMem-Multi, it scores 89.6 and 74.4, respectively, exceeding the strongest evaluated public memory baselines by over 8 points each. These results highlight its potential for persistent, personalized assistance in multi-party multimodal interactions. Code and datasets are available at https://voxpolymem.github.io/VoxPolyBench/demo/
