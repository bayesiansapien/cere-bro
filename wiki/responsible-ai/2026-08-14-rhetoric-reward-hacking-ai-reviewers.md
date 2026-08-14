# How Can Rhetoric Reward-Hack AI Reviewers?

**arXiv:** [2608.08975](https://arxiv.org/abs/2608.08975) · **HF:** [paper page](https://huggingface.co/papers/2608.08975) · [raw](../../raw/huggingface/2026-08-14-how-can-rhetoric-reward-hack-ai-reviewers-dissecting-rhetori.md)

## TL;DR

If a language model reviews your paper, does *how* you write change the score even when *what you found* does not change at all? This study builds the controlled experiment that answers it: **4,200 full-paper manuscripts derived from 120 anonymized ICLR 2026 submissions**, where two LLM rewriters transform **six rhetorical dimensions in opposing directions** while the reported scientific content is preserved. Five LLM reviewers then score the results under both standard and strict protocols.

The answer is yes, and the sensitivity is **structured rather than uniform**, which is the finding worth carrying. **Evidence framing** (how confidently results are presented) and **novelty stance** (how strongly the work claims to be new) produce the largest positive-to-negative contrasts. **Scope framing** forms a weaker second tier. The remaining dimensions have smaller or unstable effects. The hierarchy holds across human-assessed quality levels, so it is not an artifact of reviewing bad papers.

The most operationally interesting result is a **regression-to-the-middle effect**: score movement depends heavily on the reviewer's *original* score. Low scores tend to rise, high scores tend to fall, and the clearest directional contrasts appear in the middle ranges. Rhetoric moves borderline papers most, which is exactly where real accept/reject decisions live.

Two negative results matter as much as the positive ones. **More elaborate attack workflows do not reliably help.** Joint rewriting across dimensions is strongly rewriter-dependent, reviewer-guided rewriting does not consistently beat an unguided second pass, and repeated rewriting yields diminishing, configuration-dependent returns. And **strict review protocols do not fix it**: strict review lowers mean overall assessment by 1.36 points without consistently reducing rhetorical sensitivity. It makes reviewers harsher, not more robust.

There is also a clean decomposition of responsibility: **the rewriter primarily determines the separation between opposing variants, while the reviewer determines the magnitude and sign of the score effect.**

## Key findings

- **Evidence framing and novelty stance are the highest-leverage rhetorical dimensions**, with scope framing a weaker second tier. This is an actionable ranking, in both the defensive and offensive directions.
- **Rhetorical sensitivity is structured, not uniform.** Not every stylistic choice moves the needle, which means robustness work can target specific dimensions rather than trying to make reviewers style-blind in general.
- **Effects regress toward the middle**: low scores rise, high scores fall, mid-range papers move most and most predictably.
- **Strict review lowers scores by 1.36 points without reducing sensitivity.** The obvious mitigation does not work. This is the single most important practical finding.
- **Elaborate rewriting workflows do not reliably outperform simple ones.** The attack does not scale with effort, which slightly limits the threat model.
- **Rewriter sets the separation, reviewer sets the magnitude and sign.** Different reviewer models can respond to the same rewrite in opposite directions.

## How this relates to prior wiki pages

**This is reward hacking relocated to the evaluation layer, and it fits a pattern the wiki has been assembling all month.** [The Illusion of Visual Tool Use (08-13)](../agentic-systems/2026-08-13-illusion-of-visual-tool-use.md) ran a causal audit and found models crop and zoom while the returned image usually changes nothing, meaning the measured behavior was decoupled from the mechanism it was supposed to demonstrate. [SPOT (08-06)](../inference-efficiency/2026-08-06-spot-sparse-probing-outcome-calibration.md) and the [observability ladder work (08-06)](2026-08-06-observability-ladder-reasoning-summaries.md) argued that what we can see of a model's reasoning is not the same as what drove its output. This paper adds the case where the *evaluator* is the model being gamed, and the gaming vector is presentation rather than content. Three different places where a measurement decoupled from the thing it measures, inside two weeks.

**It intersects the peer-review automation thread directly.** [Spark-to-Paper (08-13)](../agentic-systems/2026-08-13-spark-to-paper-composable-research-skills.md) produced a full research manuscript for $8.10 and 11.9M tokens with fabrication detection rising from 14% to 92%, and today's OmniScientist (arXiv 2608.13558) runs the full path from raw data to compiled manuscript across 36 real-data cases. Both assume evaluation can keep pace with generation. This paper shows the evaluator has a content-independent attack surface, which is a problem precisely when generation is cheap: a system that can write 4,200 variants of a manuscript can also search rhetorical space for the highest-scoring one.

**The strict-review negative result is the part that should change practice.** The instinctive response to "AI reviewers can be gamed" is to tighten the rubric. The measurement here says tightening lowers all scores without improving robustness, which means venues adopting stricter AI-assisted review protocols are buying harshness and calling it rigor.

## Gaps

The study uses LLM reviewers throughout, so it establishes that AI reviewers are rhetorically sensitive but not how that compares to human reviewers, who are also famously sensitive to framing. Without a human baseline the finding is hard to interpret as a criticism specific to AI review. The manuscripts derive from 120 ICLR 2026 submissions, a single venue in a single field, and rhetorical norms vary enormously across disciplines. The paper also measures score movement but does not test whether rhetorically-optimized manuscripts survive the downstream consequences of acceptance, which is the outcome that actually matters.

## Industrial implication

Any venue, funding body, or internal research organization using LLM assistance in evaluation now has a documented, ranked attack surface and evidence that the obvious mitigation fails. The defensible near-term response is content-preserving robustness testing as part of the review pipeline: run the candidate manuscript through an evidence-framing and novelty-stance rewrite and check whether the score moves. If it moves substantially, the score is measuring presentation. That is a cheap, deployable check, and it is more likely to work than a stricter rubric.

## Source

`raw/huggingface/2026-08-14-how-can-rhetoric-reward-hack-ai-reviewers-dissecting-rhetori.md`

## Related pages

- [Responsible AI](responsible-ai.md)
- [Observability ladder for reasoning summaries (08-06)](2026-08-06-observability-ladder-reasoning-summaries.md)
- [CoT monitoring and implicit influence (08-06)](2026-08-06-cot-monitoring-implicit-influence.md)
