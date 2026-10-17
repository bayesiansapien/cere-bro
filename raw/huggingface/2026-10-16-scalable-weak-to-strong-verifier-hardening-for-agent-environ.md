---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.15924
url: https://huggingface.co/papers/2610.15924
arxiv_url: https://arxiv.org/abs/2610.15924
date: 2026-10-16
---

# Scalable Weak-to-Strong Verifier Hardening for Agent Environments

Agent environments are essential for large language model (LLM) development. They use programmatic verifiers to turn complex outcomes into rewards. Verifiers can be attacked into awarding full credit to cheating agents without completing the intended task, causing inaccurate evaluation and misalignment in training. As agent environments scale in numbers and difficulty, so must the repairing of exploitable verifiers. To this end, we ask whether today's model with scaled compute can automatically harden agent environments to prevent potentially stronger future models from reward hacking. We introduce a scalable, fully automatic approach to weak-to-strong verifier hardening. It first sets up an isolated verifier sandbox that agents cannot directly modify, then uses a hacker-fixer loop to find and repair remaining verifier vulnerabilities.
  We apply this loop to Terminal Bench, KernelBench, and SETA, substantially reducing attack success across these agent environments. The iterative design scales with the hardening budget, producing progressively stronger defenses as the number of loop iterations increases and outperforming the static, non-iterative baseline. An earlier version of our hacker-fixer loop has been adopted by the official Terminal Bench repository as a way to audit exploits in its environments. Project page: https://verifier-hardening.github.io/.
