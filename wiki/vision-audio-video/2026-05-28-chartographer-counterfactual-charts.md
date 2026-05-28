# Chartographer: Counterfactual Chart Generation for VLM Evaluation

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.27311](https://arxiv.org/abs/2605.27311) · [HuggingFace](https://huggingface.co/papers/2605.27311) · [raw](../../raw/huggingface/2026-05-28-chartographer-counterfactual-chart-generation-for-evaluating.md)

## TL;DR

Standard chart-QA benchmarks let models shortcut to answers using prior familiarity with the underlying chart and its world-knowledge content rather than actually reasoning over the visualization. Chartographer counters this by reverse-engineering each chart into executable code, validating reconstruction fidelity, then producing seed-controlled counterfactual variants whose underlying chart and correct answer change while the chart-question pairing stays fixed. New answers are derived from the executable QA logic. Applied to existing chart-QA datasets, the framework reveals failures hidden by single-chart scores: VLMs that solve an original chart often fail its counterfactual variants, especially when the variant requires a novel visual-reasoning path through the same question.

## Key findings

- Reverse-engineering charts to executable code enables systematic seed-controlled counterfactual generation.
- VLMs that answer original chart questions correctly often fail their counterfactual variants.
- Failures are most common when the counterfactual demands a visual-reasoning path the original chart did not.
- The framework applies to existing chart-QA datasets without re-curating tasks.

## How this fits prior wiki state

Chartographer joins today's eval-rigor cluster alongside LiveBrowseComp ([[2026-05-28-livebrowsecomp-search-agents-priors]], same memorization-vs-reasoning frame), HRBench ([[2026-05-28-hrbench-thinking-mode-switch]], thinking-mode switching has no universal best strategy), VibeSearchBench ([[2026-05-28-vibesearchbench-long-horizon-search]], progressive-disclosure simulator drops best F1 to 30.30), and ITBench-AA (yesterday). The shared finding is that static benchmarks systematically overstate model capability because the original test inputs are partially memorized; counterfactual or live-fact reformulations expose the gap.

The Chartographer trick of reverse-engineering data into generative code so counterfactuals can be produced programmatically is the operational primitive. The same approach should transfer to any visual-reasoning benchmark whose original test items can be reconstructed as code.

## Related pages

- [[2026-05-28-livebrowsecomp-search-agents-priors]] — eval-rigor finding on search agents
- [[2026-05-28-vibesearchbench-long-horizon-search]] — progressive-disclosure user simulator
- [[2026-05-28-hrbench-thinking-mode-switch]] — thinking-mode benchmarking
- [[agent-benchmarks]] — concept page

## Research angle

The natural extension is reverse-engineer-and-mutate as a general benchmark hardening primitive. Any benchmark whose items can be reconstructed as code (charts, tabular reasoning, math word problems, code-execution traces) can be counterfactualized this way. The pattern across this week is that the field is converging on procedurally generated counterfactual evaluation as the next layer of benchmark rigor. The harder open question is whether models can be trained on the counterfactual distribution without overfitting to it, which would close the loop from evaluation back to training.
