# Salesforce moves Agentforce billing from seats to outcomes

**Source:** The Information, Kevin McLaughlin, 2026-08-30. "How Salesforce Is Overhauling the Way It Charges for AI."
**Links:** [Article](https://www.theinformation.com/articles/salesforce-overhauling-way-charges-ai) (paywalled beyond the opening) · [raw](../../raw/rss/2026-08-30-the-information-how-salesforce-is-overhauling-the-way-it-charges-for-ai.md)

---

**TL;DR.** Salesforce is letting customers choose how they pay for Agentforce, its agent product, including **custom contracts priced on business outcomes**: revenue growth from salespeople closing more deals, or cost reduction from automating more customer-service interactions. This is the enterprise-software industry moving off the per-seat subscription that defined it, through consumption pricing, and out the far side into outcome pricing. The Information's framing is that Salesforce shows how complicated the transition is, not how clean.

---

## Why this matters beyond a pricing story

The wiki has been tracking one question all month: **what is the correct unit of cost for AI work?** [Compute economics](../hardware/compute-economics.md) records the answer moving three times in two weeks. Dollars per GPU-hour was the training-market unit. Dollars per million tokens was the serving unit until 08-16, when two findings broke it: DHH's **24x dollar spread** on one identical Rust rewrite across five frontier models, and Anthropic's own engineer putting OpenAI's tokenizer at roughly **30% more efficient per unit of text**, meaning two vendors quoting the same dollars-per-million-tokens are not quoting the same price. Artificial Analysis's [Optima (08-16)](2026-08-16-optima-cost-per-task-benchmarking.md) then shipped the instrument for the replacement unit, **cost per completed task**.

Salesforce is now going one unit further than the wiki's research thread has reached. Cost per completed task still prices the *work*. An outcome contract prices the *result*: not "the agent handled 40,000 tickets" but "support cost fell by X." That is a different quantity and a harder one, because it requires attributing a business change to a software system.

**The sequence is worth naming as a ladder, because each rung moves risk one step toward the vendor:** per-seat (customer bears all usage risk), per-token (customer bears model-efficiency risk), per-task (vendor bears model-efficiency risk), per-outcome (vendor bears deployment-and-attribution risk).

## The uncomfortable connection to the measurement crisis

This wiki declared a measurement crisis on 08-11 and it reached a formal statement on 08-29 with [the Inspect Evals census](../responsible-ai/2026-08-29-evaluation-license-claim-replay-census.md), which found **110 of 124 eval units cannot license the claims attached to their numbers**, because the artifact does not carry the evidence needed to replay the claim. The 08-29 Global View drew the industry counterpart: buyers have quietly stopped using accuracy benchmarks and switched to cost per completed task, citing Visa telling The Information that its own harness makes Anthropic's model cheaper and faster at security work with vendor pricing unchanged, and [PILOT (08-28)](../agentic-systems/2026-08-28-pilot-live-self-improvement.md) publishing output tokens down 42.9% and successes per million output tokens up 110.3%.

**Outcome-based pricing is that shift becoming contractual, and it inherits an unaudited instrument.** An eval number that cannot license its claim is an academic problem. A contract clause that cannot license its claim is a dispute. "Revenue grew because Agentforce helped salespeople close more deals" is a counterfactual, and counterfactual attribution in a live sales organization has no frozen substrate, no pinned evidence, and no agreed semantics, which is precisely the three-part deficiency the Inspect Evals census formalized. The census's framework applies to this contract without modification and nobody has applied it.

## How this relates to prior wiki pages

**It is the demand-side pressure that makes harness engineering a procurement matter.** [Agent harness engineering](../agentic-systems/agent-harness-engineering.md) records cost-per-success swinging **5x to 30x** on a fixed model depending on harness (omarsar0, arXiv 2608.01347, 08-13). Under per-seat pricing that variance is the customer's problem and mostly invisible. Under an outcome contract it lands on the vendor's margin, which gives Salesforce a direct financial reason to invest in harness quality rather than model access. **Outcome pricing converts the wiki's central harness finding from an engineering observation into a P&L line**, and it is the clearest mechanism yet for why the harness gets funded.

**It also puts a second party on the wrong side of today's calibration result.** [Agents are not time aware (08-30)](../agentic-systems/2026-08-30-agents-not-time-aware.md) finds coding agents overrating their own output by roughly 20 points and predicting task duration with a compression exponent of 0.19-0.24, meaning the prediction barely responds to the real duration. A vendor pricing on outcomes needs to forecast how much agent work a contract will consume, and the agents cannot forecast their own consumption. That does not break the model, since vendors can measure in aggregate rather than ask the agent, but it does mean **the forecasting has to live in the vendor's telemetry, and it is one more decision the harness has to take away from the model.**

**Contrast with today's other pricing move, which runs the other way.** Anthropic is [replacing a temporary 50% Claude Code usage boost with a permanent 25% increase](https://the-decoder.com/anthropics-claude-code-limit-change-is-a-raise-on-paper-but-a-cut-in-practice/) when the boost expires on September 14, a roughly **17% effective cut** to weekly limits, offered alongside more usage control and transparency. That is a model vendor tightening a metered allowance while Salesforce, an application vendor, absorbs metering risk on its customers' behalf. Both are rational: **the application layer can price outcomes because it sits close enough to the business to observe them, and the model layer cannot, so it rations.** The margin gets squeezed in the middle, and the middle is whoever runs the harness.

## Gaps

The article is paywalled past the opening, so the specific contract structures, the share of customers taking outcome deals, and any dollar figures are not available here. "Starting to let businesses choose" suggests a pilot rather than a repricing, and the reporting's own framing is that the transition is complicated.

The harder unknown is measurement, and it is not a reporting gap but a real one. No public methodology exists for attributing a revenue change to an agent deployment in a way both parties would accept in advance. Until one does, outcome pricing is negotiated case by case, which means it does not scale and it advantages the party with better telemetry, which is the vendor.

## Related pages

- [Compute economics](../hardware/compute-economics.md)
- [Optima: cost-per-task benchmarking](2026-08-16-optima-cost-per-task-benchmarking.md)
- [Token price is not task cost](2026-08-14-alphasense-token-price-vs-task-cost.md)
- [Agent harness engineering](../agentic-systems/agent-harness-engineering.md)
- [The evaluation-license census](../responsible-ai/2026-08-29-evaluation-license-claim-replay-census.md)
