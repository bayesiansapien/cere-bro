---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.509590+00:00
arxiv_id: 2610.10808
url: https://huggingface.co/papers/2610.10808
arxiv_url: https://arxiv.org/abs/2610.10808
date: 2026-10-14
---

# Controlled Acquisition and Abstention in Three-Channel Score Conflicts

When audio, video, and text disagree, accuracy alone does not show whether to acquire another source or abstain. We study these choices in a controlled three-score benchmark: a policy observes two signed scores, may request the third at a cost, and can abstain. The primary reward is mechanism-specific: abstention is correct only for one designated ambiguity mechanism and is penalized under mixed corruption. Matched controls show that a threshold policy matches always-request decisions with fewer requests; its advantage over always-answer fusion depends on the reward assigned to that ambiguity. On a partially held-out synthetic split, the threshold policy reaches 0.789 +/- 0.006 targeted decision accuracy and 0.481 +/- 0.014 utility across 83 seeds. A three-score majority reference reaches 0.626 +/- 0.008 and 0.252 +/- 0.016, but uses more information. In a matched-budget test, a train-only value selector improves utility over no-query and matched-random policies at 10% and 25% budgets, while pair uncertainty has higher utility at every budget. At 50% and 63.7% budgets, the selector lowers utility despite slightly higher non-ambiguous accuracy. If all abstentions are scored incorrect, majority outranks the threshold policy in utility. At a central temporal setting, full-trace controls match the neural models while position perturbations separate them. On held-out-actor emotion clips, eight-frame fusion has opposite-signed accuracy differences for two encoder pairs, with both actor intervals containing zero; matched-request routing gains are small and uncertain. These results separate full-modality accuracy from pre-request selection value and show that selection value depends on budget and the observed-pair ranking.
