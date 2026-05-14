---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.08737
url: https://huggingface.co/papers/2605.08737
arxiv_url: https://arxiv.org/abs/2605.08737
date: 2026-05-14
---

# The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs

On-policy distillation (OPD) is widely used for LLM post-training. When pushed with a reward-extrapolation coefficient lambda > 1, the student can lift past the teacher in domain, but past a threshold lambda-star the same step violates the output contract on structured-output tasks. In a single-position Bernoulli reduction, we derive a closed-form base-relative clip-safety threshold lambda-star(p, b, c) determined by three measurable quantities: the teacher modal probability, the warm-start mass, and the importance-sampling clip strength. Above lambda-star the extrapolated fixed point exits the clip-safe region, changing training from format-preserving to format-collapsing. We extend the rule to calibrated K-ary listwise JSON tasks where a single binding equivalence class dominates the output contract and SFT retains parse headroom. On Amazon Fashion, three pre-registered tests (a fine-grid cliff interval, a budget-extension test, and a small-clip cross-prediction) all fall within their locked prediction windows, with the small-clip value matching the closed-form prediction below grid resolution. Operating just below lambda-star, ListOPD brings a 1.7B Qwen3 student to in-domain parity with an 8B-SFT baseline (pre-registered 3-seed) at one-fifth the parameters. The gain is driven primarily by format adherence: NDCG@1 on parsed outputs remains flat across lambda, while parse validity sharply changes at the predicted boundary.
