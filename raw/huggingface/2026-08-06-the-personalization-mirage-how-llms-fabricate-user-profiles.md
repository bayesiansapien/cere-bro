---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04570
url: https://huggingface.co/papers/2608.04570
arxiv_url: https://arxiv.org/abs/2608.04570
date: 2026-08-06
---

# The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads

Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined. We study over-inference (OI): the phenomenon where LLMs fabricate user attributes beyond what evidence supports. We introduce MirageBench, comprising 150 personas balanced across stereotypical, counter-stereotypical, and neutral profiles, 6 personalization tasks spanning an ``imagination gradient'', a four-way faithfulness taxonomy operationalized by an independent judge (validated against a blind human annotator on 400 claims: Cohen's kappa = 0.863 four-class, kappa = 0.900 binary), and a leaderboard of 12 models across 7 families on 143616 judged claims. We find that over-inference is pervasive: every one of the 12 models over-infers 35%--49% of its claims (cross-model mean 41.6%; claim-weighted 41.8%), with no model in this evaluation escaping it. Most strikingly, we surface a Self-Monitoring Inversion: at the model-selection level, models' self-assessed OI is negatively rank-correlated with their judge-measured OI (rho = -0.60, p = 0.044; exploratory, wide bootstrap CI [-0.90, +0.06], n = 12). The models that report the least over-inference tend to be flagged as fabricating the most, so self-reported confidence is a misleading signal for comparing models, even though within a single model self-audit still ranks that model's own claims moderately well (AUROC 0.58--0.83). We further show that OI is task-dependent (27%--59%) and that, in a multi-turn pilot, inferred attributes accumulate approximately linearly with little revision. MirageBench positions external verification, rather than model self-report, as a more reliable foundation for trustworthy personalization.
