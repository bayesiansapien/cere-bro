---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: sqlite-utils 4.0rc3
url: https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything
published: 2026-07-06
author: 
---

# sqlite-utils 4.0rc3

<p><strong>Release:</strong> <a href="https://github.com/simonw/sqlite-utils/releases/tag/4.0rc3">sqlite-utils 4.0rc3</a></p>
        <p>I hoped to release <code>sqlite-utils 4.0</code> stable this weekend, but as I worked through the backlog of issues and PRs with a combination of Claude Fable 5 and GPT-5.5 the changelog since rc2 <a href="https://sqlite-utils.datasette.io/en/latest/changelog.html#rc3-2026-07-05">kept getting bigger</a>.</p>
<p>The biggest new feature is support for introspecting and creating compound foreign keys - a feature that involves a subtle breaking change to <a href="https://sqlite-utils.datasette.io/en/latest/python-api.html#foreign-keys">table.foreign_keys</a> and hence needed to land for the 4.0 stable release.</p>
<p><code>sqlite-utils</code> also now follows SQLite's convention for case insensitive column names, which turned out to touch <a href="https://sqlite-utils.datasette.io/en/latest/changelog.html#case-insensitive-column-matching">a bunch of different places at once</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/sqlite-utils">sqlite-utils</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/gpt">gpt</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
