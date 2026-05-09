---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-09T03:30:58.725649+00:00
title: Quoting Luke Curley
url: https://simonwillison.net/2026/May/9/luke-curley/#atom-everything
published: 2026-05-09
author: 
---

# Quoting Luke Curley

<blockquote cite="https://moq.dev/blog/webrtc-is-the-problem/"><p>WebRTC is designed to <strong>degrade and drop my prompt</strong> during poor network conditions.</p>
<p>wtf my dude</p>
<p>WebRTC aggressively drops audio packets to keep latency low. If you’ve ever heard distorted audio on a conference call, that’s WebRTC baybee. The idea is that conference calls depend on rapid back-and-forth, so pausing to wait for audio is unacceptable.</p>
<p>…but as a user, I would much rather wait an extra 200ms for my slow/expensive prompt to be accurate. After all, I’m paying good money to boil the ocean, and a garbage prompt means a garbage response. It’s not like LLMs are particularly responsive anyway.</p>
<p><strong>But I’m not allowed to wait</strong>. It’s <em>impossible</em> to even retransmit a WebRTC audio packet within a browser; we tried at Discord. The <em>implementation</em> is hard-coded for real-time latency <strong>or else</strong>.</p></blockquote>
<p class="cite">&mdash; <a href="https://moq.dev/blog/webrtc-is-the-problem/">Luke Curley</a>, OpenAI’s WebRTC Problem, in response to <a href="https://openai.com/index/delivering-low-latency-voice-ai-at-scale/">How OpenAI delivers low-latency voice AI at scale</a></p>

    <p>Tags: <a href="https://simonwillison.net/tags/webrtc">webrtc</a>, <a href="https://simonwillison.net/tags/openai">openai</a></p>
