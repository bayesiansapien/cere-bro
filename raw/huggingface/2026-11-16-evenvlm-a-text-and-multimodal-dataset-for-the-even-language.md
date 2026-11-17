---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.004062+00:00
arxiv_id: 2611.16500
url: https://huggingface.co/papers/2611.16500
arxiv_url: https://arxiv.org/abs/2611.16500
date: 2026-11-16
---

# EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning

We present EvenVLM, the first text and multimodal (VQA) dataset for Even (Lamut), an endangered Northern Tungusic language spoken by approximately 6,800 people in Siberia. Our dataset comprises 50,521 structured Even-Russian entries extracted from dictionary and phrasebook sources via GPT-4o Mini-based parsing, from which we synthetically generate 107,543 training examples spanning translation, grammar, reading comprehension, and semantic classification. To address tokenization inefficiency on Even's agglutinative morphology, we propose a three-step tokenizer expansion algorithm that adds Even-specific graphemes (eng, oe, o-umlaut), whitelisted vocabulary, and BPE merges, reducing average tokens per word by 27% (4.99 to 3.64). Using LoRA fine-tuning of Qwen3-VL-4B, we adapt the model for text tasks (0.53% trainable parameters, rank 32) and separately for visual question answering (rank 64, frozen vision encoder). Our best configuration achieves 11.4% exact match and a 13.6 weighted score on text benchmarks, 0.1283 chrF for sentence translation, and 65% accuracy on VQA (up from 0% for the base model and text-only fine-tuning). We release our datasets, evaluation benchmarks, and training pipeline to support further research on Even and other low-resource languages.
