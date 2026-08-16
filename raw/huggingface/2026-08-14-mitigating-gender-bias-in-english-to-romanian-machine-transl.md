---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.08606
url: https://huggingface.co/papers/2608.08606
arxiv_url: https://arxiv.org/abs/2608.08606
date: 2026-08-14
---

# Mitigating Gender Bias in English to Romanian Machine Translation

Machine translation (MT) systems often fail to correctly translate gender, especially when converting from a gender-neutral language like English to a gendered target language such as Romanian. This bias results in translations that default to masculine forms or reinforce gender stereotypes. We propose a hybrid pipeline to mitigate this issue by combining large language model (LLM)-based gender classification with neural machine translation (NMT). Our system uses a fine-tuned LLM to detect the intended gender of target words in English sentences and insert inline gender hint tags. These tagged sentences are then passed to a Transformer model fine-tuned to generate morphologically correct Romanian translations. To support this, we introduce three novel datasets for gender disambiguation and translation. Our approach improves gender accuracy on the WinoMT and WinoGender benchmarks by over 40 percentage points compared to a baseline MT system. This is the first method to explicitly address and evaluate gender bias in English-Romanian MT using both LLM inference and tag-aware translation.
