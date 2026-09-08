---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-08T04:52:33.780835+00:00
title: Video compressor
url: https://simonwillison.net/2026/Sep/7/video-compressor/
published: 2026-09-07
---

# Video compressor

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/video-compressor">Video compressor</a></p>
        <p>I recorded a short demo video of <a href="https://simonwillison.net/2026/Sep/7/equal-earth/">my Equal Earth</a> animation on my phone and wanted to publish an optimized version of that video (using FFMPEG) on my blog, so I had Claude Fable 5.1 in Claude Code for web <a href="https://claude.ai/code/session_01QHTdJZ4xg6TZfDXCmuvAE9">build me this tool</a> using the WebAssembly build of FFMPEG.</p>
<p><img alt="Screenshot of a video compression web tool. Under &quot;Versions to generate&quot; is a table of five presets (Largest, Large, Medium, Small, Smallest) with output sizes of 854×370 or 640×276, CRF quality settings from 22 to 28, and audio bitrates from 128 to 64 kbps, plus options for encoder speed, H.264 profile, 30 fps limit, stripping metadata, dropping audio, and encoding only the first 10 seconds. A green &quot;Generate versions&quot; button reads &quot;Done: 5 versions in 11.8s.&quot; Below, &quot;Results, smallest first&quot; shows three video players: Smallest at 145 KB (48% of original), Medium at 241 KB (79%), and Small at 264 KB (87%), each with a Download .mp4 button and a collapsible ffmpeg command." src="https://static.simonwillison.net/static/2026-09-07/video-compressor.webp" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/ffmpeg">ffmpeg</a>, <a href="https://simonwillison.net/tags/video">video</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
