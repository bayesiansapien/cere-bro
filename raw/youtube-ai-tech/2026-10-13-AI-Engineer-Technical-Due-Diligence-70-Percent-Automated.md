# What Technical Due Diligence Finds When the Deck Says "70% Automated" (Soukaïna Abelhad)

**Channel:** AI Engineer
**Published:** 2026-10-13
**Source:** https://www.youtube.com/watch?v=gDRCpTMCqEU

## TL;DR
Most inflated AI automation numbers are not fabricated. They are real measurements stretched into conclusions they cannot support. Abelhad, an AI evaluation lead who has worked on both the investor and builder side, gives a three-check filter for any "X% automated" claim: (1) arithmetic, does human labor actually fall as workload grows; (2) definition, is "automated" AI-drafted, human-edited, human-approved, or truly straight-through; (3) evaluation, who defines quality and does an expert agree with the automated grader. Only claims that survive all three get translated into unit economics, with "cost per accepted autonomous task" as the target metric. Short, sharp, and correct. One attribution slip: the grader-vs-maintainer study she credits to Meta is from METR.

## Key Takeaways
- **Headline numbers carry their scope.** The famous "55.8% faster" Copilot result came from 95 developers building one JavaScript HTTP server from a template against 12 visible tests. Valid experiment, narrow task.
- **Check 1, arithmetic.** Faros telemetry (10,000+ devs, 1,255 teams): high-AI-adoption teams merged 98% more PRs, but review time rose 91% and PRs got 154% larger. More work entered the system and the human review load grew with it. Ask for an 18-month series of workload volume vs fully loaded human labor (operators, reviewers, labelers, escalation, rework). If labor tracks volume, it is assistance, not labor removal.
- **Check 2, definition.** Automation ladder: AI-drafted, human-edited, human-approved, no human intervention. Only the last one is "straight-through processing" (a finance term), and it needs a named boundary: drafted, approved, or in production? "AI-attributed" and "autonomous" are different claims. Uber's "70% of PRs AI-attributed" says nothing about autonomy, and period and denominator were undisclosed.
- **Check 3, evaluation.** Blind maintainer review of 296 AI-generated SWE-bench patches found merge rates ~24 points below what the automated grader implied. Her own experience: 10 of 10 outputs passed automated validation, few survived expert review. Ask who labeled ground truth, whether experts agree, whether agreement is measured, what the judge was validated against, and what bad output escaped.
- **Builder.ai as the cautionary tale.** WSJ questioned its AI claims in 2019. In May 2025 the FT reported 2024 revenue revised from ~$220M to ~$55M; it went into US bankruptcy in early June 2025. The warning existed for six years; no process turned it into a gate. She is careful to say the collapse was revenue and financing, not AI positioning alone.
- **Economics last.** Eligible workflow value x adoption x straight-through success x accepted quality, minus AI cost, human review, escalation and rework. Failures, escalations and rework all count against cost per accepted autonomous task.
- **Closing rule:** diligence is not asking whether the number is impressive, it is asking what must be true for the number to matter.

## Architecture & Optimization Mechanics
- **Automated graders are optimistic estimators.** Test-passing is necessary, not sufficient. The grader-human gap is a calibration error that should be measured and reported like any other bias, ideally as grader precision against expert labels.
- **Autonomy rate is a conditional metric.** P(no human touch AND accepted | eligible task) is what matters. "AI-attributed share" conditions on nothing and inflates with every autocomplete.
- **Hidden labor is a cost term, not a footnote.** Review, rework and escalation scale with output volume. Faros shows the review queue is where AI throughput gains go to die.
- **Same pattern as eval for compression/routing:** a cheaper model "passing" an automated eval is the first check, not the last. Expert agreement on a sample is the real ceiling.

## Grounded Context (Web Enrichment)
The numbers mostly hold up. Faros AI's 2025 "productivity paradox" telemetry matches her figures exactly (21% more tasks, 98% more PRs, 91% longer review, 154% larger PRs, 9% more bugs per dev), with the important caveat that it is observational vendor data, which she states. The 296-patch blind maintainer study (scikit-learn, Sphinx, pytest maintainers) is METR's, not Meta's: roughly half to two-thirds of grader-passing patches would not be merged, the average gap was 24.2 points, and even known-good human patches were approved only 68% of the time, so the gap partly reflects maintainer taste and agents never got to iterate on review feedback. Builder.ai's $220M to $55M revision and SDNY/SEC probes are confirmed; Chapter 7 specifically appears in fewer sources than generic "insolvency."

The Uber example is better than she lets on. Secondary coverage of a September 2026 Rosenblatt note reports "over 70% of PRs involving AI," while earlier Uber commentary put autonomous-agent-produced code changes at roughly 10 to 11%. That is a 6-7x spread between "AI-attributed" and "autonomous" at the same company, which is her entire definition argument in one data point. See [[2026-10-05-AI-Engineer-Your-LLM-Judge-Is-A-Confident-Liar-Browserbase]] for the grader-calibration side and [[2026-06-03-YC-AI-Native-Services-Playbook]] for the "AI-native services" margin claims this checklist should be pointed at.

## Real-World Application / Actionable Step
- **Investing:** before buying into any "AI-native" services or automation story, ask for (a) headcount vs volume time series, (b) straight-through rate with a named boundary, (c) grader-vs-expert agreement numbers. No answer on (c) is a red flag.
- **Your own routing/compression claims:** report "accepted-quality rate under expert review" alongside automated eval pass rate. Measure grader-human agreement on a 100 to 200 sample and publish the gap.
- **Adopt her metric internally:** cost per accepted task (including retries, escalations to the big model, and human fixes) is the right objective for a router, not cost per call.
