---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.29874
url: https://huggingface.co/papers/2611.29874
arxiv_url: https://arxiv.org/abs/2611.29874
date: 2026-11-25
---

# Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays

Feedback tools and research on learner writing need transcriptions of handwritten essays that keep exactly what the student wrote: misspellings, line breaks, struck-through words and insertions. Vision-language models (VLMs) read handwriting well, but they also tend to rewrite it into correct language. We measure this on BRESSAY, 1,000 handwritten Brazilian Portuguese essays, with a benchmark that adds error preservation, invented errors, edit-markup precision and recall and line structure to the character error rate (CER) and uses paired bootstrap confidence intervals. We restrict the study to open-weight models that schools can run on their own hardware. Of 22 open baselines, the best, Qwen3-VL 235B-A22B, reaches 5.6% CER on the 199 test pages; none reproduces the edit markup reliably, and every VLM replaces 39-78% of the words absent from a Portuguese dictionary with dictionary words. We fine-tune LightOnOCR-3-1B on the 647 training pages in 85 minutes on one GPU. The resulting Escriba-OCR-1B reaches 2.06% CER, 3.5 points below the best baseline (95% CI [-4.2, -2.9]); under the ICDAR 2024 competition metric it reaches 2.1% CER, below the best published page-level results (2.2-2.4%). It recovers 67% of insertions and 77% of illegible deletions, and reproduces the line structure of 97% of the pages, but still normalises 60% of likely misspellings. Three seeds agree within 0.04 CER points, and quantised to 4 bits the model runs on an ordinary CPU at about one minute per page. On 40 letters of another corpus it matches its base model (without that model's appended comments) but misreads unseen words more often; weight interpolation recovers half the gap. A teacher's review finds that 45% of the judgeable apparent corrections are errors in the BRESSAY ground truth, so dictionary-based scores likely understate preservation. We release the model, the benchmark code and the review data.
