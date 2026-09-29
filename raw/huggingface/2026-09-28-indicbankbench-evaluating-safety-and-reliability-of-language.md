---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.597944+00:00
arxiv_id: 2609.29167
url: https://huggingface.co/papers/2609.29167
arxiv_url: https://arxiv.org/abs/2609.29167
date: 2026-09-28
---

# IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants in Indian Retail Banking

Banking assistants must use account-specific information to answer requests and, in many cases, take actions through tools. Evaluating only the final response misses important errors. An assistant may ask for information it already has, rely on stale context, select the wrong account, or write an invalid value after stating the correct one. We introduce IndicBankBench, a 799-case benchmark for Indian retail banking spanning five operational domains, a capability/refusal domain, and twenty primary axes. Cases are evaluated at four stages: safety, action and tool use, response adequacy, and advisory quality. Tool use and most safety checks are deterministic. A narrow resolver handles only ambiguous confirmation-before-write cases, while a separate LLM judge evaluates semantic response adequacy. We run every case three times and report strict pass^3, which requires success on all trials. Across the eleven evaluated models, strict reliability ranges from 43.7% to 58.2%, whereas at-least-once success ranges from 60% to 74%. This gap shows that at-least-once success can overstate dependable banking behavior. The case-level diagnostics also distinguish systems that ask unnecessary questions from those that act but fail to reconcile customer context or fully resolve the request. We release the cases, mock environment, and evaluation harness.
