---
source: farmer/huggingface
farmed: 2026-09-23T05:53:04.588715+00:00
arxiv_id: 2609.24058
url: https://huggingface.co/papers/2609.24058
arxiv_url: https://arxiv.org/abs/2609.24058
date: 2026-09-23
---

# All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts

Multilingual scene text recognition (STR) remains challenging due to the scarcity of training data for most languages and the difficulty of serving diverse scripts within a single model. Existing solutions either deploy one recognizer per language, inflating cost and introducing error accumulation, or rely on massive vision-language models (VLMs) that are expensive and still inaccurate on many scripts. In this work, we pursue an all-in-one multilingual recognizer that is simpler than per-language experts, lighter than VLMs, and more accurate than both. First, we construct TextMuSS-10M, a large-scale synthetic scene text dataset spanning 10 scripts and 229 languages. It provides balanced and sufficient supervision where real data is unavailable. Second, we propose ScriptMoE, a script-aware Mixture-of-Experts (MoE) architecture. It shares a single visual encoder and replaces the dense decoder with a sparse MoE block, which consists of an image-level router dispatches each image to the top-2 script-aligned experts and a shared expert absorbs cross-script knowledge. Extensive experiments on our assembled TextMuSS-Bench (10 scripts, 10,899 images) show that ScriptMoE achieves the highest accuracy of 82.06%, outperforming the strongest STR baseline by 1.31%. On the CC-OCR end-to-end multilingual task, replacing only the recognizer in PP-OCRv5 with ScriptMoE lifts F1 score from 65.71% to 80.89%, slightly surpassing the best VLM (80.73%) at a fraction of the parameter count.
