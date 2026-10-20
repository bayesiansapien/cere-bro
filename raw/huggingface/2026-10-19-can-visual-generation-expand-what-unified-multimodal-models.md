---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.21459
url: https://huggingface.co/papers/2610.21459
arxiv_url: https://arxiv.org/abs/2610.21459
date: 2026-10-19
---

# Can Visual Generation Expand What Unified Multimodal Models Know?

Unified multimodal models (UMMs) receive image-generation supervision that exposes them to visual information not fully documented in text. Can learning to generate images expand what pretrained models know? We introduce Knowledge Transfer Probing (KTP), a controlled protocol that supplies new knowledge through image-generation training and tests its accessibility through text-only question answering. Across seven knowledge categories and three UMMs, we observe direct but uneven transfer from visual supervision to language. Motivated by these observations, we successively introduce Textual Alignment and Interleaved Image--Text Alignment, which connect generation and answering through shared knowledge and interleaved responses, respectively. Guidance on selected entities can improve knowledge access on other entities without QA supervision, with additional gains from interleaved alignment. Further analysis shows that knowledge correctly reproduced in images is often more accessible through text, although substantial gaps remain between the two forms of access. These findings support visual generation as a source of knowledge beyond textual supervision, and motivate joint investigation of training data design and model architecture to make this knowledge more broadly accessible.
