---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.230209+05:30
arxiv_id: 2610.19551
url: https://huggingface.co/papers/2610.19551
arxiv_url: https://arxiv.org/abs/2610.19551
date: 2026-10-15
---

# TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering

Text-to-image models increasingly generate readable Chinese text that still contains local rendering defects, such as a character with an extra or missing stroke or a malformed component. Such errors are invisible to OCR and vision-language models, which are trained for recognition and are therefore invariant to the very structural deviations that define a rendering error. We formalize text rendering verification as a target-conditioned problem: given a target character and an image crop, decide whether the crop is a correct rendering of that character. Our verifier TEXTVERIFIER feeds the text tower a character's Ideographic Description Sequence (IDS) rather than a single-character symbol, and is trained on 12.7M crop-IDS pairs plus label-free "same-character, different-quality" hard pairs sampled from the training trajectory of a text-region inpainting model. To evaluate this ability we build TEXTRENDERBENCH-ZH, the first per-character benchmark for generated Chinese text, annotating position, identity, and correctness for 7,358 characters. TEXTVERIFIER reaches an F1 of 0.844, far above OCR confidence (0.526), a general VLM (0.329), and TextPecker (0.590). Used as a per-character reward for Flow-GRPO post-training, it further reduces rendering errors, showing that its score can both detect and correct errors.
