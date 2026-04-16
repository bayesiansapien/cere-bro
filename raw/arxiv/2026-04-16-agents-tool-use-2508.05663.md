---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2508.05663
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2508.05663
published: 2026-04-16
authors: Xingran Chen, Parimal Parag, Rohit Bhagat
---

# Random Walk Learning and the Pac-Man Attack

**arXiv:** https://arxiv.org/abs/2508.05663
**Authors:** Xingran Chen, Parimal Parag, Rohit Bhagat

## Abstract

arXiv:2508.05663v4 Announce Type: replace-cross  Abstract: Random walk (RW)-based algorithms have long been popular in distributed systems due to low overheads and scalability, with recent growing applications in decentralized learning. However, their reliance on local interactions makes them inherently vulnerable to malicious behavior. In this work, we investigate an adversarial threat that we term the ``Pac-Man'' attack, in which a malicious node probabilistically terminates any RW that visits it. This stealthy behavior gradually eliminates active RWs from the network, effectively halting the learning process without triggering failure alarms. To counter this threat, we propose the Average Crossing (AC) algorithm--a fully decentralized mechanism for duplicating RWs to prevent RW extinction in the presence of Pac-Man. Our theoretical analysis establishes that (i) the RW population remains almost surely bounded under AC and (ii) RW-based stochastic gradient descent remains convergent under AC, even in the presence of Pac-Man, with a quantifiable deviation from the true optimum. Our extensive empirical results on both synthetic and real-world datasets corroborate our theoretical findings. Furthermore, they uncover a phase transition in the extinction probability as a function of the duplication threshold. We offer theoretical insights by analyzing a simplified variant of the AC, which sheds light on the observed phase transition.
