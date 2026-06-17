# Learning from the Self-Future: On-policy Self-distillation for dLLMs (d-OPSD)

**TL;DR.** On-policy self-distillation (OPSD) post-trains LLMs by having the model learn from a privileged version of itself, but every existing OPSD method is autoregressive-centric: it injects privileged information via left-to-right *prefix* conditioning with token-level divergence loss. That design conflicts with diffusion LLMs (dLLMs), which generate in arbitrary order by iterative denoising. d-OPSD is the first OPSD framework built for dLLMs. Two changes: (1) construct the self-teacher with self-generated answers as *suffix* conditioning, so the student learns from its own "self future-experience" rather than a left-to-right prefix; (2) move supervision from token-level to *step-level*, aligning with the denoising process. Across four reasoning benchmarks d-OPSD beats RLVR and SFT with far better sample efficiency — about 10% of RLVR's optimization steps.

**Source:** HuggingFace · [arxiv 2606.18195](https://arxiv.org/abs/2606.18195) · [code](https://github.com/xingzhejun/d-OPSD)

```mermaid
flowchart LR
  G[Self-generated answer] -->|suffix conditioning| TEACH[Self-teacher<br/>future-experience]
  TEACH --> STEP[Step-level supervision<br/>aligned to denoising]
  STEP --> STU[dLLM student]
  STU --> OUT[Beats RLVR/SFT<br/>~10% of RLVR steps]
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class G input
  class TEACH,STEP aux
  class STU,OUT output
```

## Key findings

- **First OPSD for diffusion LLMs.** Prior OPSD assumes autoregressive prefix conditioning; d-OPSD replaces it with suffix conditioning suited to arbitrary-order denoising.
- **"Self future-experience":** the self-teacher is built from the model's own generated answers used as a suffix, not from a privileged left-to-right prefix.
- **Step-level, not token-level, supervision** aligns the loss with the dLLM denoising trajectory.
- **~10% of RLVR's optimization steps** to beat RLVR and SFT on four reasoning benchmarks — a large sample-efficiency win.

## Relation to prior wiki

- This ports the on-policy self-distillation line — [SDPG](2026-06-04-sdpg-self-distilled-policy-gradient.md), [HINT-SD](2026-05-25-hint-sd-targeted-hindsight-self-distillation.md), [PBSD](../llms-foundation-models/2026-06-09-pbsd-bayesian-self-distillation.md) — into the diffusion-LLM world for the first time. The wiki's earlier [d-OPSD step-distilled diffusion](2026-05-07-d-opsd-self-distillation-step-distilled-diffusion.md) (05-07) shared the diffusion focus but on *step distillation*; this is full post-training self-distillation.
- The sample-efficiency story (10% of the steps) echoes [TIP](2026-04-16-tip-token-importance-on-policy-distillation.md) (04-16, train on ~10% of teacher tokens) and the [Less-is-More ESR](2026-05-28-less-is-more-esr-on-policy-distillation.md) line — the recurring finding that most post-training compute is spent on signal-free updates.
- Updated in [knowledge-distillation](knowledge-distillation.md).

## Gaps

Diffusion LLMs are still niche relative to autoregressive models, so the practical impact depends on dLLMs mattering. Four reasoning benchmarks only; no agentic or long-context evaluation, and no head-to-head against an autoregressive model of equal size on the same tasks.

Raw: `raw/huggingface/2026-06-17-learning-from-the-self-future-on-policy-self-distillation-fo.md`
