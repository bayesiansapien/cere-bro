---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.932264+00:00
arxiv_id: 2611.28194
url: https://huggingface.co/papers/2611.28194
arxiv_url: https://arxiv.org/abs/2611.28194
date: 2026-11-24
---

# HEP-Ex-Bench: Evaluating Agentic Performance in High Energy Physics Experiment Data Analyses with Sealed Worlds

Agentic systems are increasingly being explored for automating experimental high-energy physics measurements, but the correctness of their results can today be reliably evaluated only via extensive expert review. To address this, we propose a method to perform detailed quantitative evaluations of agent-driven analyses through the use of blind analysis and injection tests, which are critical in a typical expert review. Agents develop a data analysis pipeline on a public dataset, while the evaluation is performed on programmatically generated sealed private datasets where signals are injected and simulation settings varied within realistic detector uncertainties. By requiring agents to provide a single workflow that is evaluated across these "sealed worlds", we are able to test the accuracy and robustness of the workflows. We demonstrate the approach on four tasks built from CMS open data and present it as a way to reliably benchmark scientific work in experimental high-energy physics. At the time of writing, the best-performing model, Gemini 4 Argon, reaches 60% of the score of the expert reference analyses on average, ahead of GPT 6 Astra at 38% and Claude Opus 5.5 at 31%. In individual sessions on one of the tasks, Gemini 4 Argon exceeds the reference. The benchmark is hosted at https://hep-ex-bench.github.io
