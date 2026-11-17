---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.001572+00:00
arxiv_id: 2611.17811
url: https://huggingface.co/papers/2611.17811
arxiv_url: https://arxiv.org/abs/2611.17811
date: 2026-11-16
---

# AI Reviews Are Biased Towards the Appendix

Large language models (LLMs) are increasingly used by reviewers to highlight weaknesses during the reviewing process, and their outputs often shape the reviews that humans submit. Prior work studies how LLM reviews align with human ones, yet we know little about which parts of a paper these models actually criticize. In this work, we investigate 2,000 papers from ACL, EMNLP, COLM, and ICLR, and show that the latest GPT and Claude models draw about 50% or more of their review weaknesses from the appendix. This behavior holds across the API, coding-agent, and web access methods for using LLMs to review a paper. In contrast, we find that humans draw only 8.4% of their weaknesses from the appendix, and these weaknesses primarily revolve around a paper's presentation and content related to its core idea. Meanwhile, LLMs draw weaknesses from deep in the appendix that concern fine-grained technical details not central to the paper's contributions. We anticipate that our analysis will contribute to the scholarly discourse on AI reviews. Our code is publicly available at: https://github.com/cincynlp/review_appendix.
