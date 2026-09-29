---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.601756+00:00
arxiv_id: 2609.23551
url: https://huggingface.co/papers/2609.23551
arxiv_url: https://arxiv.org/abs/2609.23551
date: 2026-09-28
---

# Paragraph Boundaries Are Not White Space:Compression Depth as the Signature of Hierarchical Structure

Standard positional encodings represent position as a one-dimensional reading-order coordinate, but reading order alone does not determine hierarchical textual structure. We use a hierarchical rotary positional encoding (hRoPE) that represents paragraph, sentence, and token indices as separate channels, hold the token sequence fixed, intervene on the paragraph coordinate p1, and measure cross-paragraph attention with a token-distance-exact estimator. Attention is compressed relative to a token-distance-matched baseline in every corpus, but compression alone is not diagnostic of true structure: an architecturally identical channel with density-matched random labels is compressed too, more shallowly. What distinguishes real structure is the depth of compression, which is greater and corpus-dependent while the control's is not. Comparing eight corpus-only quantities across three constructs (lexical persistence, paragraph length, embedding-based coherence), none fully reproduces the cross-corpus ordering of depth, though embedding-based coherence comes closest. Compression depth, not its location, is the reproducible signature of genuine paragraph structure in our setting.
