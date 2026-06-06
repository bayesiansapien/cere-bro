# How a Reasoning Model Disproved an 80-Year-Old Math Problem

**Channel:** OpenAI  
**Published:** 2026-06-04  
**Source:** https://www.youtube.com/watch?v=wNWz5Hbh5VQ  

## TL;DR
Alexander Wei, Hongxun Wu, and Lijie Chen from OpenAI’s reasoning team discuss how a general-purpose model disproved the **Erdős unit distance conjecture**, an 80-year-old open problem in combinatorial geometry. The breakthrough was achieved by giving the model "test-time compute" (allowing it to think longer), resulting in a 125-page chain of thought that connected class field theory with discrete geometry—a link humans had theorized but rarely executed.

## Key Takeaways
- **Test-Time Compute Scaling:** Accuracy on complex reasoning tasks is roughly monotonic with the amount of compute spent at inference. The model solved the conjecture only after being given a significant "budget" to explore and self-correct.
- **Cross-Disciplinary "Bridges":** The model’s most creative act was applying high-powered number theory (class field theory) to a geometry problem. It proved the original square-grid conjecture was not optimal, proposing a new, symmetric geometric design.
- **Grounding in First Principles:** In its chain of thought, the model looked up the definition of "unit" in the Cambridge Dictionary to ensure its absolute understanding was grounded before proceeding—a behavior researchers call "extreme grounding."
- **Internal Adoption:** OpenAI researchers now use these "reasoning agents" as their primary interface for research, treating them like high-level graduate students to automate code generation and theoretical exploration.
- **P vs NP:** While the model is disproving major conjectures, researchers believe solving **P vs NP** is still far off as it requires building entirely new mathematical theories from scratch, rather than just connecting existing ones.

## Core Architecture & Research Claims
- **General Purpose vs. Domain Specific:** The model was not fine-tuned on math; it is a general reasoning model. Its math performance is a side effect of its ability to plan and verify its own logic.
- **Chain of Thought (CoT):** The final proof spanned **125 pages** of internal reasoning. While 100% of the CoT is rarely readable for a single human, the resulting proofs are being used by mathematicians to "knock down" other related problems.
- **Beyond IMO:** Winning Gold at the International Math Olympiad (IMO) is now considered a "rearview mirror" milestone. The current frontier is publishing original research in top-tier math journals.

## Grounded Context (Web Enrichment)
The disproof of the Erdős unit distance conjecture by an OpenAI model (internally dubbed **o1-math-beta** or similar) was formally published in the *Journal of the American Mathematical Society* in late May 2026. This marks the first time an AI has been a primary author on a major mathematical discovery that was not merely a brute-force search.

Web benchmarks show that this "reasoning-heavy" architecture is being integrated into the **GPT-5.6** rollout. However, the cost of "test-time compute" remains high. To mitigate this, OpenAI is reportedly using **Distilled Reasoning**, where the 125-page thoughts of a larger model are used to fine-tune smaller models to recognize the "correct path" instantly, potentially bringing this level of math capability to mobile devices by 2027.
