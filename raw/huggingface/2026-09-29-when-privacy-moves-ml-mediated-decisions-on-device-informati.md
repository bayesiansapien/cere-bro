---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936745+00:00
arxiv_id: 2609.33312
url: https://huggingface.co/papers/2609.33312
arxiv_url: https://arxiv.org/abs/2609.33312
date: 2026-09-29
---

# When Privacy Moves ML-Mediated Decisions On Device: Information and Incentive Misalignment in Auctions

Moving ML-mediated decision making onto privacy-preserving clients decentralises the economic decision along with the inference. Shared budget constraints then depend on information that cannot be globally current, creating an information-structure failure that conventional pacing is not designed to solve. We study this information misalignment in an auction-logic-faithful on-device simulation with 36 campaigns and 50 devices. Accounting is in dimensionless integer score units; no currency semantics are claimed. Across 30 paired demand paths, proportional Even pacing overspends 17.77% after one tick of staleness and 1,669.31% after 50 ticks under the original 20-times budget pressure. The effect does not depend on that severe a budget: at two-times pressure, 50-tick overspend remains 106.95%. A visible-budget no-sale guard makes zero-lag compliance exact at this score-unit granularity, yet leaves 11.88% overspend at one tick because other devices' debits remain invisible. A declared bursty, heterogeneous-device sweep retains a strictly increasing mean lag curve. We derive a finite-window expected excess-debit bound under conditional charge caps and find positive paired slack in every bounded-value cell. A second, incentive misalignment arises when the ML/pacing score transformation is allowed to change payment units: 98.23% of rival auctions at one tick admit a profitable deviation. An executable implementation-level counterexample isolates the runner-up's multiplier in the winner's price. Critical-base-bid payment is per-auction DSIC conditional on current multipliers, but does not establish dynamic truthfulness and does not repair base-value ranking disagreement.
