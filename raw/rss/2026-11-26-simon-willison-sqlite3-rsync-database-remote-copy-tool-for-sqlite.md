---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-27T05:29:25.097914+00:00
title: sqlite3_rsync: Database Remote-Copy Tool For SQLite
url: https://simonwillison.net/2026/Nov/26/sqlite3-rsync/
published: 2026-11-26
author: 
---

# sqlite3_rsync: Database Remote-Copy Tool For SQLite

<p><strong><a href="https://www.sqlite.org/rsync.html">sqlite3_rsync: Database Remote-Copy Tool For SQLite</a></strong></p>
This additional SQLite tool has been around for a while now - it was added as "experimental" <a href="https://www.sqlite.org/releaselog/3_47_0.html">in SQLite 3.47.0 in October 2024</a> and enhanced in <a href="https://www.sqlite.org/releaselog/3_50_0.html">SQLite 3.50.0 in May 2025</a>. It was only today that I understood one of its most attractive characteristics.</p>
<p>Normally, if you want to grab a snapshot copy of a SQLite database, you need to use either the <a href="https://www.sqlite.org/backup.html">backup API</a> or <a href="https://www.sqlite.org/lang_vacuum.html#vacuuminto">VACUUM INTO</a>. In both cases you need enough disk space to create a duplicate copy of your database, so if you're on a small instance and you already use more than half of the available disk you are plain out of luck.</p>
<p><code>sqlite3_rsync</code> can copy a snapshot of your database over an SSH connection to another machine, without first needing to create a full local copy!</p>
<p>It's also good for synchronizing an existing copy of a database without re-transmitting the entire thing over the network. It works in a similar way to regular rsync:</p>
<blockquote>
<p>The core idea behind the protocol is that the replica sends cryptographic hashes for pages or groups of pages over to the origin side. The origin sends back page content that differs, or requests finer-grain hashes if a multi-page hash does not match. If the origin and replica start out being vastly different, the total network bandwidth can exceed the size of the entire database, due to the overhead of exchanging hashes, but the excess bandwidth is not great - a few percent at most.</p>
</blockquote>
<p><strong>Update</strong>: Hah! Turns out <a href="https://simonwillison.net/2024/Oct/4/sqlite-rsync/">I wrote about this application of sqlite_rsync</a> back in October 2024 when the tool was first released.


    <p>Tags: <a href="https://simonwillison.net/tags/backups">backups</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a></p>
