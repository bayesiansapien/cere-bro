---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.220415+05:30
arxiv_id: 2610.09788
url: https://huggingface.co/papers/2610.09788
arxiv_url: https://arxiv.org/abs/2610.09788
date: 2026-10-12
---

# Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression

Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the structure of rubric-guided evaluations to guide compression, LatentGRM learns compact continuous trajectories that support autonomous pairwise judgments without generating textual assessments. A separate interpreter reconstructs evaluation text from these trajectories, providing an offline view of the information retained under compression. Under matched training data and backbones, LatentGRM achieves competitive aggregate preference accuracy relative to explicit Supervised Fine-Tuning (SFT) judges at both 4B and 8B scales. Across four benchmark domains, LatentGRM-8B compresses evaluation trajectories by 8.9--9.2x and reduces total judge inference time by 6.1--7.0x at vote@5. Controlled rubric interventions show that criterion-dependent preference information is carried through the latent sequence. Together, these results demonstrate that continuous latent evaluation can substantially reduce inference cost while preserving competitive judgment quality.
