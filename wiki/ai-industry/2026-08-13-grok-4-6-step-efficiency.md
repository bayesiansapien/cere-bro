# Grok 4.6: frontier intelligence sold on steps-per-task, not on the benchmark

**Source:** [The Decoder](https://the-decoder.com/spacexais-grok-4-6-matches-openais-best-model-and-undercuts-it-on-price/) · [model card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf) · [Artificial Analysis](https://x.com/ArtificialAnlys/status/2087603281791246749) · raw: [`raw/rss/2026-08-12-the-decoder-spacexai-s-grok-4-6-matches-openai-s-best-model-and-und.md`](../../raw/rss/2026-08-12-the-decoder-spacexai-s-grok-4-6-matches-openai-s-best-model-and-und.md), [`raw/twitter/2026-08-13-morning.md`](../../raw/twitter/2026-08-13-morning.md)

## TL;DR

SpaceXAI released Grok 4.6 at the same price as Grok 4.5. It scores **61 on the Artificial Analysis Intelligence Index**, tying GPT-5.6 Sol and trailing only Claude Opus 5. That is the headline, and it is the least interesting number in the release.

The interesting number is the one about *how it works*, not how well: on agentic tasks it **completes complex workflows in about 53 steps where Claude Opus 5 needs 103**, at a price more than **60 percent lower**. Roughly half the steps at roughly 40% of the price is a compounding cost advantage, because in an agent loop every step is a full round trip carrying the accumulated context. The comparison the market will actually run is dollars-per-completed-task, and on that axis Grok 4.6 is not tying the frontier, it is undercutting it by a large multiple.

The model card, read by Hugging Face's Elie Bakouch, sharpens the picture into an unusually legible profile of what SpaceXAI optimized for:

- **Large gains on DeepSearchQA and their internal KernelBench.** KernelBench is GPU kernel generation. A frontier lab reporting big internal gains on writing GPU kernels is a Tier-1 signal on its own.
- **Best on SpaceXAI's internal engineer benchmark**, with the obvious caveat Bakouch names himself: they likely trained on similar data.
- **State of the art on "inferenceEval", which measures optimization of their own chat inference.** The model is being explicitly optimized to optimize the serving stack it runs on.
- **Behind the frontier on public SWE evals**: Terminal-Bench 3.0, SWE Marathon v1.1, DeepSWE.

That last bullet next to the first three is the whole story. Grok 4.6 is strong on the benchmarks SpaceXAI built and weaker on the ones it did not. Whether that reads as focused optimization or as benchmark fitting depends entirely on whether the internal benchmarks measure something real, and there is no way to check from outside.

Two more items from the release. **Grok 4.6 Fast runs at $4 in / $12 out per million tokens**, which DHH noted is about a quarter of the price of comparable "fast" tiers. And Elon Musk announced **Grok 4.7 in three to four weeks**, initial training complete, now in supplemental training on "a massive amount of SpaceX company data."

---

## The harness detail that matters most

From [@aksheyd](https://x.com/aksheyd/status/2087622695718662338): **"Grok 4.6 optimized the Grok Build harness for itself."**

That single sentence is the industry twin of the day's strongest research result. [AI4AI at Test-Time (08-13)](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md) showed that a strong model writing an inference-time harness for a weaker model nearly doubles the weaker model's accuracy with its weights frozen, going from 0.49 to 0.91 across four Theory-of-Mind benchmarks, and that the gains come from offloading unstable reasoning into deterministic code, routing per question type, and enforcing answer format. AI4AI is strong-to-weak. Grok Build is **self-to-self**: the model tuned the scaffold it runs inside.

Put next to the 53-versus-103 step count, the plausible reading is that a meaningful share of Grok 4.6's agentic efficiency is harness, not weights. Nobody outside SpaceXAI can decompose it, and SpaceXAI did not publish the decomposition. That is exactly the ablation the field needs and exactly the one a competitive lab has no incentive to run.

---

## How this relates to prior wiki pages

**It is the industry data point for [Agent Harness Engineering](../agentic-systems/agent-harness-engineering.md).** That concept page's spine is the measurement that harness choice swings cost-per-success 5x to 30x on a fixed model. Grok 4.6 ships a 2x step reduction against the best available model and simultaneously discloses that it tuned its own harness, without separating the two contributions.

**It sits in tension with the 08-12 benchmark cluster.** [DSAgentBench, SPIEval and VibeLifeBench (08-12)](../agentic-systems/2026-08-12-agent-benchmark-cluster.md) found the best agent in the world completing 56.70% of real data-science workflows, with 79% of SPIEval failures being inaccurate information localization. Those benchmarks measure whether the agent finishes. Grok 4.6's step count measures how expensively it gets wherever it gets. **A model that fails in half as many steps is cheaper, not better**, and the release does not report completion rates on the benchmarks that are hard to fit.

**It confirms the [A²E finding (08-11)](../agentic-systems/2026-08-11-harness-evolution-cluster.md) that no model-harness combination wins across all task types,** from the other direction. Strong on internal engineering and kernel work, behind on Terminal-Bench and SWE Marathon, is precisely a model-harness combination that wins on some task types and not others.

## Gaps

The internal benchmarks (KernelBench, inferenceEval, the SpaceXAI engineer benchmark) are unpublished and self-scored, and Bakouch flags the likely training-data overlap. The step-count comparison comes from Artificial Analysis rather than a paper, with no per-task breakdown, so it is unclear whether the reduction holds on the task types where Grok trails. And no decomposition of model contribution versus harness contribution is offered anywhere.

## Industrial implication

If you are budgeting agent workloads, **stop comparing on price per million tokens and start comparing on steps to completion times price per step**. Grok 4.6 is the first release marketed primarily on that composite, and it is the correct metric. Two models can tie on an intelligence index and differ by 4x in what a finished task costs.

The second-order read is competitive. Optimizing a model to optimize its own inference stack is a flywheel argument, and SpaceXAI is now claiming it explicitly with inferenceEval. If it works, serving-cost advantage compounds inside one lab in a way benchmark scores do not, and it is invisible to every public leaderboard.

---

**Related:** [Agent Harness Engineering](../agentic-systems/agent-harness-engineering.md) · [AI4AI at Test-Time](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md) · [Digest 2026-08-13](../daily-digest/2026-08/2026-08-13.md)
