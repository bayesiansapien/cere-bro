---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-14T06:17:27.915562+00:00
title: commit-rewriter 0.1
url: https://simonwillison.net/2026/Sep/14/commit-rewriter/
published: 2026-09-14
author: 
---

# commit-rewriter 0.1

<p><strong>Release:</strong> <a href="https://github.com/simonw/commit-rewriter/releases/tag/0.1">commit-rewriter 0.1</a></p>
        <p>I built this little web app the other day to help edit the commit messages for the <a href="https://datasette.io/blog/2026/september-security-releases/">Datasette security releases</a>. The initial commits were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication.</p>
<p>If you want to edit the commit messages for a repository you can run it like this:</p>
<pre><code>uvx commit-rewriter path/to/repo
</code></pre>
<p>Omit the path if you are already in the directory for that repo.</p>
<p><img alt="Screenshot of the commit-rewriter web interface. A heading reads commit-rewriter above the repository path and current branch and commit hash, with a short description of the tool. A toolbar shows a pending edits count with Discard drafts and Rewrite commit messages buttons, followed by a search box for message, author, or hash and an Edited only checkbox. A left sidebar titled Navigate commits lists recent commit messages with their short hashes. The main panel shows a card for each commit with its hash, author and timestamp, an editable text area containing the commit message, and a View full formatted diff toggle." src="https://static.simonwillison.net/static/2026/commit-rewriter.webp" /></p>
<p>When you submit your edits the tool creates a timestamped branch of your current repo state - to allow you to revert if you need to - and then rewrites every commit from the first one you edited to the most recent.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/git">git</a>, <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a></p>
