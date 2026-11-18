---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.107154+00:00
arxiv_id: 2611.21072
url: https://huggingface.co/papers/2611.21072
arxiv_url: https://arxiv.org/abs/2611.21072
date: 2026-11-17
---

# Sage S2.1 Flash Technical Report

We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over scientific evidence and act in interactive environments. Sage Sci-Perception uses dedicated encoders for molecular graphs and biological sequences and represents spectra as ordered patches of measurements. Modality-specific projectors map these representations into the input space of a shared backbone, which processes them alongside text and images. To develop the model's agent capabilities, we construct verifiable environments for tool use, search, and coding, as well as specialized workflows involving machine learning experiments and scientific software. Task completion is checked against execution results, changes in environment state, or submitted artifacts. We evaluate Sage S1.5 Flash on 33 benchmarks across seven domains. In the primary comparison against five baselines, it ranks first on OfficeQA Pro (72.2), MLE-bench Lite (90.3 HumanRank), Harvey LAB, and SpreadsheetBench~2, and second on OSWorld-Verified (85.2), WebArena-Verified (67.6), and DeepResearch Bench~II (54.2). These results show particular strengths in using documentary evidence, producing verifiable workbooks, and carrying out machine learning tasks, alongside competitive performance in desktop and browser workflows that require the model to act on visual feedback.
