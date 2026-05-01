---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-01T08:07:09.911670+00:00
title: Codex CLI 0.128.0 adds /goal
url: https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything
published: 2026-04-30
author: 
---

# Codex CLI 0.128.0 adds /goal

<p><strong><a href="https://github.com/openai/codex/releases/tag/rust-v0.128.0">Codex CLI 0.128.0 adds /goal</a></strong></p>
The latest version of OpenAI's Codex CLI coding agent adds their own version of the <a href="https://ghuntley.com/ralph/">Ralph loop</a>: you can now set a <code>/goal</code> and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted.</p>
<p>It looks like the feature is mainly implemented though the <a href="https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/continuation.md">goals/continuation.md</a> and <a href="https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/budget_limit.md">goals/budget_limit.md</a> prompts, which are automatically injected at the end of a turn.

    <p><small></small>Via <a href="https://twitter.com/fcoury/status/2049917871799636201">@fcoury</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/prompt-engineering">prompt-engineering</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/system-prompts">system-prompts</a>, <a href="https://simonwillison.net/tags/codex-cli">codex-cli</a>, <a href="https://simonwillison.net/tags/agentic-engineering">agentic-engineering</a></p>
