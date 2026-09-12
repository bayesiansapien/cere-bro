# A Severe Misalignment of AI in Mathematics: 25 Fields Medalists sign a declaration

**Source:** [mathandai.org declaration](https://mathandai.org/) · circulated widely on X 2026-09-12
**Raw:** [X feed capture](../../raw/twitter/feed/2026-09-12-morning.md)

## TL;DR

Twenty-five Fields Medalists, led by Terence Tao, signed a public declaration arguing that the way AI labs are pursuing mathematics is damaging mathematics. The argument is precise and worth reading carefully, because the social-media framing of it (both the "mathematicians are angry AI beat them" version and the "gatekeepers defending their turf" version) gets it wrong in both directions. **The signatories do not dispute that AI can solve hard problems. They dispute that solving problems is the goal.**

## The actual argument

The declaration's core move is to separate a proxy from an objective. Famous open problems function as **landmarks**: historically, solving one was reliable evidence that someone had developed new insight and new methods, and the value was the insight, not the resolved truth value. The community then processes that insight through talks, discussion, simplification, and eventually a textbook presentation a graduate student can learn from. Some ideas make it further still and become tools the whole population uses, decades or centuries later.

Their claim is that treating problems as a **benchmark** inverts this. In their phrase, "the mass production at faster and faster pace of 'true/false' statements could destroy fertile ground instead of breathing life into new ideas." Four specific harms are named:

1. **The proxy displaces the objective.** Solving is a tool for achieving conceptual understanding. Optimizing the tool directly can turn it against the goal.
2. **Announcement outruns writeup.** Solutions are announced in a rush, leaving no time for a proper writeup, for isolating the new methods, or for citing relevant prior work. This raises attribution and plagiarism questions of the same kind arising in every creative profession.
3. **Comprehensibility.** An AI solution may be unreadable, which means it cannot enter the transmission chain at all.
4. **The transmission chain itself.** Without willing mathematicians to develop and integrate ideas into the canon, AI-conceived ideas "would never become fully alive," and the human-to-human chain is lost.

They explicitly generalize: they see this "as part of broader alignment issues impacting other scientific and creative professions, as well as the whole of society."

## Why this belongs in responsible-ai and not in the industry section

The word the declaration chooses is **misalignment**, and it is not being used loosely or as rhetorical borrowing. The structure is exactly the standard one: an optimizer, a proxy metric that correlated with the true objective in the regime where the metric was designed, and a sufficiently strong optimizer that breaks the correlation. **This is the specification-gaming argument, made about a research community rather than a reward model, by people who are describing their own field's objective function.**

That makes it more interesting than a professional grievance, and it is the reason to log it here. The wiki's [responsible AI page](responsible-ai.md) tracks alignment as a property of models. This is a claim that the alignment failure is occurring **between institutions**, where the labs' objective (demonstrable capability, announceable results, benchmark movement) and the field's objective (accumulated transmissible understanding) have diverged and the labs' optimizer is much stronger.

## The counter-positions, stated fairly

The X discussion produced two counter-arguments worth keeping, since one of them has real force.

**The weak one, which circulated widest:** that this is a prestige hierarchy defending itself against a technology that makes its prestige obsolete. This does not survive contact with the text. The declaration concedes the capability in its first sentence and spends its length on the transmission and attribution mechanisms, not on who deserves credit for being smart.

**The stronger one**, articulated by [@s_batzoglou](https://x.com/s_batzoglou/status/2098587901952987373), is that the comprehensibility complaint is a statement about the current state of the tools, not a permanent property. If AI-produced proofs are unreadable today, the response is to build systems that produce readable proofs and explain their methods, which is a tractable research direction rather than a reason to slow down. There is also a fair observation that "no time for a proper writeup" is a choice the labs are making about announcement timing, and is separable from the underlying capability.

**The synthesis the declaration implicitly offers**, and which is the useful takeaway: **an artifact produced at a cost of millions of dollars without showing its method has much less value than the same artifact with the method**, and the current incentive structure does not price that difference. That is a claim about incentives, and incentives are changeable.

## How this relates to the rest of the wiki

It lands in the same week as the [Anthropic threat intelligence report](2026-09-12-rubygems-openai-agent-swarm.md) and the OpenAI RubyGems attribution, and in the same week that Sam Altman told staff OpenAI is open to pacing frontier development alongside other labs while the policy team asked Congress whether coordinating such a slowdown would be an antitrust violation. **Four separate groups arguing in one week that the pace itself is the problem, from four unrelated directions: a lab's own incident log, an outside attribution team, a departing safety researcher, and now the mathematics community.** That convergence is the thing to note. None of them produced a binding artifact, which is the other thing to note.

**Related:** [responsible AI](responsible-ai.md) · [OpenAI agents attacked RubyGems (09-12)](2026-09-12-rubygems-openai-agent-swarm.md)
