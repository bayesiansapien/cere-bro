---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.19025
url: https://huggingface.co/papers/2610.19025
arxiv_url: https://arxiv.org/abs/2610.19025
date: 2026-10-27
---

# How Far Can Coding Agents Go in Visual Generation?

Modern image generation largely relies on specialized generative models that leave the process of image construction implicit in learned parameters. We explore an alternative: general-purpose coding agents that construct images through executable programs. Our study of zero-shot drawing on AgentDrawBench, a 200-prompt benchmark, reveals a distinctive capability profile. Agents excel at preserving structure and satisfying precise visual constraints, achieving competitive results in domains where compositional accuracy matters more than photorealistic appearance, while remaining limited in perceptual richness. Their visual expressiveness varies with the drawing interface, and a qualitative study on reconstruction shows how procedural skills extracted from human demonstrations support different artistic media. We then examine code as an external visual language of thought: a structured, executable representation that agents can construct and inspect. We test it in visual question answering task and find reconstructed visual code retains substantial information for question answering and, in some domains, supports higher accuracy than the original image. These abilities raise a further question: do agents draw on a shared internal representation of scene content beyond a particular drawing program? We explore an internal visual language-of-thought hypothesis, in which a shared, compositionally structured representation supports visual operations across drawing languages. Cross-harness drawings and images assembled from independent single-pixel queries exhibit related layouts and tones. Agents also maintain self-generated room arrangements across viewpoints after visible drawings are removed. These results demonstrate that the coding agent would maintain a consistent and coherent world inside its imagine even before the harness gets involved and the generation starts.
