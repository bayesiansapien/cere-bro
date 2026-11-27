---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.909990+00:00
arxiv_id: 2611.33894
url: https://huggingface.co/papers/2611.33894
arxiv_url: https://arxiv.org/abs/2611.33894
date: 2026-11-26
---

# SIA: Selective Image Analogy

Image analogy transfers a demonstrated transformation from a before/after pair (A, A') to a new query image B. Existing methods assume all changes in (A, A') should be fully transferred, limiting flexibility when users want only a subset of the demonstrated edits. We introduce Selective Image Analogy (SIA), a new setting where a single demonstration pair encodes multiple edits, and the user selects at inference time which edits to apply to B. To support this, we curate a multi-edit analogy dataset with full-edit and partial-edit targets. We then train a model that first learns to transfer the complete demonstrated transformation, and then gains selective control through a mask-aligned suppression mechanism: a token-gated LoRA that restricts adapter updates to suppressed edit tokens during denoising, paired with a concept suppression vector that weakens the selected tokens in the text embeddings before denoising. Together, these components allow SIA to suppress unwanted edits that remain visible in A', while preserving the user-selected ones, all without requiring a new demonstration pair for each edit combination. We perform extensive quantitative and qualitative evaluations along with user studies to demonstrate the efficacy of our approach.
