---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-20T05:05:03.829631+00:00
title: "PostgreSQL 19 Released"
url: https://simonwillison.net/2026/Nov/19/postgresql-19/
published: 2026-11-19
author: 
---

# PostgreSQL 19 Released

<p><strong><a href="https://www.postgresql.org/about/news/postgresql-19-released-3449/">PostgreSQL 19 Released</a></strong></p>
Most years PostgreSQL ships a new release in September, but this year's release came two months later <a href="https://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html">thanks mainly</a> to the flurry of issues that the PostgreSQL team needed to address as part of the ongoing AI-reported vulnerability apocalypse.</p>
<p>This release was definitely worth the wait. My favorite new feature is this one:</p>
<blockquote>
<p>For applications that send reads to standbys, PostgreSQL 19 adds "read-your-writes" consistency with the new <a href="https://www.postgresql.org/docs/19/sql-wait.html"><code>WAIT FOR LSN</code></a> command. A session on a standby can use <code>WAIT FOR LSN</code> to wait until the standby has replayed the write-ahead log (WAL) up to a specific <a href="https://www.postgresql.org/docs/19/wal-internals.html">log sequence number (LSN)</a> before running a query, so the application can read data it just wrote on the primary.</p>
</blockquote>
<p>In practice, that looks like this:</p>
<pre><code>UPDATE movie SET genre = 'Dramatic' WHERE genre = 'Drama';
SELECT pg_current_wal_insert_lsn();
</code></pre>
<p>That returns a value like <code>0/0306EE20</code>. Store that somewhere (a signed cookie would work) such that on a subsequent request your application can do:</p>
<pre><code>WAIT FOR LSN '0/0306EE20' WITH (TIMEOUT '0.1s');
SELECT * FROM movie WHERE genre = 'Drama';
</code></pre>
<p>The timeout is optional - if you provide one you'll get an error if the replica you are talking to doesn't catch up within the specified time.</p>
<p>I first encountered this pattern <a href="https://www.mediawiki.org/wiki/Manual:Database_access#Lag">in Wikipedia</a>, which has a hand-rolled version of this built against MySQL replication:</p>
<blockquote>
<p>In addition to this, MediaWiki attempts to ensure that the user sees events occurring on the wiki in chronological order. A few seconds of lag can be tolerated, as long as the user sees a consistent picture from subsequent requests. This is done by saving the primary binlog position in the session, and then at the start of each request, waiting for the replica to catch up to that position before doing any reads from it.</p>
</blockquote>
<p>Here's <a href="https://github.com/wikimedia/mediawiki/blob/1ff78194b182ee4b5b3678f7d9fc9aefd0852cf7/includes/libs/Rdbms/Replication/MysqlReplicationReporter.php#L238-L299">the relevant MediaWiki code</a>, which these days uses MySQL's <a href="https://dev.mysql.com/doc/refman/9.7/en/gtid-functions.html#function_wait-for-executed-gtid-set">WAIT_FOR_EXECUTED_GTID_SET()</a> function and falls back to <a href="https://dev.mysql.com/doc/refman/8.4/en/replication-functions-synchronization.html#function_source-pos-wait">SOURCE_POS_WAIT()</a>.

    <p><small></small>Via <a href="https://lobste.rs/s/pqyuhk/postgresql_19_released">Lobste.rs</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/mysql">mysql</a>, <a href="https://simonwillison.net/tags/postgresql">postgresql</a>, <a href="https://simonwillison.net/tags/replication">replication</a>, <a href="https://simonwillison.net/tags/scaling">scaling</a>, <a href="https://simonwillison.net/tags/wikipedia">wikipedia</a>, <a href="https://simonwillison.net/tags/ai-security-research">ai-security-research</a></p>
