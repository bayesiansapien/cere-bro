---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13831
url: https://huggingface.co/papers/2605.13831
arxiv_url: https://arxiv.org/abs/2605.13831
date: 2026-05-14
---

# Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context

Long-context modeling is becoming a core capability of modern large vision-language models (LVLMs), enabling sustained context management across long-document understanding, video analysis, and multi-turn tool use in agentic workflows. Yet practical training recipes remain insufficiently explored, particularly for designing and balancing long-context data mixtures. In this work, we present a systematic study of long-context continued pre-training for LVLMs, extending a 7B model from 32K to 128K context with extensive ablations on long-document data. We first show that long-document VQA is substantially more effective than OCR transcription. Building on this observation, our ablations further yield three key findings: i) for sequence-length distribution, balanced data outperforms target-length-focused data (e.g., 128K), suggesting that long-context ability requires generalizable key-information retrieval across various lengths and positions; ii) retrieval remains the primary bottleneck, favoring retrieval-heavy mixtures with modest reasoning data for task diversity; iii) pure long-document VQA largely preserves short-context capabilities, suggesting that instruction-formatted long data reduces the need for short-data mixing. Based on these findings, we introduce MMProLong, obtained by long-context continued pre-training from Qwen2.5-VL-7B with only a 5B-token budget. MMProLong improves long-document VQA scores by 7.1% and maintains strong performance at 256K and 512K contexts beyond its 128K training window, without additional training. It further generalizes to webpage-based multimodal needle retrieval, long-context vision-text compression, and long-video understanding without task-specific supervision. Overall, our study establishes a practical LongPT recipe and an empirical foundation for advancing long-context vision-language models.
