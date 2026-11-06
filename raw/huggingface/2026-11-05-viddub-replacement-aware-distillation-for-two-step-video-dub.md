---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.304004+00:00
arxiv_id: 2611.03404
url: https://huggingface.co/papers/2611.03404
arxiv_url: https://arxiv.org/abs/2611.03404
date: 2026-11-05
---

# VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing

Video dubbing aims to synthesize lip movements that match target speech while preserving the speaker identity, head pose, and background of a source video. Existing editors are predominantly trained via self-reconstruction under original paired audio, even though the source mouth becomes a conflicting target when driving speech is replaced. We introduce replacement-aware cross-audio supervision: paired-audio samples use full-frame reconstruction, whereas unpaired replacement-audio samples mask out source-mouth reconstruction losses and supervise the mouth solely through audio-visual synchronization while preserving unmasked facial regions and background. Because offline dubbing provides the complete source video and target speech beforehand, we present VidDub, a full-context diffusion editor distilled into two denoising steps (2 NFE). Our replacement-aware teacher first learns accurate lip synchronization without regressing toward conflicting source mouth movements. Matched trajectory regression then transfers the teacher's CFG-guided trajectories to a two-step student, and distribution matching distillation recovers visual quality after step compression. We will release the curated training dataset, VidDub-Bench, fixed paired- and cross-audio evaluation manifests, preprocessing outputs, and unified evaluation code. Across three training seeds, masking out conflicting source-mouth reconstruction improves cross-audio Sync-C by 0.833; the final two-step model combines strong lip synchronization with superior visual quality, identity preservation, and visual speech recognition across four benchmarks.
