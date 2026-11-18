---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.115231+00:00
arxiv_id: 2611.20595
url: https://huggingface.co/papers/2611.20595
arxiv_url: https://arxiv.org/abs/2611.20595
date: 2026-11-17
---

# Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures

LLM agents answer questions by calling APIs and trusting the results. An API can fail silently. It ignores part of a request, such as a misnamed filter, yet returns HTTP 200 and a plausible but wrong result. Current fixes, such as checklists, reviewer models and LLM judges, ask the model to catch it. But models often see the problem and answer anyway. We present SilentGuard, which moves the decision from the model to the harness running tool calls. It tests each result against invariants that any correct API must satisfy and withholds values that break one. We find silent failures in 11 of 15 public research APIs, with counts inflated up to 691 times. Current fixes leave over 70% of answers wrong, and agents report 77.4% of counts a judge flags. Across 7 open models, SilentGuard cuts wrong answers on its target faults from 74.0% to 1.7%, with no loss on fault-free tasks. On three frontier models they fall from 70.2% to 0.5%. A warning from the same check leaves 70.1% wrong, so enforcement is the key. On new fault types, the harness alone cuts wrong answers from 61.1% to 24.5%. It avoids wrong answers by abstaining rather than recovering.
