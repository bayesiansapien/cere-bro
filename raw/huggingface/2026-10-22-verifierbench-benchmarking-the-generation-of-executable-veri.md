---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.195055+00:00
arxiv_id: 2610.28679
url: https://huggingface.co/papers/2610.28679
arxiv_url: https://arxiv.org/abs/2610.28679
date: 2026-10-22
---

# VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents

Agents need reliable ways to validate their outputs, both when completing tasks and when filtering synthetic training data. We study verifier generation: from the instruction and environment available for solving a task, an agent writes an executable verifier that must accept every valid solution and reject invalid ones. We introduce VerifierBench, a benchmark of 222 tasks from six agent benchmarks spanning tool-call, state-based, and code verification, with 4,993 hidden test cases that include alternative valid solutions and attacks; Verifier4Verifier (V4V), a six-check audit, screens its source verifiers and test suites. Across 19 models in a common agent harness, normalized balanced accuracy ranges from 10.6 to 62.1, with generated verifiers consistently rejecting invalid solutions more reliably than they accept valid ones. This apparent strength can mask overly restrictive verification: most false rejections in the analyzed records come from verifiers that accept no tested solution to a task. Case studies reveal unsupported assumptions about solution formats, tool use, and code changes that exclude valid solutions. These errors survive self-testing because agents test solutions that share the verifier's mistaken assumptions, or submit verifiers without confirming that any correct solution passes. These findings suggest testing both whether a verifier accepts a correct solution and whether it accepts other solutions permitted by the task. The project page and dataset are publicly available.
