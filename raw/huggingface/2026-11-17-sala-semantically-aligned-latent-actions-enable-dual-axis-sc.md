---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.110706+00:00
arxiv_id: 2611.17110
url: https://huggingface.co/papers/2611.17110
arxiv_url: https://arxiv.org/abs/2611.17110
date: 2026-11-17
---

# SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models

Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAMs can offer greater training efficiency and potentially lower inference costs by avoiding explicit pixel prediction during policy learning and execution. However, most existing LAMs learn latent actions solely through video reconstruction, which can cause their representations to cluster by visual appearance rather than by the underlying actions. As a result, they struggle to align human actions with their robot counterparts. To bridge the gap, we introduce SALA, which emphasizes establishing the semantic correspondence for latent actions. Without requiring paired data, we use the language descriptions of unpaired human and robot clips to estimate semantic similarities and supervise cross-embodiment correspondence. Specifically, we translate these similarities into soft neighborhood structures that guide human latent actions toward semantically related robot latents, while robot action reconstruction grounds the latent space in control. The resulting shared latent action space provides a unified supervision signal for training an embodied foundation model on both human and robot videos. Notably, latent action supervision enables scaling along two axes: (1) pre-training on increasing amounts of general human video consistently reduces robot action prediction error on downstream tasks, and (2) post-training on increasing amounts of task-specific human video substantially improves real-world robot task success rates.
