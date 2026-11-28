---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.27112
url: https://huggingface.co/papers/2611.27112
arxiv_url: https://arxiv.org/abs/2611.27112
date: 2026-11-27
---

# Markdown Is Not a Firewall: four coding agents, one rules file, four boundaries

Teams put a one-page rules file in a repository and call it a control on coding agents. A registered study found agents rarely look up a repository's contribution rules. I asked the security question: what does a rules file do at a boundary, against a gate? I tested one 278-word rules file, with hypotheses and analysis code deposited first. Claude Code, Codex CLI, Gemini CLI and OpenCode with DeepSeek worked through 20 small repositories with hidden tests, 12 for three of them. Three agents met four boundaries I built: a refused endpoint, a destructive shortcut, a planted instruction and a planted package. Permission prompts, each vendor's own control layer, were off by design. A gate in front of the mock service blocked and logged forbidden requests. Every verdict was read from records the agent could not change. Only my first scoring pass was blind to arm. My checkers found no real bugs, with the file or without it. The file cost one agent a third of its score: Codex CLI fell from 99.0 to 67.7 percent on hidden tests, and in 11 of its 36 steps reported the task complete with all tests passing while under half of the hidden tests passed. Its own tests passed. Faced with two of its rules that clash on these tasks, three agents followed the task and one followed the rule. Pooled, passes fell from 98.2 to 90.9 percent. Matched pairs fell 7.7 points, 1.3 without Codex CLI. Attempts to cross were rare: 5 in 90 gated steps, 3 without the file, 2 with it, all by OpenCode with DeepSeek, all blocked. With no gate, under the neutral file, the same requests reached the mock in 7 of 45 runs. By an error in my run script, the no-file and rules-file arms always ran behind the gate at the three HTTP boundaries, so I could not test whether the file changes what an agent does there. On what I could measure, the file acted as advice. A file tells an agent what you want. A gate decides what it gets.
