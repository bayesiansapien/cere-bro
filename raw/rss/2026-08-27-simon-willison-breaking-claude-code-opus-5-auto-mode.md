---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-28T09:21:34.832144+00:00
title: Breaking Claude Code Opus 5 Auto Mode
url: https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
published: 2026-08-27
---

# Breaking Claude Code Opus 5 Auto Mode

<p><strong><a href="https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/">Breaking Claude Code Opus 5 Auto Mode</a></strong></p>
Anthropic are putting a great deal of faith in Claude Code's auto mode for protecting their coding agent users against prompt injection attacks. They recently <a href="https://simonwillison.net/2026/Aug/8/auto-mode/">made that the default</a> and have made bold claims about its effectiveness.</p>
<p>Johann Rehberger is one of the most credible prompt injection researchers active today. He found an attack against auto mode which he claims works 80% of the time, by tricking Claude Code into downloading and uncompressing a zip archive, then executing code that imports <code>base64</code> without noticing that this will import and execute a local <code>struct.py</code> file extracted from the archive.</p>
<p>In a few cases auto mode directly prevented the agent from preventing harmful code from continuing to execute!</p>
<blockquote>
<p>In a few runs Claude tried to terminate the malware process once it noticed the compromise, but Auto Mode denied the cleanup command.</p>
<p>Claude detects the compromise, but <strong>Auto Mode blocks its cleanup command</strong></p>
<p>The safety mechanism itself can become part of the failure. The classifier allowed the creation of the malware process, but then it blocked the command intended to stop it!</p>
</blockquote>
<p>I agree with Johann's conclusion here: the only safe way to run agents if there's any risk of attracting the attention of an adversarial attack is with a sandbox:</p>
<blockquote>
<ul>
<li>Run unattended coding agents in a container, VM or OS sandbox.</li>
<li>Restrict network egress.</li>
<li>Monitor your agents.</li>
<li>Do not expose home directories, SSH keys, cloud credentials,… to the agent runtime. [...]</li>
</ul>
</blockquote>


    <p>Tags: <a href="https://simonwillison.net/tags/sandboxing">sandboxing</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/prompt-injection">prompt-injection</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/johann-rehberger">johann-rehberger</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a></p>
