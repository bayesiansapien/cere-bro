---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.17697
url: https://huggingface.co/papers/2610.17697
arxiv_url: https://arxiv.org/abs/2610.17697
date: 2026-10-16
---

# LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification

AI systems now write long and difficult mathematical proofs, and checking their step-by-step validity is becoming a bottleneck. A learned verifier could check proofs cheaply, but training one requires a correctness label on every step, and such labels are hard to obtain for open-ended proofs. Existing methods take them from human annotators, which is costly, or derive them from final answers, which proofs do not have, and formalizing each proof in Lean requires expert effort. We introduce LeanPRM, a framework that uses the Lean proof assistant to create step-level labels for natural-language proofs. A model writes a natural-language proof together with a paired formal proof, without feedback from Lean. Lean then labels every step, and a second model discards failures caused only by the formal syntax, so that the negative labels mark errors in the mathematics. LeanPRM contains 10,634 proofs with 152K labeled steps and no human annotation. A Qwen3-4B verifier trained on LeanPRM raises exact step-label accuracy on a held-out set of 200 proofs (LeanPRM-Bench) from 48.2 to 74.7, as opposed to 60.3 when the same base model is trained on PRM800K. It also selects better proofs in best-of-N selection on IMO-level problems, and outperforms the PRM800K-trained verifier on three of four external verification benchmarks. Training on LeanPRM improves verifiers at every size from 0.6B to 8B parameters on LeanPRM-Bench, Hard2Verify and IMO-GradingBench. Given the labels need no human annotation, LeanPRM can grow with the supply of formal statements, offering a path to step-level feedback on AI-generated proofs that are hard for humans to check.
