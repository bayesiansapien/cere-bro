---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.533557+00:00
arxiv_id: 2611.00359
url: https://huggingface.co/papers/2611.00359
arxiv_url: https://arxiv.org/abs/2611.00359
date: 2026-11-13
---

# Humanized but Still True? Auditing Facts and Detection in AI-Text Humanizers

AI "humanizers" rewrite machine-generated text so that detectors classify it as human-written. Public leaderboards score evasion and embedding similarity, but not whether checkable details survive. We check whether numbers, dates, person and organization names, and quoted spans survive each rewrite, using a rule-based checker validated by two AI annotators (precision 0.84-1.00, recall 0.93-0.95; no human annotation). In the October 2026 cycle of a public humanizer leaderboard, all 11 commercial tools changed or dropped at least one of these units in 35-65% of the documents that contained one. Most changes were to quoted spans; counting numbers and names alone, 10 of the 11 tools still altered at least one in 20% or more of the documents. The September 2026 cycle was similar (19-50%). An open 12B humanizer kept at least 97% of numbers and names in fact-dense U.S. federal agency text, but reworded 67-78% of the quoted spans, against its own prompt. Unit retention and detector evasion were not clearly related across tools (Spearman rho = -0.46, 95% CI -0.65 to 0.08), and the open model's four released files (two of them quantization-aware low-bit files) did not show the pre-registered monotone trade-off. On federal texts with matched human, AI-styled and humanized versions, a general-purpose decision model, Jev, asked a single zero-shot question, separated human originals from humanized rewrites with AUROC 0.864 (0.827-0.902), 0.18-0.22 higher than Binoculars, Fast-DetectGPT and the adversarially trained RADAR, while calling 24% of the human originals AI at a 0.5 threshold. On the AI-styled rewrites by 2026 models, both perplexity-based detectors scored below chance (AUROC 0.37 and 0.39), also with line breaks removed. Hypotheses, data rules and analyses were frozen before the main runs; two earlier data contacts are disclosed. We release the checker and the per-item results.
