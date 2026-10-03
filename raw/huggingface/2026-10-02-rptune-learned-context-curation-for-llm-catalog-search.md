---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819862+00:00
arxiv_id: 2610.00964
url: https://huggingface.co/papers/2610.00964
arxiv_url: https://arxiv.org/abs/2610.00964
date: 2026-10-02
---

# RPTune: Learned Context Curation for LLM Catalog Search

For small merchant businesses (SMBs) whose catalogs fit within a long-context LLM, full-catalog prompting offers a compelling alternative to multi-stage retrieval designed primarily for large marketplaces with millions of items. However, fitting the full catalog into the context window does not ensure that the model can use it effectively, since LLMs do not exploit long contexts uniformly. We therefore study in-context catalog search through two complementary questions: (1) how to curate and present catalogs to the LLM, and (2) how to adapt the LLM for product selection on curated contexts.
  We propose RPTune, an end-to-end framework that couples learned catalog curation with LLM post-training using automatically generated, catalog-grounded supervision. An encoder-reorganizer curator orders and prunes products guided by downstream LLM feedback, while the resulting curated catalogs in turn improve the effectiveness of LLM post-training with a context-relative reward. We evaluate RPTune on 7 real merchants spanning distinct retail verticals, using 100 complex conversational queries per merchant. RPTune consistently improves search accuracy across both proprietary and open-weight LLMs, with context curation yielding gains of up to 31.4 percentage points and post-training adding a further 10.3 points on average.
