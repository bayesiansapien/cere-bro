---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "Changes to GitHub Copilot Individual plans"
url: https://simonwillison.net/2026/Apr/22/changes-to-github-copilot/#atom-everything
published: 2026-04-22
---

# Changes to GitHub Copilot Individual plans

<p><strong><a href="https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/">Changes to GitHub Copilot Individual plans</a></strong></p>
On the same day as Claude Code's temporary will-they-won't-they $100/month kerfuffle (for the moment, <a href="https://simonwillison.net/2026/Apr/22/claude-code-confusion/#they-reversed-it">they won't</a>), here's the latest on GitHub Copilot pricing.</p>
<p>Unlike Anthropic, GitHub put up an official announcement about their changes, which include tightening usage limits, pausing signups for individual plans (!), restricting Claude Opus 4.7 to the more expensive $39/month "Pro+" plan, and dropping the previous Opus models entirely.</p>
<p>The key paragraph:</p>
<blockquote>
<p>Agentic workflows have fundamentally changed Copilot’s compute demands. Long-running, parallelized sessions now regularly consume far more resources than the original plan structure was built to support. As Copilot’s agentic capabilities have expanded rapidly, agents are doing more work, and more customers are hitting usage limits designed to maintain service reliability.</p>
</blockquote>
<p>It's easy to forget that just six months ago heavy LLM users were burning an order of magnitude less tokens. Coding agents consume a <em>lot</em> of compute.</p>
<p>Copilot was also unique (I believe) among agents in charging per-request, not per-token. (<em>Correction: Windsurf also operated a credit system like this which they <a href="https://windsurf.com/blog/windsurf-pricing-plans">abandoned last month</a></em>.) This means that single agentic requests which burn more tokens cut directly into their margins. The most recent pricing scheme addresses that with token-based usage limits on a per-session and weekly basis.</p>
<p>My one problem with this announcement is that it doesn't clearly clarify <em>which</em> product called "GitHub Copilot" is affected by these changes. Last month in <a href="https://teybannerman.com/strategy/2026/03/31/how-many-microsoft-copilot-are-there.html">How many products does Microsoft have named 'Copilot'? I mapped every one</a> Tey Bannerman identified 75 products that share the Copilot brand, 15 of which have "GitHub Copilot" in the title.</p>
<p>Judging by the linked <a href="https://github.com/features/copilot/plans">GitHub Copilot plans page</a> this covers Copilot CLI, Copilot cloud agent and code review (features on <a href="https://github.com/">GitHub.com</a> itself), and the Copilot IDE features available in VS Code, Zed, JetBrains and more.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=47838508">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/github">github</a>, <a href="https://simonwillison.net/tags/microsoft">microsoft</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/github-copilot">github-copilot</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm-pricing">llm-pricing</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a></p>