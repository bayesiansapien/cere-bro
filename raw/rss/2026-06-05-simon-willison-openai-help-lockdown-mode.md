---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-06T09:05:21.154870+00:00
title: "OpenAI Help: Lockdown Mode"
url: https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything
published: 2026-06-05
author: ""
---

# OpenAI Help: Lockdown Mode

<p><strong><a href="https://help.openai.com/en/articles/20001061-lockdown-mode">OpenAI Help: Lockdown Mode</a></strong></p>
OpenAI first teased this <a href="https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/">in February</a>, but now it's live and "rolling out to eligible personal accounts, including Free, Go, Plus, and Pro, and self-serve ChatGPT Business accounts":</p>
<blockquote>
<p>Lockdown Mode is designed to help prevent the final stage of data exfiltration from a prompt injection attack by limiting outbound network requests that could transfer sensitive data to an attacker. Lockdown Mode does not prevent prompt injections from appearing in the content ChatGPT processes. For example, a prompt injection could appear in cached web content or in an uploaded file, and could still affect the behavior or accuracy of a response.</p>
</blockquote>
<p>This looks really good to me.</p>
<p>The <a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">Lethal Trifecta</a> occurs when an LLM system has access to all three of access to private data, exposure to untrusted content and a way to steal data and transmit it back to the attacker.</p>
<p>The only way to solve the trifecta is to cut off one of the three legs, and by far the easiest leg to restrict without making your LLM systems far less useful is the exfiltration vectors to steal data.</p>
<p>It looks to me like lockdown mode directly attacks that leg, using mechanisms that are deterministic and, crucially, are not evaluated by AI systems that themselves can be subverted by sufficiently devious attacks.</p>
<p>The existence of lockdown mode does however imply that ChatGPT, in its default settings, does <em>not</em> provide robust protection against sufficiently determined data exfiltration attacks!


    <p>Tags: <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/prompt-injection">prompt-injection</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/lethal-trifecta">lethal-trifecta</a></p>
