# Jiayi Weng: Learning Beyond Gradients

**Source:** [trinkle23897.github.io blog post](https://trinkle23897.github.io/learning-beyond-gradients/) · amplified by [@MillionInt tweet](https://nitter.net/MillionInt/status/2053310486335324620#m) · [raw twitter file](../../raw/twitter/2026-05-10-morning.md)
**Tier:** 2 — Agentic systems / RL critique

## TL;DR

Jiayi Weng (former OpenAI / Tianshou author) argues that the next paradigm after pretraining and RL is **iterated heuristic learning**: a coding agent reads failures, edits a programmatic policy, runs it, and continues. As proof, Codex iterated a pure NumPy + cv2 closed-loop heuristic policy for VizDoom D3 Battle, no neural network training, no map, no object coordinates, no seed-specific routes. It works. The framing in the tweet that amplified it: "this is unfortunately mostly a bearish take on RL."

## What is being claimed

- The classical objection to heuristic policies (handcrafted rules, expensive to maintain, brittle) was a maintenance-cost argument, not a capability argument.
- Coding agents change the maintenance cost curve. A policy expressed in Python is now **continuously editable by an AI** in response to failures, in a tight read-failure-edit-run loop. The artifact lives in source control rather than weights.
- Continual learning has stalled in the neural-network frame because of catastrophic forgetting. In the program frame, "learning something new" is a code edit, not a parameter update, so adding a new capability does not overwrite an old one.
- Weng frames the open question explicitly: **could iterated heuristic learning be the next paradigm after pretraining, RLHF, and RL/RLVR?**

## Why this matters in light of prior wiki pages

This is the second non-RL alternative paradigm to land in three weeks.

- **2026-04-16 PreRL / DSRL** moved RL from P(y|x) to P(y) (the marginal). It is still RL, but at a different distribution layer.
- **2026-04-19 VGF** reframed behavior-regularized RL as optimal transport. Still RL, different math.
- **2026-05-10 (this post) Iterated heuristic learning** says: skip the gradient entirely, let the agent edit code.

If the wiki was reading these as "RL has multiple layers of improvement still to mine," Weng's piece is the alternative reading: "the gradient may be the wrong substrate to begin with for some classes of problem." He does not argue this universally, his demo is VizDoom D3 (a small policy with structured state), not a frontier agentic task. But the framing is the deeper claim.

The composition with the **skill curation cluster (StraTA, Skill1, SkillOS — 2026-05-09)** is direct. SkillOS already separates a frozen executor from a trainable curator that updates an external SkillRepo. Weng's framing is the next step: **the SkillRepo is just code, and the curator is the coding agent**. The persistent-skill-memory thread arrived at the same architecture from the agent side; Weng arrives at it from the RL-critique side.

The connection to **2026-05-08 ResRL** (negative-sample projection in RL) is also visible. ResRL is a careful structural fix to GRPO's bias. Weng would say: maybe GRPO is the wrong layer to fix.

## Open questions

- **What classes of problem benefit?** VizDoom D3 has dense, observable state and discrete action structure. The bet that this transfers to open-ended agentic tasks (web browsing, code review, multi-document research) is unproven.
- **The "code corpus" version of catastrophic forgetting.** Code edits do interfere. Add a new branch in a heuristic and you can break an old branch. The claim that "rules don't overwrite" is true at the file level but may not be true at the behavioral level.
- **What is the ceiling?** The headline VizDoom result is "works surprisingly well." Surprising relative to what? A pure-NN baseline trained for the same compute? A skill-augmented agent? The post does not give the comparison.

## Implication for cere-bro tracking

This is a meta-level signal worth flagging. The wiki has been logging RL-improvement papers (TIP 04-16, LongAct 04-18, PreRL 04-16, VGF 04-19, ResRL 05-08, Balanced Aggregation 05-09) as if RL is the substrate to fix. Weng's framing is that some classes of agentic learning may not need that substrate at all. If a major lab publishes an iterated-heuristic-learning paper at the frontier scale within 90 days, the framing-shift becomes load-bearing.

## Related pages

- [Skill curation cluster (StraTA / Skill1 / SkillOS, 2026-05-09)](2026-05-09-skill-curation-cluster-strata-skill1-skillos.md)
- [PreRL / DSRL (2026-04-16)](../llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md)
- [ResRL (2026-05-08)](../llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md)
- [RL for LLMs concept page](../llms-foundation-models/rl-for-llms.md)
