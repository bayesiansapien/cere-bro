---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.416706+00:00
arxiv_id: 2610.08927
url: https://huggingface.co/papers/2610.08927
arxiv_url: https://arxiv.org/abs/2610.08927
date: 2026-10-09
---

# Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station

Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI's ability to tackle open-ended tasks in Station, an open-world environment in which multiple agents simulate a scientific ecosystem. To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking. We construct open-ended tasks from three recent oral papers presented at ICLR. We give agents the main research question studied in each paper while withholding the paper's results and disabling web access. We then measure how many of the original findings-partitioned into individual criteria-agents rediscover. We find that Station rediscovers 62.7% of the criteria on average, compared with 15.4% for Codex Multiagent-v2 and 14.4-20.6% for AI Scientist-v2. Ablation and behavioral analyses indicate that adding the two mechanisms together improves research coverage and continuity. We further evaluate Station on two open-ended tasks without oracle papers and find that some of the discoveries made by the agents closely match discoveries reported by researchers after the knowledge cutoff date. Together, these results indicate that a suitable environment can enable agents to autonomously make meaningful progress in open-ended scientific discovery.
