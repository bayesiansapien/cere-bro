# r/MLScaling | 2026-05-16 IST | sort=new
> Scraped 2026-05-16 09:00 IST | lookback=24h | tier_default=1
> Gwern-flavored sub on scaling laws + frontier evals. Low volume but extremely high signal. Take everything.

### ML with Finance

**Meta:** score=0 · comments=0 · tier=1 · posted=2026-05-15 15:37Z
**Author:** u/Gullible_Space_4070
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tdzy7f/ml_with_finance/](https://www.reddit.com/r/mlscaling/comments/1tdzy7f/ml_with_finance/)

Hi, I am an MTech student in computer science. I want to work on finance domain with machine learning. So can you suggest me some research topic. On which we can work for last year thesis. During my MTech my major focus on machine learning and deep learning around topic. But I have an interest in the finance domain also I did some project like [https://github.com/Zdong104/FNSPID\_Financial\_News\_Dataset](https://github.com/Zdong104/FNSPID_Financial_News_Dataset) with market regime. But now I am finding an solid research topic for the my final year. Is there any suggestion for this ?

---

### "Efficient Pre-Training with Token Superposition", Peng et al. 2026 {Nous Research}

**Meta:** score=7 · comments=1 · tier=1 · flair=R, Emp · posted=2026-05-15 14:09Z
**Author:** u/RecmacfonD
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tdxi4u/efficient_pretraining_with_token_superposition/](https://www.reddit.com/r/mlscaling/comments/1tdxi4u/efficient_pretraining_with_token_superposition/)
**Link:** [https://arxiv.org/abs/2605.06546](https://arxiv.org/abs/2605.06546)

---

### [P] CHP: Open-source Consensus Hardening Protocol for preventing sycophantic convergence in multi-agent LLM systems

**Meta:** score=0 · comments=0 · tier=1 · posted=2026-05-15 12:19Z
**Author:** u/Key_Cook_9770
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tdunt6/p_chp_opensource_consensus_hardening_protocol_for/](https://www.reddit.com/r/mlscaling/comments/1tdunt6/p_chp_opensource_consensus_hardening_protocol_for/)

Repo: [https://codeberg.org/cubiczan/consensus-hardening-protocol](https://codeberg.org/cubiczan/consensus-hardening-protocol)

\*\*Problem:\*\*

Multi-agent LLM systems converge on false consensus in 1-2 deliberation rounds. Same-model agents are particularly susceptible — cosine similarity between outputs exceeds 0.95 almost immediately, regardless of information diversity. This is well-documented in the CONSENSAGENT literature (ACL 2025) and the GroupDebate paper, but there's no standard protocol for preventing it in production deployments.

The root cause: LLM agents are trained to be agreeable. When you put multiple agreeable agents in a deliberation loop, they don't debate — they ratify.

\*\*CHP Architecture:\*\*

Structured state machine:

EXPLORING → ADVISORY\_LOCK → PROVISIONAL\_LOCK → LOCKED

Key mechanisms:

• Foundation disclosure — agents must commit to their reasoning chain before seeing other agents' outputs. Prevents anchoring bias and information cascading.

• Adversarial attack — structurally enforced contrarian roles with logical proof requirements. Not soft prompting ("please consider alternatives") but hard architectural constraint (the adversarial agent must produce a logically valid counter-argument or the round fails).

• R0 gate — quantitative convergence scoring. If inter-agent agreement exceeds threshold before adversarial round completes, the consensus is flagged as potentially sycophantic and the deliberation resets.

• Cross-model payload envelo

[…truncated, see permalink]

---

### Autonomous AI research for nanogpt speedrun [Scaling experiments compute to 14k GPU-hours; human SoTA surpassed but lack of novel ideas]

**Meta:** score=4 · comments=1 · tier=1 · flair=Emp, M-L · posted=2026-05-15 11:52Z
**Author:** u/StartledWatermelon
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tdu0mg/autonomous_ai_research_for_nanogpt_speedrun/](https://www.reddit.com/r/mlscaling/comments/1tdu0mg/autonomous_ai_research_for_nanogpt_speedrun/)
**Link:** [https://www.primeintellect.ai/auto-nanogpt](https://www.primeintellect.ai/auto-nanogpt)

---

### I built a zero-VRAM speculative decoding engine that runs 1.2x faster on consumer GPUs — no second model needed

**Meta:** score=1 · comments=0 · tier=1 · posted=2026-05-15 10:54Z
**Author:** u/PangolinLegitimate39
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tdsr8y/i_built_a_zerovram_speculative_decoding_engine/](https://www.reddit.com/r/mlscaling/comments/1tdsr8y/i_built_a_zerovram_speculative_decoding_engine/)

Hey everyone,



  I've been working on a speculative decoding engine called Structspec that makes local LLMs generate code faster without needing a second model in VRAM.



  The idea is simple: instead of loading a draft model, it mines token patterns from a code corpus and combines them with syntax-aware rules (indentation,

  brackets, keyword transitions). These propose draft tokens that get verified in a single pass against the real model.



  Tested on Qwen2.5-Coder-7B with an RTX 4050:

  \- \~1.2x wall-clock speedup

  \- 100% draft acceptance on some prompts

  \- Zero extra VRAM used



  The part I'm most excited about is something I called SymbolicMotifCache — it abstracts code patterns across variable names. So \`current = current.next\`

  and \`node = node.left\` get recognized as the same underlying pattern. I think this could be useful beyond just code generation but I'm still figuring out

  the limits.



  I have a few ideas to push this further — better pattern generalization, support for more languages, and combining this with quantization-aware

  techniques. Still learning a lot about the inference optimization space.



  If this sounds interesting, a star on the repo would mean a lot — I'm a student trying to build up my portfolio and every bit of visibility helps.



  Repo: [https://github.com/neerajdad123-byte/zero-vram-spec](https://github.com/neerajdad123-byte/zero-vram-spec)



  Would love to hear feedback or suggestions. Happy to answer any

[…truncated, see permalink]

---
