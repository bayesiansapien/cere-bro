# HarnessTax: the same model bills 5x more in a different harness (2026-09-22)

**TL;DR.** HarnessTax runs **21 model-harness combinations across 60 tasks** and reports the cleanest version yet of a claim this wiki has been assembling for a week: **harness choice moves cost far more than it moves success.** Across the grid, cost per attempt spans **$0.67 to $1.33** while success spans **96.7% to 97.8%**. That is roughly a **2x cost spread for a 1.1-point accuracy spread**, with the headline case being the same model billing about **5x more** depending on the harness wrapped around it. **9 of 12 configurations beat vendor-default Claude Code.**

## The mechanism, and why it is a context problem

The study's most useful structural finding is not the spread itself but its source. Pi averaged **15 turns**, yet the heavy setup carried **more than 10 times the initial context**, because **longer instructions and larger tool definitions ride along on every call**. The cost difference is not extra reasoning or extra turns. It is standing context, multiplied by turn count.

That is a compounding tax with a simple shape: a harness's fixed overhead is paid once per call, so a heavy harness on a long-horizon task pays it dozens of times for a benefit that was only ever needed once. **The lean setup, with four tools (read, write, edit, bash), still holds the cost-success frontier.**

Co-author @melissapan's framing is worth recording verbatim in paraphrase: **many harness choices run on tribal knowledge and word of mouth, so it is genuinely unclear which setup wins on accuracy or cost for a given workload.** That is an admission that the field's default configurations are unmeasured folklore.

## Relation to prior wiki knowledge

**This is the fourth independent result in six days saying the same thing, which closes a prediction.** The [09-19 digest](../daily-digest/2026-09/2026-09-19.md) predicted that a harness-versus-backbone ablation would become standard in coding-agent papers by year end, citing three results in three days: the [09-17 seven-way comparison](2026-09-17-harness-choice-costs-not-success.md) finding harness choice moves cost not success, the [09-18 component ablation](2026-09-18-harness-design-component-ablation.md) whose findings were conditional on the backbone, and SKILL.state's 16x. **HarnessTax is the fourth and the most systematic: a full 21-combination grid rather than a comparison of a handful.** The prediction is effectively resolved three months early, and the standard it predicted now has a reference implementation to copy.

**The context-overhead mechanism is confirmed from three directions on a single day.** [RRSI](2026-09-22-rrsi-regularized-harness-evolution.md) cut **30% of policy tokens** by pruning accreted harness scaffolding, which is the same tax measured as a saving. The [09-22 harness blueprint](../ai-routing/2026-09-22-decision-model-benchmark-ladder-and-routing-tax.md) circulating on X devotes three of its ten steps to tiered tool disclosure and conditional instruction loading, and reports that **reading and searching consume 56.2% of tool turns and 46.5% of tokens while writing code is under 10%**. [Harness-Zero](../inference-efficiency/2026-09-22-harness-zero-harness-distillation.md) removes the harness entirely at deployment and performs *better* (44.3% against 41.7% with it attached), which is that tax showing up as a performance penalty rather than a billing line. **Four results, one day, one mechanism: standing context is the dominant recurring cost of an agent, and nearly every default harness carries too much of it.**

**It gives the pricing page its grid.** [`agent-harness-engineering.md`](agent-harness-engineering.md) recorded on 08-13 that industry had started pricing the harness directly and on 08-28 that a cost-per-success number had finally arrived. HarnessTax supplies the two-dimensional version: cost and success as separate axes over a model×harness grid, which is the shape a buying decision actually has. **This should be the default reporting format for agent results, in the same way the [JevBench geometric mean](../ai-routing/2026-09-20-jev-ecosystem-census-72h.md) over intelligence, calibration, speed and cost is the right default for routing results.** Both refuse to let accuracy buy its way out of a cost problem.

## Gaps

60 tasks is a small suite for a 21-cell grid, so per-cell confidence is thin and the 1.1-point success spread is plausibly inside noise, which would make the real finding "harness does not affect success at all" rather than "affects it slightly." The task mix is not characterized in the summary, and harness overhead should matter far more on long-horizon work than on short tasks, so the spread is likely a function of the suite's horizon distribution. The study also treats success as binary; the [09-21 RecreationWorld finding](../daily-digest/2026-09/2026-09-21.md) that a 58.1% aggregate concealed a 2.8% all-tests-pass rate suggests a harness could be trading full-pass rate for partial credit invisibly.

## Industrial implication

The immediately actionable version: **audit your standing context before you change models.** If 9 of 12 configurations beat the vendor default, the default is leaving money on the table for most workloads, and the lean four-tool setup is the frontier. For vendors, this is an uncomfortable result, because the defaults that ship are the ones optimized for demo breadth rather than for cost, and the study makes that legible to buyers for the first time.

## Source

Raw: [`raw/twitter/feed/2026-09-22-morning-ranked.json`](../../raw/twitter/feed/) (@AlphaSignalAI, reporting the HarnessTax study; co-author @melissapan quoted)

## Related

- [`agent-harness-engineering.md`](agent-harness-engineering.md)
- [`2026-09-17-harness-choice-costs-not-success.md`](2026-09-17-harness-choice-costs-not-success.md)
- [`2026-09-18-harness-design-component-ablation.md`](2026-09-18-harness-design-component-ablation.md)
- [`2026-09-22-rrsi-regularized-harness-evolution.md`](2026-09-22-rrsi-regularized-harness-evolution.md)
