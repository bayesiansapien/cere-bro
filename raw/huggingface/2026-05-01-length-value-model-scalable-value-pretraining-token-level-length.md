---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.27039"
url: https://huggingface.co/papers/2604.27039
arxiv_url: https://arxiv.org/abs/2604.27039
date: 2026-05-01
---

# Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling

Token serves as the fundamental unit of computation in modern autoregressive models, and generation length directly influences both inference cost and reasoning performance. Despite its importance, existing approaches lack fine-grained length modeling, operating primarily at the coarse-grained sequence level. We introduce the Length Value Model (LenVM), a token-level framework that models the remaining generation length. By formulating length modeling as a value estimation problem and assigning a constant negative reward to each generated token, LenVM predicts a bounded, discounted return that serves as a monotone proxy for the remaining generation horizon. This formulation yields supervision that is annotation-free, dense, unbiased, and scalable. Experiments on LLMs and VLMs demonstrate LenVM provides a highly effective signal at inference time. On the LIFEBench exact length matching task, applying LenVM to a 7B model improves the length score from 30.9 to 64.8, significantly outperforming frontier closed-source models. Furthermore, LenVM enables continuous control over the trade off between performance and efficiency. On GSM8K at a budget of 200 tokens, LenVM maintains 63% accuracy compared to 6 percent for token budget baseline. It also accurately predicts total generation length from the prompt boundary. Finally, LenVM's token-level values offer an interpretable view of generation dynamics, revealing how specific tokens shift reasoning toward shorter or longer regimes. Results demonstrate that LenVM supports a broad range of applications and token length can be effectively modeled as a token-level value signal, highlighting the potential of LenVM as a general framework for length modeling and as a length-specific value signal that could support future RL training.
