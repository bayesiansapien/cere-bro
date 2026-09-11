---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.10016
url: https://huggingface.co/papers/2609.10016
arxiv_url: https://arxiv.org/abs/2609.10016
date: 2026-09-11
---

# MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes

We introduce MetroLLM-Bench, a 955-case benchmark for testing language models as the policy layer of a transit kiosk. It covers six real metro systems, ranging from 37 to 414 stations, and eleven categories that include routing, fare calculation, disruptions, accessibility, and adversarial input. In each case, the model must call structured tools and submit a machine-renderable terminal state containing an outcome, a per-ticket fare quote when applicable, and a kiosk action. Fourteen deterministic scoring components form Tier 1; eight semantic-quality components form Tier 2, six of which use a language-model judge. We report Tier 1 and the combined score of both tiers. A stratified 75/25 split reserves 717 cases for training-data generation and 238 for held-out evaluation.
  We evaluate twenty-six models from six vendors, of which twenty-three are ranked. On the held-out partition, a 4B Qwen 3.5 student trained through parameter-efficient fine-tuning (PEFT) exceeds both GPT-5.6 tiers on Tier 1 (91.3 against 90.6 and 90.0) and matches GPT-5.4 full at maximum reasoning effort (91.4), with a 2.6 GB Q4_K_M footprint. Larger 9B and 27B students provide no further Tier 1 improvement over the 4B student at this training scale. Across the four Qwen sizes, the PEFT gain over the corresponding base model decreases from +7.03 points at 2B (three training seeds) to -0.91 at 27B; every seed shows the same direction at every size. A deterministic rule-based baseline reaches 84.6 on Tier 1, with the remaining language-model advantage concentrated in policy adaptation, compound scenarios, accessibility, and temporal reasoning. Muse Glimmer 30B leads the composite ranking, and serving configuration alone moves the Qwen 3.5-to-3.8 comparison by 2.7 Tier 1 points. The benchmark, harness, reproduction guide, and fine-tuned students are released at https://github.com/continker/metrollm-bench.
