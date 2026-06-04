# Task Fidelity Scaling Laws — Kobie Crawford, Snorkel

**Channel:** AI Engineer  
**Published:** 2026-06-02  
**Source:** [https://www.youtube.com/watch?v=YYH0DMQr30A](https://www.youtube.com/watch?v=YYH0DMQr30A)  

## TL;DR
Kobie Crawford argues that for agentic Reinforcement Learning (RL) tasks, **task fidelity (quality)** is a more significant performance driver than model size or compute scale. By filtering training tasks through a rigorous "four gates" acceptance framework, Snorkel achieved a **5x performance uplift** (6% improvement vs. 1%) compared to training on unfiltered data. This research shifts the focus from "scaling models" to "scaling data quality," proving that cleaner training signals lead to superior tool discipline and reasoning in autonomous agents.

## Key Takeaways
- **Data Quality > Model Scale:** In agentic contexts, increasing the fidelity of training tasks is more effective than simply increasing the number of parameters or compute budget.
- **The "Four Gates" of Task Fidelity:** High-quality tasks must be:
    1. **Achievable:** Solvable within the environment.
    2. **Non-trivial:** Require multi-step reasoning.
    3. **Functionally Correct:** Logic and success criteria must match.
    4. **Reliable Environment:** Containerized and stable to ensure failures are due to model logic, not infra bugs.
- **Clean Failure Signals:** High-fidelity tasks produce failures that models can actually learn from (e.g., logic errors), whereas low-fidelity tasks produce "noisy" failures (e.g., environment crashes) that degrade RL reward signals.
- **Expert-in-the-Loop:** Human expertise is critical for defining rubrics and generating ground truth data that can then be used to train LLM judges at scale.

## Core Architecture & Research Claims
The central claim is that **"accepted" (high-fidelity) tasks** correlate with better model behaviors, such as 2x more tool calls and higher reasoning density. In a controlled RL training experiment, the high-fidelity group provided a 6% uplift over the base model, while the low-fidelity group provided only 1%, despite using identical compute and sample counts. This suggests that "task fidelity" is a primary scaling law for agentic intelligence.

## Grounded Context (Web Enrichment)
Web enrichment confirms that Snorkel AI has formalized this research into a "frontier AI data lab" methodology. The "Task Fidelity Scaling Laws" framework was notably featured at the AI Engineer conference, where Crawford demonstrated that a 4B parameter model fine-tuned on high-fidelity tasks could exhibit better tool discipline than a 235B parameter frontier model. 

Further updates indicate that Snorkel has released the **Snorkel Agentic Coding Benchmark**, consisting of 100 multi-step coding tasks across varying difficulty tiers. This benchmark is designed to validate long-horizon planning and error recovery, providing a standardized way to measure the impact of task quality on agentic performance. The company continues to advocate for "fixing tasks before scaling models" as the most efficient path to reliable AI agents.
