---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13291
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13291
published: 2026-04-16
authors: Harun Ur Rashid, Mingxin Li, Aleksandra Pachalieva
---

# Physics-informed reservoir characterization from bulk and extreme pressure events with a differentiable simulator

**arXiv:** https://arxiv.org/abs/2604.13291
**Authors:** Harun Ur Rashid, Mingxin Li, Aleksandra Pachalieva

## Abstract

arXiv:2604.13291v1 Announce Type: new  Abstract: Accurate characterization of subsurface heterogeneity is challenging but essential for applications such as reservoir pressure management, geothermal energy extraction and CO$_2$, H$_2$, and wastewater injection operations. This challenge becomes especially acute in extreme pressure events, which are rarely observed but can strongly affect operational risk. Traditional history matching and inversion techniques rely on expensive full-physics simulations, making it infeasible to handle uncertainty and extreme events at scale. Purely data-driven models often struggle to maintain physics consistency when dealing with sparse observations, complex geology, and extreme events. To overcome these limitations, we introduce a physics-informed machine learning method that embeds a differentiable subsurface flow simulator directly into neural network training. The network infers heterogeneous permeability fields from limited pressure observations, while training minimizes both permeability and pressure losses through the simulator, enforcing physical consistency. Because the simulator is used only during training, inference remains fast once the model is learned. In an initial test, the proposed method reduces the pressure inference error by half compared with a purely data-driven approach. We then extend the test over eight distinct data scenarios, and in every case, our method produces significantly lower pressure inference errors than the purely data-driven model. We also evaluate our method on extreme events, which represent high-consequence data in the tail of the sample distribution. Similar to the bulk distribution, the physics-informed model maintains higher pressure inference accuracy in the extreme event regimes. Overall, the proposed method enables rapid, physics-consistent subsurface inversion for real-time reservoir characterization and risk-aware decision-making.
