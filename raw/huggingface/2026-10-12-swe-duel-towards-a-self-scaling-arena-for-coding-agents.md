---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.218562+05:30
arxiv_id: 2610.12569
url: https://huggingface.co/papers/2610.12569
arxiv_url: https://arxiv.org/abs/2610.12569
date: 2026-10-12
---

# SWE-Duel: Towards a Self-Scaling Arena for Coding Agents

Static coding benchmarks are fixed at release. Over time their tasks leak into training data, and stronger agents eventually saturate them. We argue that a benchmark should instead aim to be self-scaling: its tasks and oracles are created at evaluation time, so no content exists in advance to leak, and its difficulty is set by the participating agents rather than fixed at release. We introduce SWE-Duel, an arena in which two coding agents evaluate each other over mirrored Red-Blue turns. In each turn, the Red agent works on a real repository across three context-isolated sessions. It proposes and implements a new feature with feature tests, then embeds a subtle bug in that feature along with sealed bug-triggering tests. The resulting pull request is admitted only if (1) it passes the feature tests and the repository's existing tests while failing exactly the bug tests, and (2) a fresh session of the same agent can repair the bug blind, which rules out unsolvable tasks. The Blue agent then reviews the pull request without being told a bug exists. It wins only if its revision passes all three test suites, and then the two agents swap roles. We run a tournament among 11 model-harness participants on 15 repositories in five languages for 1,500 turns. The leaders win in different ways. GPT-5.5 with Codex CLI ranks first as the strongest solver, repairing 98.3% of the defects it reviews. Claude Opus 4.8 with mini-swe-agent ranks second as the strongest task author, with a 27.3% Red win rate. Finally, within one model family, tasks written by the newest version defeat a fixed-reference solver far more often than those of older versions (42.9% vs. 4.0%), giving preliminary evidence that task difficulty scales with task authoring capability.
