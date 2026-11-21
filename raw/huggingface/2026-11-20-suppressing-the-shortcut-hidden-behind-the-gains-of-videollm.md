---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.390502+00:00
arxiv_id: 2611.25776
url: https://huggingface.co/papers/2611.25776
arxiv_url: https://arxiv.org/abs/2611.25776
date: 2026-11-20
---

# Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning

Supervised fine-tuning (SFT) is the stage in which Video Large Language Models (VideoLLMs) advance their capability to reason over video. However, the VideoLLM also learns to answer from textual regularities of its training data, a shortcut that bypasses the video. The regularities behind the shortcut are hard to define at the data level, and the shortcut forms regardless of training epoch, data size, or backbone. The shortcut is hidden behind a rise in accuracy within the training distribution, yet it is not required for the rise and even costs SFT the gain the video offers under distribution shift. We therefore propose Video-Evidence Training via Orthogonal projection (VETO), which intervenes on the fine-tuning update where the shortcut is written rather than on the data. VETO calibrates the subspace that the text alone occupies in the activations of the base model and projects the update onto its orthogonal complement. The VideoLLM is thus left to ground its answer in the full input, with the shortcut suppressed as it forms and never defined. Across seven VideoLLMs, VETO preserves the gain of SFT on the training distribution and suppresses the shortcut. On six benchmarks under shift it gains more than SFT and answers from the full input rather than the shortcut. Code is available at https://github.com/Youngwoo-git/VETO.
