---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.35450
url: https://huggingface.co/papers/2610.35450
arxiv_url: https://arxiv.org/abs/2610.35450
date: 2026-10-27
---

# OBB-PBD: Extending Parallel Box Decoding to Oriented Bounding Boxes for Referring Expression Grounding in Aerial Imagery

Referring expression grounding in overhead imagery requires oriented bounding boxes rather than horizontal ones, since aerial objects appear at arbitrary orientations. Most grounding models emit box coordinates sequentially; Parallel Box Decoding (PBD) instead predicts all geometry slots in one forward pass, but only for four-coordinate horizontal boxes. We extend this block-aligned interface to a six-slot oriented representation using a double-angle parameterization. Rather than assuming correctness from a decreasing loss curve, we verify the extension with image/prompt-shuffle controls and visibility/leakage probes, which show that the corrected model depends on both the image and the prompt rather than on prompt statistics alone. On the aerial vehicle visual grounding (AVVG) benchmark, whose targets are genuinely oriented, the extended model improves rotated intersection over union (rotIoU) from 0.1253 for the zero-shot baseline to 0.303 +/- 0.012 (mean +/- standard deviation over three training seeds) across the complete 6139-record test split spanning all 120 images. Learning oriented boxes rather than their axis-aligned envelopes adds 0.055 +/- 0.008 rotIoU beyond a matched control (per-seed 95% confidence intervals all excluding zero), whereas block expansion alone yields no rotIoU gain distinguishable from zero.
