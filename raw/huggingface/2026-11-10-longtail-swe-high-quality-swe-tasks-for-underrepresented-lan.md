---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.323407+00:00
arxiv_id: 2611.10304
url: https://huggingface.co/papers/2611.10304
arxiv_url: https://arxiv.org/abs/2611.10304
date: 2026-11-10
---

# Longtail-SWE: High-Quality SWE Tasks for Underrepresented Languages

Challenging repository-level benchmarks remain limited for many programming language ecosystems, where filtering scarce candidates with ambiguous descriptions or defective tests can discard valuable engineering problems. We introduce Longtail-SWE, a benchmark of 202 issue-resolution tasks across 13 languages with limited coverage in existing repository-level benchmarks: Clojure, Dart, Elixir, Erlang, F#, Haskell, Julia, Kotlin, Lua, OCaml, R, Scala, and Swift. Its construction uses a solver--judge--repairer pipeline: a solver attempts each candidate task, and a judge reviews the task together with the solver's trajectory and test results to guide revisions to tests and task descriptions. These revisions aim to correct tests that reject valid alternative implementations or accept incorrect solutions while retaining challenging tasks and preserving their intended requirements. We evaluate nine model configurations, including frontier models, and analyze task-solving performance, consistency across repeated attempts, and resource usage. We release all benchmark instances, executable environments, complete construction and evaluation tooling, and agent trajectories, together with an additional set of easier tasks to support evaluation of smaller models.
