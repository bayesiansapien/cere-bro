# BES: Bidirectional Evolutionary Search for Self-Improving Language Models

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28814](https://arxiv.org/abs/2605.28814) · [HuggingFace](https://huggingface.co/papers/2605.28814) · [code](https://github.com/Embodied-Minds-Lab/BES) · [raw](../../raw/huggingface/2026-05-28-self-improving-language-models-with-bidirectional-evolutiona.md)

## TL;DR

BES augments best-of-N and tree-search with two complementary moves. Forward search adds evolutionary recombination operators that mix partial trajectories so candidates can escape the narrow entropy shell that pure autoregressive expansion is confined to. Backward search recursively decomposes the original task into checkable subgoals so the forward search gets dense intermediate feedback instead of one final reward signal. The paper proves that expansion-only search is confined to a narrow entropy shell while evolutionary recombination escapes it, and that backward decomposition exponentially reduces the samples needed to hit a correct answer. Empirically BES improves on post-training tasks where mainstream algorithms fail to improve, and beats existing open-source frameworks on three open-problem benchmarks in both average and best-case performance.

```
Forward expansion only (best-of-N, tree search):
   ●─►● ┐
   ●─►● ├─ confined to narrow entropy shell around the model's mode
   ●─►● ┘

BES forward + backward:
                       backward decomposition: goal ─► subgoal₁, subgoal₂ ...
                                                          ▼  dense reward
   ●─►● ─┐
   ●─►● ─┼─►─ recombine ─► new candidate outside the original shell
   ●─►● ─┘
```

## Key findings

- Theoretical result: expansion-only search is provably confined to a narrow entropy shell around the model's mode; evolutionary recombination can leave it.
- Theoretical result: backward subgoal decomposition exponentially reduces required samples to find a correct answer.
- Empirical: BES makes consistent gains on post-training tasks where mainstream algorithms produce no improvement.
- Empirical: beats existing open-source frameworks on three open problem-solving benchmarks in both average and best-case.

## How this fits prior wiki state

BES is the cleanest formal argument so far for why pure best-of-N hits a ceiling on hard problems: the candidates are samples from the same posterior, so they cover one narrow region of the solution space. This connects to yesterday's CPT ([[2026-05-27-cpt-collaborative-parallel-thinking]]) which observed empirically that parallel reasoning branches re-derive each other's work; BES gives a formal frame for that observation and an operational fix (recombination operators). The backward-decomposition half connects to the "sparse-to-dense reward" line ([[2026-05-13-sparse-to-dense-reward-principle]]) — both are about turning a thin terminal signal into a thicker intermediate one.

## Related pages

- [[2026-05-27-cpt-collaborative-parallel-thinking]] — empirical version of the entropy-shell problem
- [[2026-05-13-sparse-to-dense-reward-principle]] — dense intermediate feedback
- [[2026-04-20-stop-path-pruning-parallel-reasoning]] — pruning parallel reasoning

## Research angle

The proof that recombination escapes the entropy shell is the most useful piece. It quantifies what every test-time-search practitioner already suspects: throwing more best-of-N at a hard problem fails because the samples are not actually independent in solution-space. A natural extension is to apply BES inside on-policy distillation rollouts, where ESR (today) already shows that the rollout is wasted past a prefix; a hybrid recipe might use ESR-truncated forward rollouts plus backward subgoal feedback for the supervision signal.
