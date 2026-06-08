# Codex Helps Amgen Focus on Patients

**Channel:** OpenAI  
**Published:** 2026-06-04  
**Source:** https://www.youtube.com/watch?v=uU3LUMcNgfA  

## TL;DR
Amgen leverages OpenAI Codex to abstract away the "boring bits" of coding, allowing biostatisticians and geneticists to focus on high-impact scientific discovery and patient outcomes rather than manual analysis scripts.

## Key Takeaways
- **Impact over Volume:** The goal at Amgen is not to write more code, but to do better science; Codex facilitates this by handling tedious data analysis structures.
- **Series of Small Bets:** Amgen’s AI strategy is a series of small deployments across the company that compound into a large-scale impact.
- **Natural Language Analysis:** Scientists can now write a prompt and have Codex figure out the structure of the analysis and provide articulated business context.

## Architecture & Optimization Mechanics
For the Senior AI Researcher, this case study highlights the **GPT-Rosalind integration**. Released in April 2026, GPT-Rosalind is OpenAI's first domain-specific model for life sciences. Amgen uses this model within the Codex "operating layer" to handle specialized bioinformatics tasks. The optimization here is in the **mixture-of-experts (MoE)** architecture of GPT-Rosalind, which allows for extremely efficient retrieval across human genetics and biochemistry datasets.

## Grounded Context (Web Enrichment)
Web enrichment shows that Amgen is currently participating in an **FDA pilot program (announced April 2026)** to report clinical trial data in real-time. This is enabled by Codex’s ability to monitor safety signals continuously in trials like the **Phase 1b STREAM-SCLC** for the drug Imdelltra (tarlatamab). 

Furthermore, Amgen’s **Center for Design and Analysis (CfDA)** is utilizing "digital twins"—patient-level predictive models—that are optimized for inference speed using vLLM to run thousands of simulations per hour.

## Real-World Application / Actionable Step
- **MoE Research:** Study the GPT-Rosalind MoE gating mechanism. If a biostochastic prompt is detected, how does the model route to the "Genomics Expert" vs. the "Coding Expert" sub-models?
- **Protocol:** Amit should investigate if "domain-specific pruning" (e.g., pruning non-biological pathways in a general model) can replicate GPT-Rosalind's performance for his own biotech clients.
