---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.14354"
url: "https://huggingface.co/papers/2605.14354"
arxiv_url: "https://arxiv.org/abs/2605.14354"
date: 2026-05-16
---

# LLM-based Detection of Manipulative Political Narratives

We present a new computational framework for detecting and structuring manipulative political narratives. A task that became more important due to the shift of political discussions to social media. One of the primary challenges thereby is differentiating between manipulative political narratives and legitimate critiques. Some posts may also reframe actual events within a manipulative context.
  To achieve good clustering results, we filter manipulative posts beforehand using a detailed few-shot prompt that combines documented campaign narratives with legitimate criticisms to differentiate them. This prompt enables a reasoning model to assign labels, retaining only manipulative narrative posts for further processing.
  The remaining posts are subsequently embedded and dimensionality-reduced using UMAP, before HDBSCAN is applied to uncover narrative groups. A key advantage of this unsupervised approach is its independence from a predefined list of target categories, enabling it to uncover new narrative clusters.
  Finally, a reasoning model is employed to uncover the narrative behind each cluster. This approach, applied to over 1.2 million social media posts, effectively identified 41 distinct manipulative narrative clusters by integrating prompt-based filtering with unsupervised clustering.
