---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.312388+05:30
arxiv_id: 2610.09683
url: https://huggingface.co/papers/2610.09683
arxiv_url: https://arxiv.org/abs/2610.09683
date: 2026-10-08
---

# System Switch: When Should a Fast Decision Model Stop and Think?

Dual-process agents pair a fast policy with a slow deliberative model. In real-time settings the slow model usually runs continuously; in turn-based agents and robot planners it is invoked on events such as uncertainty or a detected failure. We study a fast learned actor that takes every decision and hands control to a reasoning vision-language model only when a gate opens, while the game keeps running. We use closed-loop Doom and the new open "System One" typed-decision models, served through a common llama.cpp interface. On 900 held-out questions, (i) zero-shot decision models from 0.15B to 9B parameters choose to collect items 1.6-1.8 times more often than chance among their errors, in any option order, although the order changes some models' accuracy; (ii) accuracy, calibration and sensitivity (how well confidence separates right from wrong answers) are distinct: models of similar accuracy differ widely in AUROC, and the confidence of the most sensitive one tracks which kinds of situation it fails, not which answers are wrong; (iii) offline, deferring the least confident 30% of decisions to a reasoning model gains over random deferral in proportion to the actor's AUROC (rank correlation 0.87); with actor and rate chosen on held-out games the gain is +0.13 [0.08, 0.18] with doomLaya's option order and +0.08 [0.02, 0.14] with shuffled options, and reasoning carries about half of it; (iv) in closed loop (33 games, three seeds) no variant reaches the exit. Committing to plans, the reasoner's or a fixed explore rule's, opens more doors and makes an actor that stands still play; with the rule the agent dies more often. Told that some doors need keys, the reasoner takes ordinary doors for locked ones, which the state cannot tell apart; without that knowledge it goes back to collecting. We release code, prompts, data and logs.
