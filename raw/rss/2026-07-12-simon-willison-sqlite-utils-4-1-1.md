---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.122950+00:00
title: sqlite-utils 4.1.1
url: https://simonwillison.net/2026/Jul/12/sqlite-utils/#atom-everything
published: 2026-07-12
---

# sqlite-utils 4.1.1

<p><strong>Release:</strong> <a href="https://github.com/simonw/sqlite-utils/releases/tag/4.1.1">sqlite-utils 4.1.1</a></p>
        <p>Mainly a fix for an edge case that regular Claude chat spotted while <a href="https://claude.ai/share/564b187d-d126-47ea-9b59-07c16ade0b70">experimenting with the 4.1 release</a> to answer a question about ON DELETE.</p>
<blockquote>
<ul>
<li><code>table.transform()</code> now raises a <code>TransactionError</code> if called while a transaction is open with <code>PRAGMA foreign_keys</code> enabled and the table is referenced by foreign keys with destructive <code>ON DELETE</code> actions - <code>CASCADE</code>, <code>SET NULL</code> or <code>SET DEFAULT</code>. The pragma cannot be changed inside a transaction, so previously dropping the old table as part of the transform could fire those actions and silently delete or modify referencing rows. See <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-transform-foreign-keys-transactions">Foreign keys and transactions</a> for details and workarounds. (<a href="https://github.com/simonw/sqlite-utils/issues/794">#794</a>)</li>
<li>The <a href="https://sqlite-utils.datasette.io/en/stable/cli.html">CLI</a> and <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html">Python API</a> documentation now cross-reference each other: CLI sections link to the equivalent Python API functionality and Python API sections link back to the corresponding CLI command. (<a href="https://github.com/simonw/sqlite-utils/issues/791">#791</a>)</li>
</ul>
</blockquote>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/sqlite-utils">sqlite-utils</a></p>
