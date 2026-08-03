# AISPA: User-Centric System Prompt Auditing for LLM Applications

**arxiv:** [2607.28617](https://arxiv.org/abs/2607.28617) · **Source:** [HuggingFace Daily Papers, 2026-08-03](../../raw/huggingface/2026-08-03-aispa-user-centric-system-prompt-auditing-for-large-language.md)

## TL;DR

The system prompt is the layer where a developer decides how a model behaves toward the person using it, and almost none of them are published. AISPA audits **3,249 instructions from the system prompts of 88 commercial AI products**, classifying each instruction as protective of users or working against them, along eight user-facing dimensions.

Four findings, and the third and fourth are the ones that matter.

1. **Enormous variance in design effort.** Some organizations average over 60 protective instructions per product. Others average fewer than five.
2. **Protection is near-universal and shallow.** 98.9% of products contain at least one protective instruction. Only **24% cover all eight dimensions.** Everyone does a bit; almost nobody does the set.
3. **The trend is real.** System prompts have grown steadily longer and more protective over time, so this is an area where commercial practice is genuinely improving without regulation forcing it.
4. **Roughly 40% of products contain at least one instruction that works against the user's interest**, and protective and problematic instructions routinely sit in the same prompt.

That last pairing is the finding. It is not that some companies protect users and others do not. It is that **the same prompt does both**, which means a compliance check that looks for the presence of protective language passes a prompt that also contains the opposite.

## Why this belongs in the wiki

It is the first empirical measurement here of the governance layer that actually ships. Model cards, alignment training and safety evaluations all operate on the model. The system prompt operates on the deployment, is changed weekly with no review, is invisible to users and regulators, and overrides a great deal of what alignment training installed. A 40% problematic-instruction rate across 88 commercial products is a bigger governance surface than most of what the policy conversation covers.

It also composes with a result from earlier this week. [Safeguards Based on Copyable Context (08-03)](2026-08-03-copyable-context-safety-trilemma.md) proved that when a safeguard conditions on copyable evidence, an exact floor on attacker assistance follows regardless of how good the classifier is. **The system prompt is copyable evidence, and this paper shows it is also the main safety artifact in commercial products.** Read together: the layer doing most of the deployed safety work is the layer with a theorem saying it cannot be reliable, and 40% of the time it is also being used against the user it is nominally protecting.

## Relation to prior wiki state

Extends the transparency thread on [responsible AI](responsible-ai.md) from claims about models to claims about products. The wiki's prior entries in this area are about whether a readout of the model can be trusted, and the pattern established there is that every measured safety readout comes in weaker than its headline: [faithfulness metrics near chance (05-26)](2026-05-26-faithfulness-metrics-meta-evaluation.md), [deception probes shattering under a benign style shift (06-03)](2026-06-03-deception-probes-pressure-test.md), [filler tokens defeating chain-of-thought monitoring (08-03)](2026-08-03-filler-token-invisible-reasoning.md). AISPA is the deployment-layer instance of the same shape: the artifact everyone assumes is doing the protective work is, when measured, doing something else about 40% of the time.

## Gaps

The protective-versus-problematic labels are a judgement call and the paper's classification pipeline is doing a lot of unexamined work; "works against user interests" covers everything from dark-pattern retention language to a legitimate business constraint the user would not choose, and those should not be one category. System prompts of commercial products are obtained by extraction rather than disclosure, so the corpus is biased toward products whose prompts leak, and the extracted text may be partial. The eight dimensions are the authors' taxonomy with no external validation that they are the dimensions users care about. And there is no temporal control on the "growing more protective" claim beyond the products sampled, so it could be a composition effect from newer products entering the set.

## Industrial read

The deployable artifact is the taxonomy, not the audit. Eight dimensions with per-instruction labels is a checklist any team can run against its own system prompt in an afternoon, and the 24% full-coverage figure says most teams would fail it. The regulatory read is more interesting: **system prompt disclosure is a cheaper transparency intervention than anything else currently proposed**, requires no interpretability research, and this paper is the first dataset showing there is something to find.

## Related pages

- [Responsible AI](responsible-ai.md)
- [Safeguards Based on Copyable Context (08-03)](2026-08-03-copyable-context-safety-trilemma.md)
- [Filler-token invisible reasoning (08-03)](2026-08-03-filler-token-invisible-reasoning.md)
