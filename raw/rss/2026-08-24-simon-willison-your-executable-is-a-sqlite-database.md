---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T08:53:56.243728+00:00
title: Your executable is a SQLite database
url: https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/
published: 2026-08-24
author: 
---

# Your executable is a SQLite database

<p><strong><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">Your executable is a SQLite database</a></strong></p>
Farid Zakaria describes a neat Linux pattern for creating a SQLite database file that can be directly used as an executable binary.</p>
<p>The trick sets the SQLite file format's 4-byte application ID (68 bytes into the file) to SELF, standing for Structured Executable &amp; Linkable Format.  The various components of the ELF executable format are then arranged into a number of different SQLite tables, using <a href="https://github.com/fzakaria/selfdb/blob/main/schema/self.sql">this schema</a>.</p>
<p>Their <code>self-exec</code> interpreter (<a href="https://github.com/fzakaria/selfdb/blob/main/loader/self-exec.c">C code here</a>) can then extract and execute the necessary pieces.</p>
<p>You can additionally use a Linux mechanism called <a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">binfmt_misc</a> to teach the kernel to execute that any time it encounters an executable matching that binary pattern. Farid uses NixOS here, but without NixOS I think registration looks something like this:</p>
<pre><code>printf '%s\n' ':self:M:68:SELF::/usr/local/bin/self-exec:' \
  &gt; /proc/sys/fs/binfmt_misc/register
</code></pre>

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=49415271">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/c">c</a>, <a href="https://simonwillison.net/tags/linux">linux</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a></p>
