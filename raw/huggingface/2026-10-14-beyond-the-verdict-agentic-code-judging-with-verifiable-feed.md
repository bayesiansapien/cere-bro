---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.510559+00:00
arxiv_id: 2610.18760
url: https://huggingface.co/papers/2610.18760
arxiv_url: https://arxiv.org/abs/2610.18760
date: 2026-10-14
---

# Beyond the Verdict: Agentic Code Judging with Verifiable Feedback

Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In competitive programming, however, official judging systems provide authoritative verdicts under finite submission budgets, without revealing failure explanations or failing inputs. To provide informative feedback without consuming official submissions, we formulate a task in which a model judges and diagnoses a candidate program using only the problem statement and source code, with generated counterexamples serving as checkable evidence. To evaluate this task, we build USACO-JUDGE from the USACO 2026 contests, using accepted and unaccepted programs written by human experts and multiple LLMs. We then train ARBITER, a 35B mixture-of-experts (MoE) agentic verifier, with reinforcement learning in a generic execution sandbox. Training raises counterexample success on incorrect programs from 40.61% to 62.67% and mean binary verdict accuracy on USACO-JUDGE from 71.41% to 87.41%, approaching frontier verification performance. Beyond verification, ARBITER outperforms baselines in both code selection and refinement. In an IOI 2026 case study, ARBITER-guided refinement raises GPT-OSS-120B's expected score above the gold-medal threshold under the official submission limit.
