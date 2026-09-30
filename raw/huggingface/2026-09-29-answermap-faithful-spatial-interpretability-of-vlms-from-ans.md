---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935242+00:00
arxiv_id: 2609.35247
url: https://huggingface.co/papers/2609.35247
arxiv_url: https://arxiv.org/abs/2609.35247
date: 2026-09-29
---

# AnswerMap: Faithful Spatial Interpretability of VLMs from Answer Posteriors

When a VLM answers a visual query, current interpretability tools rely on text rationales, which use a mismatched modality, or on internal read-outs, which originate too early to reflect the final output and require white-box access to the model. We introduce AnswerMap, a training-free, task-agnostic, black-box visual rationale constructed from the output head. The image is cut into K row and K column bands, each shown alone to the frozen model along with the query in the format of a yes/no relevance question. The outer product of the row and column ``yes'' posteriors gives the query-conditioned spatial map. Crucially, by defining a fixed read-out R (e.g., expectation, maximum) on top of AnswerMap, we can derive continuous outputs like location natively. This bypasses the reliance on discrete text tokens for continuous-output tasks and guarantees an image-dependent answer by construction. However, a rationale can be confabulated, so we validate AnswerMap across four models and three query distributions with two tests: (a) agreement with the model's own generated point and (b) deletion of the map's region. The map lands where the model points (AUC 0.85 against 0.38 for attention), and deleting its region flips 53% of correct answers (against 19% for attention's). Beyond establishing faithfulness, we demonstrate the map's task-agnostic utility through three distinct read-outs: its maximum flags hallucinated objects without generation, its expectation localizes correctly when the model's own pointing fails, and its top-mass region, fed back as a crop, fixes half of the model's wrong answers. AnswerMap thus offers a new lens on VLM interpretability and, through its read-outs, a new output interface for visual tasks beyond text tokens.
