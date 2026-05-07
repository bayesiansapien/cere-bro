# The First Token Knows: Single-Decode Confidence for Hallucination Detection

**arXiv:** [2605.05166](https://arxiv.org/abs/2605.05166)
**Tier:** 2 — responsible-ai / inference efficiency

## TL;DR

The normalized entropy of the top-K logits at the first content-bearing answer token of a single greedy decode (call it phi_first) matches or modestly exceeds semantic self-consistency on closed-book short-answer factual QA. AUROC 0.820 vs 0.793 across three 7-8B models (Llama-3.1-8B, Mistral-7B-v0.3, Qwen2.5-7B) on PopQA + TriviaQA (n=1000 each). Compute saving is structural: one greedy decode versus one greedy + ten samples + NLI clustering. Roughly 1/11 the generation cost.

## What the metric does

phi_first reads the entropy of the top-K logits at the model's first content-bearing answer token, after a single greedy decode. The signal is that low-entropy top-K means the model has high confidence in the answer's first content word, which correlates strongly with whether the eventual full answer is hallucinated.

```
Question: "What year did the Treaty of Westphalia end?"
                            │
                            ▼
              greedy decode begins
                            │
                            ▼
       first content-bearing token: "1"
       top-K logits at this position: [1, 6, 7, ...]
                            │
                            ▼
           normalized entropy of these logits
                            │
                            ▼
              phi_first = uncertainty score
```

Compare to the standard alternative (semantic self-consistency):
```
greedy decode (1×) + 10 sampled decodes + NLI model clusters answers by meaning
→ uncertainty = inverse of cluster agreement
```

## Result summary

| Method | AUROC (mean across 3 models × 2 benchmarks) |
|---|---|
| phi_first (single decode) | **0.820** |
| Semantic self-consistency (1 + 10 + NLI) | 0.793 |
| Surface-form self-consistency | 0.791 |

phi_first is moderately to strongly correlated with semantic agreement (Pearson 0.54-0.76). A logistic ensemble of phi_first + semantic agreement yields only +0.02 AUROC over phi_first alone, evidence that phi_first captures most of semantic agreement's discriminative power.

The partial-correlation analysis on answer length is the methodological touch worth noting. The apparent association between phi_first and answer length largely disappears after controlling for correctness. The signal is real, not a length artifact.

## How this relates to prior wiki work

- **Net new** for the responsible-ai topic. The wiki has been tracking [agent security](../agentic-systems/2026-05-04-agentic-pentester-architecture.md) (05-04) and [agentic posttraining alignment](../agentic-systems/2026-04-22-ml-intern-agentic-posttraining.md) (04-22), but no prior page has covered hallucination-detection efficiency.
- **Cross-source intersection** with the wiki's general inference-efficiency thread. phi_first reduces hallucination guardrail compute by an order of magnitude. If this generalizes beyond closed-book short-answer QA, it's deployment-changing.
- **Connection to today's [SxS Disclosure Policies](../llms-foundation-models/2026-05-08-sxs-disclosure-policies-llm-reasoning.md)** paper. Both papers operate on the question of when an LLM commits to an answer. phi_first reads commitment from the model's logits. SxS makes commitment a learned action. Two complementary framings of the same problem.

## What's surprising

The recommendation in the abstract is the kind of falsifiable claim that's rare in this literature. "First-token confidence should be reported as a default, low-cost baseline before invoking sampling-based uncertainty estimation." This is a methodological intervention as much as a result. If the broader literature adopts phi_first as a baseline, it will reset the bar that subsequent uncertainty-estimation methods need to clear.

## Open questions

1. **Long-form generation.** All experiments are short-answer factoid QA. Whether the first-token signal survives in long-form structured generation is open.
2. **Tool-grounded outputs.** The wiki's main interest is agentic systems where the "answer" is a tool call. phi_first as a deployment-time gate at the first action token is the obvious next experiment.
3. **Multi-stage reasoning.** Chain-of-thought prefixes the answer with reasoning. Where exactly is the "first content-bearing answer token" in a CoT trajectory? The paper's setup is direct-answer; CoT is where the practical questions live.

## Why it matters

Production-scale hallucination detection has been blocked on cost. Ten-sample generation per question is not deployable for most agent systems. phi_first is one decode. The cost structure of hallucination guardrails changes by an order of magnitude if this generalizes. For the wiki's [agent-security thread](../daily-digest/2026-05/2026-05-06.md), this is the deployment-time piece that production agents need.
