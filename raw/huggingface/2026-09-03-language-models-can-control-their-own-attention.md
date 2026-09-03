---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.02737
url: https://huggingface.co/papers/2609.02737
arxiv_url: https://arxiv.org/abs/2609.02737
date: 2026-09-03
---

# Language Models Can Control Their Own Attention

Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach mitigates this cost by pre-selecting relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motivated by the simple question: wouldn't the model already know which parts of the context are relevant? To this end, we introduce Declarative Attention (DA), a protocol that elicits the model to declare where it needs to attend within its chain-of-thought, partitioning generation into three modes: <global> (full context), <focus> (a specific region), and <local> (recent output only). The inference engine parses these declarations like tool calls and skips most of the KV cache read. Under zero-shot evaluation across 15 long-context tasks, DA on off-the-shelf models (Gemma-4-31B, Qwen-3.6-27B) significantly reduces total attended tokens during decoding (52.0%, 31.1%) with modest accuracy drops (1.27pp, 2.75pp) that shrink with model scale. DA unlocks a new axis of sparse attention, with further potential under training-based methods that future work can explore.
