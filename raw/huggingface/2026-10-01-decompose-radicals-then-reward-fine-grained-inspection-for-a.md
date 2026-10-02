---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350871+05:30
arxiv_id: 2609.37569
url: https://huggingface.co/papers/2609.37569
arxiv_url: https://arxiv.org/abs/2609.37569
date: 2026-10-01
---

# Decompose Radicals, Then Reward: Fine-Grained Inspection for Accurate Chinese Text Rendering

Rendering accurate Chinese text remains challenging for text-to-image models. Existing OCR-based reinforcement-learning rewards compare decoded transcripts with target strings. Such rewards overlook the compositional nature of Chinese writing: an ideograph consists of reusable components arranged through explicit spatial relations, yet OCR evaluates it as an atomic character. Consequently, visually different radical-level errors may receive equally coarse feedback, encouraging glyphs that merely resemble the target instead of faithfully reproducing its internal structure. We employ Ideographic Description Sequences (IDS), which comprise spatial operators and character components, and train an expert IDS recognizer to transcribe rendered Chinese text into this representation. Building on this recognizer, we introduce IDSpect, which deterministically decomposes the target text into IDS tokens and aligns crop-level visual IDS predictions with the target sequence. Globally unique token credit makes this comparison robust to the order of detected text regions. Combined with a whole-character semantic reward, IDSpect supplies fine-grained credit with component and spatial-relation without changing the image generator or adding inference-time cost. Experiments with GRPO post-training of Qwen-Image demonstrate that IDSpect achieves leading structural quality and semantic alignment on LongText and GenTextEval.
