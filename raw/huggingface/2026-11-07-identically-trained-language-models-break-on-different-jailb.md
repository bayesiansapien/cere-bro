---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.595855+00:00
arxiv_id: 2610.34074
url: https://huggingface.co/papers/2610.34074
arxiv_url: https://arxiv.org/abs/2610.34074
date: 2026-11-07
---

# Identically Trained Language Models Break on Different Jailbreaks

Jailbreak benchmarks test one checkpoint and treat which jailbreaks break it as a property of its pretraining data and safety training. We ask whether another pretraining run of the same data, given the same safety training, would break on the same jailbreaks. For each of 25 pretraining data recipes, we take 1B base models from 3 pretraining seeds and give each the same safety post-training with 2 post-training seeds, for 150 models in all. We then collect 20 responses from every model to a shared set of jailbreak prompts and correlate the per-prompt non-refusal rates between every pair of models. On average, two post-trained copies of the same pretraining run have per-prompt non-refusal rates that correlate at 0.984. A different pretraining seed lowers the correlation to 0.811, and a different data recipe lowers it only slightly further, to 0.779. These results indicate that which jailbreaks break a checkpoint depends much more on its pretraining run than on its data, a pattern that holds in all 25 data recipes and at 150M and 300M parameters. In practice, the best of 91 attack templates found on one checkpoint stays the best after a new pretraining seed in only 27% of model pairs, against 67% after a new post-training seed. Each pretraining run also leaves a fingerprint: across 3,211 prompts, a model's per-prompt non-refusal rates identify its pretraining run among all 75 runs every time, and a random subset of 50 prompts still does so 98% of the time.
