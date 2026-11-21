---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.383379+00:00
arxiv_id: 2611.25387
url: https://huggingface.co/papers/2611.25387
arxiv_url: https://arxiv.org/abs/2611.25387
date: 2026-11-20
---

# TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs

Humans act in the visual world by inferring the 3D layout behind a 2D view, predicting how an action changes it, and correcting themselves after seeing the result. Can multimodal large language models (MLLMs) do the same? CAPTCHAs offer a natural test, since humans solve them through this very loop, clicking and dragging on the screen and adjusting after each result. Yet existing CAPTCHA benchmarks are largely solved and rarely spatial, while spatial benchmarks rarely require action. We therefore present TuringSpace, a synthetic web environment of 125 interactive CAPTCHAs that span five spatial abilities and must be solved through clicks and drags on the screen. Every task is a program that generates new instances with a checker and an oracle, so the tasks also form a scalable training gym. Humans solve 94.1% of the tasks, whereas the best model, GPT-6 Astra, still fails 25.9% of them, and the best open-weight model, Kimi K3, fails 68.0%. Our further analysis shows that most failures come from misreading the screenshot, and that model reasoning rarely corrects a wrong belief but hallucinates evidence to defend it. To test whether such spatial abilities can be learned, we fine-tune Qwen3.5-9B on this gym. Its success rate rises from 1.6% to 33.1%, above Kimi K3, and it improves on all seven out-of-distribution benchmarks, including a 9.9-point gain on the real-world indoor videos of VSI-Bench. These results show that grounding spatial intelligence in screen actions exposes what MLLMs lack and offers a scalable way to teach it, with gains that transfer to real-world scenes. We will release TuringSpace to support further study.
