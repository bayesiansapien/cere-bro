# r/MLScaling | 2026-05-15 IST | sort=new
> Scraped 2026-05-15 09:00 IST | lookback=24h | tier_default=1
> Gwern-flavored sub on scaling laws + frontier evals. Low volume but extremely high signal. Take everything.

### I trained Qwen3.5 to jailbreak itself with RL, then used the failures to improve its defenses

**Meta:** score=8 · comments=1 · tier=1 · posted=2026-05-14 23:39Z
**Author:** u/girishkumama
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tdf6he/i_trained_qwen35_to_jailbreak_itself_with_rl_then/](https://www.reddit.com/r/mlscaling/comments/1tdf6he/i_trained_qwen35_to_jailbreak_itself_with_rl_then/)
**Link:** [https://i.redd.it/s05xx0t5v61h1.png](https://i.redd.it/s05xx0t5v61h1.png)

---

### GET 1.3X WITH ZERO VRAM OVERHEAD!!!!!

**Meta:** score=0 · comments=0 · tier=1 · posted=2026-05-14 13:23Z
**Author:** u/PangolinLegitimate39
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tcy3h2/get_13x_with_zero_vram_overhead/](https://www.reddit.com/r/mlscaling/comments/1tcy3h2/get_13x_with_zero_vram_overhead/)

[https://github.com/neerajdad123-byte/zero-vram-spec](https://github.com/neerajdad123-byte/zero-vram-spec)  
I replaced draft model entirely with a python rule based AST predictor which seems working well in predicting grammer forced tokens and also indentations 

While doing this project i learnt many things about implementation of all types of spec decoding and also   
how tokens work and everything about MTP(multi token prediction) and many things 

Looking up for an intenship  
passion is to build things   
Leave a star for me it would be very much helpful to me

---

### Exploring Governance, Reliability, and Failure Boundaries in Autonomous Enterprise Systems

**Meta:** score=1 · comments=0 · tier=1 · posted=2026-05-14 11:23Z
**Author:** u/Dry-Ad-8454
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tcv7jk/exploring_governance_reliability_and_failure/](https://www.reddit.com/r/mlscaling/comments/1tcv7jk/exploring_governance_reliability_and_failure/)

Been thinking a lot about what governance, observability, and failure handling look like once enterprise systems become increasingly autonomous.

Most discussions around AI agents focus on capability. I’m more interested in reliability, control boundaries, and operational reality at scale.

That line of thinking led me to put together a book:  
*The Autonomous Enterprise: Architecture, Security, and Governance of Next Generation AI Agent Systems*

Book:  
[https://zenodo.org/records/18369118](https://zenodo.org/records/18369118)

Repo:  
[https://github.com/22louis2/the-autonomous-enterprise](https://github.com/22louis2/the-autonomous-enterprise)

I’d genuinely appreciate criticism, gaps, counterarguments, or perspectives from people working in this space. I’m still learning, refining my thinking, and would love strong feedback that can shape future iterations of the work.

---

### The 0% Challenge: Is any LLM actually "solving" SWE-Bench without memorization?

**Meta:** score=0 · comments=4 · tier=1 · posted=2026-05-14 08:34Z
**Author:** u/OK_Simon_666
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tcs037/the_0_challenge_is_any_llm_actually_solving/](https://www.reddit.com/r/mlscaling/comments/1tcs037/the_0_challenge_is_any_llm_actually_solving/)

I've been looking at SWE-Bench leaderboards on and off over the past few years, and something still feels fundamentally broken about how we define "agentic capability."

We keep seeing models hit 30%, 40%, or even 60%+ on SWE-Bench Verified. The hype train says we're nearing "AI Software Engineers." But here's the elephant in the room: contamination isn't just a bug. It's the feature.

The "Air-Gapped" Hypothesis

Consider a simple experiment: force models to resolve issues in a completely isolated environment. No internet access, No searching for similar PRs, No issue IDs in the prompt.

My hot take? Most frontier models would see their scores collapse toward 0%.

Why this might be happening:

Verbatim patching: There's a growing informal consensus among practitioners who've run internal de-contaminated evals that models aren't genuinely "reasoning" through a codebase. Instead, they appear to be recalling specific Git commit hashes and file paths — because large chunks of SWE-Bench exist verbatim in pre-training corpora.

The "search" proxy: Many high-scoring agents use browse/search tools. In practice, they often locate the original GitHub PR that fixed the exact issue they're supposed to solve. That's not engineering. That's plagiarism with a tool-use wrapper.

Environment reality check: A real engineer can debug a legacy, private repo they've never seen before. Current LLMs tend to fall apart the moment you move them from "popular public Python repo" to "private internal 

[…truncated, see permalink]

---
