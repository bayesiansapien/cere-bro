---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.14589
url: https://huggingface.co/papers/2605.14589
arxiv_url: https://arxiv.org/abs/2605.14589
date: 2026-05-19
---

# EndPrompt: Efficient Long-Context Extension via Terminal Anchoring

Extending the context window of large language models typically requires training on sequences at the target length, incurring quadratic memory and computational costs that make long-context adaptation expensive and difficult to reproduce. We propose EndPrompt, a method that achieves effective context extension using only short training sequences. The core insight is that exposing a model to long-range relative positional distances does not require constructing full-length inputs: we preserve the original short context as an intact first segment and append a brief terminal prompt as a second segment, assigning it positional indices near the target context length. This two-segment construction introduces both local and long-range relative distances within a short physical sequence while maintaining the semantic continuity of the training text--a property absent in chunk-based simulation approaches that split contiguous context. We provide a theoretical analysis grounded in Rotary Position Embedding and the Bernstein inequality, showing that position interpolation induces a rigorous smoothness constraint over the attention function, with shared Transformer parameters further suppressing unstable extrapolation to unobserved intermediate distances. Applied to LLaMA-family models extending the context window from 8K to 64K, EndPrompt achieves an average RULER score of 76.03 and the highest average on LongBench, surpassing LCEG (72.24), LongLoRA (72.95), and full-length fine-tuning (69.23) while requiring substantially less computation. These results demonstrate that long-context generalization can be induced from sparse positional supervision, challenging the prevailing assumption that dense long-sequence training is necessary for reliable context-window extension. The code is available at https://github.com/clx1415926/EndPrompt.
