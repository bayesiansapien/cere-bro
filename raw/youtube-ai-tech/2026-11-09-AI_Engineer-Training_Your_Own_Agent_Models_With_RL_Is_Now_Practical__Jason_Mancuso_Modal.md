# Training Your Own Agent Models With RL Is Now Practical (Jason Mancuso, Modal)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=3nDMYV-QHLs

## TL;DR
Modal argues that treating models as swappable backends is a losing strategy for agent companies, and that agent RL is now stable enough to own. Their recipe (GRPO + masked importance sampling + score centering + top-p sampling with mask replay) tolerates 4-5x more trainer/sampler mismatch than a homogeneous setup, which lets them run asynchronous RL with rollouts spread across 15-20 cloud providers, mixed GPU generations (B200, H200, H100, A100) and even mixed precision (BF16 and FP8) while staying as stable as all-B200. Sparse weight deltas (100-1000x sparser than full weights) make cross-cloud weight broadcast cheap. Result on Qwen 3.6 35B MoE: stable training and 15% cheaper rollouts with zero per-GPU inference tuning.

## Key Takeaways
- **Why fine-tune agents:** reliability SLOs require owning inference; proprietary data absent from pretraining breaks frontier models; vertical integration wins where competition is on task-intelligence-per-dollar (coding first, others next).
- **Why RL over SFT:** SFT on production traces is brittle because agent sessions branch; deployment hits branches never seen in training. RL explores branches during training.
- **You already have the ingredients:** a deployed harness plus evals/A-B tests is an RL environment. Mine failing production traces to synthesize training tasks.
- **Instability sources:** (1) staleness from async RL (rollouts from v1 training v3), (2) systems-level numerical mismatch between trainer and sampler kernels.
- **Recipe:**
  - GRPO base.
  - Masked importance sampling: per-token correction for both staleness and kernel mismatch, masking extreme ratios.
  - Score centering: removes drift that accumulates in weights across steps, not just per token.
  - Top-p with mask replay: the trainer replays the sampler's top-p mask so it never scores tokens the sampler could not have emitted. With top-p, score centering becomes exact rather than approximate.
- **Compute ratio:** agent RL runs about 2 inference GPUs per training GPU, so two thirds of a co-located cluster is rollout.
- **Sparse deltas:** delta between step t and t+1 is 100-1000x sparse; off-the-shelf compression cuts trainer-to-sampler traffic about 1000x, so samplers can live outside the training cluster.
- **Stack:** Miles (RL framework) + SGLang; source release promised.

## Architecture & Optimization Mechanics
- **Mismatch tolerance is the unlock for heterogeneous compute.** Once the correction absorbs kernel differences, you can treat old/cheap GPUs and quantized replicas as valid rollout workers. Modal ran an FP8 H200 pool alongside BF16 and the correction still learned from quantized rollouts.
- **Quantization as a rollout accelerator:** the talk explicitly notes per-GPU quantization tuning was not done. Rollout generation dominates RL cost, so FP8/INT4 sampler replicas with IS correction is a direct lever on RL cost, and it is your exact skill set.
- **Disaggregated RL:** sparse delta broadcast turns RL into the same disaggregation pattern as prefill/decode separation. Trainer stays on a contiguous high-end block; rollouts go wherever capacity is cheapest.
- **MoE relevance:** the testbed is a 35B MoE. Router logits are a known mismatch hotspot (expert selection flips under tiny numerical differences), so a recipe stable on MoE across GPU types and precisions is a meaningful result.
- **Top-p mask replay** is the subtle piece: without it, the trainer assigns probability to tail tokens the sampler truncated, producing huge importance ratios. Masking the same support on both sides fixes the support mismatch, not just the ratio.

## Grounded Context (Web Enrichment)
Modal's blog post "Toward RL on mixed-precision, mixed-accelerator samplers" confirms the setup: async RL on agentic coding tasks with GRPO plus masked importance sampling, samplers running each accelerator's native kernels and scaling up and down mid-run. I could not independently confirm "score centering" as a named technique in public sources; treat the talk as the primary reference until the code drops. The broader field is converging on the same direction: a 2026 paper on entropy-scaled trust regions argues magnitude-only importance-ratio masking breaks at low token entropy, which is a known weakness the Modal recipe may or may not address.

The sparse-delta claim is well corroborated. Hugging Face's TRL delta weight sync reports roughly 1% of BF16 elements change per RL step, cutting per-step transfer on Qwen3-0.6B from 1.2 GB to 20-35 MB. An arXiv paper (2605.07330, SparseRL-Sync) reports 32-54x raw reduction and 60-101x with lossless compression, and NVIDIA's NeMo-DCR does bit-exact delta-compressed refit. Note the gap: independent numbers are 50-100x, while Modal claims about 1000x. The higher figure is plausible with low learning rates and aggressive compression but should be verified against the released code. The "science of RL is figured out" framing is marketing; stability is much better, but reward hacking and environment quality remain unsolved.

## Real-World Application / Actionable Step
- Run a small experiment: async GRPO with a BF16 trainer and an FP8 (or GPTQ INT4) vLLM/SGLang sampler, with and without masked importance sampling plus top-p mask replay. Measure reward stability and the token-level KL between sampler and trainer. If INT4 rollouts train stably, that is a publishable compression-for-RL result.
- Characterize MoE router agreement between trainer and quantized sampler (fraction of tokens with differing top-k experts). This is likely the dominant mismatch term and a natural place for a targeted correction.
- For routing work: the business case here (own a fine-tuned small model for SLO-critical traffic) is the same economics as routing. A routed system with an RL-tuned in-house model for the high-volume path is the logical end state.
- Watch for Modal's source release on Miles + SGLang and diff its loss against standard GRPO to pin down what "score centering" actually is.
