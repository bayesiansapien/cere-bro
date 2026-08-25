---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T14:24:43.465427+05:30
title: smolmachines / smolvm as a sandbox for untrusted Python & JavaScript
url: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
published: 2026-08-19
---

# smolmachines / smolvm as a sandbox for untrusted Python & JavaScript

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/smolmachines-untrusted-sandbox#readme">smolmachines / smolvm as a sandbox for untrusted Python &amp; JavaScript</a></p>
        <p>I tasked Claude Fable 5 running in Claude Code for web with the following research task:</p>
<blockquote>
<p><code>Put https://smolmachines.com through its paces as a fast secure sandbox. Explore what it would take to use this to run untrusted Python and JavaScript code in a way that is limited in what RAM and CPU time it can take up (protection against "while true") with no network access and filesystem access only to designated files</code></p>
<p><code>Goal is to be able to use this to execute user-provided tasks for things like data transformations</code></p>
</blockquote>
<p>It quickly ran into a problem: the Claude Code for web environment can't run <a href="https://smolmachines.com">smol machines</a>. Quoting the <a href="https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/smolmachines-untrusted-sandbox/notes.md#environment-check">notes it wrote</a>:</p>
<blockquote>
<ul>
<li>This Claude Code container: Linux 6.18.5-fc-v20 (itself a Firecracker guest), 4 vCPU, 15GB RAM. <strong>No /dev/kvm, no vmx/svm CPU flags</strong> → no nested virt.</li>
<li><code>smolvm machine run</code> fails as expected: "kvm not available".</li>
<li>Plan B: GitHub Actions ubuntu runners DO expose /dev/kvm → run the real test battery via a temporary workflow on this branch, collect logs, remove workflow in final commit.</li>
</ul>
</blockquote>
<p>And Plan B is <a href="https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/.github/workflows/smolvm-sandbox-test.yml">what it did</a>, installing smolvm and running <a href="https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/smolmachines-untrusted-sandbox/run-tests.sh">these tests</a> directly in a GitHub Actions runner against that branch.</p>
<p>That was a creative solution to the environmental limits posed by Claude Code for web. Another example of Fable being <a href="https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/">relentlessly proactive</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/research">research</a>, <a href="https://simonwillison.net/tags/sandboxing">sandboxing</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/github-actions">github-actions</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
