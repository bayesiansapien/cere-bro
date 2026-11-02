# I Don't Fear AI Slop. I Fear Untold Stories (Zack Proser, WorkOS)

**Channel:** AI Engineer
**Published:** 2026-11-02
**Source:** https://www.youtube.com/watch?v=1et3Lb_KLQo

## TL;DR
Proser argues that the bigger loss is not AI slop but good work that never gets written up because engineers think "I'm not a writer." His fix is to "build a factory." An expert encodes their taste for a craft into an automated pipeline and hands it to people who would otherwise not produce anything. At WorkOS, his Slack-native "Blog Bot" (on Cloudflare, connected to Granola, Slack, and image generation) produces 85 to 90% complete on-brand drafts and raised publishing velocity across the org. Quality is protected by human ownership. A person shapes the draft and signs it, and the bar is "Is it true, useful, beautiful, and does it help anyone?"

## Key Takeaways
- **Asymmetric leverage:** a simple interface (Slack mention) sits on top of a complex system with data connectors to every internal source, custom tools, human-in-the-loop fact confirmation, and an image endpoint tuned to match the design team's style.
- **Output quality:** drafts are 85 to 90% done, not one-shot ready to publish. A human must read the whole thing, iterate, and put their name on it.
- **Craft framing (from WorkOS founder Michael Grinich):** a cymbal factory mass-produces at machine speed, but a veteran musician still plays and approves every unit. Craft runs through the whole line, not just the hand-made parts.
- **Blacksmith metaphor:** the human is the spark (decides a story is worth telling), the bellows (keeps shaping drafts across many iterations), and the quench (publishes and stands behind every claim).
- **Process equivalence:** if a reader can't tell hand-written from "14 LLM iterations plus hand edits," the process doesn't matter to them. Judge the artifact.
- **Factories for small audiences:** he built a bedtime-story app for his two toddlers in 4 hours with Opus. It turns the day's photos into narrated, animated stories starring the kids, with voice control for "again, again." Repeat requests average about 3 per story.
- **Call to action:** find the craft where you have strong opinions, encode them into a tool, and give it to someone who doesn't normally create.

## Architecture & Optimization Mechanics
- **Taste distillation as a product pattern.** The "factory" is a system prompt, a set of tools, and a retrieval layer that encodes one expert's quality rubric. It is effectively **distilling a human expert's preference model into a reusable pipeline**, the prompt-level counterpart of distilling a teacher model into a student.
- **The design that matters:** the human checkpoint sits at the *end* (quench), not throughout. Generation is cheap and verification is concentrated. This mirrors speculative decoding: a cheap drafter proposes, and an expensive verifier accepts or rejects.
- **Weak spot:** "publishing velocity increased" has no numbers attached (no post counts, traffic, or engagement). The equivalence claim also ignores reader trust costs (see below). The talk is more conviction than evidence.

## Grounded Context (Web Enrichment)
The "readers flinch" objection Proser describes is backed by research. A 2026 ACM FAccT study, "Full Disclosure, Less Trust?" (Prajod et al.), found that **detailed** AI-use disclosures lowered reader trust and subscription intent, one-line disclosures did not, and both increased source-checking. About two-thirds of participants still *wanted* detailed disclosure ([arXiv 2601.09620](https://arxiv.org/abs/2601.09620)). The sample was small (n=40, news only), but the result complicates Proser's "process doesn't matter to the reader" claim. Readers say they want process transparency, and then trust less when they get it. A human byline plus accountability, which is his "quench," is the practical way through.

The "factory for two people" point lines up with the 2026 trend toward disposable, personal software built in hours with frontier coding agents. The economics have flipped. An audience of two now justifies a custom app because build cost has collapsed to an afternoon.

## Real-World Application / Actionable Step
- **Build a "research writeup factory" for your team:** a Slack or CLI bot that takes an experiment run ID (W&B or MLflow), pulls configs, eval tables, and the relevant PR diffs, and drafts an internal or external post in your house style (claim, setup, numbers with std, caveats). You own the rubric. Teammates who never write up their pruning or routing results now will.
- **Put the verifier at the end:** require the author to confirm every number against the source run before posting. Automate generation, and keep sign-off human.
- **Encode your taste explicitly:** write down the 10 to 15 rules you use to judge a compression or routing paper (baselines, hardware-realistic latency, quality metrics beyond perplexity). That list is your factory's system prompt and is reusable for reviewing papers too.
