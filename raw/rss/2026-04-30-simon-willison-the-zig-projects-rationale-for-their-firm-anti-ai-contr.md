---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "The Zig project's rationale for their firm anti-AI contribution policy"
url: https://simonwillison.net/2026/Apr/30/zig-anti-ai/#atom-everything
published: 2026-04-30
---

# The Zig project's rationale for their firm anti-AI contribution policy

<p><a href="https://ziglang.org/">Zig</a> has one of the most stringent <a href="https://ziglang.org/code-of-conduct/">anti-LLM policies</a> of any major open source project:</p>
<blockquote>
<p>No LLMs for issues.</p>
<p>No LLMs for pull requests.</p>
<p>No LLMs for comments on the bug tracker, including translation. English is encouraged, but not required. You are welcome to post in your native language and rely on others to have their own translation tools of choice to interpret your words.</p>
</blockquote>
<p>The most prominent project written in Zig may be the <a href="https://bun.com/">Bun</a> JavaScript runtime, which was <a href="https://bun.com/blog/bun-joins-anthropic">acquired by Anthropic</a> in December 2025 and, unsurprisingly, makes heavy use of AI assistance.</p>
<p>Bun operates its own fork of Zig, and recently <a href="https://x.com/bunjavascript/status/2048427636414923250">achieved a 4x performance improvement</a> on Bun compile after adding "parallel semantic analysis and multiple codegen units to the llvm backend". Here's <a href="https://github.com/oven-sh/zig/compare/upgrade-0.15.2%E2%80%A6upgrade-0.15.2-fast">that code</a>. But <a href="https://twitter.com/bunjavascript/status/2048428104893542781">@bunjavascript says</a>:</p>
<blockquote>
<p>We do not currently plan to upstream this, as Zig has a strict ban on LLM-authored contributions.</p>
</blockquote>
<p>In <a href="https://kristoff.it/blog/contributor-poker-and-ai/">Contributor Poker and Zig's AI Ban</a> (<a href="https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban">via Lobste.rs</a>) Zig Software Foundation VP of Community Loris Cro explains the rationale for this strict ban. It's the best articulation I've seen yet for a blanket ban on LLM-assisted contributions:</p>
<blockquote>
<p>In successful open source projects you eventually reach a point where you start getting more PRs than what you’re capable of processing. Given what I mentioned so far, it would make sense to stop accepting imperfect PRs in order to maximize ROI from your work, but that’s not what we do in the Zig project. Instead, <strong>we try our best to help new contributors to get their work in, even if they need some help getting there</strong>. We don’t do this just because it’s the “right” thing to do, but also <strong>because it’s the smart thing to do</strong>.</p>
</blockquote>
<p>Zig values contributors over their contributions. Each contributor represents an investment by the Zig core team - the primary goal of reviewing and accepting PRs isn't to land new code, it's to help grow new contributors who can become trusted and prolific over time.</p>
<p>LLM assistance breaks that completely. It doesn't matter if the LLM helps you submit a <em>perfect</em> PR to Zig - the time the Zig team spends reviewing your work does nothing to help them add new, confident, trustworthy contributors to their overall project.</p>
<p>Loris explains the name here:</p>
<blockquote>
<p>The reason I call it “contributor poker” is because, just like people say about the actual card game, “you play the person, not the cards”. In contributor poker, you bet on the contributor, not on the contents of their first PR.</p>
</blockquote>
<p>This makes a lot of sense to me. It relates to an idea I've seen circulating elsewhere: if a PR was mostly written by an LLM, why should a project maintainer spend time reviewing and discussing that PR as opposed to firing up their own LLM to solve the same problem?</p>

    <p>Tags: <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/zig">zig</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-ethics">ai-ethics</a>, <a href="https://simonwillison.net/tags/open-source">open-source</a>, <a href="https://simonwillison.net/tags/javascript">javascript</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/bun">bun</a></p>