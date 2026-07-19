---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.122259+00:00
title: lobste.rs is now running on SQLite
url: https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything
published: 2026-07-14
---

# lobste.rs is now running on SQLite

<p><strong><a href="https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite">lobste.rs is now running on SQLite</a></strong></p>
Community site <a href="https://lobste.rs">Lobsters</a> has been planning a migration away from MariaDB <a href="https://github.com/lobsters/lobsters/issues/539#issuecomment-4959857588">since August 2018</a> - originally targeting PostgreSQL, but last year they decided to <a href="https://github.com/lobsters/lobsters/issues/539#issuecomment-2964114295">investigate SQLite</a> instead.</p>
<p>This weekend they completed the migration, and now consider it stable enough that it looks like this is the permanent architecture for the site going forward:</p>
<blockquote>
<p>SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down</p>
</blockquote>
<p>The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB. <a href="https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite#c_c9ydhs">There's also</a> a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack_attack database used by the <a href="https://github.com/rack/rack-attack">Rack::Attack</a> middleware for blocking and throttling abusive requests.</p>
<p>There are plenty more details in both the linked thread and this <a href="https://github.com/lobsters/lobsters/pull/1927">SQLite migration PR</a> by Thomas Dziedzic, which added 735 lines and removed 593 lines across 30 commits and 188 files. That PR built on top of previous PRs <a href="https://github.com/lobsters/lobsters/pull/1705">#1705</a>, <a href="https://github.com/lobsters/lobsters/pull/1871">#1871</a>, and <a href="https://github.com/lobsters/lobsters/pull/1924">#1924</a>.</p>
<p>This is a really useful case study, and a great reminder that you can get a whole lot done with a single server and SQLite in 2026.


    <p>Tags: <a href="https://simonwillison.net/tags/migrations">migrations</a>, <a href="https://simonwillison.net/tags/ops">ops</a>, <a href="https://simonwillison.net/tags/rails">rails</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/lobsters">lobsters</a></p>
