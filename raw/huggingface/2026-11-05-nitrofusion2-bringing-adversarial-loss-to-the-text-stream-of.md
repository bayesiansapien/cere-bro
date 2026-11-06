---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.304980+00:00
arxiv_id: 2611.05648
url: https://huggingface.co/papers/2611.05648
arxiv_url: https://arxiv.org/abs/2611.05648
date: 2026-11-05
---

# NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers

Adversarial diffusion distillation has conventionally relied on image features for discrimination. We revisit this choice for multimodal diffusion transformers (MMDiTs), whose text stream becomes image-dependent through joint attention. We introduce Text-Stream Adversarial Distillation (TSAD), which exploits intermediate text-token states as a new adversarial representation. Because the text stream has already read the image while remaining tied to the text condition, changing that condition changes what information it extracts from the image. Building on this property, we introduce Aspect-Cued Discrimination (ACD), which conditions the discriminator on different aspects of the sample, such as typography, objects, or style, to steer which properties are emphasized during adversarial training. Building on the expert-discriminator design of NitroFusion, we integrate TSAD and ACD in NitroFusion2. NitroFusion2 brings few-step distillation from the conventional 4-8-step regime down to just 1-2 steps at comparable quality. At one step, it produces sharp rendered text and rich fine-grained details, making one-step generation practical rather than merely a stress test for distillation. At two steps, it remains competitive across the evaluated benchmarks. These results establish the MMDiT text stream as a powerful and steerable representation for adversarial diffusion distillation.
