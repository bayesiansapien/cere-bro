---
source: farmer/huggingface
farmed: 2026-05-05T00:00:00
arxiv_id: 2605.02240
url: https://huggingface.co/papers/2605.02240
arxiv_url: https://arxiv.org/abs/2605.02240
date: 2026-05-05
---

# PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments

We introduce PhysicianBench, a benchmark for evaluating LLM agents on physician tasks grounded in real clinical setting within electronic health record (EHR) environments. The benchmark addresses gaps in existing medical agent evaluation by focusing on complex, multi-step clinical workflows rather than simple knowledge recall.

The benchmark comprises 100 long-horizon tasks derived from actual consultation cases, each independently reviewed by physician panels. Tasks are executed within a real EHR environment using standard vendor APIs and span 21 medical specialties with diverse workflow types. Each task requires approximately 27 tool calls and involves data retrieval across patient encounters, clinical reasoning, action execution, and documentation.

Results demonstrate substantial challenges ahead: the best-performing model achieves only 46% success rate (pass@1), while open-source models reach at most 19%. This reveals a meaningful capability gap between current LLM agents and the demands of autonomous clinical work.
