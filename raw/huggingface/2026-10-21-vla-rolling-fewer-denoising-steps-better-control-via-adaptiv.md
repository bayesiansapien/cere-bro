---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.639571
arxiv_id: 2610.25043
url: https://huggingface.co/papers/2610.25043
arxiv_url: https://arxiv.org/abs/2610.25043
date: 2026-10-21
---

# VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse

Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, and the next chunk is regenerated from fresh noise. We show that this discarded tail retains transferable denoising progress: action-tail initialization can match or outperform a native 10-step Gaussian baseline using fewer denoising steps. However, the optimal denoising budget varies substantially across samples, indicating that tail reuse should be adapted to the updated environment. Based on this observation, we introduce VLA-Rolling, a lightweight inference framework that reuses action tails through three stages: action-tail inheritance, per-action confidence estimation, and confidence-guided refinement through renoising and denoising budget allocation, while the underlying VLA remains frozen. Across π_{0.5}, SmolVLA, X-VLA, and MolmoAct2 on LIBERO, MetaWorld, LIBERO-Plus, and RoboTwin 2.0, VLA-Rolling reduces action-chunk inference cost in all 16 model--benchmark pairs, achieving up to a 1.48times speedup, while improving success rate in 14 pairs by up to 15.08 percentage points. These results show that action tails are not merely discarded predictions, but reusable intermediate states that enable more efficient and accurate VLA inference. These results demonstrate that the action tail can support the generation of better actions with fewer denoising steps. Our project is available at https://chenbao123ww.github.io/VLA-Rolling/.
