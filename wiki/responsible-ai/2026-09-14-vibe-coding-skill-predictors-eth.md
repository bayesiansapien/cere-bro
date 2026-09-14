# What actually predicts success at vibe coding: a preregistered ETH Zürich study

**Source:** Thorgeirsson, Weidmann and Su, CHI '26. Surfaced 2026-09-14 via the X home feed, [@IntuitMachine](https://x.com/IntuitMachine/status/2099268716521226718). **Raw:** [feed capture](../../raw/twitter/feed/2026-09-14-morning-ranked.json)
**Date:** 2026-09-14

## TL;DR

"Vibe coding" is Karpathy's term for pure natural-language programming: you never see or touch the source code, you only write prompts and judge the running app. The industry story attached to it is that programming knowledge stops mattering and communication skill takes over. A **preregistered study with N=100** tested that directly, in a purpose-built environment where the code was genuinely hidden and only a live preview was visible, on expert-vetted GUI tasks (replicate a working app, add features to it, build a deliberately decontextualized toy app with no recognizable name). Participants also took established instruments for computer-science achievement, writing skill and general cognitive ability. **Computer-science knowledge is the stronger predictor, contributing roughly twice the unique variance of writing skill** (standardized betas 0.356 versus 0.244; zero-order correlations r = .39 and r = .29). CS achievement still predicts performance after controlling for general intelligence (partial r = .281), while writing's direct link weakens.

## The two findings that are not obvious

**1. Writing matters, but only through the prompt.** Prompt quality **mediated 52% of the writing-to-performance link**. Participants who wrote clearer, better-organized, more lexically diverse prompts (measured by MTLD and HD-D, standard lexical-diversity indices) produced substantially better applications. Writing skill does not help directly; it helps by producing a better specification. That is classic requirements engineering relocated into a chat box.

**2. Self-reported frequency of LLM use correlated *negatively* with performance.** r = -.258 with vibe-coding performance and r = -.282 with writing skill, and zero correlation with CS knowledge. Heavy casual users were **worse** at the exact skill the tools claim to democratize. The authors offer two non-exclusive explanations: over-reliance atrophies the ability to structure intent precisely, or weaker writers lean on LLMs more and the relationship is selection rather than causation. Either way, "just use it more" is not a training strategy.

## Why this is a responsible-AI item rather than a tooling item

The finding sits inside the deskilling question, and it has a measured shape rather than a rhetorical one. The same week, [The Decoder reported a two-year university study](https://the-decoder.com/two-year-university-study-finds-banning-ai-from-classrooms-leaves-students-worse-off/) in which a law professor compared an AI ban, unguided AI use and structured AI training across two cohorts: **the no-AI group finished last both years**, and the researcher wrote "I was wrong," having assumed unguided use would do more harm than good. **Put the two together and they are consistent rather than contradictory**: banning the tool loses, using it casually loses, and what wins is the combination of domain fundamentals plus deliberate specification practice. That is a much narrower and more actionable claim than either "AI makes students worse" or "AI democratizes programming."

## How this relates to what the wiki already knows

The [responsible AI page](responsible-ai.md) has tracked cognitive-offloading concerns mostly as assertion. This is the first preregistered measurement in that thread with a mediation model attached, and its practical reading for tool builders is specific: the bottleneck is not that users write bad prompts in the abstract, it is that they under-specify. The authors' own recommendations are prompt linters scoring clarity, completeness and boundary conditions in real time, and better state observability so a user can explore a running system without reading code.

**One caveat the authors flag themselves.** They tested *pure* vibe coding, with code fully hidden. In real hybrid tools where you can inspect and patch the code, CS knowledge should predict even more strongly, because it works through both the prompting channel and direct repair. **Pure vibe coding is the lower bound on how much programming knowledge matters, not the upper bound.**

## Gaps

Student population, single institution, GUI-app tasks only. The negative correlation with LLM-use frequency is self-reported usage, which is a weak instrument. And the study measures short-task performance, not the thing anyone actually cares about, which is whether a system built this way survives maintenance.

## Related pages

- [Responsible AI](responsible-ai.md)
- [Agent harness engineering](../agentic-systems/agent-harness-engineering.md)
