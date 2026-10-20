# Insurance Claims Are AI's Messiest Data Problem | Denys Linkov, Wisedocs

**Channel:** AI Engineer
**Published:** 2026-10-18
**Source:** https://www.youtube.com/watch?v=W4pnzOURwHQ

*Workshop, AI Engineer New York. Vendor talk (Wisedocs, complex medical claims processing).*

## TL;DR
Complex medical claims (workers' comp, auto, liability in a ~$1T P&C market) are the worst-case enterprise document problem: 50 different state intake forms, 50%+ duplicate records in some jurisdictions, commingled patients, faxes, conflicting diagnoses, missing x-rays, and single PDFs as large as 8 GB. AI only works once a layered pipeline (OCR, extraction models, VLMs, classifiers, summaries, human verification) has turned that mess into clean, verified data. Wisedocs built the MLCR benchmark with Artificial Analysis: top models went from about 20% to about 75% accuracy within months, but completeness is still unsolved. The real payoff is cross-claim analytics (provider networks, cost inflation, fraud rings), not single-claim Q&A.

## Key Takeaways
- **Digital transformation is unfinished.** Most firms never completed cloud, big-data or data-lake projects before AI arrived. Nobody in the room could pick a new AI vendor within a week.
- **Fax market is still over $7B and growing.** EHR adoption was 8% in 2008 and only reached 80 to 90% after COVID.
- **Loss ratio** (payouts over premiums, around 50% in his figures) is what insurers optimize; AI has to move it, or move claim cycle time.
- **Litigation asymmetry:** plaintiff firms (paid 9 to 15% in California workers' comp, up to 33 to 40% elsewhere) adopted AI faster than insurers because speed and claim size directly drive their fees.
- **Data defects:** duplicates (often intentional follow-up resends), commingled records (Bob Joe vs Bob Joe Jr., a HIPAA risk), copy-paste between visits, every hospital's EMR built differently, poorly scanned handwriting.
- **Within-claim AI wins:** deduplication, missing-record detection (progress note references an x-ray that is not in the package), conflicting-diagnosis flags with page references.
- **MLCR benchmark:** 6 tiers of questions, first 3 tiers open-sourced, harder tiers private on Artificial Analysis. Scored on conciseness, accuracy and completeness against human expert answers with a triple-judge panel. GPT models more accurate but omit details; Anthropic models more complete.
- **Cross-claim insights:** patient travel within network, lawyer/doctor/chiropractor co-occurrence graphs, ICD code co-occurrence, per-provider price inflation (e.g. 10% YoY on physio), counterfactual network steering.
- **Architecture (Q&A):** OCR and image preprocessing, then NLP/entity extraction models, VLMs for structuring, custom classifiers, a summary layer, human verification, then analytics. Information density rises at each layer, verified at each step.
- **Own models for cost:** they train their own classifiers and extractors instead of "token-max reasoning for every problem." Asked about Jev (Typesafe AI's decision model, part of the October 2026 decision-model wave, see [[2026-10-18-AI-Engineer-OpenProse-Stop-Telling-Agents-How]]), he was only surprised it took so long: LLMs are the wrong tool for pure classification.
- **Regulation:** always human-in-the-loop, auditable pipeline, no black box. He estimates this removes about 70% of regulator concerns.

## Architecture & Optimization Mechanics
- **Pyramid of models.** Cheap specialized models handle the high-volume bottom layers (OCR, entity extraction, classification); frontier LLMs only see the concentrated, verified top layer. This is LLM routing applied by pipeline stage rather than by query.
- **Context is not the fix.** An 8 GB, multi-thousand-page claim cannot be stuffed into any window. Hierarchical summarization with verification at each level is the working pattern.
- **Errors compound upstream.** A commingled record or bad OCR at layer 1 poisons every downstream answer, so per-layer calibration matters more than final-answer evals.
- **Completeness is the hard metric.** Accuracy can be high while the model silently omits a surgery or a conflicting note. In claims, omission is the costly failure.

## Grounded Context (Web Enrichment)
MLCR-AA (Medical Long Context Reasoning) is live on Artificial Analysis. Case files are 70 to 150 pages; any answer over the conciseness limit scores zero; three LLM judges decide accuracy and completeness by majority vote. Claude Fable 5.1 (max effort) currently leads at 71.1%, Claude Fable 5 at 64.4%, Claude Opus 5 (high) at 59.4%. The median model scores under 15%, and Kimi K3 leads open weights at 38.3% ([Artificial Analysis](https://artificialanalysis.ai/evaluations/mlcr-aa), [AlphaSignal](https://alphasignal.ai/news/artificial-analysis-mlcr-aa-shows-most-ai-models-fail-medical-reasoning), [Crypto Briefing](https://cryptobriefing.com/wisedocs-mlcr-aa-leaderboard-medical-ai-reasoning/)). Linkov's "about 75%" is slightly higher than the public 71.1% top score, likely a different config or the accuracy-only axis.

His accuracy-versus-completeness split holds up: GPT-6 Astra (max) scores 98.3% on judged accuracy but lower on completeness, while Fable 5.1 leads completeness at 89.0%. The median-below-15% finding is the more important signal: most models, including many cheap ones you would route to, fail long-context medical reasoning outright. The talk offers no hard ROI numbers (he admits they cannot yet claim an industry-wide cycle-time reduction).

## Real-World Application / Actionable Step
- **Routing:** MLCR-AA is a good stress test for a long-context router. Medians under 15% mean "route long, document-heavy queries to a cheap model" is likely to fail badly. Add a document-length and task-type feature that forces escalation above a page threshold.
- **Eval design:** split your router or compressed-model evals into accuracy and completeness. Quantized and pruned models tend to lose recall of minor details first, which an accuracy-only judge will miss.
- **Cost:** copy the pyramid. Use small fine-tuned extractors (or a distilled 1 to 3B model) for layers 1 to 3 and send only summaries to the frontier model. Measure cost per verified field, not per token.
- **Investing angle:** P&C insurers with documented claims-AI programs (lower loss-adjustment expense) are where efficiency gains show up first; check loss-adjustment expense ratios rather than press releases.
