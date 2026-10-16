---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.231902+05:30
arxiv_id: 2610.17079
url: https://huggingface.co/papers/2610.17079
arxiv_url: https://arxiv.org/abs/2610.17079
date: 2026-10-15
---

# Rethinking LLM-Guided Visual Question Answering: Does Deeper Knowledge Integration Really Help?

Knowledge-based Visual Question Answering (VQA) requires reasoning that extends beyond visible image content, demanding external commonsense and factual knowledge. While recent work leverages Large Language Models (LLMs) as knowledge sources, the question of how deeply such guidance should be integrated into a vision language architecture remains underexplored. In this work, we generate structured reasoning guidance, visual focus concepts, distractor elements and external knowledge using Llama~3.3~70B and systematically compare two integration strategies within a unified frozen ViT + FLAN-T5 framework on the OK-VQA benchmark: decision level late fusion and attention-matrix injection. Contrary to the prevailing assumption that deeper integration is superior, we find that shallow late fusion achieves the strongest results (39.4% exact match, +10.0 over the no guidance baseline), outperforming deep attention modification (31.8%) under data scarce fine-tuning. We further contribute an LLM based augmentation pipeline that expands training data more than tenfold via question paraphrasing. Our findings indicate that integration depth must be matched to the data regime.
