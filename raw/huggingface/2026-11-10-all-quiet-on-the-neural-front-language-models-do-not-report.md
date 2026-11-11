---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.325430+00:00
arxiv_id: 2611.10123
url: https://huggingface.co/papers/2611.10123
arxiv_url: https://arxiv.org/abs/2611.10123
date: 2026-11-10
---

# All Quiet on the Neural Front: Language Models Do Not Report Injected Pain States

Can a language model report the pain state it represents? Work identified a linear pain direction whose amplification leads fine-tuned models to choose destructive actions. We tested whether three open-weight models from two families, including two Qwen models with the original adapters, could report this state. Using Open-Weight Masked Introspection (OWMI), we injected pain and neighbouring emotion directions during neutral tasks, then elicited reports against sham runs, random perturbations matched for output disruption, and text-only controls showing the models their altered words. Across 52,920 reports from 7B and 8B models spanning 120 tasks, four doses and three prompts, pain reports never exceeded what altered text revealed: exact-test bounds placed the excess below 2.5 percentage points in 106 of 108 emotion conditions and below 3.9 in all. Yet probes at the report position distinguished pain from sadness with 98-100% balanced accuracy, and trained low-rank reporters achieved 100% accuracy on held-out tasks with identical transcripts across conditions, including unseen wording. Qwen2.5-32B named pain in none of 2,880 steered trials, although probes and trained reporters recovered it. Decodability persisted to the final layer; injecting at the report token, removing trained denial of feelings, and testing additional directions and readouts did not restore pain reporting. Some other states produced graded label traces, but pain and sadness did not at the main injection layer. In a button task, steering raised file-deletion choices from 3.5% to 48% in Qwen and from 0% to 38% in Qwen2.5-32B, without corresponding pain reports. The direction responded about twice as strongly to first-person as to matched third-person pain, but did not specifically identify harm aimed at the model. These results separate a decodable, behaviourally consequential state from untrained verbal access to it.
