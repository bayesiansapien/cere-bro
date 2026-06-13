# Stop Making Models Bigger, Make Them Behave — Kobie Crawdord, Snorkel

**Channel:** AI Engineer  
**Published:** June 10, 2026  
**Source:** https://www.youtube.com/watch?v=TNwJ1LMiENk  

## TL;DR
Kobie Crawford from **Snorkel AI** demonstrates how a **4-billion-parameter model** can outperform a **235-billion-parameter reasoning model** on financial tool-use tasks (FinQA). The secret is not more parameters, but **Reinforcement Learning (RL)** focused on "Tool Discipline"—achieved for under $500 in 21 hours using the **GRPO** algorithm.

## Key Takeaways
- **The "Terence Tao" Effect:** Massive models (like the 235B reasoning model) are often "too smart" but lack discipline. They may know complex math but fail to check which SQL tables actually exist, leading to hallucinations.
- **Behavior > Knowledge:** For tool-use, the bottleneck is often **behavioral discipline** (checking schemas, handling errors) rather than raw reasoning depth.
- **The $500 RL Win:** Using **GRPO** (Group Relative Policy Optimization) on a 4B model for 21 hours yielded a 2x performance jump, outperforming models nearly 60x its size.
- **Single-Table vs. Multi-Table:** Surprisingly, training on **single-table** tasks generalized better to hard multi-table questions than curriculum learning or mixed training. Fixing the core "Tool Use" failure mode (checking tables/schemas) was the primary driver of success.

## Architecture & Optimization Mechanics
This is a masterclass in **Inference Optimization** and **Model Behavioral Alignment**.
- **GRPO Algorithm:** Snorkel used GRPO, which optimizes behavior without the massive compute overhead of traditional PPO, by comparing relative performance within a group of model outputs.
- **FinQA Environment:** A fully self-contained, container-agnostic environment was used to ensure the model had a "verifiable playground" for tool use.
- **Tool Discipline Workflow:** The optimized 4B model learned a strict protocol: 1. `get_table_names` -> 2. `get_table_info` (schema) -> 3. Execute Query -> 4. Self-Correct on error. The larger model skipped to step 3 and hallucinated on failure.

## Grounded Context (Web Enrichment)
In 2026, the **"Small Model Revolution"** is peaking. While frontier models like **Mythos 5** push the ceiling of AGI, Snorkel's research proves that for enterprise tasks (Finance, Legal, Health), **Surgical RL** is more cost-effective than scaling. The "FinQA Reasoning" benchmark has become the standard for assessing **Agentic Tool Use**. Snorkel’s use of "experts-in-the-loop" to generate high-quality RL feedback data remains their core differentiator against labs relying solely on synthetic data.

## Real-World Application / Actionable Step
**Amit’s Optimization Strategy:**
- **Routing Logic:** Amit should stop routing "Hard" financial or tool-use queries to the 200B+ models by default. Instead, use a **Task-Specific 4B RL-tuned model**. This is a 60x reduction in inference cost with *higher* accuracy.
- **Error-Correction Loops:** When building routing engines, implement the "Tool Discipline" protocol (Discovery -> Inspection -> Execution -> Correction) as a prompted or fine-tuned behavior.
- **Action:** Visit the **OpenEnv** GitHub repo to download the FinQA environment and run a local test of a 4B model versus a larger one on his own financial data.
