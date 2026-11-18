---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.114327+00:00
arxiv_id: 2611.20192
url: https://huggingface.co/papers/2611.20192
arxiv_url: https://arxiv.org/abs/2611.20192
date: 2026-11-17
---

# GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis

Scene text synthesis requires stroke-accurate characters rendered in a specified layout, as well as visual coherence with the surrounding scene. To achieve this, existing methods commonly pre-render the target text at its intended locations to form a glyph image that jointly specifies layout and glyph structure. However, this representation ties the resolution of each glyph to its target region, limiting fine-grained stroke guidance for small, densely packed, or structurally complex text. To tackle this, we propose GlyphAtlas, a scene text synthesis framework that retains the glyph image as a spatial anchor and supplies fine-grained stroke references through a dedicated glyph atlas. The atlas renders and encodes each character or word in a separate cell, decoupling reference resolution from target-region size. We further introduce atlas-anchored attention, which lets each text region retrieve stroke detail only from its corresponding atlas cells to refine the coarse glyph structure provided by the glyph image. This coarse-to-fine conditioning simplifies stroke rendering while preserving explicit layout correspondence. We optimize GlyphAtlas with a mask-weighted flow matching objective and a timestep-weighted text perceptual loss for writing accuracy and background consistency. Random resolution augmentation of atlas cells supports adjustable atlas budgets at inference. Extensive experiments demonstrate that GlyphAtlas achieves stroke-accurate synthesis of small, dense, and structurally complex text, zero-shot transfer to languages unseen during task-specific training, and leading performance in scenes with many text regions. project page: https://fr0zencrane.github.io/project-glyphatlas/
