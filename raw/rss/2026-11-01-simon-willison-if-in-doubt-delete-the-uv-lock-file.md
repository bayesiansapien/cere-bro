---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-02T09:58:44.942144+00:00
title: "If in doubt, delete the uv.lock file"
url: https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/
published: 2026-11-01
author: 
---

# If in doubt, delete the uv.lock file

<p>I've been getting the occasional confusing Python dependency error since switching over to Python 3.15 and the rule I'm having to remember is:</p>
<p><strong>If in doubt, delete the uv.lock file</strong></p>
<p>Most of my projects are libraries which don't include a <code>uv.lock</code> file, since it's rude for a library dependency to lock versions for anything else that uses it.</p>
<p>Running <code>uv run pytest</code> etc tends to leave <code>uv.lock</code> files lying around, which are listed in <code>.gitignore</code> and so do not get committed to my repositories.</p>
<p>But... sometimes that <code>uv.lock</code> pins a version of a dependency that doesn't yet have a Python 3.15 wheel. An example from earlier today:</p>
<pre><code>error: Failed to build `watchfiles==1.1.1`
  cause: Call to `maturin.build_wheel` failed

error: the configured Python interpreter version (3.15) is newer
than PyO3's maximum supported version (3.14)
</code></pre>
<p>Deleting that file and running <code>uv run pytest</code> again usually fixes the problem.</p>

    <p>Tags: <a href="https://simonwillison.net/tags/uv">uv</a>, <a href="https://simonwillison.net/tags/til">til</a>, <a href="https://simonwillison.net/tags/python">python</a></p>
