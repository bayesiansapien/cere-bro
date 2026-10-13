---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.223544+05:30
arxiv_id: 2610.07207
url: https://huggingface.co/papers/2610.07207
arxiv_url: https://arxiv.org/abs/2610.07207
date: 2026-10-12
---

# Distributionally Robust Mixture-of-Experts Training

Mixture-of-Experts (MoE) transformers scale capacity by activating only a few experts per token, but this sparsity creates a hidden reliability problem: when routing is imperfect, load-balanced models may send tokens to experts that are insufficiently trained for the assigned inputs. We propose Distributionally Robust MoE Training (DRMoET), a drop-in objective that treats layer-wise experts as endogenous robustness groups and optimizes high-loss routing outcomes rather than merely equalizing traffic. DRMoET updates a per-layer expert distribution by an entropy-regularized softmax rule on EMA-smoothed, activation-weighted expert losses, strengthening plausible non-top routing paths while preserving standard MoE computation. Under the FLAME-MoE recipe at 746M-total and 10.3B-total scales, DRMoET improves downstream averages over both standard FLAME-MoE and auxiliary-loss-free balancing. At 10.3B total parameters and 67B training tokens, DRMoET improves the seven-task average from 0.6625 to 0.6767, while the auxiliary-loss-free baseline achieves 0.6431. Mechanistic analyses show lower expert-loss variance with nearly unchanged mean loss, 4.3% lower excess loss under forced mid-k misrouting, and improved domain-expert specialization. These results position routing robustness-not only utilization balance-as a practical objective for reliable sparse MoE scaling. Project page and code are available at: https://drmoet.github.io/.
