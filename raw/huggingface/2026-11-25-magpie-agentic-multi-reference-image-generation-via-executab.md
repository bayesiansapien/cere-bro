---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32462
url: https://huggingface.co/papers/2611.32462
arxiv_url: https://arxiv.org/abs/2611.32462
date: 2026-11-25
---

# MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction

Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the intended scene remains challenging. Although existing methods provide various forms of compositional guidance, the planned relationships are not always explicitly instantiated for inspection and refinement before image synthesis. To address this limitation, we introduce MAGPIE, which represents the intended composition as a simplified 3D scene defined by an executable Blender program. A coding agent links each scene instance to its reference, checks the geometry and rendered view against the instruction, and revises the program to correct discrepancies. The final proxy rendering serves as a visual plan for the image generator. Using MAGPIE-Instruct-3K, we train the generator to follow this plan while drawing each subject's appearance from its reference. MAGPIE improves both Qwen and FLUX on DreamOmni2 and SconeEval. With FLUX, it improves overall success on DreamOmni2 by 28.21 percentage points over the original backbone and achieves the highest overall score among the models evaluated on SconeEval.
