---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.26081
url: https://huggingface.co/papers/2610.26081
arxiv_url: https://arxiv.org/abs/2610.26081
date: 2026-10-20
---

# DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal

Video overlay removal aims to recover scenes obscured by subtitles, titles, and logos while preserving surrounding content. Existing methods use temporal propagation or source-conditioned generation, but can leave residual overlays and distort scene structure when useful source information is obscured. We propose DeOverlay, a source-anchored flow model that reconstructs the clean video from the source latent with fixed source guidance. Specifically, we train a shared velocity network along paired source-to-clean paths using region-weighted flow matching, enabling successive cor- rections from intermediate states. To select local source cues, we develop visibility-normalized temporal aggregation that excludes masked positions and averages the remaining observations. Global source context and edit-region embeddings complement these cues through additive condi- tioning, retaining a single video-token sequence. To evaluate scene recovery across diverse overlay conditions, we introduce DVTE-Bench, comprising 1,631 paired videos across eight text-overlay categories, with OCR-screened clean targets, frame-aligned pixel masks, and a common evaluation protocol. Experiments on the complete release show that DeOverlay outperforms four baselines on all five reconstruction and perceptual metrics, reducing Mask LPIPS and Mask VFID by 58.3% and 70.3%, respectively, relative to the strongest evaluated baseline. Additional qualitative examples demonstrate the removal of graphic logos and stickers. We will make the complete benchmark, evaluation code, and test outputs availabl. Project page:https://yahooo-m.github.io/DVTE-Bench/
