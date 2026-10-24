---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.886309+00:00
arxiv_id: 2610.22722
url: https://huggingface.co/papers/2610.22722
arxiv_url: https://arxiv.org/abs/2610.22722
date: 2026-10-23
---

# The LLM-Attacker: A Unified Red-Team Framework for Privacy Evaluation of Split and Distributed LLM Systems

Split language models keep input text on a client but send intermediate representations to a server. Attacks can reconstruct text from these messages. Comparing privacy evaluations is difficult when attackers see different messages, know different model weights or use different datasets and recovery measures. We present LLM-Attacker, a framework that records these choices and lets researchers check, compare and extend an evaluation. Compatible attacks reuse recorded messages, and their predictions are saved for independent scoring. The scoring rule requires a linked undefended reference before a defence can pass. Reports also identify attacks that remain untested. In a controlled GPT-2 experiment, adding gradients returned during training increased token recovery from 94.20% to 97.38% and exact-document recovery from 13.71% to 37.77%. The 95% interval for the token gain lay above the two-percentage-point threshold fixed before testing. This experiment is shared with a companion study; here, it tests how the evaluation responds to a change in attacker access. Further studies measure how corpus choice and compression defences affect recovery, compare an adapted published attack with its reference implementation, and test the measurement code. The framework reports implementation checks separately from measured attack effectiveness. Each privacy claim should state the attacker, dataset and scoring rule, report its controls and identify untested attacks.
