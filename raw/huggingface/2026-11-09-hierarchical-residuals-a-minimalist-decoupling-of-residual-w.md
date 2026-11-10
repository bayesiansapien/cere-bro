---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.205192+00:00
arxiv_id: 2610.41711
url: https://huggingface.co/papers/2610.41711
arxiv_url: https://arxiv.org/abs/2610.41711
date: 2026-11-09
---

# Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute Width

Residual connections underpin Transformers, but they implicitly tie the residual width carried through depth to the compute width used inside each layer. We introduce Hierarchical Residuals (HiRes), a minimalist architectural change that decouples these dimensions, widening the residual state while keeping per-layer compute width fixed. HiRes groups layers into blocks: standard d-dimensional PreNorm layers operate inside each block, while a wider D-dimensional PostNorm outer residual connects blocks. Learned read/write projections bridge the two spaces at block boundaries, leaving individual Transformer layers unchanged. Across different model sizes and depths, HiRes consistently outperforms vanilla residual addition, with fitted scaling laws indicating a 1.30-fold improvement in FLOPs efficiency. On OLMoE-1B-7B pretraining for 500B tokens, HiRes achieves 0.0208 lower training loss and 1.14-point higher downstream accuracy. HiRes is also competitive with other residual expansion methods such as VWN, mHC and AttnRes with less activation memory and I/O costs. Built from only dense projections and normalizations, it requires neither specialized kernels nor infrastructure-level optimizations. HiRes thus exposes residual width as a practical scaling variable using only standard operators.
