---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.34719
url: https://huggingface.co/papers/2611.34719
arxiv_url: https://arxiv.org/abs/2611.34719
date: 2026-11-27
---

# Reading, Not Adapting: Unlocking Frozen Visual Knowledge for AI-Generated Image Detection

Generalization to unseen image generators has driven efforts to adapt pretrained visual representations for detection. Yet recent findings show that vision foundation models already encode transferable detection knowledge, while further adaptation can impair generalization. This motivates a shift from backbone adaptation to knowledge readout. Conventional linear probing offers a direct way to read this knowledge but is limited to final-layer RGB features. Multi-cue detectors broaden the evidence base, but their designs introduce other tradeoffs: adaptation may compromise pretrained transferability, heterogeneous encoders complicate feature integration, and late fusion precludes intermediate cross-view interaction. To overcome these limitations, we propose ReMoT, a Mixture-of-Transformers-inspired framework that reads complementary knowledge from spatially aligned RGB and wavelet views within a fully frozen visual foundation. ReMoT employs staged joint attention to enable controlled local and global cross-view interaction, while learnable fusion queries progressively read complementary evidence across Transformer depth without writeback. ReMoT achieves 91.2% average accuracy across eight benchmark groups with 3,074 trainable parameters, attaining the highest overall average among the evaluated methods. These results support structured knowledge readout as a promising alternative to backbone adaptation. Code is available at https://github.com/yunncheng/ReMoT.
