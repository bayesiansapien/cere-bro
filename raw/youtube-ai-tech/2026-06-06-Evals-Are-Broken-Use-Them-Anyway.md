# Evals Are Broken, Use Them Anyway

**Channel:** AI Engineer  
**Published:** 2026-06-06  
**Source:** https://www.youtube.com/watch?v=QuuIywMG4s8  

## TL;DR
Ara Khan (Cline) delivers a critique of current LLM evaluation methods, arguing that while public benchmarks are often "maxed out" or "vibes-based," they remain essential for "hill-climbing" agent performance. He introduces **Terminal-Bench** (89 real-world tasks) and the **Harbor** orchestration framework as the new standard for measuring long-horizon agentic behavior, moving past simple one-shot evaluations.

## Key Takeaways
- **The Two Camps of Wrong:** People fail by either blindly trusting leaderboard numbers (which are often overfitted) or by relying purely on "taste/vibes" without empirical data.
- **Hill-Climbing Methodology:** Success comes from getting an initial score (e.g., Cline's 43% on Terminal-Bench) and methodically fixing "Zone 1" (infrastructure/mechanical) and "Zone 2" (reasoning/nuance) failures.
- **Terminal-Bench:** A collaboration between Stanford and the Laude Institute focusing on 89 tasks that take 30-40 minutes each, requiring agents to maintain system integrity while solving complex engineering problems.
- **Harbor & Infrastructure:** Evaluations must run in isolated, parallel VMs (using Modal or Daytona) to prevent agents from interfering with the host and to ensure reproducible results.

## Architecture & Optimization Mechanics
- **Harness vs. Model:** High performance is often a result of the **agentic harness** (prompting, tool-calling loops, retries) rather than just the model. A model like Claude 3.5 Sonnet might perform better in one harness than another.
- **Nuance Improvements:** Optimization involves finding model-specific prompt techniques (e.g., Anthropic vs. Gemini) and managing "thinking behavior" to prevent models from getting stuck in repetitive loops ("strokes").
- **Parallel Execution:** Using frameworks like Harbor allows running the entire 89-task suite in parallel, meaning the evaluation time is limited only by the slowest task.

## Grounded Context (Web Enrichment)
**Terminal-Bench 2.0** has recently become the gold standard for "agentic" evaluation, largely replacing older benchmarks like HumanEval which are considered "solved" or "leaked." The **Laude Institute** (often playfully called the Luddite Institute) continues to maintain the Harbor framework, which has been integrated into the CI/CD pipelines of major AI labs.

Recent data from the **SWE-bench** leaderboard shows a similar trend: the gap between "bare" models and "agentic systems" (like Cline or Devin) is widening, proving that the **orchestration layer** is where the most significant optimization gains are currently being made.

## Real-World Application / Actionable Step
- **Apply Hill-Climbing to Routing:** Amit should build a specialized "Routing-Eval" using **Harbor** to test his model compression and routing algorithms. Instead of "vibes," he should measure the exact success rate of routed queries against a deterministic test suite.
- **Action:** Clone the `Terminal-Bench` repository and run a subset of tasks against his current optimization harness to establish a baseline score.
