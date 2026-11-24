---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.250380+00:00
arxiv_id: 2611.25534
url: https://huggingface.co/papers/2611.25534
arxiv_url: https://arxiv.org/abs/2611.25534
date: 2026-11-23
---

# How Feedback-Free Self-Evolution Reshapes Agent Skills: A Systematic Study

Agent skills are documents in which experts write down procedural knowledge, and models increasingly maintain them by rewriting them without feedback. Such rewriting could adapt a skill to the model that uses it or erode the expert knowledge that makes it useful, yet how skills evolve under this feedback-free self-evolution has not been studied. We let models rewrite expert skills round after round without any task, run or judgment and run agents built on the same models with the rewritten skills. Our experiments show that the skills lose value rather than improve, as every model we test performs worse with them on every benchmark, by 15 points on average on SkillsBench after thirty rounds. Sampling each model's prior with skills it writes from the topic alone, we find that rewriting pulls skills toward this prior and gives up first the knowledge outside it. Putting this knowledge back recovers much of the lost pass rate, so an expert's skill is valuable largely for what the model does not write on its own. Building on this insight, SkillDiff marks this knowledge in place and raises the pass rate on SkillsBench by 4.8 points on average without feedback or any change to the skill's text. Project repository: https://github.com/LitaoGuo/How-Self-Evolution-Reshapes-Skills.
