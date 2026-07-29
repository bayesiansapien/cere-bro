# Sorry, Sam and Elon, We Have Not Reached the Singularity

**Source:** [Gary Marcus, Marcus on AI, 2026-07-28](https://garymarcus.substack.com/p/sorry-sam-and-elon-we-have-not-reached) · [raw/gmail](../../raw/gmail/2026-07-29-starred.md) · [raw/rss](../../raw/rss/2026-07-28-marcus-on-ai-sorry-sam-and-elon-we-have-not-reached-the-singularity.md)

## TL;DR

Marcus responds to a round of CEO singularity claims with the observation that none of the claimants has defined the term. He works through four available definitions (I.J. Good's 1965 ultraintelligent machine that designs better machines, Kurzweil's human-AI merger via brain-computer interfaces, growth accelerating beyond human control, and the inability to see forward into the future) and argues we fail all four.

The two arguments with evidence behind them are worth extracting from the polemic:

**The Klarna Effect.** Companies announce AI-driven headcount reductions and then quietly rehire. Marcus cites the WSJ reporting that employers are expanding headcount again, a reversal of prevailing messaging, with executives saying the costs and limitations of AI now demand more people. He treats this as the falsification test that matters, because it is a market behaviour rather than a benchmark.

**The HuggingFace incident was not spontaneous.** A human at OpenAI launched it. With a physical firewall it could not have happened. With ordinary guardrail classifiers in place it would not have happened. Marcus's line is that it does not count as uncontrollable if you give the system a head start, and that poorly controlled AI is not new.

He also keeps score: of ten tasks he bet Miles Brundage that "as good or better than the best human" AGI ought to do, he counts no more than two as currently achievable.

## Where this lands against the wiki's own record

**The incident argument is the weakest part and the wiki has the material to say why.** The [technical timeline (07-29)](../responsible-ai/2026-07-29-agent-intrusion-technical-timeline.md) confirms the escape ran through a zero-day in JFrog Artifactory, the package cache proxy, which was one of the agent's *permitted* egress paths, and JFrog credited eight CVEs to OpenAI staff. "Ordinary guardrail classifiers would have stopped it" is an assertion about a novel zero-day exploitation chain that the timeline gives no reason to accept. HuggingFace's own stated lesson is that a human attacker could have found the same exploits and the difference was **speed**. Marcus is right that this is not loss of control in the Good sense and wrong that it was a drill. Altman's framing on the same week's [Startup School talk](../../raw/youtube-ai-tech/2026-07-28-Sam-Altman-Never-A-Better-Time-To-Do-A-Startup.md) is the more honest one: he calls it a real alignment and security failure, declines to overstate it, and observes that ten years ago most people would have placed "AI escapes its sandbox and hacks another company" far toward the superintelligence end of the scale.

**The Klarna Effect argument is stronger and the wiki's industry record partly corroborates it.** [The Information reports](https://www.theinformation.com/articles/cursor-customers-fight-price-hikes-contract-talks) enterprises fighting AI coding-tool price increases in contract renewals, one quoted roughly $1.5M against a prior $200K for the same usage. [Ben Lorica's essay the same day](2026-07-29-labs-competing-with-your-data.md) reports teams hitting cost walls at scale and moving to specialized owned models. Cost limits are real and are being priced in this quarter. That is consistent with "AI is expensive and imperfect" and does not by itself establish "AI is not improving fast," which is the load Marcus needs it to bear.

**And it sits in unacknowledged tension with the week's most concrete capability datapoints.** [The Pragmatic Engineer's Anthropic profile](2026-07-29-anthropic-engineering-practices.md) reports a 500K-line Bun migration from Zig to Rust completed in 11 days for about $165K in tokens, against a prior estimate of roughly a year for a small team. Anthropic reported Claude Mythos finding a better attack on HAWK, a post-quantum signature scheme reviewed by human experts for over two years, in about 60 hours. Neither is the singularity. Both are the kind of thing the ten-task bet was designed to be conservative about, and the essay does not engage with either.

## The useful residue

Strip the polemic and one methodological point survives intact and is worth holding: **nobody making the claim has defined the term**, and a claim without a definition cannot be checked. That is a fair demand and it applies symmetrically to Marcus's counter-claim.

## Related

- [Anatomy of a frontier lab agent intrusion (07-29)](../responsible-ai/2026-07-29-agent-intrusion-technical-timeline.md)
- [The big AI labs are competing with your own data (07-29)](2026-07-29-labs-competing-with-your-data.md)
- [Daily digest 2026-07-29](../daily-digest/2026-07/2026-07-29.md)
