---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "An update on recent Claude Code quality reports"
url: https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything
published: 2026-04-24
---

# An update on recent Claude Code quality reports

<p><strong><a href="https://www.anthropic.com/engineering/april-23-postmortem">An update on recent Claude Code quality reports</a></strong></p>
It turns out the high volume of complaints that Claude Code was providing worse quality results over the past two months was grounded in real problems.</p>
<p>The models themselves were not to blame, but three separate issues in the Claude Code harness caused complex but material problems which directly affected users.</p>
<p>Anthropic's postmortem describes these in detail. This one in particular stood out to me:</p>
<blockquote>
<p>On March 26, we shipped a change to clear Claude's older thinking from sessions that had been idle for over an hour, to reduce latency when users resumed those sessions. A bug caused this to keep happening every turn for the rest of the session instead of just once, which made Claude seem forgetful and repetitive.</p>
</blockquote>
<p>I <em>frequently</em> have Claude Code sessions which I leave for an hour (or often a day or longer) before returning to them. Right now I have 11 of those (according to <code>ps aux  | grep 'claude '</code>) and that's after closing down dozens more the other day.</p>
<p>I estimate I spend more time prompting in these "stale" sessions than sessions that I've recently started!</p>
<p>If you're building agentic systems it's worth reading this article in detail - the kinds of bugs that affect harnesses are deeply complicated, even if you put aside the inherent non-deterministic nature of the models themselves.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=47878905">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/prompt-engineering">prompt-engineering</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a></p>