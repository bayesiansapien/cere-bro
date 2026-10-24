---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.876020+00:00
arxiv_id: 2610.24738
url: https://huggingface.co/papers/2610.24738
arxiv_url: https://arxiv.org/abs/2610.24738
date: 2026-10-23
---

# Editing Images into Reusable Layers via Compositional Edit-Prior Distillation

High-quality image editing requires precise modification of target regions while preserving the content of unrelated regions. Existing editing models produce flattened outputs that limit precise local manipulation and layer reuse, while decomposition methods typically optimize layer recovery separately from instruction-driven editing. To this end, we introduce LayerEditor, a unified framework that couples instruction-guided image editing with controllable generation of reusable RGBA layers. At its core, In-Context RGB-Alpha Token Modeling jointly represents the edited canvas and an ordered sequence of RGB-Alpha layers within a single token sequence, enabling semantic edits and explicit control over individual layer content. To retain the pretrained model's editing capability during adaptation to layered outputs, we propose Compositional Edit-Prior Distillation, which transfers its editing prior to both the edited canvas and the image composed from the predicted layers. To support training and evaluation, we construct LayerEditor-100K, a large-scale paired image-editing dataset with ordered RGBA layer annotations, and introduce dedicated benchmarks for layered editing. Extensive experiments demonstrate that LayerEditor maintains strong editing fidelity while generating accurate RGBA layers, supporting both flexible layer-level manipulation and multi-layer decomposition.
