---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.22849
url: https://huggingface.co/papers/2608.22849
arxiv_url: https://arxiv.org/abs/2608.22849
date: 2026-08-25
upvotes: 2
authors: ["Ziyuan Wang", "Bohao Tang", "Fei Zhang", "Shuo Han", "Pengfei Liu"]
---

# RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling

**Upvotes:** 2
**Authors:** Ziyuan Wang, Bohao Tang, Fei Zhang, Shuo Han, Pengfei Liu

Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution. We present RIBOSPAN, a 1.61-billion-parameter bidirectional RNA foundation model natively pretrained with context lengths up to 10,240 nt. RIBOSPAN combines dense bidirectional self-attention, single-nucleotide tokenization, and attention-isolated sequence packing to enable high-resolution modeling of complete long RNAs. We evaluate the model through nucleotide reconstruction, a controlled long-context representation benchmark, and frozen RNA-type representation analysis. Native 10K pretraining preserves strong reconstruction at 10,240 tokens, while continued pretraining with 40% masking improves recovery under heavy corruption while preserving representation quality. The long-context benchmark further shows that native 10K models maintain strong contextual responsiveness and context-specific representation separation while keeping perturbation-induced representation changes highly localized. Inference-time YaRN scaling recovers much of the contextual organization lost by direct extrapolation of short-context models, but induces substantially greater distal representation diffusion. Frozen-representation evaluations further demonstrate state-of-the-art RNA representation quality, with RIBOSPAN achieving the strongest overall performance across diverse RNA types and retaining a clear advantage on long RNAs. Building on the same backbone, we develop a multidimensionally conditioned discrete-diffusion framework for full-length mRNA generation and redesign, including synonymous-codon diffusion for protein-preserving CDS optimization. Together, RIBOSPAN establishes a powerful long-context foundation for transferable RNA representation learning and full-transcript mRNA design.
