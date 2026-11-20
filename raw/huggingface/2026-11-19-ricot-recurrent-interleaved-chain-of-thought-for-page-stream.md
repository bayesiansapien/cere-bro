---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.145896+00:00
arxiv_id: 2611.22382
url: https://huggingface.co/papers/2611.22382
arxiv_url: https://arxiv.org/abs/2611.22382
date: 2026-11-19
---

# RICoT: Recurrent Interleaved Chain-of-Thought for Page Stream Segmentation

Large language models (LLMs) have renewed interest in Page Stream Segmentation (PSS), splitting a multi-page file into its constituent documents. Yet published LLM methods still frame the task as boundary classification over one or a few neighboring pages, and commercial document-splitting APIs do not disclose their methods. We reimagine PSS for LLMs as a sequential process over the whole stream and propose RICoT (Recurrent Interleaved Chain-of-Thought), a prompting framework that works through the pages as a reader would: within a sliding window it reasons about each page and commits its boundary decision before moving on, and across windows it carries forward a compact record of what it has read, keeping per-call cost bounded. We also introduce FinancePSS-205, a benchmark of 205 real-world, de-identified financial page streams, to be released publicly. On FinancePSS-205, RICoT matches or outperforms pairwise and windowed prompting with the same backbone for each of three open-weight LLMs; on a TABME test subset, RICoT with GLM-5 reaches document F1 0.847 and boundary F1 0.915, above published zero-shot results. A 2B-parameter student, trained on a larger teacher's decisions with and without the page-level reasoning, performs comparably in both modes and comes within 0.05 document F1 of the strongest prompted model on FinancePSS-205.
