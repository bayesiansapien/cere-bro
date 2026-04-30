---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "What's new in pip 26.1 - lockfiles and dependency cooldowns!"
url: https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything
published: 2026-04-28
---

# What's new in pip 26.1 - lockfiles and dependency cooldowns!

<p><strong><a href="https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/">What&#x27;s new in pip 26.1 - lockfiles and dependency cooldowns!</a></strong></p>
Richard Si describes an excellent set of upgrades to Python's default <code>pip</code> tool for installing dependencies.</p>
<p>This version drops support for Python 3.9 - fair enough, since it's been EOL <a href="https://devguide.python.org/versions/">since October</a>. macOS still ships with <code>python3</code> as a default Python 3.9, so I tried out the new Python version against Python 3.14 like this:</p>
<pre><code>uv python install 3.14
mkdir /tmp/experiment
cd /tmp/experiment
python3.14 -m venv venv
source venv/bin/activate
pip install -U pip
pip --version
</code></pre>
<p>This confirmed I had <code>pip 26.1</code> - then I tried out the new lock files:</p>
<pre><code>pip lock datasette llm
</code></pre>
<p>This installs Datasette and LLM and all of their dependencies and writes the whole lot to a 519 line <code>pylock.toml</code> file - <a href="https://gist.github.com/simonw/ff52c33f4d3a381b8e53c6a3aa0213f8">here's the result</a>.</p>
<p>The new release also supports dependency cooldowns, <a href="https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/">discussed here previously</a>, via the new <code>--uploaded-prior-to PXD</code> option where X is a number of days. The format is <code>P-number-of-days-D</code>, following <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO duration format</a> but only supporting days.</p>
<p>I shipped a new release of LLM, version 0.31, <a href="https://simonwillison.net/2026/Apr/24/llm/">three days ago</a>. Here's how to use the new <code>--uploaded-prior-to P4D</code> option to ask for a version that is at least 4 days old.</p>
<pre><code>pip install llm --uploaded-prior-to P4D
venv/bin/llm --version
</code></pre>
<p>This gave me version 0.30.

    <p><small></small>Via <a href="https://lobste.rs/s/w2oiaq/what_s_new_pip_26_1_lockfiles_dependency">Lobste.rs</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/packaging">packaging</a>, <a href="https://simonwillison.net/tags/pip">pip</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/supply-chain">supply-chain</a></p>