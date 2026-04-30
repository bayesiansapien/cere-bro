---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.26186
url: https://huggingface.co/papers/2604.26186
arxiv_url: https://arxiv.org/abs/2604.26186
date: 2026-04-30
---

# FASH-iCNN: Making Editorial Fashion Identity Inspectable Through Multimodal CNN Probing

**Authors:** Ryan A. Rossi, Franck Dernoncourt (Adobe Research)

Fashion AI systems routinely encode the aesthetic logic of specific houses, editors, and historical moments without disclosing it. We present FASH-iCNN, a multimodal system trained on 87,547 Vogue runway images across 15 fashion houses spanning 1991–2024 that makes this cultural logic inspectable. Given a photograph of a garment, the system recovers which house produced it, which era it belongs to, and which color tradition it reflects. A clothing-only model identifies the fashion house at 78.2% top-1 across 14 houses, the decade at 88.6% top-1, and the specific year at 58.3% top-1 across 34 years with a mean error of just 2.2 years. Probing which visual channels carry this signal reveals a sharp dissociation: removing color costs only 10.6pp of house identity accuracy, while removing texture costs 37.6pp, establishing texture and luminance as the primary carriers of editorial identity. FASH-iCNN treats editorial culture as the signal rather than background noise, identifying which houses, eras, and color traditions shaped each output so that users can see not just what the system predicts but which houses, editors, and historical moments are encoded in that prediction.

## Key findings

- **Dataset**: 87,547 Vogue runway images, 15 houses, 1991–2024; training on clothing crops extracted via SegFormer.
- **House identity**: 78.2% top-1 from clothing crop alone (8.5x majority baseline); texture/luminance are primary carriers (removing color costs only 10.6pp; removing texture costs 37.6pp).
- **Temporal identity**: 88.6% decade accuracy; 58.3% year accuracy across 34 years; mean error 2.2 years.
- **Face modality**: Adds negligible signal when garment is full-color (-0.6pp), but +20.8pp on silhouette input — contribution is inversely proportional to garment information richness.
- **Hierarchical color pipeline**: Berlin-Kay (9 classes) → CSS named colors → constrained LAB regression; reduces perceptual error from ΔE₀₀=15.0 to 9.10 (39% improvement).
- **Multi-slot palette prediction**: Remains an open problem — secondary palette slots (c2–c6) are largely uncorrelated with the dominant color signal.
