---
source: farmer/huggingface
farmed: 2026-08-12T03:51:07Z
arxiv_id: 2607.27670
url: https://huggingface.co/papers/2607.27670
arxiv_url: https://arxiv.org/abs/2607.27670
date: 2026-08-12
---

# JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles

Jigsaw puzzle solving requires jointly reasoning about visual content and geometric constraints, yet existing benchmarks use rectangular cuts that create ambiguous ground truth in texture-repeated regions. We introduce \ours{}, a benchmark with tab-and-blank interlocking pieces where geometric constraints provide strong local compatibility requirements that, combined with visual content, yield unambiguous ground truth. Across 95K instances at four grid densities (4times4 to 16times16), we find that zero-shot VLMs largely lack geometric reasoning: only one of five frontier models (GPT-5.5) exceeds random baseline on 4times4 puzzles, while all others perform at chance level. While supervised fine-tuning achieves >97\% on 4times4, all models collapse on larger grids: GPT-5.5 drops from 70\% to near-random on 8times8, and even fine-tuned models fall below 5\% on 12times12. This scaling cliff'' suggests current architectures cannot maintain consistent constraint satisfaction as the number of pieces increases.  establishes scalable geometric reasoning as an open challenge for vision-language models.
