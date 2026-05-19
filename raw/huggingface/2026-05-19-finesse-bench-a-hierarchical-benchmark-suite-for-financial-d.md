---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.15482
url: https://huggingface.co/papers/2605.15482
arxiv_url: https://arxiv.org/abs/2605.15482
date: 2026-05-19
---

# FINESSE-Bench: A Hierarchical Benchmark Suite for Financial Domain Knowledge and Technical Analysis in Large Language Models

Large language models (LLMs) are increasingly being applied to financial analysis, reporting, investment decision support, risk management, compliance, and professional training. However, robust evaluation of their domain competence in finance remains incomplete. Widely used open benchmarks such as FinQA, ConvFinQA, and TAT-QA have played an important role in advancing financial question answering and numerical reasoning, but they focus primarily on question answering over financial reports and do not provide an explicit hierarchy of professional difficulty. Broader resources, including FinanceBench, PIXIU, FinBen, and FLaME, expand the coverage of financial tasks, yet the problem of evaluating the transition from foundational knowledge to expert-level financial reasoning remains open. In this work, we present FINESSE-Bench, a suite of eight specialized benchmarks comprising 3,993 questions for hierarchical evaluation of financial competencies in LLMs. FINESSE-Bench combines exam-oriented datasets inspired by professional certifications (CFA-like Levels 1-3, CMT-like Level 2, and CFTe-like Level 1), applied trading task collections, and a Russian-language olympiad benchmark. This design enables evaluation of domain breadth, performance degradation as difficulty increases, the ability to solve computational tasks, and model behavior in specialized financial domains. We also describe a unified evaluation protocol covering multiple-choice questions, numerical answers, and short open-ended responses, together with an automated scoring scheme for freeform answers based on the LLM-as-judge paradigm. FINESSE-Bench is intended both as a complement to existing open financial benchmarks and as a tool for more substantive evaluation of professionally relevant financial competencies in large language models.
