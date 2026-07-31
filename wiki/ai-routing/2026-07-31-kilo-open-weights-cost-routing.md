# Kilo Code: Open Weights Are 79% of the Workload, and a 25x Price Gap Buys 5 Points

**Source:** Kilo Code blog, via [@kilocode on X](https://x.com/kilocode/status/2083199456401379586) · [Open Weights Is All You Need](https://blog.kilo.ai/p/open-weights-is-all-you-need) · [Kimi K3 + Grok 4.5 Built the Same Database as Claude Opus 5 at 1/25th the Price](https://blog.kilo.ai/p/kimi-k3-grok-45-built-the-same-database)
**Author:** Job Rietbergen, Kilo (acquired by Anaconda)

## TL;DR

Two posts, one argument, and the second is the evidence for the first. Kilo runs the application and routing layer for coding agents, so it sees which model actually gets each task. Its claim is that **open-weight models now carry 79% of its workload**, published as data behind the *Open Weights and American AI Leadership* letter that 230-plus organizations signed. The controlled experiment behind that number: give a **Kimi K3 (planning) plus Grok 4.5 (implementation)** pair and **Claude Opus 5 alone** the same two-phase job, design an embedded database from a spec then build it, and crash-test both with a harness written before either model ran. Result: **93/100 versus 98/100**, identical crash-test outcomes, at **$1.27 versus $31.71**. A **25x** price gap bought five points, and those five points came entirely from tests, documentation and code hygiene, not from correctness.

## The mechanism behind the five points

The gap is not a capability gap in the usual sense, it is a **harness behaviour** gap. Opus 5 ran a **150-step build/test/fix loop by default**. The budget combination mostly went **one-shot**. That is a difference in how much iteration each setup elected to do, which is a scaffolding parameter as much as a model property, and it is exactly the kind of thing a routing layer can change without changing models.

Kilo's own framing of the conclusion is the sharpest line in either post: *"The future isn't open vs closed. It's routing between both, and never getting locked into one."*

## What is claimed, and what to discount

- **79% of Kilo's coding workload runs on open weights.** This is first-party telemetry from a company that sells routing and has just published it in support of a policy position it holds. Directionally credible, self-interested in exactly the way that should be priced in.
- **Closed frontier models still win on the hardest problems**, which Kilo states plainly. The claim is about the other 80%, on cost, privacy and control.
- **Kimi K3 is the largest open-weight model released**, published by Moonshot AI on 2026-07-27, with inference providers serving it within a day.
- The database experiment is **n=1 on one task**. Two setups, one spec, one crash-test harness. Treat the 25x as a real order of magnitude and the 93-versus-98 as a single sample.

## Relation to prior wiki state

**This is the sharpest practitioner data point yet on the gap [llm-routing.md](llm-routing.md) has been tracking between what the market pays for routing and what the literature says routing is worth.** That page's current state records Stripe reportedly near a **$10 billion** acquisition of OpenRouter at roughly **70x** revenue, against [When is routing meaningful (07-20)](2026-07-20-when-is-routing-meaningful.md), which found many reported routing gains vanish under honest accounting of the router's own cost, and [IBM's system-optimization work (07-15)](2026-07-15-model-routing-system-optimization-ibm.md), which argued routing is priced wrong at the system level. Kilo's number is a third position that neither side models: the gain is not benchmark accuracy and it is not router overhead, it is **procurement**. A 25x price ratio at a five-point quality cost does not need a clever router to be worth capturing. It needs someone willing to not default to the frontier model.

That matches the [Gradient Ventures figure recorded on 07-30](llm-routing.md), where portfolio companies shifting work off proprietary models save **50-80%**, and it extends [DSPy task-model separation (07-25)](2026-07-25-dspy-task-model-separation-550x.md), which reported a **550x** cost gap between task and model choice on the same problem. Three independent measurements now say the same thing: **the dominant cost variable in an agent stack is which model you defaulted to, and the academic routing literature is measuring a much smaller effect than the one practitioners are capturing.**

**It also refines [Kilo's own plan/implement split (06-16)](2026-06-16-kilo-plan-implement-model-split.md).** That entry recorded the design, routing planning and implementation to different models. This is that design measured against a single frontier model on a controlled task, with the cost ratio attached.

**Industry-side confirmation of the open-weights thread.** [Ben Lorica's essay (07-28)](../ai-industry/2026-07-29-labs-competing-with-your-data.md) reported 25-plus startups building the reinforcement-fine-tuning stack so enterprises can own specialized models built on open weights, with 10 to 30 point gains on well-defined tasks. Kilo supplies the demand-side number that makes that market rational.

## Links

- [llm-routing.md](llm-routing.md)
- [Kilo plan/implement model split (06-16)](2026-06-16-kilo-plan-implement-model-split.md)
- [Daily digest 2026-07-31](../daily-digest/2026-07/2026-07-31.md)
