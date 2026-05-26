# Google DeepMind's AlphaProof Nexus solves decades-old math problems for a few hundred dollars

**Source:** [The Decoder](https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/), 2026-05-25.
**Topic:** AI for mathematics / formal-proof systems.

## TL;DR

DeepMind's AlphaProof Nexus has autonomously solved nine open Erdős problems, including two that have stood for 56 years, at a reported inference cost of a few hundred dollars per problem. The system is built on the Lean compiler: every proof step is mechanically verified rather than relying on human review. The headline accuracy is a 2.5 percent overall success rate on the open-problem set Nexus was run against, which is low in isolation but high relative to the prior baseline of "essentially zero autonomous discovery of long-standing open problems."

## How this differs from OpenAI's Erdős result

OpenAI's earlier counterexample to the unit-distance conjecture (covered in DAIR.AI's 2026-05-24 weekly Top AI Papers, reaching the wiki via Gmail starred and the 2026-05-25 LWiAI podcast) produced a natural-language proof that nine external mathematicians (including Noga Alon, Tim Gowers, Melanie Matchett Wood) then verified and rewrote. AlphaProof Nexus does the opposite: the proof is written directly in Lean and is verified mechanically by the compiler before a human ever reads it. Two different bets on what an AI math system should look like:

- **OpenAI Erdős (natural language)**: produces a candidate proof in mathematical prose. Human experts verify and translate. The bottleneck is human time after the model.
- **DeepMind AlphaProof Nexus (Lean)**: produces a Lean program. The Lean compiler verifies. The bottleneck is the formalization burden on the input side and the model's ability to navigate Lean's tactic space.

Both approaches have now produced novel mathematics on long-standing open problems within roughly two weeks of each other. That is a regime shift.

## Key facts

- Nine open Erdős problems solved autonomously.
- Two of the solved problems had been open for 56 years.
- Reported inference cost per problem: a few hundred dollars.
- Overall success rate over the open-problem set: 2.5 percent.
- Proof substrate: Lean (compiler-verified, no human verification loop on the substance).

## How this relates to prior wiki pages

This extends the 2026-05-24 thread (DAIR.AI summary of the OpenAI unit-distance result + LWiAI podcast roll-up on 2026-05-25) on AI math research as a credible source of novel results. The DAIR.AI summary explicitly raised the open question of whether the OpenAI result was a one-off or the start of a regime. AlphaProof Nexus, landing nine days later with a different methodology and a different lab, suggests the regime view is correct. The two systems collectively put AI in a position to contribute novel mathematics rather than merely solve graded-curriculum problems.

For long-running wiki threads on agentic discovery, this also connects to AutoTTS (the 2026-05-11 paper covered in the 05-25 digest) where Claude Code searched the algorithm-design space for $40 and found a 70-percent-cheaper alternative to self-consistency. AlphaProof Nexus and AutoTTS are different domain points on the same curve: autonomous AI systems are now producing genuinely new mathematical and algorithmic results at low marginal cost.

## Research angle

The 2.5 percent success rate is the load-bearing number. It says: the system fails 97.5 percent of the time, but succeeds non-trivially. The selection problem (which problems to try, how to budget) becomes the limiting factor on practical throughput. The next open problem worth tracking is whether AlphaProof Nexus's Lean-native approach can be coupled with the OpenAI-style natural-language exploratory phase, with Lean used as the verifier at the end. That would combine OpenAI's broad exploratory reach with DeepMind's mechanical-verification rigor and is the obvious composition for the next system.

## Industry implication

If a major math journal accepts an AI-generated proof on its own merits (no human-readable companion paper required), the credit and authorship question gets rewritten. DeepMind's Lean-verified output is structurally closer to that bar than a natural-language proof. Within 12 months it is plausible that a top-tier journal publishes a Lean-formal proof of a long-standing open problem with an AI system listed as primary author.
