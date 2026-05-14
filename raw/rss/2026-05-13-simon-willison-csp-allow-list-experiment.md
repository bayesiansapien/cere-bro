---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-14T03:50:13.322968+00:00
title: CSP Allow-list Experiment
url: https://simonwillison.net/2026/May/13/csp-allow/#atom-everything
published: 2026-05-13
author: 
---

# CSP Allow-list Experiment

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/csp-allow">CSP Allow-list Experiment</a></p>
        <p>An experiment that shows that you can load an app in a CSP-protected sandboxed iframe (see <a href="https://simonwillison.net/2026/Apr/3/test-csp-iframe-escape/">previous note</a>) and have a custom <code>fetch()</code> that intercepts CSP errors and passes them up to the parent window... which can then prompt the user to add that domain to an allow-list and then refresh the page.</p>
<p><img alt="Screenshot of a web tool titled &quot;CSP Allow-list Experiment&quot; with buttons Reset sample, Clear allow-list, Refresh preview. Left panel shows HTML source code starting with &lt;!doctype html&gt;. Right panel shows Preview with CSP header default-src 'none'; script-src 'unsafe-inline'; style-s... and heading &quot;Sandbox fetch test&quot;. A modal dialog from tools.simonwillison.net is overlaid reading: &quot;The sandbox tried to connect to: https://api.inaturalist.org   Add this origin to the CSP connect-src allow-list and refresh the page?&quot; with an unchecked checkbox &quot;Don't allow tools.simonwillison.net to prompt you again&quot; and Cancel and OK buttons. Below is &quot;Messages from sandbox&quot; showing fetch-catch blocked https://api.inaturalist.org/v1/observations?per... connect-src · https://api.inaturalist.org. At the bottom left is &quot;Allowed fetch() origins&quot; with an input field containing https://api.github.com, an Add button, and a tag https://api.github.com x." src="https://static.simonwillison.net/static/2026/csp-allow.jpg" /></p>
<p>I built this one with GPT-5.5 xhigh running in the Codex desktop app.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/content-security-policy">content-security-policy</a>, <a href="https://simonwillison.net/tags/iframes">iframes</a>, <a href="https://simonwillison.net/tags/security">security</a></p>
