---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-13T03:34:05.407534+00:00
title: OpenAI WebRTC Audio Session, now with document context
url: https://simonwillison.net/2026/Jun/12/openai-webrtc/#atom-everything
published: 2026-06-12
author: 
---

# OpenAI WebRTC Audio Session, now with document context

<p><strong><a href="https://tools.simonwillison.net/openai-webrtc">OpenAI WebRTC Audio Session, now with document context</a></strong></p>
I built the first version of this tool <a href="https://simonwillison.net/2024/Dec/17/openai-webrtc/">in December 2024</a> to try out the then-new OpenAI WebRTC API for interacting with their realtime audio models.</p>
<p>Last month OpenAI <a href="https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/">introduced a brand new model</a> to that API called <a href="https://developers.openai.com/api/docs/models/gpt-realtime-2">GPT‑Realtime‑2</a>, which they promoted as "our first voice model with GPT‑5‑class reasoning" - with a Sep 30, 2024 knowledge cut-off.</p>
<p>I've been waiting for that model to show up in the ChatGPT iPhone app but it still hasn't, so I revisited my old playground.</p>
<p>You can now pick the better model, and you can also paste in a big chunk of document context so you can have as audio conversation in your browser about whatever information you think would be useful to explore in a conversational way.</p>
<p><img alt="Screenshot of a web interface titled &quot;OpenAI WebRTC Audio Session&quot; with a gray status dot. Form fields: &quot;OpenAI API Token&quot; showing a masked password of dots, &quot;Voice&quot; dropdown set to &quot;Coral&quot;, &quot;Model&quot; dropdown set to &quot;gpt-realtime-2&quot;. A collapsible section labeled &quot;▼ Document context (optional — paste text to talk about)&quot; with bold instruction &quot;Paste a document here before starting the session and the model will be able to discuss it with you&quot; above a textarea containing a pasted Markdown document about whether DuckDB can run untrusted SQL as safely as Datasette runs SQLite. Below are a blue &quot;Start Session&quot; button and a gray disabled &quot;Mute Mic&quot; button, then a green success message &quot;Session established successfully!&quot; At the bottom, a dark panel headed &quot;Last transcript&quot; reads: &quot;DuckDB can be made about as safe as SQLite for running untrusted SELECT queries, but only if you lock it down properly. Using read only true by itself is not enough, because SQL can still&quot; (text cut off)." class="blogmark-image" src="https://static.simonwillison.net/static/2026/openai-webrtc-document-context.jpg" />


    <p>Tags: <a href="https://simonwillison.net/tags/audio">audio</a>, <a href="https://simonwillison.net/tags/tools">tools</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/multi-modal-output">multi-modal-output</a>, <a href="https://simonwillison.net/tags/webrtc">webrtc</a></p>
