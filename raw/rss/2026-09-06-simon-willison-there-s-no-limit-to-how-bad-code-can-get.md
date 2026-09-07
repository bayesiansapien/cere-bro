---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-07T03:49:28.698295+00:00
title: There's No Limit to How Bad Code Can Get
url: https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/
published: 2026-09-06
author: 
---

# There's No Limit to How Bad Code Can Get

<p><a href="https://lobste.rs/s/rfn2mn/there_s_no_limit_how_bad_code_can_get#c_8kdtaw">My comment</a> on <a href="https://lobste.rs/s/rfn2mn/there_s_no_limit_how_bad_code_can_get">There&#x27;s No Limit to How Bad Code Can Get</a> &mdash; Lobste.rs.</p><p><em>[In reply to a comment about burning it down to start from scratch when technical debt becomes overwhelming]</em></p>
<p>In my experience it's <em>so rare</em> for that to work.</p>
<p>You announce the old thing is irrecoverably drowning in tech debt. You spin up a team to rewrite it from scratch. Work begins.</p>
<p>Meanwhile the old thing remains a moving target: it's running the core business, so changes are still necessary. The developers working on it know that it's going to be made obsolete by the new thing soon, so they don't have any incentive to go beyond the smallest effort possible to add the new features. Technical debt continues to mount.</p>
<p>Meanwhile, the team working on the new thing are ambitious and probably a little naive. They start out at a great pace - it's greenfield after all - but as time progresses it becomes apparent that nobody fully understands the behavior and scope of the thing they are replacing. If it was well documented and tested it wouldn't <em>need</em> to be replaced, after all...</p>
<p>After months (or even years) without delivering value, the pressure is on to "ship it", so the new system is launched to handle a subset of what the old system handled - or often for some new feature that was too hard to build with the now mostly unmaintained old system.</p>
<p>... so now you have TWO systems in production - the janky old system that nobody wants to touch, and a new system which handles just a few production features and is 80% inactive code that is meant to replace the old system, eventually.</p>
<p>If you're <em>really lucky</em> the company won't have lost patience with the new system and will allow that work to continue. The longer this all takes, and the longer the old system stays in production and stubbornly continues to work, the higher the risk that "priorities have changed" and the new system total replacement work is abandoned, leaving you with two systems where you used to have one.</p>
<p>The best article I've read about completing this process responsibly is <a href="https://lethain.com/migrations/">Migrations: the sole scalable fix to tech debt</a> by Will Larson.</p>
<p>If I run into a situation like this in the future, my strong recommendation will be to shore up the old system with as much automated testing as possible and then seeing if targeted refactors can get it to the desired shape. My hunch is that in many cases that will have a much higher chance of success than the siren call of a greenfield replacement.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/migrations">migrations</a>, <a href="https://simonwillison.net/tags/technical-debt">technical-debt</a></p>
