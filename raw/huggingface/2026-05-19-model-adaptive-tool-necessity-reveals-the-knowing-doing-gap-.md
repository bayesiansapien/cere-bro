---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.14038
url: https://huggingface.co/papers/2605.14038
arxiv_url: https://arxiv.org/abs/2605.14038
date: 2026-05-19
---

# Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use

Large language models (LLMs) increasingly act as autonomous agents that must decide when to answer directly vs. when to invoke external tools. Prior work studying adaptive tool use has largely treated tool necessity as a model-agnostic property, annotated by human or LLM judge, and mostly cover cases where the answer is obvious (e.g., fetching the weather vs. paraphrasing text). However, tool necessity in the wild is more nuanced due to the divergence of capability boundaries across models: a problem solvable by a strong model on its own may still require tools for a weaker one. In this work, we introduce a model-adaptive definition of tool-necessity, grounded in each model's empirical performance. Following this definition, we compare the necessity against observed tool-call behavior across four models on arithmetic and factual QA dataset, and find substantial mismatches of 26.5-54.0% and 30.8-41.8%, respectively. To diagnose the failure, we decompose tool use into two stages: an internal cognition stage that reflects whether a model believes a tool is necessary, and an execution stage that determines whether the model actually makes a tool-call action. By probing the LLM hidden states, we find that both signals are often linearly decodable, yet their probe directions become nearly orthogonal in the late-layer, last-token regime that drives the next-token action. By tracing the trajectory of samples in the two-stage process, we further discover that the majority of mismatch is concentrated in the cognition-to-action transition, not in cognition itself. These results reveal a knowing-doing gap in LLM tool-use: improving tool-use reliability requires not only better recognition of when tools are needed, but also better translation of that recognition into action.
