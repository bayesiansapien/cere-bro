---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.301787+00:00
arxiv_id: 2611.04391
url: https://huggingface.co/papers/2611.04391
arxiv_url: https://arxiv.org/abs/2611.04391
date: 2026-11-05
---

# Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on robot data. We introduce H2RB (Human-To-Robot Bridge), a human-robot co-training framework for adapting pretrained VLA policies from unpaired human and robot demonstrations. H2RB bridges the embodiment gap at both interfaces: geometry-anchored alignment grounds human and robot observations in a compatible representation, while a decoupled-decoder tokenizer shares action latents without forcing both domains through a single action mapping. This design allows human demonstrations to provide useful behavioral supervision while retaining the rich visual, semantic, and control priors of the pretrained VLA. Across real-world tasks, H2RB substantially improves object transfer performance from 8.0 to 51.8 and enables skill transfer to score 62.7, in settings where co-train baselines totally fail to transfer human-demonstrated skills. The benefit also persists under object-placement shifts, improving out-of-distribution transfer from 6.0 to 45.3. H2RB suggests a way for human demonstrations to serve as a scalable supervision source for adapting pretrained robotic policies, reducing the dependence on costly target-robot data collection.
