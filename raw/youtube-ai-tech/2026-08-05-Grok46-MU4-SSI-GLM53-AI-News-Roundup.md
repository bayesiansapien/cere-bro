# Grok 4.6 HUGE LEAKS, OpenAI 'mu4', GLM 5.3, Codex 2.0, SSI Model, Flux 3 & More

**Channel:** WorldofAI
**Published:** 2026-08-05
**Source:** https://www.youtube.com/watch?v=JJvSODvTCes

## TL;DR
A rumour roundup, and the value is entirely in separating the confirmed from the speculated, because the video does not. Confirmed: Grok 4.6 lands 7 August 2026, at 2 trillion parameters against Grok 4.5's 1.5T, with Grok 4.7 at 2.1T a few weeks behind. Reported by a well-connected source but unconfirmed by the company: Safe Superintelligence shipping its first model in August, which would contradict SSI's own stated position that its first product would be the superintelligence itself. Pure leak: an OpenAI internal checkpoint called mu4, possibly becoming GPT-5.7, alongside Astra as a separate and larger effort. Also covered: GLM 5.3 imminent and explicitly not multimodal, Ling 3.0 Flash from Ant Group shipping in BF16 and FP8, Flux 3 video at $0.17 per second, and a Codex overhaul promised in two to three months.

## Key Takeaways
- **Grok 4.6 is real and dated.** 7 August 2026, 2T parameters, trained on the Colossus cluster in Memphis which now houses over 500,000 GPUs across two buildings. Arena evaluation the following week. Grok 4.7 at 2.1T expected late August or early September.
- **The pre-release demos are the only substantive evidence and they are narrow.** A Minecraft clone with working shaders, a Three.js CD player with functional eject animation and disc selection, a cozy room with a storm including generated thunder audio. All produced at what the reviewer notes is Arena's typical low reasoning effort.
- **SSI's August model is a second-hand claim.** Gavin Baker said it on Invest Like the Best. SSI has never announced it. The reviewer flags this honestly and raises the right objection: SSI recently described discovering a new research paradigm and received additional Nvidia compute, which is not the posture of a company about to ship.
- **The stronger objection the video misses:** Sutskever has publicly said SSI's first product will be the safe superintelligence itself. A conventional model release would be a strategy reversal, not a milestone.
- **mu4 is a leak with a plausible provenance chain.** The same leaker previously surfaced an Anthropic release. mu3 was reportedly visible in a six-second segment of a deleted OpenAI video, with "Medium" beside it, suggesting a size or effort tier. mu4 entered testing this week. Astra is described as separate and possibly GPT-6 foundation.
- **GLM 5.3 is near, and ZAI confirmed it will not be multimodal.** CLSA reporting says the focus is real-world coding via better training data, stronger post-training and faster infrastructure, with an entirely new architecture in the generation after.
- **Ling 3.0 Flash from Ant Group ships BF16 and FP8 checkpoints at release.** Shipping both precisions on day one is now table stakes for open weights.
- **Flux 3 video: $0.17 per second, up to 20 seconds, native 1080p, open weights promised.** Twenty seconds costs $3.40.

## Architecture & Optimization Mechanics
The most valuable technical content in this video is not in the video. It is in the context behind the SSI rumour, and it is worth extracting because it bears directly on inference economics.

Gavin Baker's actual discussion on that podcast was about continual and sample-efficient learning: the scenario where a model is trained once on something like 10 trillion tokens and then deployed to keep learning from its own interactions, sample-efficiently, without retraining from scratch. If that works, the industry's cost structure inverts. Today the split is a very large one-time training cost amortised over inference, with periodic full retrains. Under continual learning, the retrain line goes away and is replaced by ongoing weight updates during deployment, which changes what a serving stack has to do. Weights become mutable at serving time, which breaks the assumption underlying almost every deployment optimization currently in use. Static post-training quantization assumes fixed weights. A pruning mask calibrated once assumes the surviving weights stay meaningful. KV cache and weight caching across replicas assume all replicas hold identical parameters. None of that survives a model whose weights drift per deployment.

That is the reason the SSI rumour matters more than the Grok date, and the video treats them as equivalent news items. If SSI's "new research paradigm" is in this family, the relevant question is not whether it benchmarks well but whether it invalidates the current serving playbook.

On the announced items, two are worth reading as signals about where the field's efficiency work is going. Ant Group shipping Ling 3.0 Flash with both BF16 and FP8 checkpoints at release, rather than leaving FP8 to the community, indicates that vendor-side quantization has become part of the release artifact rather than a downstream activity. That is good for deployment and slightly bad for anyone whose value-add was producing the quantized variant. Worth checking whether the FP8 checkpoints being shipped are naive per-tensor casts or properly calibrated, because the two differ substantially in quality retention and vendors do not always say which they did.

The second is ZAI's confirmation that GLM 5.3 will not be multimodal, which the reviewer treats as a straightforward disappointment. It is more interesting than that. DeepSeek and Qwen have both gone multimodal; ZAI is spending its parameter and training budget entirely on text and coding. That is a deliberate specialisation bet, and if GLM 5.3 lands competitive on coding against multimodal peers at lower cost, it is evidence that multimodality carries a real capability tax on text tasks. That is a testable proposition and a genuinely useful one for routing: a text-only specialist may be the right default tier with a multimodal model reserved for queries that actually need vision.

Finally, the Grok scaling numbers deserve a sceptical note. 1.5T to 2T to 2.1T across three releases in roughly two months is parameter count growth with no disclosed information about active parameters or architecture. Compared with [Qwen3.8-Max at 2.4T total and 95B active](2026-08-04-Qwen38-Max-2p4T-MoE-Sparsity-Frontier.md), a total-parameter figure alone says nothing about serving cost. Until xAI publishes activation counts, "2 trillion parameters" is a marketing number, not an engineering one.

## Grounded Context (Web Enrichment)
The Grok 4.6 details check out and are firmer than the video's "leak" framing suggests. Musk confirmed the 7 August 2026 release, and the model is reported at 2 trillion parameters against 1.5T for Grok 4.5, trained on the Colossus cluster. Grok 4.7 at 2.1 trillion is expected a few weeks later. Arena evaluation is scheduled for the week following launch. Importantly, no official specs, pricing or benchmarks existed at the time of this video, so every performance claim including the reviewer's guess that it lands just behind Kimi K3 is speculation.

One point needs care. The video says the model "appeared on LMArena under the code name Colossus." Colossus is definitively the name of xAI's Memphis supercomputing cluster, not a model codename, and the two are easy to conflate. Anonymous arena codenames are a real phenomenon, so it is possible a checkpoint appeared under that string, but the claim is unverified and the far more likely reading is confusion between the model and the cluster it was trained on. Do not repeat the codename claim as fact.

The video's reference to "SpaceX AI" reads like an error but may not be one. Contemporary coverage of Grok 4.5 describes it as entering private beta at SpaceX and Tesla and refers to the model as SpaceX's, so the corporate relationship between xAI and SpaceX appears to have changed. Worth verifying before making any statement about which entity ships these models.

On SSI, the facts are: founded June 2024 by Ilya Sutskever, Daniel Gross and Daniel Levy, $1 billion seed at a $5 billion valuation within three months, a further $2 billion at $32 billion by April 2025, and no commercial product with a public commitment to keeping it that way until the mission is complete. Gavin Baker's August claim came on Invest Like the Best with Patrick O'Shaughnessy, and SSI has not confirmed it. The strongest counterargument, raised on X and not in the video, is that Sutskever has stated the first product will be the safe superintelligence, so any conventional model release would represent an abandonment of the stated plan rather than progress toward it. Baker is genuinely well-connected and the claim should not be dismissed, but the base rate for a lab reversing its founding commercial position on a podcast rumour is low.

The mu4 material is unverified throughout and should be treated as such. A checkpoint name glimpsed in a deleted video and a leaker's report of testing is not evidence of a release timeline, a model size, or a product name. The mapping of mu4 to GPT-5.7 and Astra to GPT-6 is the video's speculation, presented alongside confirmed facts without a change in tone. The Astra claim that it produced ten new results on long-standing open problems in mathematics and theoretical computer science comes from OpenAI's own promotional material and has not been independently assessed.

Transcript quality is poor and several names are corrupted: "Kim K3" is Kimi K3, "Ilia Saskcover" and "Sutsker" are Ilya Sutskever, "Elamarina" and "Alamarina" are LMArena, "3GS" is Three.js, "EF-16" is BF16, "Miniax" is MiniMax, "Groc" is Grok, "JLM" is GLM, and "Enthropic" is Anthropic.

## Real-World Application / Actionable Step
Do not reprioritise anything on the strength of this video. The single dated, confirmed item is Grok 4.6 on 7 August, and even there no benchmarks or pricing existed at recording time. The correct action is to wait for the Arena evaluation the week after launch and for a published active-parameter count before forming any view on where it sits on the cost-quality frontier.

The item worth actual attention is the continual-learning thesis behind the SSI rumour, independent of whether SSI ships anything. Spend an hour writing down which parts of your current deployment stack assume weights are immutable after training. Static quantization calibration, fixed pruning masks, weight-identical replicas, cached compiled kernels for a specific weight layout. That list is your exposure if continual learning becomes practical, and it is worth having before the question becomes urgent rather than after. This is cheap, it does not depend on any rumour being true, and it identifies which optimization investments are robust to that shift and which are not.

Second, run the multimodality tax experiment when GLM 5.3 lands. Compare it against a multimodal peer of similar active-parameter count on pure text and coding tasks. If the text-only specialist wins at equal or lower serving cost, that is a directly actionable routing result: default to a text specialist and escalate to multimodal only on queries with actual image or video input. Most production traffic is text, so if the tax is real the blended saving is substantial.

Third, when Ling 3.0 Flash is evaluated, check what the FP8 checkpoint actually is before using it. Vendor-supplied FP8 ranges from carefully calibrated per-channel scaling to a naive cast, and the quality difference is large. If the release does not document the method, measure it against the BF16 baseline on your own tasks rather than assuming the vendor did the work.

Related: [When Will The Benchmaxxing Plague End](2026-08-02-Benchmaxxing-Plague-Surge-AI.md) applies with unusual force here, since this video's entire content is pre-release claims with no independent measurement behind any of them.

Sources:
- [Grok 4.6 Release Date (Aug 7): What's Confirmed & Expected, OrcaRouter](https://www.orcarouter.ai/blog/grok-4-6-release-date)
- [Grok 4.6 & 4.7: Release Dates, Specs, and What xAI Is Planning, TBreak](https://tbreak.com/grok-4-6-4-7-xai-release-date-specs/)
- [Grok 4.6 Explained: 2T AI Model vs Kimi K3, 4sAPI](https://blog.4sapi.com/blog/grok-4-6-2t-ai-model-analysis)
- [SSI To Come Out With Their Model In August, Claims Gavin Baker, OfficeChai](https://officechai.com/ai/ssi-to-come-out-with-their-model-in-august-claims-gavin-baker/)
- [Safe Superintelligence Inc., Wikipedia](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.)
- [Safe Superintelligence Inc., official site](https://ssi.inc/)
- [Ilya Sutskever's SSI: The $32B Bet on a Post-Scaling Paradigm, StartupHub.ai](https://www.startuphub.ai/ai-news/ai-figures/2026/figure-ilya-sutskever-ssi-financial-breakdown-2026-06-06)
