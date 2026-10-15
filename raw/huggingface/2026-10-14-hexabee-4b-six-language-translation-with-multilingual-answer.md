---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.509045+00:00
arxiv_id: 2610.16361
url: https://huggingface.co/papers/2610.16361
arxiv_url: https://arxiv.org/abs/2610.16361
date: 2026-10-14
---

# HexaBee-4B: Six-Language Translation with Multilingual Answering and Bidirectional Supervision

Multilingual translation requires a model to preserve meaning while producing text in a requested language. We present HexaBee-4B, a translator adapted from Gemma 3 4B IT through three stages: Wikipedia continued pretraining, joint multilingual answering and answer-text translation, and bidirectional translation specialization. The intermediate stage connects two tasks through shared multilingual answers: answering a question in the requested language and translating an answer into that language. It comprises 19.46 million answering records, including 5.76 million cross-language question-answer pairs, and 10.70 million answer-text translations. The final stage uses 658,274 forward and reverse synthetic translation examples. On 36,572 synthetic test examples spanning all 30 directions among Arabic, Chinese, English, Hebrew, Persian, and Spanish, HexaBee-4B achieves direction-macro chrF++ of 73.75, compared with 57.11 for Gemma 3 4B IT and 66.83 for Gemma 3 12B IT. BLEU, TER, COMET, and a matched model-judged subset support the same overall ranking. These results demonstrate improved translation across the six-language set, with chrF++ gains in every evaluated direction over both baselines.
