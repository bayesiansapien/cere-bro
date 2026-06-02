---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.28132
url: https://huggingface.co/papers/2605.28132
arxiv_url: https://arxiv.org/abs/2605.28132
date: 2026-06-02
---

# Which Pretraining Paradigm Better Serves Spatial Intelligence? An Empirical Comparison of Vision-Language and Video Generation Models

Spatial intelligence requires visual representations that capture both semantic objects and geometric structure in the physical world. To support this, two major pre-training schemes are now widely used as foundation backbones: Vision-Language Models (VLMs), which use language supervision to align visual observations with semantic concepts, and Video Generation Models (VGMs), which learn from temporally evolving visual worlds. However, it still remains unclear which pre-training scheme provides a better representation substrate for spatial intelligence. In this paper, we present the first systematic frozen-feature probing study of VLMs and VGMs across three representative axes of spatial intelligence: semantic tagging, instance grouping, and 3D geometry prediction. Using the lightweight probe, our framework enables a controlled comparison of what information is already encoded in frozen representations from two model families. Experimental results reveal a clear complementarity: VLMs are stronger at semantic tagging and instance grouping, while VGMs provide more accessible signals for dense geometry and camera motion. Moreover, a naive fusion of the two already yields a representation that excels at both geometry and semantics, suggesting a promising direction for building stronger spatial-intelligence backbones by effectively integrating features from both model families. Our code is available at https://github.com/om-ai-lab/Probing-VLM-VGM{https://github.com/om-ai-lab/Probing-VLM-VGM}.
