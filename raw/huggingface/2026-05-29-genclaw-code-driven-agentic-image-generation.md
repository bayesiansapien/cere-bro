---
source: farmer/huggingface
farmed: 2026-05-29T09:54:41Z
arxiv_id: 2605.30248
url: https://huggingface.co/papers/2605.30248
arxiv_url: https://arxiv.org/abs/2605.30248
date: 2026-05-29
---

# GenClaw: Code-Driven Agentic Image Generation

Image generation models have evolved from text-conditioned pixel synthesis toward multimodal agents endowed with visual comprehension and tool invocation capabilities. Yet, existing agents remain at the mercy of underlying black-box image models. Their workflow is trapped in a repetitive cycle of prompt rewriting for generation refinement, leaving them with no mechanism to directly manipulate the canvas. In essence, the potential of LLMs to serve as a genuine "brush" for precise visual construction remains largely untapped. In this paper, we propose GenClaw, a code-driven agentic image generation paradigm that empowers the agent to create like a human artist: first conceptualizing, then sketching, and finally coloring. Specifically, the agent first constructs the conceptual knowledge and context through search and reasoning. It then utilizes code (e.g., SVG, HTML, Three.js) to render executable visual sketches. Finally, it employs an image generation model to supplement textures, materials, and photorealism. In this workflow, code serves as a controllable intermediate canvas bridging linguistic reasoning and pixel synthesis, seamlessly integrating programmatic logic with the visual expressiveness of generative models. By transforming image generation from a black-box paradigm into a staged process akin to authentic human creation, GenClaw offers a step toward for highly controllable and interpretable visual generation systems.
