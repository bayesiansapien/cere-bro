---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "Serving the For You feed"
url: https://simonwillison.net/2026/Apr/24/serving-the-for-you-feed/#atom-everything
published: 2026-04-24
---

# Serving the For You feed

<p><strong><a href="https://atproto.com/blog/serving-the-for-you-feed">Serving the For You feed</a></strong></p>
One of Bluesky's most interesting features is that anyone can run their own <a href="https://simonwillison.net/atom/everything/bluesky custom feed">custom "feed" implementation</a> and make it available to other users - effectively enabling custom algorithms that can use any mechanism they like to recommend posts.</p>
<p>spacecowboy runs the <a href="https://bsky.app/profile/did:plc:3guzzweuqraryl3rdkimjamk/feed/for-you">For You Feed</a>, used by around 72,000 people. This guest post on the AT Protocol blog explains how it works.</p>
<p>The architecture is <em>fascinating</em>. The feed is served by a single Go process using SQLite on a "gaming" PC in spacecowboy's living room - 16 cores, 96GB of RAM and 4TB of attached NVMe storage.</p>
<p>Recommendations are based on likes: what else are the people who like the same things as you liking on the platform?</p>
<p>That Go server consumes the Bluesky firehose and stores the relevant details in SQLite, keeping the last 90 days of relevant data, which currently uses around 419GB of SQLite storage.</p>
<p>Public internet traffic is handled by a $7/month VPS on OVH, which talks to the living room server via Tailscale.</p>
<p>Total cost is now $30/month: $20 in electricity, $7 in VPS and $3 for the two domain names. spacecowboy estimates that the existing system could handle all ~1 million daily active Bluesky users if they were to switch to the cheapest algorithm they have found to work.


    <p>Tags: <a href="https://simonwillison.net/tags/go">go</a>, <a href="https://simonwillison.net/tags/scaling">scaling</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/software-architecture">software-architecture</a>, <a href="https://simonwillison.net/tags/tailscale">tailscale</a>, <a href="https://simonwillison.net/tags/bluesky">bluesky</a></p>