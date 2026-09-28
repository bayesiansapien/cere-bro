---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-28T05:07:11Z
title: Bluesky reply bot checker
url: https://simonwillison.net/2026/Sep/27/bluesky-bot-check/
published: 2026-09-27
---

# Bluesky reply bot checker

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/bluesky-bot-check">Bluesky reply bot checker</a></p>
        <p>Automated reply bots on Twitter are a <em>scourge</em> - as someone with a decent number of followers I attract a swarm of these, such that anything I post there attracts dozens of mindless automated replies.</p>
<p>They've started manifesting on Bluesky as well.</p>
<p>Unlike Twitter, Bluesky still has a freely available and useful API. The lack of such a thing doesn't slow down the bots, but it does make investigating them a lot more frustrating.</p>
<p>So I had Opus 5.5 <a href="https://github.com/simonw/tools/pull/348">vibe code this tool</a>, which examines any Bluesky profile for evidence of a likely reply bot.</p>
<p>It looks for signals like replies posted within seconds of other posts from the same account, or accounts that never post their own content (or images or links) but instead consistently reply to messages from other, higher-follower users.</p>
<p>It also looks for question marks, because I'm <em>extra</em> infuriated by reply bots that I no tie me to waste my time answering a question that no human ever posed.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/twitter">twitter</a>, <a href="https://simonwillison.net/tags/bluesky">bluesky</a>, <a href="https://simonwillison.net/tags/vibe-coding">vibe-coding</a>, <a href="https://simonwillison.net/tags/ai-misuse">ai-misuse</a></p>