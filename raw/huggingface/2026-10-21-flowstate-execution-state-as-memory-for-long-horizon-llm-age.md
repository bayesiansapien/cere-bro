---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.642743
arxiv_id: 2609.34565
url: https://huggingface.co/papers/2609.34565
arxiv_url: https://arxiv.org/abs/2609.34565
date: 2026-10-21
---

# FlowState: Execution State as Memory for Long-Horizon LLM Agents

Long-horizon tasks require LLM agents to continually draw on information from earlier interactions. However, retaining the full history increases context costs, while compressing it risks losing details needed later, and the relevance of historical information often becomes apparent as the task progresses. To address these challenges, we propose FlowState, which treats execution state as memory that can be retained and revisited across requests, unifying current decision-making with the reuse of historical information. FlowState preserves semantically typed state nodes, their relations, and references to raw tool observations, separating persistent retention from on-demand access. Within a single execution loop, Incremental State Update (ISU) maintains the current state based on new inputs and feedback, while Progressive State Access (PSA) progressively reveals historical states and supporting evidence as needed during reasoning. Together, these mechanisms enable agents to reassess prior decisions in light of new information and guide subsequent actions. Compared with a full-context baseline using the same DeepSeek-V4-Flash model, FlowState improves the average success rate on MemoryArena and the average pass rate on τ^3-Bench by 4.55 and 13.95 percentage points, respectively, while reducing total token consumption by 43.2% and 40.6%. These results demonstrate the performance and efficiency advantages of FlowState on long-horizon tasks.
