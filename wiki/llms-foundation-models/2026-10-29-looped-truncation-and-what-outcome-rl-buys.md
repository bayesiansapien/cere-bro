# Looped transformers: don't truncate; outcome RL mostly buys finishing and reliability

**Sources (HuggingFace 2026-10-28):** [Truncate or Not?, 2610.26030](https://arxiv.org/abs/2610.26030) · [What Outcome RL Buys, 2610.34894](https://arxiv.org/abs/2610.34894) · [Multiscale Policy Optimization, 2610.35013](https://arxiv.org/abs/2610.35013) (HF #2).

**TL;DR.**
- **Truncate or Not?** Looped transformers reuse one block of layers to get depth without parameters, trained with backprop through time (BPTT). Truncating BPTT to the last few loops saves compute but biases gradients. Across ~600 runs the authors fit one scaling law with "effective parameters" for looping and truncation. It favours *full* BPTT: at matched compute, full BPTT through fewer loops beats truncation. With model size free, two fully trained loops are optimal, reaching lower loss than the compute-optimal non-looped model with ~27% fewer non-embedding parameters for 8% more training compute.
- **What Outcome RL Buys.** Splitting pass@1 gains of 20 released RL models (1.5B-32B) into finishing (answering before the token budget runs out), reliability (right when finished) and reach (solving what the base never solves in eight tries): under tight budgets 82% of the change is finishing; with enough tokens it is reliability; reach adds at most 2.1 points, and only 3.5% of 144 "RL-only" physics solves held up on re-check.
- **Multiscale Policy Optimization (MPO).** Critic values vary mainly across turns, so credit assignment and importance sampling are anchored at the turn level with finer token credit inside; consistent gains on search, tool use and automation with 4B and 30B-A3B models.

## Relation to prior wiki
- **Extends** [looped transformers](looped-transformers.md): a parameter-efficiency result (27% fewer parameters) is a compression result by another name.
- **Confirms** the [RL for LLMs](rl-for-llms.md) consensus since Yue et al. 2025 that outcome RL sharpens rather than extends. It also ties to effort economics: much of what RL "buys" is finishing within budget, which a bigger budget also buys.
