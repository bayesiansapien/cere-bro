---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32973
url: https://huggingface.co/papers/2611.32973
arxiv_url: https://arxiv.org/abs/2611.32973
date: 2026-11-25
---

# SpecEngineeringBench: Evaluating Coding Agents as Autonomous Specification Engineers

Autonomous specification engineering requires coding agents to translate functional requirements into executable tests and use the results to discover and validate defects. However, existing benchmarks evaluate coding agents on explicitly specified test generation tasks, commonly providing an issue description, a designated test entry point, or files to inspect, leaving the ability to determine what to test and where to investigate insufficiently evaluated. Relying on such clues bypasses the challenge of mapping requirements to implementations and proactively uncovering unknown defects. We propose SpecEngineeringBench, comprising 100 instances from 78 open-source Python repositories across 16 application categories, with multiple recorded defects in each instance. Two independent tasks evaluate complementary capabilities: generating test suites and discovering defects through execution analysis. The evaluation combines test validity, defect detection, and coverage with localization precision and recall. Across seven frontier coding agents, results reveal that test validity and coverage decouple from defect exposure: agents achieve a 91.47% Head Pass Rate and 80.48% Change-focused Coverage alongside a 26.36% Fail-to-Pass Rate, while localization recall drops from 78.11% at the file level to 51.29% at the function level. Autonomous test generation improves file, function, and hunk localization recall by 4.99, 2.77, and 2.69 percentage points over relying solely on existing repository test suites.
