---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.511124+00:00
arxiv_id: 2610.16117
url: https://huggingface.co/papers/2610.16117
arxiv_url: https://arxiv.org/abs/2610.16117
date: 2026-10-14
---

# Beyond Perfect Teammates: Multi-Agent Collaboration with Unreliable Colleagues

LLM-based multi-agent collaboration is increasingly used to solve complex tasks by dividing work among specialized agents and integrating complementary expertise. Yet existing systems and evaluations largely rest on an implicit perfect-colleague assumption: collaborators provide correct and complete information and respond promptly to requests. In realistic teamwork, however, collaborators may return information that does not answer the intended question, provide insufficient detail to support a decision, or fail to respond to a request. To separate task-solving competence from the ability to recover an unreliable evidence-gathering process, we introduce the Unreliable Colleagues Benchmark (UnCoBench), which organizes behavioral failures through Misaligned, Incomplete, and Missed settings. The main agent need to verify contextual correctness, diagnose information gap and track unresolved dependencies in order to obtain the correct evidence for solving the task. We also introduce a verifiable and scalable automated generation pipeline that pairs LLM-based scenario generation with executable checks of answer uniqueness and role necessity. Results across ten models show that similar reliable-setting performance can result in different robustness to unreliable evidence. Trace analysis reveals frequent omissions of corrective follow-up, and the recovery behavior involves inefficient waiting and redundant queries. These findings show that robust collaboration requires not only sound reasoning, but also targeted action to diagnose evidence failures, recover relevant information, and integrate it into decisions. Our data and source code are available at https://github.com/iNLP-Lab/UnCoBench.
