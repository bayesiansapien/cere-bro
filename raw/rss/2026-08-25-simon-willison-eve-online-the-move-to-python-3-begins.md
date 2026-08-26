---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-26T07:18:10.709306+00:00
title: EVE Online: The Move to Python 3 Begins!
url: https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/
published: 2026-08-25
---

# EVE Online: The Move to Python 3 Begins!

<p><strong><a href="https://www.eveonline.com/news/view/the-move-to-python-3-begins">EVE Online: The Move to Python 3 Begins!</a></strong></p>
EVE Online has been one of the most interesting case studies in Python at scale for over twenty years now.</p>
<p>They've been running on <a href="https://github.com/stackless-dev/stackless/wiki/">Stackless Python</a> since their launch in 2003, and their last major upgrade was 16 years ago, to Stackless Python 2.7 <a href="https://www.eveonline.com/news/view/stackless-python-2.7">in 2010</a>.</p>
<p>Their upgrade to Python 3 will start using the <a href="https://python-future.org/futurize.html">futurize</a> script against 2.4 million lines of code, followed by careful manual review of the ~20,000 places where Python 2 and 3 behavior differ - for example <code>1 / 2</code> is <code>0</code> in Python 2 but is <code>0.5</code> in Python 3.</p>
<p>There's nothing in this announcement about how they plan to replace Stackless, but at their conference last year they presented <a href="https://youtu.be/-x299qHLQs0">Scheduling in Carbon: Leaving Stackless Python Behind</a> describing how they replaced Stackless in the Carbon engine for their more recent game EVE Frontier, using their (now open source) <a href="https://github.com/carbonengine/scheduler">carbonengine/scheduler</a> library.

    <p><small></small>Via <a href="https://lobste.rs/s/e1oalq/move_python_3_begins">Lobster.rs</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/eve-online">eve-online</a>, <a href="https://simonwillison.net/tags/migrations">migrations</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/python3">python3</a>, <a href="https://simonwillison.net/tags/stackless">stackless</a></p>
