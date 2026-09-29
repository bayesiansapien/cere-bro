---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.598145+00:00
arxiv_id: 2609.30670
url: https://huggingface.co/papers/2609.30670
arxiv_url: https://arxiv.org/abs/2609.30670
date: 2026-09-28
---

# TRACE: Temporal Audit and Condition-aware Evaluation of Streaming Video Understanding

Streaming video understanding requires models to interpret evidence as it arrives, yet current evaluations often report task scores without specifying when evidence becomes valid, how visual history is maintained, or how responses are triggered. As a result, similar scores may correspond to different workloads, failure modes, and operational behavior. We introduce TRACE (Temporal Audit and Condition-aware Evaluation), a condition-aware benchmark and evaluation framework that makes these factors explicit. TRACE combines temporally audited visual tasks with evidence timing and instruction-dependent trigger annotations, a unified causal Core--Adapter protocol that controls information availability while recording actual history processing and response events, and multidimensional reporting of answer quality, timeliness, response-selection behavior, workload, completion, and reliability. On 1,240 records from 517 videos, we evaluate eight publicly available models or systems in eight configurations. We find that nearly identical QA accuracy can mask substantial differences in completion, answer validity, and generation workload, while proactive performance separates into response quality, response delay, false alarms (responses emitted while no target window is currently valid and a later one remains), and missed target windows. These results show that streaming-video performance should be interpreted as execution-conditioned system behavior rather than a single score. Our benchmark and code can be accessed at https://github.com/om-ai-lab/trace-bench{https://github.com/om-ai-lab/trace-bench}.
