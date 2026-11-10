# Right Answer, Wrong Reasons: AI Forecasts Costco (Hassan El Mghari & Omar El Mghari, Together AI)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=dznCt8xPW7o

## TL;DR
An open model built a financial model to forecast the profit impact of Costco's September 2024 membership fee hike ($60 to $65 standard, $120 to $130 executive). It landed within 4.4% of reported results. A former CFO and auditor (Hassan's father) then showed it was right by luck. Two wrong assumptions cancelled out: the hike was applied to the global member base instead of only US/Canada, and the executive-tier share was a hallucinated 15% when Costco's filings disclosed about 45%. Fix just one and the error jumps to 28%. The lesson is that "luck is not a control." Accuracy on a single backtest says nothing about correctness, and domain-expert checks need to be codified into the pipeline.

## Key Takeaways
- **Avoid lookahead leakage:** newer open models (GLM-5.3 and others) already knew about the hike, so they used pre-July-2024-cutoff models (gpt-oss-120b, Llama-3.3-70B). Probe the model ("did Costco change its fee in 2024?") before backtesting.
- **Pipeline:** 214 filings, about 3,000 timestamped facts, filtered to the cutoff, then 16 parallel gpt-oss-120b sessions each writing a formula-based model (14 formulas, assumptions, filing constants) as structured JSON.
- **Structured output over in-context math:** the model emits formulas (e.g. fee revenue recognized ratably over 52 weeks), and a deterministic engine evaluates them in about 10 ms.
- **Engineering checks:** no self-referencing formulas, a fee increase must raise revenue, and so on. Failures were fed back up to 2 retries. 5 of 16 runs passed.
- **Parallel sampling beat prompt tuning:** 16 runs cost $0.19 total and yielded more valid models than hours of prompt iteration.
- **Forecast:** about +$560M profit over 2 years. The 5 passing builds had errors of 0.7% to 5.2% (average 4.4%).
- **Audit failures:** the executive share had a real citation ("increased penetration") but an invented number, plus invented bounds (5 to 30%) that excluded the true value. A US/Canada lever had zero effect, so the lever was broken. Across the 16 runs, fee-uplift estimates ranged from $0.5B to $6B against roughly $450M recalculated.
- **Auditor trick:** to detect offsetting errors, correct one assumption and see whether accuracy collapses.
- **Three lines of defense:** management controls (code checks), internal audit (domain accounting checks), external audit (independent human judgment).

## Architecture & Optimization Mechanics
- **LLM as model-compiler, not calculator:** the expensive model runs once to emit a program, and inference afterwards is free and deterministic. This amortization pattern also applies to routing: have an LLM synthesize cheap deterministic rules, then serve those rules.
- **Best-of-N with verifiers:** 16 samples of a small open model plus hard constraint checks beat one tuned prompt. This is test-time compute scaling with a cheap model. The verifier only checks structural validity, though, not semantic truth, which is exactly where it failed.
- **Provenance gap:** each assumption needs a numeric citation to a source fact, not just a qualitative one. An "assumption has a number found in the corpus" check would have caught the 15% vs 45% error.
- **Sensitivity testing:** a lever with zero sensitivity is a bug signal. Automated one-at-a-time perturbation would have flagged the dead US/Canada lever.

## Grounded Context (Web Enrichment)
The real-world outcome supports the auditor, not the headline 4.4%. Costco's fee hike took effect September 1, 2024, and because fees are recognized ratably, the benefit spread across fiscal 2025 and 2026. Membership fee income reached about $5.32B in FY2025 (+10%), roughly half of $10.4B operating income. Analyst breakdowns attribute only about a quarter to a third of that growth to the hike. The rest came from member growth (paid members +6%) and executive upgrades, with renewal rates holding near 92% US/Canada and 90% globally. By late FY2026 the hike contributed under 1 point to quarterly fee growth, and ex-hike, ex-FX fee growth was about 6.8%. A clean forecast therefore needed to separate the price effect from volume and mix, which the AI model conflated. Costco's executive members were reported at roughly the mid-40% range of paid members in 2024, consistent with the speaker's 45% correction.

The broader point is well supported. Temporal leakage is a known flaw in LLM forecasting benchmarks, and choosing pre-cutoff models is the right control. A single backtest with n=1 event cannot validate a forecasting method. "Within 4.4%" was never strong evidence.

## Real-World Application / Actionable Step
- **Add an offsetting-error test to your evals:** when a compressed or routed pipeline matches the baseline on an aggregate metric, ablate one component and check for a collapse. Matching aggregates can hide cancelling errors, for example quantization noise offset by a prompt tweak.
- **Use cheap best-of-N plus verifiers as a routing baseline.** Before escalating to a frontier model, try N samples of a small open model with hard checks, and compare cost per valid output.
- **Require numeric provenance** in any RAG or agent output that drives decisions. Each number must match a span in the source.
- **Finance angle:** for COST, the fee-hike tailwind is spent. Forward fee growth depends on member growth and executive mix (roughly 7% underlying), so don't extrapolate FY2025's 10% fee growth.
