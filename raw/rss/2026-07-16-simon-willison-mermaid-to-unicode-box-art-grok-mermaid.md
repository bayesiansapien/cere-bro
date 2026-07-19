---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.121759+00:00
title: Mermaid to Unicode box art (grok-mermaid)
url: https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything
published: 2026-07-16
---

# Mermaid to Unicode box art (grok-mermaid)

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/grok-mermaid">Mermaid to Unicode box art (grok-mermaid)</a></p>
        <p>While <a href="https://simonwillison.net/2026/Jul/15/grok-build/">exploring the codebase</a> for the newly open-sourced Grok CLI coding agent I came across <a href="https://github.com/xai-org/grok-build/blob/b189869b7755d2b482969acf6c92da3ecfeffd36/crates/codegen/xai-grok-markdown/src/mermaid.rs">xai-grok-markdown/src/mermaid.rs</a>, a "self-contained terminal renderer for Mermaid diagrams" written in Rust.</p>
<p>I figured it would be fun to try that out in a browser via WebAssembly. Here's <a href="https://github.com/simonw/tools/pull/293#issue-4897479396">the prompt</a> I ran in Claude Code for web (Fable 5), and this is what the resulting tool looks like:</p>
<p><img alt="Screenshot of a Mermaid diagram editor showing source code and rendered flowchart. The code reads: graph TD Start[Request received] --&gt; Auth{Authenticated?} Auth --&gt;|yes| Rate{Rate limit OK?} Auth --&gt;|no| R401[401 Unauthorized] Rate --&gt;|yes| H(Handle request) Rate --&gt;|no| R429[429 Too Many Requests] H -.-&gt; Log[Audit log] H ==&gt; Resp[200 OK]. Below the code are controls labeled Max width: Fit output panel, Copy as text, and Copy link to this diagram. The rendered flowchart on a dark background flows top-down: Request received leads to Authenticated?, which branches yes to Rate limit OK? and no to 401 Unauthorized. Rate limit OK? branches yes to Handle request and no to 429 Too Many Requests. Handle request connects with a dotted arrow to Audit log and a thick arrow to 200 OK." src="https://static.simonwillison.net/static/2026/grok-mermaid-wasm.png" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/tools">tools</a>, <a href="https://simonwillison.net/tags/rust">rust</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/mermaid">mermaid</a>, <a href="https://simonwillison.net/tags/grok">grok</a>, <a href="https://simonwillison.net/tags/xai">xai</a></p>
