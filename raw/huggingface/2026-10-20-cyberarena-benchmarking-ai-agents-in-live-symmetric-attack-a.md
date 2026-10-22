---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.19005
url: https://huggingface.co/papers/2610.19005
arxiv_url: https://arxiv.org/abs/2610.19005
date: 2026-10-20
---

# CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat

AI agents are demonstrating increasingly strong offensive and defensive cybersecurity capabilities in the real world. Current benchmarks mostly evaluate agents in isolation against static targets. Real cyber operations, however, are dynamic and coupled: security postures constantly change as attackers and defenders adapt to each other in real time. Static benchmarks quickly saturate and miss an agent's ability to attack and defend simultaneously under live pressure. To address this gap, we present CyberArena, a dynamic, symmetric adversarial benchmark built around multi-round attack-and-defense combat. In isolated sandboxes, two agents compete under identical rules, acting concurrently as both attackers and defenders over continuously changing services. This converts static targets into evolving, semi-open challenges, directly testing an agent's speed and precision in discovering, exploiting, and patching vulnerabilities. To sustain the benchmark's longevity, an automated agentic pipeline continuously generates, reviews, and validates new environments. Furthermore, because pairwise contests are notoriously hard to quantify, we introduce a dynamical model that maps match dynamics into unified, multidimensional scores across offensive, defensive, and domain-specific capabilities. Evaluating 12 frontier LLM agents across 40 challenges in 466 matches, CyberArena separates model capabilities where single-agent baselines hit a ceiling. The trajectories read like a fight rather than an exam: defenders patch one hole and miss the next and certify repairs on stale evidence, while capable agents think a move ahead, planting backdoors for later rounds and, in one case, writing their own packet sniffer to watch the opponent. Beyond a benchmark, CyberArena serves as an adaptable, scalable experimental platform for future research on cybersecurity agents.
