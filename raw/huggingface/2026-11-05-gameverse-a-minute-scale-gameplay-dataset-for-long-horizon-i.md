---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.299176+00:00
arxiv_id: 2610.37257
url: https://huggingface.co/papers/2610.37257
arxiv_url: https://arxiv.org/abs/2610.37257
date: 2026-11-05
---

# GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling

Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon training data. Existing gameplay video datasets typically consist of clips under ten seconds, with captions that describe whole clips in coarse and undifferentiated text, which is insufficient for controllable long-horizon generation. We address this with GameVerse, a minute-scale gameplay video dataset purpose-built for long-horizon interactive world modeling. GameVerse contains 69.7K clips spanning 1,655 hours and 349.6 million frames across diverse first- and third-person gameplay, including 1,358 hours of continuous two-minute sequences, an order of magnitude longer than prior datasets. Clips pass through a unified pipeline of scene-consistent segmentation, quality filtering, camera pose estimation, and event-based caption annotation. Each clip is paired with a temporally stable camera trajectory that remains coherent across minutes, together with captions that separate static scene context from dynamic foreground events and align to event boundaries rather than fixed time windows. Comprehensive analysis shows that GameVerse surpasses existing public datasets in scale, diversity, and annotation quality. Experiments further demonstrate that training on GameVerse substantially extends the temporal horizon of interactive world models.
