---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-27T07:48:46.873974+00:00
title: Microsoft Copilot Cowork Exfiltrates Files
url: https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything
published: 2026-05-26
---

# Microsoft Copilot Cowork Exfiltrates Files

<p><strong><a href="https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files">Microsoft Copilot Cowork Exfiltrates Files</a></strong></p>
The biggest challenge in designing agentic systems continues to be preventing them from enabling attackers to exfiltrate data.</p>
<p>In this case Microsoft Copilot Cowork (yes, that's <a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">a real product name</a>) was allowing agents to send emails to the user's own inbox without approval... but those messages were then displayed in a way that could leak data to an attacker via rendered images:</p>
<blockquote>
<p>Because these messages can contain external images that trigger network requests to external websites, data can be exfiltrated when a user opens a compromised message sent by the agent.</p>
</blockquote>
<p>Since OneDrive can create pre-authenticated download links, a successful prompt injection could cause those links to be leaked, allowing files to be downloaded by the attacker.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48272354">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/microsoft">microsoft</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/prompt-injection">prompt-injection</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/exfiltration-attacks">exfiltration-attacks</a>, <a href="https://simonwillison.net/tags/lethal-trifecta">lethal-trifecta</a></p>
