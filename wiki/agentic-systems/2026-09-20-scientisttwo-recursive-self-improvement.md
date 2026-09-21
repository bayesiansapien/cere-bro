# ScientistTwo and the RSI argument: automating experimentation long before judgement

**Date:** 2026-09-20
**Topic:** agentic-systems
**Sources:** X home feed ([@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2101449041091657746), [@ai_database](https://x.com/ai_database/status/2101216062570410407)) · [Interconnects, *Where I stand on RSI*](https://www.interconnects.ai/p/where-i-stand-on-rsi)
**Raw:** `raw/twitter/feed/2026-09-20-morning-ranked.json`, `raw/gmail/2026-09-20-starred.md`, `raw/rss/2026-09-19-interconnects-ai-why-i-still-haven-t-bought-into-true-rsi.md`

---

## TL;DR

Two things landed on the same day and they read against each other usefully.

**ScientistTwo** (Google) is an automated research loop rather than a research assistant. Given a
problem statement, it proposes ideas, runs experiments, prunes what does not help, takes reviewer
feedback, and starts another round. Critically, it then **uses its own discovery as the new baseline
and improves again**. Across problems drawn from accepted ICLR, ICML and NeurIPS papers, the reported
numbers are an **80.4% success rate, improvements over the original human baseline on 86 of 107
problems, and a 25.2% average relative improvement**. Cost is about **2.5 days and $3,765 per paper**.
At least one case chained three consecutive record-breaking rounds. Nine experienced researchers
rated the outputs roughly level with the human papers overall.

**Nathan Lambert's essay** argues the opposite reading of the same era. His position, which he calls
lossy self-improvement, is that automatable research is too narrow to net a large acceleration
against the exponential cost curve of scaling laws, that parallel agents have real diminishing
returns, and that resource and political bottlenecks dominate in ways AI cannot accelerate. He quotes
Richard Ngo's framing: the short-timeline camp will turn out directionally correct relative to
outsiders but factually wrong, and things will move fast enough that it will *feel* like they were
right.

---

## The specific tension, stated precisely

ScientistTwo is evidence for exactly the thing Lambert concedes and then bounds. His claim is not
that automated research fails; it is that **automatable research is narrow**. ScientistTwo's own
framing agrees more than the headline suggests: it reports that experimentation can be automated long
before scientific judgement can. Every one of its 107 starting points is a problem humans posed and a
venue's reviewers selected. The loop improves a method; it does not choose what is worth improving.

That is the load-bearing caveat and it should not be lost. The evaluation is also mostly AI-refereed:
outputs were scored by a reviewer model, with a rebuttal model running additional experiments until a
passing grade, and **nothing was actually submitted to a conference and accepted**. A 25.2% average
relative improvement measured on benchmarks the original papers chose is a real result about
benchmark optimisation, and a much weaker result about science.

The timelines from the Dwarkesh trio episode that Lambert summarises give the useful spread. On a
10x productivity uplift for AI researchers: John Schulman says about 2 years, Beren Millidge finds
that plausible, Charlie O'Neill says 5 to 10 with the bottleneck being absorbing information and
deciding which experiment to run next. **O'Neill's stated bottleneck is precisely the half
ScientistTwo does not do.**

---

## How this sits against the wiki

**It lands on the bar that [self-evolving agents](self-evolving-agents.md) set on 09-13.** That entry
recorded a definition arriving and every system on the page sitting below it. ScientistTwo is the
strongest candidate yet to clear it, because the self-baselining step is genuine recursion rather
than a single improvement pass: round N+1's reference point is round N's output. Whether it clears
the bar depends on whether improvements compound or saturate, and three rounds is not enough data to
tell. The page's standing question, whether the loop improves the *artifact* or the *improver*,
remains unanswered here: ScientistTwo produces better methods, not a better ScientistTwo.

**It is the research-side mirror of the harness thread.** [SoL-Pi
(09-11)](2026-09-11-sol-pi-harness-auto-research.md) had NVIDIA and MIT run an automated research
loop over agent *scaffolding* rather than over ML methods, evolving four runtime mechanisms and
cutting tokens 45-49% at about 94% of task score. Chinese-language coverage of SoL-Pi circulated
widely on the feed today with the sharper framing: the argument is not about which model is cheaper,
it is that the scaffold is where the money leaks, and a team watching model prices while ignoring
harness efficiency is optimising the wrong line item. **Two automated research loops, one over
methods and one over harnesses, both reporting large wins, is the pattern.** The open question is
whether either loop's gains survive contact with a problem the loop did not get to choose.

**The economics argument is the one to track.** Lambert's sharpest point is that labs may not be able
to hold a constant fraction of compute on internal R&D as total volume rises, particularly under IPO
scrutiny. That is a falsifiable, near-term claim about capital allocation, and it intersects directly
with OpenAI's reported $278 billion cash-burn forecast through 2030 and the
[open-weight token share inversion (09-20)](../ai-industry/2026-09-20-open-weight-token-share-inversion.md),
where open models took 78.4% of gateway token volume while closed models kept 21.6% of volume and the
majority of the revenue. A lab whose volume business is eroding has less slack for speculative
internal R&D, not more.

---

## Gaps

No arXiv identifier was captured for ScientistTwo in any of today's sources, so everything here is
reconstructed from two social summaries of a Google report and should be treated accordingly. The
$3,765 per paper figure has no stated breakdown. The most important missing experiment is the
obvious one: run the loop on problems drawn from *rejected* papers, or from open problems with no
established baseline, and see whether the 80.4% survives. Improving a published method on its own
benchmark is the easiest version of the task.

---

## Related pages

- [Self-evolving agents](self-evolving-agents.md)
- [Agent harness engineering](agent-harness-engineering.md)
- [SoL-Pi: harness auto-research (09-11)](2026-09-11-sol-pi-harness-auto-research.md)
- [SoL-Pi recursive harness research loops (09-18)](2026-09-18-sol-pi-recursive-harness-research-loops.md)
- [Compute economics](../hardware/compute-economics.md)
- [Responsible AI](../responsible-ai/responsible-ai.md)
