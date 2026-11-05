---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.368416+05:30
arxiv_id: 2611.04169
url: https://huggingface.co/papers/2611.04169
arxiv_url: https://arxiv.org/abs/2611.04169
date: 2026-11-04
---

# Length Is Cheap, Competition Is Not: Attention Predicts Context Rot in Retrieval

Why do language models fail on long inputs? The common answer is length. We show that, for retrieval, length is cheap and competition is not. On five open models (0.5B to 3B parameters, four families), neutral filler costs nothing: accuracy stays at 0.97 to 1.00, up to 32K tokens on Qwen2.5-1.5B. Statements in the format of the evidence, placed at the same positions, drop it to 0.16 to 0.33. A single statement that gives the queried key a rival value multiplies the loss by 9 to 110, and every additional rival adds to it. Inside the model, one quantity tracks the failure: the attention mass left on the evidence. Across 126,473 trials it explains up to 58% of the variance in loss; log length explains at most 8%. The masked-filler protocol behind the claim that length alone hurts reproduces on MMLU (11 to 18 points lost at 30K tokens), but fails a visible control in retrieval: masking costs 45 accuracy points at 32K tokens, while the same filler left visible costs none. In retrieval, context rot is a competition for attention. We release the probe and all 126K trial-level measurements.
