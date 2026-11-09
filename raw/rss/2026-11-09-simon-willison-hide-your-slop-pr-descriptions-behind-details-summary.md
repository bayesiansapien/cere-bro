---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-09T14:17:49.617285+00:00
title: "Hide your slop PR descriptions behind <details><summary>"
url: https://simonwillison.net/2026/Nov/9/details-summary/
published: 2026-11-09
author: 
---

# Hide your slop PR descriptions behind <details><summary>

<p>Most of the changes I make to my projects these days come in the form of PRs opened for me by Claude Code or Codex. The PR is my unit of work - I use them to bundle commits together, iterating on them until a feature is complete, document decisions and then merge the finished result. Today's coding agents are great at writing PR descriptions.</p>
<h4 id="they-re-too-good-at-describing-the-work">They're too good at describing the work</h4>
<p>The problem is that they are <em>too</em> good. An agent-written PR description is accurate and comprehensive. It describes the problem, the detailed solution, and the steps taken to verify it. That's a lot of information to absorb.</p>
<p>It's not necessarily slop, but it <em>reads</em> like slop!</p>
<p>It's very easy to spot an AI-written PR, and as with other forms of AI writing my instant reaction is best summarized as "I'm not reading all of that". It doesn't matter how accurate or useful the information is, I'm instantly put off by the thought that it will take me longer to read than it took the driving author to write... even when that driving author is me!</p>
<p>I want human editorial judgement. I want someone to have thought just long enough about the PR to give me a human-approved introduction that helps me understand, at a high level, what the PR is for and whether it deserves more of my attention.</p>
<p>I think I've found a low-effort way to do this that feels right.</p>
<h4 id="hide-most-of-it-in-a-details-summary">Hide most of it in a details/summary</h4>
<p>The HTML <code>&lt;details&gt;&lt;summary&gt;</code> elements render as a collapsed heading (the summary) that can be expanded to view the larger piece of text. The code looks like this:</p>
<div class="highlight highlight-text-html-basic"><pre><span class="pl-kos">&lt;</span><span class="pl-ent">details</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">summary</span><span class="pl-kos">&gt;</span>Claude Opus 5.5<span class="pl-kos">&lt;/</span><span class="pl-ent">summary</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">h2</span><span class="pl-kos">&gt;</span>The hook<span class="pl-kos">&lt;/</span><span class="pl-ent">h2</span><span class="pl-kos">&gt;</span>
  Plugins implement <span class="pl-kos">&lt;</span><span class="pl-ent">code</span><span class="pl-kos">&gt;</span>register_agent_reference_types(datasette)<span class="pl-kos">&lt;/</span><span class="pl-ent">code</span><span class="pl-kos">&gt;</span>...
<span class="pl-kos">&lt;/</span><span class="pl-ent">details</span><span class="pl-kos">&gt;</span></pre></div>
<p>When rendered, it looks <a href="https://github.com/datasette/datasette-agent/pull/51">like this</a>:</p>
<p><img alt="Screenshot of a GitHub PR. The text &quot;Claude Opus 5.5&quot; sits next to a little black arrow. Clicking on that text expands a full description inside the PR body." src="https://static.simonwillison.net/static/2026/details-summary-pr.gif" /></p>
<p>Crucially, <code>&lt;details&gt;&lt;summary&gt;</code> <em>is supported in GitHub Markdown</em>. You can drop those tags directly into an issue comment or PR description and GitHub will hide the details and display just the summary plus an expansion arrow.</p>
<p>I've started using this for my AI-generated pull requests.</p>
<p>The opening paragraph of my PRs will be carefully selected to act as a high-level explanation of what's going on - the shortest text a human can read that will help get them up to speed.</p>
<p>I'll sometimes throw in a screenshot as well, since images are often the best way to quickly illustrate a new feature.</p>
<p>The full agent-written essay then follows in a <code>&lt;details&gt;&lt;summary&gt;</code>. I use the model name and often the effort level as that summary, to make it abundantly clear what is going on - "Claude Opus 5.5 Medium" for example.</p>
<p>My PRs don't feel nearly as sloppy now! The information is all still there, but a reader can glance at it and get the top, human-curated information without their eyes glazing over at multiple paragraphs of agent-written details.</p>
<p>I don't always write the introduction myself - sometimes the agent has given me what I need already, hidden away in the avalanche of other text. My promise to the reader is that the short opener will represent my human judgement as to what is definitely worth their time.</p>
<p>Here are some recent examples where I've used this pattern, including the opener I used:</p>
<ul>
<li>
<a href="https://github.com/simonw/datasette/pull/3052">datasette PR #3052: Redesign row page as a vertical list of fields</a> - "The row page showed its single row as a one-row table. For wide tables, like a 46-column GitHub <code>repos</code> table, that scrolled far off to the right and left most of the page blank." (then a screenshot)</li>
<li>
<a href="https://github.com/simonw/datasette/pull/3043">datasette PR #3043: Pagination bar showing which rows are on the current page</a> - "Table pages that span more than one page now make it obvious where you are, and offer navigation at the top of the page as well as the bottom." (plus screenshot)</li>
<li>
<a href="https://github.com/simonw/datasette/pull/3042">datasette PR #3042: Load edit-tools.js on demand via a small loader</a> - "<code>edit-tools.js</code> (~220KB) was loaded on every table, row and database page, even for users who couldn't edit anything. Now only load it for users who can edit when they first interact with an edit feature (including mouse over an edit link)."</li>
<li>
<a href="https://github.com/datasette/datasette-agent/pull/51">datasette-agent PR #51: register_agent_reference_types plugin hook</a> - "Lets plugins add their own kinds of item to the <code>#</code> tagging in the chat composer using a new <code>register_agent_reference_types(datasette)</code> plugin hook." - pictured above.</li>
<li>
<a href="https://github.com/simonw/llm/pull/1838">llm PR #1838: Add llm openai endpoint add/list/remove/path commands</a> - "Adds commands for managing the records in <code>extra-openai-models.yaml</code>, so OpenAI-compatible endpoints can be saved from the command line instead of by hand-editing YAML." - then copied <code>--help</code> output.</li>
</ul>
<h4 id="the-mnemonic">The mnemonic</h4>
<p>I used to have trouble remembering the order of the tags - is it <code>&lt;details&gt;&lt;summary&gt;</code> or <code>&lt;summary&gt;&lt;details&gt;</code>?</p>
<p>Here are two tricks that helped me.</p>
<p>First, and most obviously, the <code>&lt;summary&gt;</code> is clearly the bit where you summarize the details. That's the tag for your line of text that can be clicked to expand - the <code>&lt;details&gt;</code> element must then wrap everything else.</p>
<p>An even better trick is to always refer to these two tags as "details-summary".</p>
<p>"details-summary" is two syllables followed by three syllables. That rolls off the tongue more smoothly than the three-two punch of "summary-details".</p>
<p>Say "details-summary" out loud just a few times and you'll never forget the order of the tags again.</p>
<p>(I still wish GitHub would add a button to their Markdown editor for this - partly to save me painstakingly typing it on my mobile keyboard, and partly to help spread the word to more GitHub users that this feature exists.)</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/github">github</a>, <a href="https://simonwillison.net/tags/html">html</a>, <a href="https://simonwillison.net/tags/markdown">markdown</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a></p>
