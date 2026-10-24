# 1,368 AI Failures and What They Teach About Evals (Vishal Srivastava & Tanmay Sah, New York Life)

**Channel:** AI Engineer
**Published:** 2026-10-22
**Source:** https://www.youtube.com/watch?v=mMw3arwQsL0

## TL;DR
New York Life's model-risk team coded 1,368 incidents from the public AI Incident Database against a 13-sub-dimension taxonomy and found that deployment controls (decision authority, human-in-the-loop effectiveness, exposure, monitoring) predict harm better than raw model quality. Their prescription: evals should be risk-weighted and falsification-driven (build, break, fix, break again), scoped to the whole deployed system including the LLM judge, with AI only allowed to operate in the regions where it has been stress-tested.

## Key Takeaways
- **Taxonomy (3 axes, 13 sub-dimensions)** covers ~98% of incidents:
  - Technical strength (6): data quality, system design, predictive validity, fairness, failure modes, explainability.
  - Deployment controls (4): decision authority (inform vs act), human mediation, exposure control (internal vs public), monitoring/harm detection.
  - Business impact (3): financial, legal, scale.
- **Failures are compound.** Average incident involves ~6 sub-dimensions at once. Single-axis evals miss the chain.
- **Frequency is not harm.** System design and scale appear often but correlate weakly with harm. Human mediation and harm detection appear less often but correlate strongly. Ranking by group: deployment controls > business impact > technical failure.
- **Risk decomposition:** P(model fails) x P(failure reaches a real decision) x P(goes uncaught) x severity. The same model carries very different risk depending on authority and review.
- **The evaluator is part of the system.** LLM-as-judge and synthetic scenario generators can miss failures; govern them like any other component.
- **Falsify, don't confirm.** Wason's 2-4-6 task (~79% of subjects fail to find the rule because they only test confirming cases) motivates adversarial evals. Map trusted, uncertain, and high-risk regions, then route by reliability and materiality.
- **Case study:** Air Canada chatbot invented a retroactive bereavement refund; a "policy-match" claim plus adversarial refund-after-travel probes would have caught it pre-deployment.

## Architecture & Optimization Mechanics
- The "failure region map" is structurally identical to a router's confidence map. A router decides which model handles a query; their framework decides whether AI handles it at all. Both need calibrated per-region reliability, not aggregate accuracy.
- Materiality scaling means eval compute should be allocated non-uniformly: dense adversarial coverage on high-materiality slices, light sampling elsewhere. Same logic as importance-weighted calibration sets for quantization.
- Weakness: the 98% coverage number is post-hoc fitting of a taxonomy the authors designed against the same dataset. It is a descriptive claim, not a validated predictive one. No held-out validation or inter-rater agreement was shown.

## Grounded Context (Web Enrichment)
The AI Incident Database's growth is real but partly an artifact of reporting: the 2025 AI Index counted 233 incidents in 2024 (+56% YoY) and summaries of the 2026 Index cite ~362 for 2025, yet AIID's own editors say much of the rise reflects increased media scrutiny, and the database cannot be extrapolated to true incident rates. So the "near-vertical" curve in the talk overstates the underlying failure rate. The harm correlations are also biased toward incidents that became newsworthy, which naturally overweights customer-facing (exposure) and unmonitored failures.

The Air Canada case is Moffatt v. Air Canada (2024 BCCRT 149). The tribunal rejected Air Canada's argument that the chatbot was "a separate legal entity," holding the airline failed to take reasonable care. Damages were trivial (~CAD 650 to 812), but the precedent is the point: companies own their bot's statements. Minor correction: Wason described the 2-4-6 effect in 1960 but the term "confirmation bias" was popularized later.

## Real-World Application / Actionable Step
- For any routing or compressed-model deployment, add a per-slice **materiality tag** to eval sets and report worst-slice degradation, not mean accuracy. A 0.5% average drop after quantization can hide a 10% drop on the high-materiality slice.
- Build a **falsification suite**: for each claim ("INT4 model preserves tool-call correctness"), write tests designed to break it (long context, rare tools, adversarial schemas), then fix and re-break.
- Calibrate the LLM judge itself against a small human-labeled set before trusting it as the routing quality oracle.
- Route high-materiality queries to the strongest model or to human escalation by default; let cheap models earn those regions only after adversarial evidence.
