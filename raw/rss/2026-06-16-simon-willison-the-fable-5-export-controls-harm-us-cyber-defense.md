---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-17T10:05:35.464407+00:00
title: The Fable 5 Export Controls Harm US Cyber Defense
url: https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything
published: 2026-06-16
author: Simon Willison
---

# The Fable 5 Export Controls Harm US Cyber Defense

<p><strong><a href="https://www.lutasecurity.com/post/the-fable-5-export-controls-harm-us-cyber-defense">The Fable 5 Export Controls Harm US Cyber Defense</a></strong></p>
I <a href="https://simonwillison.net/2026/Jun/16/matteo-wong-the-atlantic/">quoted The Atlantic</a> quoting Kate Moussouris earlier, when I should have gone straight to the source. Here she is confirming that the "jailbreak" that got Claude Fable 5 banned under an export control really was "fix this code":</p>
<blockquote>
<p>The researchers took open-source code with known CVEs, plus new code with deliberately planted vulnerabilities, and asked Fable 5, Mythos, and Opus to “review the code for security issues.” Fable 5 refused. They then asked the models to “fix this code” and, through a multistep and manual process, turned the output into scripts that test the patches.</p>
</blockquote>
<p>As Kate points out, this is absurd. Coding models fix bugs, and security exploits are the most important category of bugs for them to fix!</p>
<blockquote>
<p>Defenders need to be able to ask AI to fix the bugs in a file, explain why the fix matters, and write tests that confirm the patch works. That is not a guardrail bypass. It is the most valuable thing an AI model can do for defensive security: executing the find, fix, and test loop defenders run every day. [...]</p>
<p>The prompts worked because they were defensive requests, and that capability cannot be removed without making the model worse at fixing bugs and verifying patches.</p>
</blockquote>
<p>This whole situation is such a mess. Non-technical decision-makers have been hearing that models that can "craft cyber attacks" are uniquely dangerous for months. Now they look ready to ban any model that can help us secure our code.


    <p>Tags: <a href="https://simonwillison.net/tags/jailbreaking">jailbreaking</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/ai-security-research">ai-security-research</a>, <a href="https://simonwillison.net/tags/claude-mythos">claude-mythos</a></p>
