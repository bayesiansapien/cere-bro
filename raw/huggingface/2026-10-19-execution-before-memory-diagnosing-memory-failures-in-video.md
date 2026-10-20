---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23542
url: https://huggingface.co/papers/2610.23542
arxiv_url: https://arxiv.org/abs/2610.23542
date: 2026-10-19
---

# Execution Before Memory: Diagnosing Memory Failures in Video World Models

A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that separates the change from the memory it should leave behind. The model first sets the scene while the change stays hidden, and only later is asked to show it, with leakage before that point kept under control. This separation locates the bottleneck: the model sets the scene but does not carry out the instructed change. The same gap appears in general memory evaluations. On that basis we propose M3-Agent (Make the Missing Move), which recursively revises the details of the input instruction so that the model successfully carries out the requested instruction. Relative to the baseline, it more than triples the MIST reveal score. On the benchmarks, WRBench's score T rises by 26.1% and MBench-T's score U by 52.7%. The method meets the problem from the execution side: it shows what the frozen model can do once the move is stated, and it sets a stricter baseline.
