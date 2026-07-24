---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.20379
url: https://huggingface.co/papers/2607.20379
arxiv_url: https://arxiv.org/abs/2607.20379
date: 2026-07-23
---

# Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations

Natural-language autoencoders score explanations of hidden activations by reconstruction: an explanation is deemed faithful if the activation can be regenerated from it. The test is structurally insensitive to individual false claims: if flipping a claim does not change the reconstruction, the claim is never penalized. We show the test is passed in two ways, neither faithful. On a released Qwen-2.5-7B verbalizer, explanations reconstruct well above chance while ~2% of specific claims are reconstruction-dependent, so the score tracks gist, not specific facts. Under exact synthetic ground truth, the standard recipe develops co-adapted private codes (false wording the reconstruction depends on) in 5/5 runs, and fixes that leave the target model unchanged do not help. We contribute two audit protocols, the grounded-vs-true cross and the evaluator swap, and RECAP (Readable Encodings via Co-trained Auxiliary Predictors): linear heads trained alongside the target model to keep designated content decodable. On RECAP-trained sandbox models, fresh verbalizers state the designated content truly and the codes vanish, at a +0.001-nat cost. This replicates on a pretrained Pythia-160M: the content becomes reliably probe-decodable, though a fresh verbalizer conveys it only in part (truth 0.44-0.46 vs a near-zero control). For interpretability, high reconstruction does not certify individual claims. For AI safety, RECAP makes designated internal content independently checkable against probes rather than asserted by prose a model can game: an independent probe scores the verbalizer's true claims above its false ones (AUC 0.96, vs 0.82 without RECAP). Against an adversary that edits an explanation to maximize the reconstruction score while lying (suppressing ~87% of its lie penalty), the RECAP probe still flags the lies (AUC 0.95) while the control probe collapses to chance (0.51).
