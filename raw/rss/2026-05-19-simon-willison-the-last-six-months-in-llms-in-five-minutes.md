---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-19T09:55:39.050921+00:00
title: The last six months in LLMs in five minutes
url: https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything
published: 2026-05-19
author: 
---

# The last six months in LLMs in five minutes

<p>I put together these annotated slides from my five minute lightning talk at PyCon US 2026, using the <a href="https://tools.simonwillison.net/annotated-presentations">latest iteration</a> of my <a href="https://simonwillison.net/2023/Aug/6/annotated-presentations/">annotated presentation tool</a>.</p>

<div class="slide" id="5-minutes-llms.001.jpeg">
  <img alt="The last six months in LLMs in
five minutes

Simon Willison - simonwillison.net

PyCon US 2026 Lightning Talk
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.001.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.001.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>I presented this lightning talk at PyCon US 2026, attempting to summarize the last six months of developments in LLMs in five minutes.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.002.jpeg">
  <img alt="The November inflection point
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.002.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.002.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Six months is a pretty convenient time period to cover, because it captures what I've been calling the <a href="https://simonwillison.net/tags/november-2025-inflection/">November 2025 inflection point</a>. November was a critical month in LLMs, especially for coding.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.003.jpeg">
  <img alt="The “best” model changed hands 5 times
between Anthropic, OpenAl and Google
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.003.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.003.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>For one thing, the supposedly "best" model (depending mostly on vibes) changed hands five times between the three big providers.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.004.jpeg">
  <img alt="Generate an SVG of a
pelican riding a bicycle
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.004.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.004.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>As always, I'm using my <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">Generate an SVG of a pelican riding a bicycle</a> test to help illustrate the differences between the models.</p>
<p>Why this test? Because pelicans are hard to draw, bicycles are hard to draw, pelicans <em>can't ride bicycles</em>... and there's zero chance any AI lab would train a model for such a ridiculous task.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.005.jpeg">
  <img alt="Five pelicans, one for each of the following models. Varying qualities!" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.005.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.005.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>At the start of November the widely acknowledged "best" model was Claude Sonnet 4.5, released on <a href="https://simonwillison.net/2025/Sep/29/claude-sonnet-4-5/">29th September</a>. It drew me this pelican.</p>
<p>In November it was overtaken by <a href="https://simonwillison.net/2025/Nov/13/gpt-51/">GPT-5.1</a>, then <a href="https://simonwillison.net/2025/Nov/18/gemini-3/">Gemini 3</a>, then <a href="https://simonwillison.net/2025/Nov/19/gpt-51-codex-max/">GPT-5.1 Codex Max</a>, and then Anthropic took the crown back again with <a href="https://simonwillison.net/2025/Nov/24/claude-opus/">Claude Opus 4.5</a>.</p>
<p>I think Gemini 3 drew the best pelican out of this lot, but pelicans aren't everything. Most practitioners will agree that Opus 4.5 held the crown for the next couple of months.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.006.jpeg">
  <img alt="The coding agents got good
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.006.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.006.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>It took a little while for this to become clear, but the real news from November was that the coding agents got <em>good</em>.</p>
<p>OpenAI and Anthropic had spent most of 2025 running <a href="https://simonwillison.net/2025/Dec/19/andrej-karpathy/">Reinforcement Learning from Verifiable Rewards</a> to increase the quality of code written by their models, especially when paired up with their Codex and Claude Code agent harnesses.</p>
<p>In November the results of this work became apparent. Coding agents went from often-work to mostly-work, crossing a quality barrier where you could use them as a daily-driver to get real work done, without needing to spend most of your time fixing their stupid mistakes.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.007.jpeg">
  <img alt="Screenshot of &quot;Initial commit&quot; on GitHub to steipete/Warelay, commit f6dd362, steipete authored on Nov 24, 2025

It's a copy of the MIT license" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.007.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.007.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in November, this happened - the first commit to an obscure (back then) repo called "Warelay" by some guy called Pete.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.008.jpeg">
  <img alt="December/January
(A little bit of LLM psychosis)
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.008.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.008.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Over the holiday period, from December to January, a whole lot of us took advantage of the break to have a poke at these new models and coding agents and see what they could do.</p>
<p>They could do a lot! Some of us got a little bit over-excited. I had my own short-lived bout of a form of LLM psychosis as I started spinning up wildly ambitious projects to see how far I could push them.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.009.jpeg">
  <img alt="micro-javascript playground
Execute JavaScript code in a sandboxed micro-javascript environment powered by Pyodide

var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var doubled = numbers.map(n =&gt; n * 2);
console.log('Doubled: &quot;', doubled);
var evens = numbers.filter(n =&gt; n % 2 === 0);
console.log('Evens: ', evens);
var sum = numbers.reduce((a, b) =&gt; a + b, @);
console.log('Sum:&quot;, sum);

Output 27
Doubled: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Evens: [2, 4, 6, 8, 10]
Sum: 55
Execution time: 8.00ms
About: micro-javascript is a pure Python JavaScript interpreter with configurable memory and time limits. This playground runs entirely in your browser using
Pyodide (Python compiled to WebAssembly). View on GitHub" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.009.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.009.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>One of my projects was a vibe-coded implementation of JavaScript in Python - a loose port of <a href="https://github.com/bellard/mquickjs">MicroQuickJS</a> - which I called <a href="https://github.com/simonw/micro-javascript">micro-javascript</a>. You can try it out in your browser in <a href="https://simonw.github.io/micro-javascript/playground.html">this playground</a>.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.010.jpeg">
  <img alt="JavaScript running in Python running in Pyodide running in WebAssembly running in JavaScript" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.010.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.010.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>That playground demo shows JavaScript code run using my micro-javascript library, in Python, running inside Pyodide, running in WebAssembly, running in JavaScript, running in a browser!</p>
<p>It's pretty cool! But did anyone out there <em>need</em> a buggy, slow, insecure half-baked implementation of JavaScript in Python?</p>
<p>They did not. I have quite a few other projects from that holiday period that I have since quietly retired!</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.011.jpeg">
  <img alt="February 2026
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.011.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.011.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>On to February. Remember that Warelay project that had its first commit at the end of November?</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.012.jpeg">
  <img alt="Warelay → CLAWDIS → CLAWDBOT →
Clawdbot → Moltbot →🦞 OpenClaw" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.012.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.012.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In December and January it had gone through <a href="https://simonwillison.net/2026/May/16/openclaw-names/">quite a few name changes</a>... and by February it was taking the world by storm under its final name, <a href="https://openclaw.ai/">OpenClaw</a>.</p>
<p>The amount of attention it got is pretty astonishing for a project that was less than three months old.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.013.jpeg">
  <img alt="Generic term: Claw
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.013.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.013.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>OpenClaw is a "personal AI assistant", and we actually got a generic term for these, based on NanoClaw and ZeroClaw and suchlike... they're called <strong>Claws</strong>.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.014.jpeg">
  <img alt="An aquarium for your Claw
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.014.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.014.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Mac Minis started to sell out around Silicon Valley, because people were buying them to run their Claws.</p>
<p><a href="https://www.dbreunig.com/">Drew Breunig</a> joked to me that this is because they're the new digital pets, and a Mac Mini is the perfect aquarium for your Claw.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.015.jpeg">
  <img alt="Alfred Molina's Doc Ock in Spider-Man 2, tearing apart a New York subway train with his four claws." src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.015.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.015.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>My favourite metaphor for Claws is Alfred Molina's Doc Ock in the 2004 movie Spider-Man 2. His claws were powered by AI, and were perfectly safe provided nothing damaged his inhibitor chip... after which they turned evil and took over.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.016.jpeg">
  <img alt="Gemini 3.1 Pro

A really good illustration of a pelican riding a bicycle.
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.016.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.016.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in February: Gemini 3.1 Pro came out, and drew me a <em>really good pelican riding a bicycle</em>. Look at this! It's even got a fish in its basket.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.017.jpeg">
  <img alt="Gemini 3 Pro pelican contrasted with Gemini 3.1 Pro, as animated SVGs" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.017.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.017.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>And then Google's Jeff Dean <a href="https://simonwillison.net/2026/Feb/19/gemini-31-pro/#jeff-dean">tweeted this video</a> of an animated pelican riding a bicycle, plus a frog on a penny-farthing and a giraffe driving a tiny car and an ostrich on roller skates and a turtle kickflipping a skateboard and a dachshund driving a stretch limousine.</p>
<p>So maybe the AI labs have been paying attention after all!</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.018.jpeg">
  <img alt="April 2026
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.018.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.018.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>A lot of stuff happened just in the past month.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.019.jpeg">
  <img alt="Gemma 4 26B-A4B (17.99GB)

A pretty decent pelican riding a bicycle, though the bike is a bit mis-shapen." src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.019.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.019.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Google released the <a href="https://simonwillison.net/2026/Apr/2/gemma-4/">Gemma 4</a> series of models, which are the most capable open weight models I've seen from a US company.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.020.jpeg">
  <img alt="GLM-5.1
MIT, 754B parameter, 1.51TB!
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.020.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.020.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also last month, Chinese AI lab GLM came out with <a href="https://simonwillison.net/2026/Apr/7/glm-51/">GLM-5.1</a> - an open weight 1.5TB monster! This is a very effective model... if you can afford the hardware to run it.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.021.jpeg">
  <img alt="" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.021.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.021.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>GLM-5.1 drew me this very competent pelican on a bicycle.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.022.jpeg">
  <img alt="The bike is wonky, the pelican is floating." src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.022.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.022.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>... though when it <a href="https://gisthost.github.io/?73bb6808b18c2482f66e5f082c75f36e">tried to animate it</a> the bicycle bounced off into the top and the bicycle got warped.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.023.jpeg">
  <img alt="Screenshot of Bluesky

Charles
‪@charles.capps.me‬
I think you should pester it with another animal using another method of locomotion. 

Something tells me it was trained for this. I can't quite put my finger on it. /s

NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER!!" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.023.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.023.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Charles <a href="https://bsky.app/profile/charles.capps.me/post/3miwrn42mjc2t">on Bluesky</a> suggested I try it with a North Virginia Opossum on an E-scooter</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.024.jpeg">
  <img alt="NORTH VIRGINIA OPOSSUM
CRUISING THE COMMONWEALTH SINCE DUSK

And a really cool illustration of a possum." src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.024.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.024.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>And it did this! I've tried this on other models and they don't even come close. "Cruising the commonwealth since dusk" is perfect. It's <a href="https://static.simonwillison.net/static/2026/glm-possum-escooter.html">animated too</a>.</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.025.jpeg">
  <img alt="Qwen3.6-35B-A3B is a 20.9GB file that runs on my laptop

It drew a better pelican on a bicycle than Opus 4.7, which messed up the bicycle frame." src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.025.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.025.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>The other neat Chinese open weight models in April came from Qwen. <a href="https://simonwillison.net/2026/Apr/16/qwen-beats-opus/">Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7</a>. That's a 20.9GB open weights model that runs on my laptop!</p>
<p>(I think this mainly demonstrates that the pelican on the bicycle has firmly exceeded its limits as a useful benchmark.)</p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.026.jpeg">
  <img alt="Claude Sonnet 4.5 pelican for comparison." src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.026.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.026.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Here's that Claude Sonnet 4.5 pelican from September for comparison. </p>
  </div>
</div>
<div class="slide" id="5-minutes-llms.027.jpeg">
  <img alt="The themes of the past 6 months:
Coding agents got really good
Local models wildly outperform expectations
" src="https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.027.jpeg" />
  <div><a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.027.jpeg" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>So those were the two main themes of the past six months. The coding agents got really good... and the laptop-available models, while a lot weaker than the frontier, have started wildly outperforming expectations.</p>
  </div>
</div>
    
        <p>Tags: <a href="https://simonwillison.net/tags/lightning-talks">lightning-talks</a>, <a href="https://simonwillison.net/tags/pycon">pycon</a>, <a href="https://simonwillison.net/tags/speaking">speaking</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/local-llms">local-llms</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/annotated-talks">annotated-talks</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a></p>
