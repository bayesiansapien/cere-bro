# Gary Marcus: Open-Source Is Not the Same as Open-Weight

**Source:** Marcus on AI · [post](https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open)
**Raw:** [raw/gmail/2026-08-11-starred.md](../../raw/gmail/2026-08-11-starred.md) (item 1) · [raw/rss/2026-08-10-marcus-on-ai-open-source-is-not-the-same-as-open-weight.md](../../raw/rss/2026-08-10-marcus-on-ai-open-source-is-not-the-same-as-open-weight.md)
**Date:** 2026-08-11 (published 2026-08-10)

## TL;DR

Marcus's argument, prompted by Meta's Muse Glimmer release and by the New York Times calling it "open source," is that the two terms differ on the two properties that made open source matter: **transparency and customizability**. An open-weight release ships the trained candidate model, not the pipeline that produced it. No raw data, no preprocessing recipe, no exact training algorithms or hyperparameters. His enumeration of what that forecloses is the useful part, because each item is a concrete experiment someone cannot run:

- A developer who hypothesizes that removing Reddit data yields a safer model cannot test it, and cannot even inspect the data to check.
- A developer who wants to filter common law from statutory law before training a legal-reasoning model cannot.
- A regulator asking how much bias toward white males the training data carries, or what bioweapons-relevant instructions it contains, cannot look.
- A scientist asking **how much of model behavior is regurgitation versus genuine extension beyond training data**, which Marcus calls arguably the central question in AI, cannot answer it. Neither can anyone check whether benchmark answers are already in the training set.
- A copyright question about how much training data was copyrighted is likewise unanswerable, which Marcus suggests is part of why labs prefer open-weight to open-source.

His counterexamples of genuinely open-source models: **AllenAI's Olmo** and **NVIDIA's Nemotron**, which ship weights, training data and recipes.

## Why this is a Deep Dive and not a Pulse bullet

It is a precise definitional claim with testable consequences, and it lands in the middle of a live policy fight this wiki has tracked since 08-02. **On the same day Marcus published, Mark Zuckerberg released Muse Glimmer under Apache 2.0, published a 6,500-word essay defending distilling other labs' models, and called on the US to reduce "friction" around open source**; the [The Information's read (08-11)](https://www.theinformation.com/articles/zuckerberg-v-amodei-ai-marketing) is that this is a marketing escalation, a longer restatement of a WSJ op-ed from two weeks earlier. Marcus's response is that Zuckerberg himself used the correct term and the press did not.

## How this relates to prior wiki pages

**It supplies the transparency half of an argument [knowledge-distillation.md](../inference-efficiency/knowledge-distillation.md) has been making from the technical half.** That page has documented since [the Distillation Panic (05-04)](../inference-efficiency/2026-05-04-distillation-panic-lambert.md) that "distillation" names two different things: copying a rival frontier model's outputs to shortcut capability, which is an IP and provenance question, and compressing a teacher you own into a student you serve, which is an efficiency technique. Marcus is drawing the same kind of distinction one layer up, between releasing an artifact and releasing a process. In both cases **the policy conversation is using a word that the technical practice splits in two**.

**It also lands on the [three open letters entry (08-02)](2026-08-02-three-open-letters-ai-governance.md).** Microsoft's 235-signatory open-weights letter defended distillation as a widely used technique for model improvement, evaluation and validation; Anthropic declined to sign and asked for a crackdown on industrial-scale distillation. Marcus's contribution is orthogonal to both sides: whatever you think of distillation, an open-weight release does not deliver the scientific auditability that the open-source framing promises regulators.

**Bengio made the safety-side version of the same complaint three weeks earlier.** The [WAIC safety forum takeaways (08-11)](../responsible-ai/2026-08-11-waic-agentic-safety-forum.md) record him naming the unique safety challenges of open-weight models: irreversibility of deployment decisions, ease of removing safeguards, and difficulty of evaluating risks once weights are widely shared. **Marcus and Bengio are complaining about the same missing artifact from opposite motivations, one wanting science and the other wanting oversight, and neither gets it from a weights drop.**

**The counterexamples matter for this wiki's sourcing.** Olmo and Nemotron being genuinely open-source means they are the only models where several claims this wiki tracks are checkable, most importantly benchmark contamination. [SWE-Bench ProMax (08-11)](../agentic-systems/2026-08-11-swe-bench-promax.md) reports that frontier models can verbatim reproduce gold patches from training data, and there is no way to verify that claim against a model whose training data is unpublished.

## Where the argument is weakest

Marcus overstates one thing: post-training is not nothing. A great deal of a modern model's behavior is set after the base run, and open weights do allow substantial redirection through fine-tuning, RL and steering, as this wiki's entire post-training corpus shows. His cake-without-the-recipe metaphor concedes this ("you can add icing"), but the essay's rhetorical weight ("developers often can't really use the open-weight models") reads as stronger than the technical record supports, given that [Applied Compute is at roughly $50M annualized revenue helping enterprises customize open models](https://www.theinformation.com/articles/applied-compute-talks-double-valuation-3-billion-open-source-demand) and is raising at a $3B valuation on exactly that demand.

The scientific and regulatory half of his argument, though, is not weakened by that, because none of those post-training levers let you see the data.

## Related

- [knowledge-distillation.md](../inference-efficiency/knowledge-distillation.md), [responsible-ai.md](../responsible-ai/responsible-ai.md)
- [Three open letters on AI governance (08-02)](2026-08-02-three-open-letters-ai-governance.md), [WAIC safety forum (08-11)](../responsible-ai/2026-08-11-waic-agentic-safety-forum.md)
