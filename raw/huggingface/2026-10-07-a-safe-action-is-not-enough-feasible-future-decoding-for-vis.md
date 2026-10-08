---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05166
url: https://huggingface.co/papers/2610.05166
arxiv_url: https://arxiv.org/abs/2610.05166
date: 2026-10-07
---

# A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies

A safe action is not necessarily a viable one. A frozen vision-language-action (VLA) policy can favor a locally admissible move that leaves no policy-supported route to safe task completion. We call this the feasibility-likelihood gap: likelihood ranks the next move, while feasibility depends on the futures it leaves open.
  To bring those futures into the decision, we derive the exact next-block marginal of the history-conditioned policy-environment trajectory law restricted to safe task completion. The derivation reveals a candidate-dependent feasible-future mass: its support records whether safe completion remains possible under the frozen continuation process, while its magnitude measures how much weighted safe-completion mass remains. Since exact evaluation is impractical online, we develop a selective finite-candidate approximation and establish conditions for recovering the best retained viable candidate.
  Our alarm-triggered, training-free reranker VICS-G lowers mean cumulative safety cost by 1.9%-57.5% across six Safety-CHORES settings while remaining within 2.5 percentage points of policy sampling in success and 0.82 steps in mean episode length. Our approach offers a promising and practical path toward safer task completion, grounded in an exact policy-relative target yet requiring neither policy retraining nor online rollouts.
