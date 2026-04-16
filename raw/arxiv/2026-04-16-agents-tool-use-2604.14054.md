---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14054
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.14054
published: 2026-04-16
authors: Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong
---

# $\pi$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data

**arXiv:** https://arxiv.org/abs/2604.14054
**Authors:** Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong

## Abstract

arXiv:2604.14054v1 Announce Type: new  Abstract: Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during task generation, an intermediate artifact that captures the reverse solution process. This reveals a new source of privileged information for self-distillation: self-play can itself provide high-quality privileged context for the teacher model in a low-cost and scalable manner, without relying on human feedback or curated privileged information. Leveraging this insight, we propose Privileged Information Self-Play ($\pi$-Play), a multi-agent self-evolution framework. In $\pi$-Play, an examiner generates tasks together with their QCPs, and a teacher model leverages QCP as privileged context to densely supervise a student via self-distillation. This design transforms conventional sparse-reward self-play into a dense-feedback self-evolution loop. Extensive experiments show that data-free $\pi$-Play surpasses fully supervised search agents and improves evolutionary efficiency by 2-3$\times$ over conventional self-play.
