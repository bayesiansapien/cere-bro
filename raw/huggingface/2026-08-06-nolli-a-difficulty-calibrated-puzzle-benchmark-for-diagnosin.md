---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04397
url: https://huggingface.co/papers/2608.04397
arxiv_url: https://arxiv.org/abs/2608.04397
date: 2026-08-06
---

# NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the English-Korean Performance Gap

We introduce NOLLI, a procedurally generated English-Korean puzzle benchmark designed to diagnose where Korean performance gaps arise. It comprises 15 puzzle types (25 tasks; 7,500 items), with every instance seed-regenerable, verified to have a unique solution, and scored deterministically. Rather than equating harder with bigger, we calibrate difficulty behaviorally, tuning each generator until a fixed reference model lands in target accuracy bands. Its three-level design combines matched direct translations, script adaptations over Hangul jamo (sub-syllabic letters), and Korean-only tasks grounded in Korean culture or orthography. We evaluate 15 frontier, open-weight, and Korean-developed models; among the 12 above a 3% overall-accuracy floor, matched English-Korean accuracy is statistically equivalent within a +/- 10 pp margin (TOST), suggesting little cost from presentation language alone. Writing-system-intensive tasks show sharper gaps: Korean Cipher falls behind English by up to 68.7 pp, whereas Cryptarithmetic over the same jamo shows no systematic penalty, and Jamo Composition accuracy predicts Korean Cipher accuracy. These contrasts are diagnostic rather than causal, consistent with difficulty in multi-step sub-syllabic execution. Korean-only tasks separate rule-application deficits, which vary in sign, from a Kinship deficit positive in all 12. Finally, a salient size measure fails to grow from Easy to Hard in 7 of 15 types, making structural size an unreliable proxy for empirical difficulty.
