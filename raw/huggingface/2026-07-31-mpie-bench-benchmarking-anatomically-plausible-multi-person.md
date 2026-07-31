---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.27616
url: https://huggingface.co/papers/2607.27616
arxiv_url: https://arxiv.org/abs/2607.27616
date: 2026-07-31
---

# MPIE-Bench: Benchmarking Anatomically Plausible Multi-Person Interaction Editing

Text-to-image and personalized editing models now synthesize high-fidelity single-subject images with ease. Yet placing multiple named people into shared contact actions such as embrace, carry, or grapple still exposes major failures: fused limbs, invented extremities, and interpenetrating bodies. Existing evaluations largely overlook these anatomical and geometric issues, and VLM-as-a-judge checklists often saturate on Interaction while the errors remain obvious to humans. We introduce MPIE-Bench, a 2,500-sample benchmark of video-mined editing triplets spanning 405 scenes, 14 interaction categories, and four contact densities (C0-C3). We also propose MPIE-Eval, whose two new axes score contact-time geometry from a frozen public multi-person mesh reconstruction. Anatomy asks whether every human-like mass is explained by a complete set of reconstructed bodies, and Interaction asks whether the penetration and surface distance between those bodies match the contact the instruction asked for. Across ten editors, mesh Anatomy tops out at 0.65 and mesh Interaction at 0.72 on two different models, so no single editor is strong on both, while VLM checklists rate the same images above 0.95. A five-rater study confirms that both axes track human judgement more closely than a zero-shot VLM judge, and the rankings hold under ablation of every weight and threshold.
