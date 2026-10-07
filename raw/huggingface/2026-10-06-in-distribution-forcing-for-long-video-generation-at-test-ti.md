---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.03120
url: https://huggingface.co/papers/2610.03120
arxiv_url: https://arxiv.org/abs/2610.03120
date: 2026-10-06
---

# In-Distribution Forcing for Long Video Generation at Test Time

Modern autoregressive (AR) video diffusion models excel at short-horizon video generation, yet generating long videos remains challenging due to drifting, where colors and textures shift, and motion dynamics decay. Existing works primarily rely on KV conditioning, which selects or modifies cached key-value (KV) entries to mitigate drifting. However, we observe that KV conditioning alone is insufficient as it assumes cached KV entries remain in-distribution. This assumption fails beyond the training horizon: nothing constrains the construction of KV entries during rollout, giving rise to the KV-provenance problem where cached entries themselves become out-of-distribution (OOD). To address this, we propose In-Distribution Forcing (ID-Forcing), a test-time framework that aligns both KV caching and KV conditioning with training configurations. Its key mechanism, self-caching, prevents OOD KV entries at their source. Each chunk is cached without attending to prior KV entry, keeping the rolling window exactly in-distribution. Consequently, ID-Forcing seamlessly extends short-horizon models to minute-scale video generation. Extensive evaluations show that our method remains competitive on standard video generation benchmark while substantially outperforming prior work in mitigating drifting, as validated by both our drift metrics and a user study.
