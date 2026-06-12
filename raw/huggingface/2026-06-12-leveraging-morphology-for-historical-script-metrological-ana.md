---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.09446
url: https://huggingface.co/papers/2606.09446
arxiv_url: https://arxiv.org/abs/2606.09446
date: 2026-06-12
---

# Leveraging Morphology for Historical Script Metrological Analysis

Advances in handwritten text recognition have enabled large-scale transcription of historical documents, but still provide limited access to interpretable visual measurements for paleography, the study of historical scripts. In this paper, our main insight is that morphological script analysis, in particular the capacity to learn character prototypes from line-level transcriptions, enables the definition of scalable, meaningful, and stable paleographic measurements. More precisely, we leverage a transformer-based detection architecture together with a prototype-based line reconstruction module to learn prototypical characters and their occurrence, deformation, and positioning.
  Our contributions are twofold. First, we introduce a deep architecture and learning methodology that enables efficient character modeling with only line-level transcription supervision, significantly improving over the Learnable Typewriter baseline and enabling accurate character bounding box prediction, unlocking its potential for paleographic measurements. Second, we introduce and demonstrate the paleographical relevance of automatic measurements enabled by our architecture for characters, bi-grams, and spaces between graphical units. For this demonstration, we extend the annotations of the codex Paris, BnF, fr. 2813, commissioned in the late fourteenth century by Charles V and copied by four hands, to 160 pages. We visualize our measurements over these pages, showing how they enable us not only to differentiate graphical profiles, but also to discover and analyze subtle variations. This case study outlines the scalability of our approach and its frugality in terms of required training data, since a single column of text is sufficient to compute our measurements on each of the 160 pages.
  Data and code are publicly available at: https://malamatenia.github.io/morphology4metrology-analysis.
