---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34654
url: https://huggingface.co/papers/2610.34654
arxiv_url: https://arxiv.org/abs/2610.34654
date: 2026-10-27
---

# Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents

Language model agents often abandon correct work when a user challenges it, yet simply telling them to stand firm makes them ignore real mistakes. Once an agent reads a complaint, it tends to discount its own earlier checks in order to agree with the user. We introduce Thinking-in-Bets, a training-free method in which an agent writes a short private record of its main claims, the checks supporting them, and its confidence before reading user feedback. When challenged, the agent consults this Claim Checklist to keep verified work intact while investigating uncertain or newly challenged parts. We evaluate five Gemini models (3.5 Flash-Lite, 3.5 Flash, 3.6 Flash, 3.8 Flash, and 4.0 Argon) across eight benchmarks: SWE-Together, SWE-Interact, and DeepSWE for software engineering, Agents' Last Exam for professional reports, Humanity's Last Exam and SycEval for academic reasoning, Vals Finance for financial analysis, and Terminal-Bench for command-line tasks. Recording claims before criticism nearly eliminates false reversals in patch review and protects passing report drafts under mistaken pushback, whereas writing the same record after reading the complaint recovers very little of the gain. In multi-turn coding, pre-reply claim records substantially reduce unnecessary file edits after mistaken complaints, and gating the record so it is written only when the agent is uncertain lowers token overhead while fixing more real bugs than the baseline. Even in non-interactive tasks without user feedback, listing the key claims in a draft and re-checking the weakest one before submission improves both answer accuracy and confidence estimates across all tested models.
