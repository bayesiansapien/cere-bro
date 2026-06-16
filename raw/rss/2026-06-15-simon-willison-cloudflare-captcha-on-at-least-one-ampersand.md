---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-16T08:23:58.311755+00:00
title: Cloudflare CAPTCHA on at least one ampersand
url: https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/#atom-everything
published: 2026-06-15
author: 
---

# Cloudflare CAPTCHA on at least one ampersand

<p><strong>TIL:</strong> <a href="https://til.simonwillison.net/cloudflare/captcha-on-at-least-one-ampersand">Cloudflare CAPTCHA on at least one ampersand</a></p>
        <p>I'm using Cloudflare's CAPTCHA (they call it a "Web Application Firewall &gt; Custom rules &gt; Managed Challenge" these days) to prevent crawlers from aggresively spidering my <a href="https://simonwillison.net/2017/Oct/5/django-postgresql-faceted-search/">faceted search engine</a> on this site, but I got fed up of even simple <code>?q=term</code> searches triggering the challenge.</p>
<p>After some mucking around with Claude Code it turns out you can register the following rule instead, so the CAPTCHA only kicks in for search URLs containing at least one ampersand:</p>
<p><code>(http.request.uri.path wildcard r"/search/*" and http.request.uri.query contains "&amp;")</code></p>
<p>And now <a href="https://simonwillison.net/search/?q=lemur">/search/?q=lemur</a> works without triggering a CAPTCHA!</p>
<p>Also included: notes on <a href="https://til.simonwillison.net/cloudflare/captcha-on-at-least-one-ampersand#trying-the-cloudflare-mcp">trying out the Cloudflare MCP with Claude Code</a>, though it turned out not to be able to edit the rules in question so I had Claude Code <a href="https://til.simonwillison.net/cloudflare/captcha-on-at-least-one-ampersand#using-the-api-instead">switch to the Cloudflare API</a> instead.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/captchas">captchas</a>, <a href="https://simonwillison.net/tags/cloudflare">cloudflare</a>, <a href="https://simonwillison.net/tags/model-context-protocol">model-context-protocol</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a></p>
