---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-17T10:05:35.464407+00:00
title: datasette-tailscale 0.1a0
url: https://simonwillison.net/2026/Jun/16/datasette-tailscale/#atom-everything
published: 2026-06-16
author: Simon Willison
---

# datasette-tailscale 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-tailscale/releases/tag/0.1a0">datasette-tailscale 0.1a0</a></p>
        <p>A very experimental alpha plugin which lets you do this:</p>
<pre><code>datasette tailscale mydata.db \
  --ts-authkey tskey-auth-xxxx --ts-hostname datasette-preview
</code></pre>
<p>This starts a localhost Datasette server with a <a href="https://tailscale.com/">Tailscale</a> sidecar that connects it to your Tailnet, such that <code>http://datasette-preview/</code> serves Datasette.</p>
<p>It's using the Python bindings for the experimental <a href="https://github.com/tailscale/tailscale-rs">tailscale-rs</a> library. I <a href="https://github.com/tailscale/tailscale-rs/issues/243">filed an issue</a> asking if there's a cleaner way of setting up the proxy mechanism.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/tailscale">tailscale</a></p>
