---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.08960
url: https://huggingface.co/papers/2606.08960
arxiv_url: https://arxiv.org/abs/2606.08960
date: 2026-06-09
---

# Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops

Agent benchmarks score submissions with outcome verifiers that are typically hand-written and brittle, leaving them open to reward hacking. We audit 1,968 tasks across five terminal-agent benchmarks and find 323 (16%) hackable by frontier models given only the task description. This corrupts both leaderboard rankings and RL training signal, yet the standard response is manual and reactive.
  We introduce the hacker-fixer loop, a method for building exploit-resistant verifiers without per-task manual patching. The loop alternates three LLM agents: a hacker tries to pass the verifier without solving the task, a fixer patches the verifier to reject each discovered exploit, and a solver confirms the patched verifier still admits legitimate solutions. The loop iterates: each patch reshapes what the verifier rewards, surfacing the next exploit. We further add verifier access, and let patches transfer across tasks, to broaden the exploits the loop discovers.
  On KernelBench, the loop drives the attack success rate from 62% to 0% on a held-out corpus of publicly reported exploits. We also find that weaker agents in the loop can defend against much stronger hackers: Gemini 3 Flash's loop drives the stronger Gemini 3.1 Pro and Claude Opus 4.7's attack success rate from 76% and 61% to 0% on KernelBench, and Gemini 3.1 Pro's from 39% to 17% on Terminal Bench across 77 tasks. We release Terminal Wrench (323 hackable environments, 3,632 hack trajectories) as a snapshot of the current attack surface, our patched verifiers, the exploits the loop discovered, and our implementation as a basis for future work.
