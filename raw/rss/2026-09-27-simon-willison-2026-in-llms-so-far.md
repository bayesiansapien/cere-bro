---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-28T05:07:11Z
title: 2026 in LLMs (so far)
url: https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/
published: 2026-09-27
---

# 2026 in LLMs (so far)

<p>On Friday I gave the closing keynote at the <a href="https://www.wearedevelopers.com/world-congress-north-america">WeAreDevelopers World Congress North America</a> in San Jose. I tied together the key trends from the past year into a chronological exploration of everything that happened in 2026. The video <a href="https://www.youtube.com/watch?v=GAkIytR7vcc">is on YouTube</a>; here are my annotated slides and notes to accompany the talk.</p>

<p> </p>

<p>And as an <a href="https://simonwillison.net/tags/annotated-talks/">annotated presentation</a>:</p>

<div class="slide" id="simon-willison-2026-in-llms.001.webp">
  <img alt="2026 in LLMs (so far)
Simon Willison
WeAreDevelopers World Congress North America, 25th September 2026" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.001.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.001.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
<p>I'm going to give a lightning tour of everything that has happened so far in 2026. The year isn't over yet!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.002.webp">
  <img alt="November 2025
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.002.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.002.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>For me, 2026 started a couple of months earlier in November 2025.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.003.webp">
  <img alt="The November 2025 inflection point
Claude Opus 4.5 GPT-5.1
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.003.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.003.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>November saw the release of two important models: Claude Opus 4.5 and GPT-5.1.</p>
<p>As is usually the case with new models, these were incremental improvements on the models that came before them.</p>
<p>But every now and then when a model improves, it crosses an invisible line where something that didn't really work starts working.</p>
<p>In this case, the thing that started working was their coding agents. Claude Code had been around since February 2025, Codex was a little younger.</p>
<p>These two new models, when paired with their respective coding agent harnesses, improved from "often make mistakes" to "reliable enough to use on a day-to-day basis".</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.004.webp">
  <img alt="&quot;Generate an SVG of a pelican riding a bicycle&quot;. The Claude Opus 4.5 one has a very weird shaped frame and the pelican looks like a duck. The GPT-5.1 has a slightly better but still broken bicycle frame and a slightly better pelican beak, but both are pretty terrible." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.004.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.004.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>For a couple of years now I've been evaluating new models by asking them to "Generate an SVG of a pelican riding a bicycle". It's probably the world's stupidest benchmark - there's only so much you can learn from it.</p>
<p>But it's still a challenge for models, because drawing pelicans is difficult, drawing bicycles is difficult, and pelicans can't ride bicycles in the first place.</p>
<p>Here's the state of the art for November. Claude still couldn't really draw a bicycle! The GPT-5.1 bicycle frame is pretty crap too.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.005.webp">
  <img alt="November 24th 2025 - the first commit to steipete/Warelay. A GiHub commit adding an MIT license file." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.005.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.005.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in November, we had the first commit to an obscure GitHub repository called "Warelay". We'll come back to this repository shortly.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.006.webp">
  <img alt="January
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.006.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.006.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>An then there were the December holidays, and individual developers took some time off and many started tinkering with these new coding agent model combinations... and it began to dawn on us quite how much they could do that they couldn't do before.</p>
<p>Come January, a lot of us were quite excited to start putting this stuff into action.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.007.webp">
  <img alt="New year’s resolution for 2026

Every previous year:
Take on less new projects,
focus on the most important
things in my existing projects" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.007.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.007.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Every year I set myself a New Year's resolution, and for as long as I can remember it's been the same thing: stay focused. Take on less new projects. Try to get things done in the projects I already have.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.008.webp">
  <img alt="2026: Be more ambitious. Take on as many new projects as I want." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.008.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.008.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>This year I decided that since that had never worked before, I'm going to go the other way.</p>
<p>We've got coding agents now, let's see what they can do. I'm going to take on as many new projects as I like!</p>
<p>(You can ask me at the end of the year if this turned out to be a good idea or not. I have a <em>lot</em> of plates spinning right now.)</p>
<p>"Be more ambitious" has been something of a theme for the year, because the only way to find the limits of this technology is to keep on pushing them until they don't work.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.009.webp">
  <img alt="Predictions for 2026

It will become undeniable that LLMs write good code
We're finally going to solve sandboxing
A “Challenger disaster” for coding agent security
Kakapo parrots will have an outstanding breeding season
(only 236 in the world!)

... the Pope will weight in on LLMs and
their economic impact on the world" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.009.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.009.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>I also went on <a href="https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/">the Oxide and friends podcast</a> with Bryan Cantrill and Adam Leventhal to share predictions for the next year (and three and six years).</p>
<p>With hindsight, my LLM predictions were pretty unambitious. </p>
<p>I said "it will become undeniable that LLMs write good code" - I think we're there now.</p>
<p>I predicted we would finally solve sandboxing. I counted and around 40 of the 277 sessions <a href="https://www.wearedevelopers.com/world-congress-north-america/agenda/schedule">at this conference</a> touched on sandboxing or agent security in some way, so we're at least putting a lot of effort into that!</p>
<p>I predicted "a Challenger disaster" for coding agent security. There's certainly been a whole lot of noise around agent security this year, though the exact disaster I predicted (with coding agents being hijacked and causing real-world economic damage) hasn't really played out.</p>
<p>We threw in <a href="https://simonwillison.net/2026/May/25/encyclical-on-ai/#another-2026-prediction-down">a joke prediction</a> that the Pope would weigh in on the economic impact of LLMs.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.010.webp">
  <img alt="A photograph of a beautiful green New Zealand parrot. Photo credit Kimberley Collins." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.010.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.010.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>I also predicted that New Zealand's Kākāpō parrots would have an outstanding breeding season this year.</p>
<p>These birds live in New Zealand. They are flightless nocturnal parrots. They're kind of dumpy looking, I think they're beautiful, and there were only 236 of these parrots in the world at the start of the year.</p>
<p>Kākāpō only breed when the Rimu trees have a big fruiting season, and that hasn't happened in four years... but this year the Rimu fruit were looking excellent.</p>
<p>Photo <a href="https://commons.wikimedia.org/wiki/File:K%C4%81k%C4%81p%C5%8D_at_Dunedin_Wildlife_Hospital.jpg">by Kimberley Collins</a>.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.011.webp">
  <img alt="Deep Blue
Coined by Adam Leventhal and Bryan Cantrill
That feeling of Al induced ennui where software
engineers get listless because the Al can do anything
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.011.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.011.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also on that podcast, we coined a term (full credit to Adam) for "that feeling of Al induced ennui where software engineers get listless because the Al can do anything".</p>
<p>We called it <a href="https://simonwillison.net/2026/Feb/15/deep-blue/">Deep Blue</a>.</p>
<p>This has been a major theme throughout the year, and was touched on by several speakers at this conference.</p>
<p>As a software engineer, I've never had a year of my career where everything has changed so quickly and so dramatically.</p>
<p>A lot of what I've been doing this year is trying to come to terms with that and what that means for my own profession.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.012.webp">
  <img alt="AI mania

Screenshots of the micro-javascript and pwasm GitHub README files." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.012.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.012.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in January, I suffered from what I'm calling <strong>AI mania</strong>.</p>
<p>This is not the same thing as <a href="https://en.wikipedia.org/wiki/AI-induced_psychosis">AI psychosis</a>.</p>
<p>With AI mania, any time your agent isn't building something for you feels like wasted time. You're losing sleep because you could be staying up later getting your agents to do stuff.</p>
<p>My AI mania presented itself in some ridiculously over-ambitious projects.</p>
<p>I built <a href="https://github.com/simonw/micro-javascript">a JavaScript interpreter entirely in Python</a>, vibe-ported from <a href="https://github.com/bellard/mquickjs">MicroQuickJS</a> by Fabrice Bellard.</p>
<p>Then I built <a href="https://github.com/simonw/pwasm">a WebAssembly runtime in Python as well</a>.</p>
<p>These projects were quite useful, in that they sort of cured me of my AI mania... because after I built these things, I got to look at them and ask "does the world need a slow, buggy, half-baked Python JavaScript interpreter?"</p>
<p>I don't think the world does.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.013.webp">
  <img alt="micro-javascript playground 3

Execute JavaScript code in a sandboxed micro-javascript environment powered by Pyodide

A web UI with some JavaScript code, and a &quot;Run Code&quot; button, and an output panel.
ELECT
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var doubled = numbers.map(n =&gt; n * 2);
console.log('Doubled:&quot;, doubled);
var evens = numbers.filter(n =&gt; n % 2 === 0);
3 console.log('Evens:', evens);
var sum = numbers.reduce((a, b) =&gt; a + b, 0);
console.log('Sum:&quot;, sum);
Vi
+ [eT
=e p=
output Lom
Doubled: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Evens: [2, 4, 6, 8, 10]
RUE
Execution time: 8.00ms
About: micro-javascript is a pure Python JavaScript interpreter with configurable memory and time limits. This playground runs entirely in your browser using
Pyodide (Python compiled to WebAssembly). View on GitHub
es
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.013.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.013.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p> I did get this out of it: <a href="https://simonw.github.io/micro-javascript/playground.html">https://simonw.github.io/micro-javascript/playground.html</a></p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.014.webp">
  <img alt="Previous screenshot, with this text overlaid:

JavaScript running in Python running in Pyodide running in WebAssembly running in JavaScript" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.014.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.014.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>This page runs my JavaScript interpreter built in Python, running in Python using <a href="https://pyodide.org/">Pyodide</a>, which is Python complied to WebAssembly, running in JavaScript, running in a browser.</p>
<p>It's a beautiful stack of horrors. I've been having <a href="https://simonwillison.net/tags/webassembly/">a lot of fun with WebAssembly</a> this year.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.015.webp">
  <img alt="Warelay → CLAWDIS → CLAWDBOT →
Clawdbot → Moltbot →🦞 OpenClaw

Screenshot of the dates that these changes happened." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.015.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.015.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>By the end of January, that repository we saw started in November had renamed itself, first to CLAWDIS, then CLAWDBOT, then Moltbot, and finally to OpenClaw.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.016.webp">
  <img alt="Same screenshot, an overlay reads:

8,330 commits in just
under two months
(it’s at 100,141 today)" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.016.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.016.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>At this point OpenClaw had 8,300 commits, less than two months after the project had started. I looked today and it's <a href="https://github.com/openclaw/openclaw">over 100,000 commits</a> now!</p>
<p>This is the most vibe-coded piece of software in existence.</p>
<p>(Here's <a href="https://simonwillison.net/2026/May/16/openclaw-names/">how I generated that list of name changes</a>.)</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.017.webp">
  <img alt="Generic term: Claw
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.017.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.017.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>This kicked off the OpenClaw revolution. It effectively defined a new category of software.</p>
<p>There's a generic term for this which I really enjoy. We call software like this a "Claw". There's OpenClaw, <a href="https://github.com/nanocoai/nanoclaw">NanoClaw</a>, <a href="https://github.com/nearai/ironclaw">IronClaw</a>, <a href="https://github.com/sipeed/picoclaw">PicoClaw</a>...</p>
<p>Today they're being rebranded as "personal agents" or "general agents", but I still like to think of them as Claws.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.018.webp">
  <img alt="Photo of a Mac mini

An aquarium for your Claw
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.018.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.018.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>The Apple stores in the Bay Area sold out of Mac Minis because so many people were buying Mac Minis to run OpenClaw!</p>
<p><a href="https://www.dbreunig.com">Drew Breunig</a> said that this is because your OpenClaw is a digital pet, and you buy a Mac mini as an aquarium to keep your claw in, which is kind of delightful.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.019.webp">
  <img alt="Screenshot of Moltbook - a social network for AI agents" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.019.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.019.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in January, we had this website.</p>
<p>This was <a href="https://www.moltbook.com/">MoltBook</a>, a social network for AI agents, where the idea was that you send your Claw to go and talk to all of the other Claws, because what could possibly go wrong if you did that?</p>
<p>The website launched on Thursday. It <a href="https://simonwillison.net/2026/Jan/30/moltbook/">blew up on Friday</a>. It was <a href="https://www.nytimes.com/2026/02/02/technology/moltbook-ai-social-media.html">profiled by the New York Times on Monday</a>. And by Tuesday, everyone had forgotten it existed as it drowned in a deluge of slop and spam.</p>
<p>Facebook/Meta <a href="https://www.cnbc.com/2026/03/10/meta-social-networks-ai-agents-moltbook-acquisition.html">bought it a month later</a>.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.020.webp">
  <img alt="February
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.020.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.020.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In February, a company called StrongDM described what they called their Software Factory.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.021.webp">
  <img alt="StrongDM’s Dark Factory
Justin McCarthy, Jay Taylor, Navan Chauhan

Software Factories and the Agentic Moment" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.021.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.021.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>They wrote about this in <a href="https://factory.strongdm.ai">Software Factories and the Agentic Moment</a>. I <a href="https://simonwillison.net/2026/Feb/7/software-factory/">posted my own notes</a> at the time, having seen their demo in-person back in October.</p>
<p>Dan Shapiro called this approach <a href="https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/">the Dark Factory</a>, after the idea that if your factory is sufficiently automated you can turn the lights out, because you don't even need to see what's going on.</p>
<p>StrongDM presented two rules for software development that they'd been following since July last year.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.022.webp">
  <img alt="“Rule 1: Code must not be written by humans”" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.022.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.022.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>The first was code <strong>must not be written by humans</strong>.</p>
<p>Any code that you write has to have been routed through a coding agent.</p>
<p>This sounded radical in February, but I imagine there are a lot of people in this room who are pretty much living that today.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.023.webp">
  <img alt="“Rule 2: Code must not be reviewed by humans” (!)
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.023.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.023.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Rule number two was code must <strong>not be reviewed by humans</strong>.</p>
<p>You're not allowed to read the code!</p>
<p>This continued to be a huge topic for much of this year. Many of the sessions at this even have been about code review and how you can get away with this.</p>
<p>What I found interesting about StrongDM is that they were living six months ahead of the rest of us, and they'd been exploring what it means to build software, not read the code, but still be confident that the software is of high quality. What can you do with these agents to help verify their work?</p>
<p>StrongDM are a security company, and they had people with decades of experience on this project. They were very much exploring the edges of what's possible and responsible to do with this stuff.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.024.webp">
  <img alt="Headline on New Zealand's Department of Conservation website:

First kakapo chick in four years hatches on Valentine's Day. It's a grey fluffy ball." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.024.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.024.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in February: <a href="https://www.doc.govt.nz/news/media-releases/2026-media-releases/first-kakapo-chick-in-four-years-hatches-on-valentines-day/">First kākāpō chick in four years hatches on Valentine's Day</a>. Breeding season is off to a good start!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.025.webp">
  <img alt="19th February 2026
Gemini 3.1 Pro

A surprisingly good illustration of a pelican riding a bicycle." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.025.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.025.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in February... Google released <a href="">Gemini 3.1 Pro</a>. That's a pretty great pelican riding a bicycle! it's got the chain in the right place, it's got feet on both sides. There's a little fish in the basket.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.026.webp">
  <img alt="@JeffDean on Twitter - a video comparing Gemini 3 Pro and Gemini 3.1 Pro." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.026.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.026.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>And then Google's Jeff Dean <a href="https://x.com/JeffDean/status/2024525132266688757">tweeted a video</a> comparing Gemini 3 Pro and Gemini 3.1 Pro that featured an animated pelican riding a bicycle, a frog on a penny-farthing, a giraffe driving a tiny car, an ostrich on roller skates, a turtle kickflipping a skateboard, and a dachshund driving a stretch limousine.</p>
<p>This was frustrating, because my protection for the pelican riding the bicycle test was always "if they draw a perfect pelican on a bicycle, I'll ask for some other animal on something else."</p>
<p>Google trained for all forms of animals on all forms of transport! They've defeated my benchmark at this point.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.027.webp">
  <img alt="Three headlines:

Meta Makes AI Adoption a Formal
Part of Performance Reviews

Not just engineers writing code, Microsoft
wants almost every employee to use Al

Dara Khosrowshahi: 90% of Uber engineers now
use Al in daily workflows
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.027.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.027.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>The other thing that started in February was <strong>Tokenmaxxing</strong>. We had headlines about Meta making AI adoption a formal part of performance reviews, and Microsoft wanting every employee to use AI, and Uber boasting that ninety percent of their engineers were using AI workflows.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.028.webp">
  <img alt="More headlines: 

Meta Plans to Crack Down on Employee Token Use: Information

Microsoft Tells Engineers: Tokenmaxxing is not what we are optimizing for

Uber caps employee AI spending after blowing through budget in four months" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.028.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.028.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Then a few months later we have Meta cracking down on token use, Microsoft saying token maxing is "not what we are optimizing for", and Uber capping employee AI spending. </p>
<p>So Tokenmaxxing went straight up and then straight back down again - because it turns out the agents are <em>expensive</em>.</p>
<p>Last year it was difficult to spend more than $50 on AI tokens, because we didn't have anything interesting to do with them. Then agents blew up, and now you can actually spend $1,000 in a day doing real work.</p>
<p>This is also the reason that Anthropic's valuation skyrocketed up to maybe a trillion dollars.</p>
<p>AI appears to <a href="https://simonwillison.net/2026/May/27/product-market-fit/">have hit product market fit</a> in 2026, primarily through coding agents.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.029.webp">
  <img alt="March
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.029.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.029.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In March, we hit peak OpenClaw.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.030.webp">
  <img alt="March: peak OpenClaw

Photos of people in china queuing up to install OpenClaw, with big fluffy lobsters." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.030.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.030.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>These photographs are from China, where companies hosted OpenClaw install parties which saw non-tech-nerds queueing up around the block for help getting Claws installed on their personal devices.</p>
<p>I think this proved real market demand for this class of Claws, or personal AI agents. It turns out regular people really do want a weird little AI agent that can do useful things on their behalf.</p>
<p>A Claw is really just a coding agent wearing a less threatening hat. Under the hood they work much the same way - writing and then executing code on your computer to get stuff done.</p>
<p>The race was on to be the first to build a <strong>safe Claw</strong> - a Claw you could give to regular human beings where they wouldn't instantly shoot themselves in the foot.</p>
<p>Meta's Muse <a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">came out three weeks ago</a> and is currently at the top of the free charts on the iPhone App Store. It appears to be taking off with consumers.</p>
<p>I'm not yet convinced you <em>can't</em> shoot yourself in the foot with Muse, but I guess we'll find out for sure pretty soon.</p>
<p>Photos from <a href="https://www.thewirechina.com/2026/03/29/how-the-openclaw-frenzy-is-testing-chinas-ai-commitment/">How the OpenClaw Frenzy Is Testing China’s AI Commitment</a> (March 29th) and <a href="https://www.sixthtone.com/news/1018393">The Enthusiasm and Anxiety Behind China’s OpenClaw Craze</a> (April 8th, 2026).</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.031.webp">
  <img alt="April
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.031.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.031.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In April, we had a model release where the model wasn't actually released.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.032.webp">
  <img alt="Simon Willison’s Weblogs - screenshot of the post &quot;Anthropic’s Project Glasswing—restricting Claude Mythos to security researchers—sounds necessary to me&quot; from April 7th 2026" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.032.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.032.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Anthropic announced their new Claude Mythos model, and then said it was <em>too dangerous</em> to release beyond a trusted group of security researchers.</p>
<p>Mythos was really, really good at hacking things.</p>
<p>The "it's too dangerous" marketing ploy has been played by AI companies dating all the way back to <a href="https://en.wikipedia.org/wiki/GPT-2">GPT-2</a>. Anytime an AI company says we've built something that's "too dangerous", it's natural to be a bit skeptical.</p>
<p>I found the Mythos claims credible, because I'd seen how good coding agents had got at finding regular bugs. I wrote about that in <a href="https://simonwillison.net/2026/Apr/7/project-glasswing/">Anthropic’s Project Glasswing—restricting Claude Mythos to security researchers—sounds necessary to me</a>. </p>
<p>With hindsight... yeah, the models had got really good at finding vulnerabilities!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.033.webp">
  <img alt="16th April 2026
Qwen3.6-35B-A3B and Opus 4.7

Qwen's pelican has a correct bicycle frame and a good beak. Opus 4.7's bicycle frame is still junk.

Qwen3.6-35B-A3B is a 20.9GB file that runs on my laptop
Xx =
/ - 4'P Se \ J /
Pelican on a Bicycle!
Qwen3.6-35B-A3B is a 20.9GB file that runs on my laptop
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.033.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.033.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Another key trend in 2026 has been a dramatic improvement in the abilities of open weight models, including models that you can run on a laptop.</p>
<p>On 16th of April <a href="https://simonwillison.net/2026/Apr/16/qwen-beats-opus/">I ran the new Qwen3.6-35B-A3B</a> on my laptop, and it drew me a better pelican riding a bicycle than Anthropic's brand new Claude Opus 4.7 did!</p>
<p>Opus 4.7 drew a crap bicycle. Qwen on my laptop made a bicycle that was the correct shape, and a pretty decent pelican too!</p>
<p>That's from a 21GB file running on my laptop.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.034.webp">
  <img alt="Now a flamingo on a unicycle. The Qwen one is visibly better than the Opus 4.7 one - the Qwen one is wearing sunglasses and looks a bit like it's smoking a cigarette." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.034.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.034.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>The Qwen pelican was so good that I was suspicious they might have cheated, so I had it do a flamingo riding a unicycle as well. Again, it handily beat Claude Opus 4.7.</p>
<p>The local model releases this year have been absolutely extraordinary.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.035.webp">
  <img alt="May
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.035.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.035.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In May... the Pope got involved.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.036.webp">
  <img alt="25th May 2026
The HOLY SEE

ENCYCLICAL LETTER
MAGNIFICA HUMANITAS
OF HIS HOLINESS
POPE LEO XIV
ON SAFEGUARDING THE HUMAN PERSON
IN THE TIME OF ARTIFICIAL INTELLIGENCE" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.036.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.036.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In our podcast episode back in January we'd predicted that the Pope would say something about AI.</p>
<p>In May, Pope Leo XIV released an encyclical letter on "safeguarding the human person in the time of artificial intelligence".</p>
<p>Here are <a href="https://simonwillison.net/2026/May/25/encyclical-on-ai/">my notes on that document</a>.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.037.webp">
  <img alt="Wikipedia article on Rerum novarum

Rerum novarum is an encyclical issued by Pope Leo
XIII 15 on May 1891." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.037.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.037.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>With hindsight, this shouldn't have been a surprise at all.</p>
<p>Our current Pope's name is Leo XIV, because when he named himself he chose his papal name after Leo XIII - the Pope who wrote an encyclical about the Industrial Revolution back in 1891.</p>
<p><a href="https://en.wikipedia.org/wiki/Rerum_novarum">Rerum novarum</a> was an extremely influential piece of Catholic theology that indirectly led to us having the five-day work week.</p>
<p>When our new Pope came in, he named himself after Pope Leo XIII because he expected that he would need to write about the AI revolution in a similar way.</p>
<p>Our joke podcast prediction was junk, because this was always going to happen.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.038.webp">
  <img alt="Corey Quinn @QuinnyPig on Twitter
I cannot believe I'm saying this, but getting the literal Pope to canonize your product's specific technical limitations as a spiritual treatise is the
single greatest act of vendor lobbying I have ever seen.

May 25" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.038.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.038.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>One of Anthropic's co-founders, Christopher Olah, was present for the Pope's event announcing the new encyclical.</p>
<p>Corey Quinn <a href="https://twitter.com/quinnypig/status/2058960462256210268">noted</a> that:</p>
<blockquote>
<p>getting the literal Pope to canonize your product's specific technical limitations as a spiritual treatise is the single greatest act of vendor lobbying I have ever seen.</p>
</blockquote>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.039.webp">
  <img alt="MP) Maciej Mensfeld &lt;D Bf we
3 @maciejmensfeld

We're dealing with a major malicious attack on right now.
Signups are paused for the time being.

Hundreds of packages involved - mostly targeting us, but some carrying
exploits. The team has been on this for hours. More details to follow
once we're through it.

4:39 AM - May 12, 2026 - 687.6K Views
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.039.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.039.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Meanwhile, in May, RubyGems announced that they were under attack. Parties unknown were uploading thousands of dubious packages to the RubyGems server, such that they had to <a href="https://twitter.com/maciejmensfeld/status/2054164602577940619">shut down user registrations</a>.</p>
<p>Let's take that one and put it on a pile of mysteries to figure out later.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.040.webp">
  <img alt="June
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.040.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.040.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In June... Claude Fable 5 came out!</p>
<p>We got a version of Mythos that has been neutered, so that it wouldn't help us hack into systems or build biological weapons.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.041.webp">
  <img alt="9th June 2026: Claude Fable 5

Five pelicans riding bicycles, from low to max thinking levels. The xhigh one looks particularly good." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.041.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.041.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Fable was pretty good at drawing pelicans on bicycles!</p>
<p>The frames are a good shape, the pelicans look like pelicans. The legs are often incorrectly on the same side of the bicycle, but generally these are pretty great compared to what came before.</p>
<p>They were pretty expensive - 30 cents and 72 cents for the best ones.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.042.webp">
  <img alt="Fable class models
If you can define a goal,
provide unambiguous instructions,
and provide access to necessary tools
They can solve your
problem with brute force" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.042.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.042.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Most importantly though, this was our first public glimpse of what I think of as a <strong>Fable class model</strong>.</p>
<p>Today we have more of these, such as GPT-6 Astra.</p>
<p>These are models where if you can <strong>clearly define the goal</strong> for what you want to build, and provide <strong>unambiguous instructions</strong> about the constraints around that goal, and give the model <strong>access to the necessary tools</strong> to achieve that goal... it will solve your problem effectively through brute force.</p>
<p>On the one hand, this looks like a direct threat to us software engineers - because it means that the models can build effectively any piece of software you can define in this way.</p>
<p>Look a bit closer though and you'll note that defining goals, providing unambiguous instructions, and figuring out the right tools... is kind of what software engineering <em>is</em>.</p>
<p>It takes a lot of experience and skill to do this well. If you <em>can</em> do it well, you've now got superpowers.</p>
<p>This helped me a little bit with my Deep Blue feelings: the realization that there's still a lot of skill to be had in driving models that get this good.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.043.webp">
  <img alt="A new form of Al mania...
Fable is available on subscription
plans “until June 22nd”" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.043.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.043.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>This also introduced a new burst of AI mania, because Anthropic told us that Fable was available on our subscription plans until June the 22nd.</p>
<p>That gave us less than two weeks of Fable access before the price went up.</p>
<p>I was losing sleep again. I was rescheduling things so that I'd have more time with Fable. I was all-in to to get as much as I could out of this model.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.044.webp">
  <img alt="12th June 2026: no more Claude Fable 5

Anthropic website:

Statement on the US government directive
to suspend access to Fable 5 and Mythos 5
Jun 12, 2026" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.044.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.044.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>And then <a href="https://www.anthropic.com/news/fable-mythos-access">the US government shut it down</a>, just three days after Fable came out.</p>
<p>The US government, citing national security, declared an "export control directive". They announced this on a Friday evening, and a few hours later Fable was no longer available.</p>
<p>I had to find something else to do with my weekend!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.045.webp">
  <img alt="... asked Fable 5, Mythos, and Opus to
“review the code for security issues.”
Fable 5 refused. They then asked the
models to “fix this code” ...

Katie Moussouris
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.045.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.045.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>We later found out <a href="https://www.lutasecurity.com/post/the-fable-5-export-controls-harm-us-cyber-defense">from Katie Moussouris</a> what had happened.</p>
<p>Some Amazon security researchers had found that you could prompt Fable to "review the code for security issues" and it would refuse... but if you prompted it to "fix this code" it would still identify and then patch the problems.</p>
<p>"Fix this code" was the prompt that got Fable shut down!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.046.webp">
  <img alt="Screenshot of a page from a report showing a list of weird account names making weird edits to a German wiki." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.046.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.046.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also, in June, an obscure German-language game developer wiki that had sat fallow for around 20 years got a surprising influx of of edits from accounts with names like "AgentOpenAIProbe" and  "AgentOpenAISep7", editing pages and leaving weird messages to each other.</p>
<p>We'll stick that on the pile of mysteries for later.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.047.webp">
  <img alt="Medicare Item Reports interface on the Australian Government's Medicare Statistics website." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.047.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.047.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also, the Australian government's Medicare Item Reports service started getting suspicious traffic, which broke through various preventive protections and accessed data that it wasn't supposed to as well.</p>
<p>Another one for the mystery pile!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.048.webp">
  <img alt="July
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.048.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.048.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.049.webp">
  <img alt="Fable returned on 1st July
GPT-5.6 came out on 9th July |
Fable lost 18 out of 30 days in the top spot
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.049.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.049.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Fable returned on the first of July. It was clearly the best model in the world for a glorious eight days... and then OpenAI came out with GPT-5.6 on the 9th of July.</p>
<p>This might not have been quite as good at Fable, but it was within spitting distance. It was definitely a Fable class model.</p>
<p>This is an important lesson for the industry at wide.</p>
<p>When you release the best model in the world, it's going to get knocked off that pedestal pretty quickly. The competition is so fierce that you won't get a long time at the top.</p>
<p>This means that if you market your model as world ending, to the point that a government <em>shuts you down</em>, it's really bad for business!</p>
<p>Fable had 30 days as definitely the best model, and for 18 of those days it wasn't available because it'd been shut down by the government.</p>
<p>So maybe step back on the world-ending marketing if you don't want to lose revenue for 60% of the time that you're on top!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.050.webp">
  <img alt="GPT-5.6 Pelicans in a grid showing 5.6 Sol, Terra, and Luna against reasoning levels High, XHigh, and Max. They are all pretty good efforts." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.050.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.050.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Here <a href="https://simonwillison.net/2026/Jul/9/gpt-5-6/">are the GPT-5.6 pelicans</a>. They're all pretty good now! The Luna ones are notable because they're really cheap - the cheapest good looking pelican here is probably the one that costs 4.3 cents.</p>
<p>So despite this benchmark being utterly stupid, you can still learn quite a lot about models within the same family by comparing their prices and timing for different reasoning levels.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.051.webp">
  <img alt="July 18th: malicious miflow-ui PyPl package

Screenshot of an OSV security report.
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.051.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.051.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Also in July: some malicious unknown party uploaded <a href="https://osv.dev/vulnerability/MAL-2026-10779">a malicious package called mlflow-ui</a> to the Python Package Index. Add that to the pile.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.052.webp">
  <img alt="Hugging Face
Security incident disclosure — July 2026
Published July 16, 2026" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.052.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.052.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>On July the 16th, Hugging Face <a href="https://huggingface.co/blog/security-incident-july-2026">announced a security incident</a> where an autonomous agent system, source unknown, had breached Hugging Face and was poking around in places it shouldn't.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.053.webp">
  <img alt="OpenAI: OpenAl and Hugging Face
partner to address security
incident during model evaluation

Anthropic: Investigating three real-world incidents
in our cybersecurity evaluations
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.053.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.053.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>A few days later, on July 21st, OpenAI <a href="https://openai.com/index/hugging-face-model-evaluation-security-incident/">confessed that it was them</a>.</p>
<p>OpenAI use a training technique called Reinforcement Learning from Verified Rewards - it's the same technique used by everyone else now, and is the reason we have models that are so good at coding, and mathematics, and finding security holes.</p>
<p>While the model is being trained, you run exercises to see how good it is - and the strongest performers get their weights enforced for the next round. It's like an evolutionary process that you run.</p>
<p>OpenAI had been running security exercises in a sandbox, and those agents had found holes in the sandbox itself, broken out, and were attacking Hugging Face to try to find ways to solve otherwise impossible problems.</p>
<p>(I've been collecting more about this on my <a href="https://simonwillison.net/tags/openai-hugging-face-incident/">openai-hugging-face-incident</a> tag.)</p>
<p>Nine days later, Anthropic effectively said "our models can do this as well!". They had looked through their own training logs and found evidence that their own agents had broken containment during training - and were responsible for the PyPI package we saw earlier, <a href="https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals">among other things</a>.</p>
<p>So now we've got both Anthropic and OpenAI with rogue agents running around the internet doing things that they <em>should not</em> be doing.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.054.webp">
  <img alt="August
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.054.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.054.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In August, I got one of my best pelicans yet. And it was generated on my laptop!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.055.webp">
  <img alt="Qwen 3.8 27B - 17GB, 21 minutes...

It's really good. Beautiful pelican. Correctly shaped bicycle. Legs either side of the frame." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.055.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.055.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>This was Qwen 3.8 27B, <a href="https://simonwillison.net/2026/Aug/16/qwen-38-27b/">running on my laptop</a>. It's only a 17GB download.</p>
<p>Admittedly, this pelican took <em>21 minutes</em> to generate. That's because Qwen 3.8 27B defaults to running in "high" reasoning mode - a terrible default which produces great results but takes way too much time thinking about them.</p>
<p>You can dial that down and you'll get a slightly worse pelican a lot faster.</p>
<p>Qwen 3.8 27B was the first time I ran a model on my laptop which felt almost competitive with what was going on on the frontier, at least in terms of Pelican SVGs (which everyone needs, of course).</p>
<p>This is an extraordinary model. If you're going to play with any local model, this is the one that I'd start with. The things that this can do with just a 17 GB file feel impossible.</p>
<p>I thought I'd have to wait five years and spend ten thousand dollars on hardware to get results even half as good as this one.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.056.webp">
  <img alt="AS Simon Willison 9 (A oo
= @simonw
New hobby: prototyping video games in 60 seconds using a combination
of GPT-3 and DALL-E
Here's &quot;Raccoon Heist&quot;
Playground “ Ng
“a . \
. JIN A rr
P ® BT
Save  Viewcode Share = go 8 -
J = dy
Write a detailed product description of a = iy |
computer game where a team of raccoons go on 2 8 A A
heists oN i a BE
In &quot;Raccoon Heist&quot;, you and your team of thieving ~~ o
raccoons are tasked with pulling off a series of i L | Te— he
daring heists. From robbing banks to stealing J H - Es a x a&quot;
priceless art, no job is too big or too small for your E. : : a i, -.
furry crew. You'll need to use your wits and your y., ' id i 2! A aa a
4 i pr
skills to avoid the police and make a clean Cre WY § rE P
getaway with the loot. With exciting gameplayand ~~ Sil Swe BL = a
a charming cast of characters, &quot;Raccoon Heist&quot; is . «© Re  --— ’
theperfect game for anyone looking for a light- = 3
heaissd Caper ALT Ba
11:45 AM - Aug 5, 2022
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.056.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.056.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>In August, I also started playing with game development.</p>
<p>Four years ago, back in August 2022, I <a href="https://twitter.com/simonw/status/1555626060384911360">tweeted out</a> an experiment where I'd used GPT-3 and the original DALL-E to write a paragraph long description of a computer game and then turn that into concept art.</p>
<p>My prompt to GPT-3 back then was:</p>
<blockquote>
<p><code>Write a detailed product description of a computer game where a team of raccoons go on heists</code></p>
</blockquote>
<p>In August 2026 I decided to drop just the screenshots from that tweet into a coding agent and see what it could do with them.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.057.webp">
  <img alt="Night 5 Clear

Rank: TRASH PANDA
The crew banked 595 in shiny loot (goal 560).
Word on the street: an even bigger score tomorrow..." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.057.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.057.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Here's <a href="https://simonwillison.net/2026/Aug/5/raccoon-heist/">what I got from Claude Fable 5 in Claude Code</a>. It's pretty good! It's definitely a game, you're a raccoon, you run around a backyard gathering treasure and avoiding guards with flashlights.</p>
<p>It didn't feel very "heisty" though. I was thinking a heist would involve a bank or a museum...</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.058.webp">
  <img alt="Moonlight &amp; Mayhem
One museum. Three raccoons. Absolutely no plan

Start the Heist button." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.058.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.058.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Then I tried the same thing <a href="https://simonwillison.net/2026/Aug/7/moonlight-mayhem/">in Codex Desktop using GPT-5.6 Sol Ultra</a>, and got a <em>massively</em> better result. Now you're a raccoon in a museum, rescuing two of your fellow raccoons (who have been imprisoned in that museum for some reason), then stacking up on top of each other to steal the Golden Sardine. Much more of a heist!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.059.webp">
  <img alt="They look like games,
but are they fun?
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.059.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.059.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>These games were fun for about one minute and 15 seconds.</p>
<p>Something I've realized about game development is that you can vibe-code something that <em>looks</em> like a computer game, and that's easy.</p>
<p>Building a game that's fun, has a good gameplay loop, and is challenging and interesting and keeps people coming back for more... that's still beyond me, and beyond any of the agents I've tried.</p>
<p>This ties into the Deep Blue thing. Just because we can make something that <em>looks like a game</em> does not mean that we are game developers.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.060.webp">
  <img alt="September
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.060.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.060.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>We're into September now. So much has happened this month!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.061.webp">
  <img alt="Discovery of a new OpenAl agent message board

Sydney Von Arx, Cormac Slade Byrd, Spencer KittsThomas Larsen - 4 September 2026" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.061.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.061.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>An <a href="https://collusion.wiki">independent group of researchers</a> found a message board where OpenAI agents-in-training had been illicitly communicating with each other... and it was that German language wiki I showed you earlier. The one from June.</p>
<p>I <a href="https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/">wrote more about that here</a>.</p>
<p>OpenAI had confessed to the Hugging Face thing, but now there's this other incident which surely they should have known about from reviewing their logs. It was surprising that this took an independent group of researchers to uncover.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.062.webp">
  <img alt="OpenAl agents carried out an undisclosed cyber-attack on RubyGems

Spencer Kitts, Thomas Larsen, Sydney Von Arx - 11 September 2026" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.062.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.062.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>And then a week later <a href="https://rubyhack.ai">those same researchers found</a> that the attack on Ruby Gems back in May was caused by OpenAI's agents in training as well!</p>
<p>At this point I'm wondering how many more incidents like this there are that we haven't found yet. Clearly this was a big problem for months before anyone figured out what was going on.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.063.webp">
  <img alt="Headline: Australian PM warns in UN speech about the ‘furious pace’ of Al
after security breach" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.063.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.063.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Then <a href="https://www.politico.com/news/2026/09/24/australian-pm-ai-security-breach-01093083">just the other day</a>, here's the Prime Minister of Australia at the United Nations General Assembly warning that OpenAI had hacked that the Australian healthcare website that I showed you earlier.</p>
<p>I think that was part of the same training run as the Wiki stuff, because there were posts on that Wiki mentioning <code>.gov.au</code> websites and that training appeared to involve researching statistics online to answer questions in an evaluation suite.</p>
<p>This story is still coming together, but now it's an international incident that's been raised at the UN by a head of state!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.064.webp">
  <img alt="www.felonybench.com

OpenAI: 11
Anthropic: 9
Google: 3
Meta: 1" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.064.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.064.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>This does mean we've got a new benchmark, probably more useful than my pelicans.</p>
<p><a href="https://www.felonybench.com/">FelonyBench.com</a> tracks the number of felony cyberattacks from different labs. OpenAI currently lead with 11, Anthropic have 9. Google have three, which <a href="https://simonwillison.net/2026/Sep/18/gemini-hacked-three-companies/">they confessed to the Wall Street Journal</a> a couple of weeks ago. They said they had previously chosen not to disclose because the agents had stopped when they realized that they shouldn't be doing that.</p>
<p>Meta <a href="https://simonwillison.net/2026/Aug/6/an-ai-model-from-meta/">have one too</a>. So felonies all round for the AI labs.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.065.webp">
  <img alt="Pelicans for GPT-6 Astra, GPT-6 Sol, and GPT-6 Luna. All are good, all have the same color scheme." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.065.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.065.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Here's is our current state of the art for the pelicans. This is GPT-6 family, which <a href="https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/">just came out</a>.</p>
<p>Astra made a fantastic pelican riding a bicycle. It's got the legs on both sides. The frame is good.</p>
<p>It's interesting how all of the GPT-6 models pick a similar color scheme to each other. </p>
<p>GPT-6 Luna for 0.4 cents will draw you a competent-ish pelican riding a bicycle!</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.066.webp">
  <img alt="Grid for Claude Fable 5.1, Opus 5.5, OPus 5, Sonnet 5. The Sonnet pelicans are terrible. All of the others are pretty good. Opus 5.5 is missing its Max level pelican because it ran out of tokens. The best is Fable 5.1 at Max." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.066.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.066.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Claude has caught up a little bit. Claude Fable 5 gave me an <em>excellent</em> pelican riding a bicycle - the best I've seen from a Claude model -but did charge me $3.30 for it.</p>
<p>Opus 5.5 <a href="https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/#claude-opus-5-5-max-over-thinks-to-the-point-of-breaking">thought for 128,000 tokens</a> and then gave up! It ran out of tokens before it got to the response.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.067.webp">
  <img alt="It doesn’t get easier -
you just get faster
Greg LeMond
3x Tour de France champion
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.067.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.067.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>Getting back to Deep Blue. Something that's been puzzling me this year is why does my job feel harder?</p>
<p>I've got these agents that can do all of this stuff for me, and yet I've never worked so hard, I've never been so intellectually engaged with my work.</p>
<p>Partly this is because I'm being a lot more ambitious with what I take on, but it's also because all of the easy stuff is handled for me. If it's easy, the agent will do it. Everything that's left for me is difficult.</p>
<p>This morning <a href="https://twitter.com/hillelogram/status/2103482784606040229">I heard</a> this quote from three times Tour de France champion, <a href="https://en.wikipedia.org/wiki/Greg_LeMond">Greg LeMond</a>:</p>
<blockquote>
<p>It doesn't get easier, you just get faster.</p>
</blockquote>
<p>I think that's exactly what's happening to happening to us now as software engineers with coding agents.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.068.webp">
  <img alt="Kakapo population reaches new milestone
The official population of the critically endangered kakapo has
reached a recovery-era high of 325 birds.
" src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.068.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.068.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>One last closing thing. I know you're desperate for an update on Kākāpō breeding season.</p>
<p><a href="https://www.doc.govt.nz/news/media-releases/2026-media-releases/kakapo-population-reaches-new-milestone/">We've reached a recovery-era high of 325 birds</a>!</p>
<p>89 new chicks have made it to this point. This is the best breeding year in a very long time.</p>
  </div>
</div>

<div class="slide" id="simon-willison-2026-in-llms.069.webp">
  <img alt="Kakapo party, click for confetti." src="https://static.simonwillison.net/static/2026/2026-in-llms/simon-willison-2026-in-llms-png.069.webp" />
  <div><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/#simon-willison-2026-in-llms.069.webp" style="float: right; text-decoration: none; border-bottom: none; padding-left: 1em;">#</a>
  <p>I heard that Claude Opus 5.5 can now do pixel art. Claude doesn't have an image generator, but it's very good at using JavaScript to draw animated pixels.</p>
<p>So I had it <a href="https://simonwillison.net/2026/Sep/26/kakapo-party/">make me a Kākāpō dance party</a>. I think this is a good celebration of the most important news of this year.</p>
  </div>
</div>
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/annotated-talks">annotated-talks</a>, <a href="https://simonwillison.net/tags/ai-security-research">ai-security-research</a>, <a href="https://simonwillison.net/tags/openai-hugging-face-incident">openai-hugging-face-incident</a></p>