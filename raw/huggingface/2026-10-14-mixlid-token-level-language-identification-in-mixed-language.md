---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.511550+00:00
arxiv_id: 2610.16601
url: https://huggingface.co/papers/2610.16601
arxiv_url: https://arxiv.org/abs/2610.16601
date: 2026-10-14
---

# MixLID: Token-Level Language Identification in Mixed-Language Text

Processing multilingual text requires both identifying a broad range of languages and distinguishing the language of each token in inputs containing multiple languages. We introduce MixLID, a token-level language identification model supporting 111 language-script combinations. MixLID follows a two-stage training process: it first learns to distinguish individual languages using the language labels of monolingual examples, then continues training on mixed-language data. The second stage uses concatenated examples from existing code-switching data alongside augmented examples created through word substitution based on correspondences between English source words and loanwords. For monolingual identification, MixLID outperforms all baselines in both accuracy and macro F1 on four benchmarks within the language coverage shared with each baseline. For mixed-language identification, it outperforms the baselines in identifying the language of individual tokens on every evaluated language pair. MixLID achieves high performance across a broad range of languages in both monolingual and mixed-language settings. The model is publicly available at https://huggingface.co/nlpai-lab/MixLID.
