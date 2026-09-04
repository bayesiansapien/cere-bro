---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.04034
url: https://huggingface.co/papers/2609.04034
arxiv_url: https://arxiv.org/abs/2609.04034
date: 2026-09-04
---

# Editable Visual Design

While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets.
  To address this, we propose Editable Visual Design, a new paradigm driven by a Coding Agent. We designate the VLM as the ``creative brain'' for requirement comprehension, task planning, and aesthetic judgment, while utilizing the image generation model as an on-demand ``visual world simulator'' to synthesize standalone visual assets. Operating under an ``imagine first, then act'' closed-loop workflow, the agent generates isolated assets, writes native HTML/CSS, and iteratively refines the design against visual rendering feedback.
  Furthermore, Agent Design Replay faithfully reproduces the creative and reasoning trajectory akin to that of professional human designers. Ultimately, the system delivers editable artifacts with decoupled layers and real text, enabling users to perform intuitive mouse dragging and layout adjustments on a graphical user interface. Validations on posters, infographics, and other scenarios show that this paradigm successfully achieves both refined aesthetics and production-grade editability.
