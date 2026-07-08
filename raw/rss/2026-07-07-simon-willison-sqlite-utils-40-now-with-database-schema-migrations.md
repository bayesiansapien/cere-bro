---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: sqlite-utils 4.0, now with database schema migrations
url: https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything
published: 2026-07-07
author: 
---

# sqlite-utils 4.0, now with database schema migrations

<p>This morning I released <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0">sqlite-utils 4.0</a>, the 124th release of that project and the first major version bump since <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v3-0">3.0</a> in November 2020. In addition to some small but significant breaking changes (described in <a href="https://sqlite-utils.datasette.io/en/stable/upgrading.html">this upgrade guide</a>), this version introduces three major features: <strong>database migrations</strong>, <strong>nested transactions</strong> (via a new <code>db.atomic()</code> method), and support for <strong>compound foreign keys</strong>.</p>
<h4 id="database-schema-migrations-using-sqlite-utils">Database schema migrations using sqlite-utils</h4>
<p>Schema migrations define a sequence of changes to be made to a SQLite database, plus a mechanism for tracking which migrations have been applied and applying any that are found to be pending.</p>
<p>Migrations are defined in Python files using the <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html">sqlite-utils Python library</a>, which includes a powerful <code>table.transform()</code> method providing <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#transforming-a-table">enhanced alter table capabilities</a> that are not supported by SQLite's <code>ALTER TABLE</code> statement.</p>
<p>(<code>table.transform()</code> implements the pattern <a href="https://www.sqlite.org/lang_altertable.html#otheralter">recommended by the SQLite documentation</a> - create a new temporary table with the new schema, copy across the data, then drop the old table and rename the temporary one in its place.)</p>
<p>Here's an example migration file which creates a table called <code>creatures</code>, adds an additional column to it in a second step, then changes the types of two of the columns in a third:</p>
<pre><span class="pl-k">from</span> <span class="pl-s1">sqlite_utils</span> <span class="pl-k">import</span> <span class="pl-v">Migrations</span>

<span class="pl-s1">migrations</span> <span class="pl-c1">=</span> <span class="pl-en">Migrations</span>(<span class="pl-s">"creatures"</span>)

<span class="pl-en">@<span class="pl-en">migrations</span>()</span>
<span class="pl-k">def</span> <span class="pl-en">create_table</span>(<span class="pl-s1">db</span>):
    <span class="pl-s1">db</span>[<span class="pl-s">"creatures"</span>].<span class="pl-c1">create</span>(
        {<span class="pl-s">"id"</span>: <span class="pl-s1">int</span>, <span class="pl-s">"name"</span>: <span class="pl-s1">str</span>, <span class="pl-s">"species"</span>: <span class="pl-s1">str</span>},
        <span class="pl-s1">pk</span><span class="pl-c1">=</span><span class="pl-s">"id"</span>,
    )

<span class="pl-en">@<span class="pl-en">migrations</span>()</span>
<span class="pl-k">def</span> <span class="pl-en">add_weight</span>(<span class="pl-s1">db</span>):
    <span class="pl-s1">db</span>[<span class="pl-s">"creatures"</span>].<span class="pl-c1">add_column</span>(<span class="pl-s">"weight"</span>, <span class="pl-s1">float</span>)

<span class="pl-en">@<span class="pl-en">migrations</span>()</span>
<span class="pl-k">def</span> <span class="pl-en">change_column_types</span>(<span class="pl-s1">db</span>):
    <span class="pl-s1">db</span>[<span class="pl-s">"creatures"</span>].<span class="pl-c1">transform</span>(<span class="pl-s1">types</span><span class="pl-c1">=</span>{<span class="pl-s">"species"</span>: <span class="pl-s1">int</span>, <span class="pl-s">"weight"</span>: <span class="pl-s1">str</span>})</pre>
<p>Save that as <code>migrations.py</code> and run it against a fresh database like this:</p>
<div class="highlight highlight-source-shell"><pre>uvx sqlite-utils migrate data.db migrations.py</pre></div>
<p>Then if you check the schema of that database:</p>
<div class="highlight highlight-source-shell"><pre>uvx sqlite-utils schema data.db</pre></div>
<p>You'll see this SQL:</p>
<div class="highlight highlight-source-sql"><pre><span class="pl-k">CREATE</span> <span class="pl-k">TABLE</span> "<span class="pl-en">_sqlite_migrations</span>" (
   <span class="pl-s"><span class="pl-pds">"</span>id<span class="pl-pds">"</span></span> <span class="pl-k">INTEGER</span> <span class="pl-k">PRIMARY KEY</span>,
   <span class="pl-s"><span class="pl-pds">"</span>migration_set<span class="pl-pds">"</span></span> <span class="pl-k">TEXT</span>,
   <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span> <span class="pl-k">TEXT</span>,
   <span class="pl-s"><span class="pl-pds">"</span>applied_at<span class="pl-pds">"</span></span> <span class="pl-k">TEXT</span>
);
<span class="pl-k">CREATE</span> <span class="pl-k">UNIQUE INDEX</span> "<span class="pl-en">idx__sqlite_migrations_migration_set_name</span>"
    <span class="pl-k">ON</span> <span class="pl-s"><span class="pl-pds">"</span>_sqlite_migrations<span class="pl-pds">"</span></span> (<span class="pl-s"><span class="pl-pds">"</span>migration_set<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span>);
<span class="pl-k">CREATE</span> <span class="pl-k">TABLE</span> "<span class="pl-en">creatures</span>" (
   <span class="pl-s"><span class="pl-pds">"</span>id<span class="pl-pds">"</span></span> <span class="pl-k">INTEGER</span> <span class="pl-k">PRIMARY KEY</span>,
   <span class="pl-s"><span class="pl-pds">"</span>name<span class="pl-pds">"</span></span> <span class="pl-k">TEXT</span>,
   <span class="pl-s"><span class="pl-pds">"</span>species<span class="pl-pds">"</span></span> <span class="pl-k">INTEGER</span>,
   <span class="pl-s"><span class="pl-pds">"</span>weight<span class="pl-pds">"</span></span> <span class="pl-k">TEXT</span>
);</pre></div>
<p>The <code>_sqlite_migrations</code> table is used to keep track of which migration functions have been run. The <code>creatures</code> table above is the schema after all three migrations have been applied.</p>
<p>To see a list of migrations, both pending and applied, run this:</p>
<div class="highlight highlight-source-shell"><pre>uvx sqlite-utils migrate data.db migrations.py --list</pre></div>
<p>Output:</p>
<pre><code>Migrations for: creatures

  Applied:
    create_table - 2026-07-07 17:58:41.360051+00:00
    add_weight - 2026-07-07 17:58:41.360608+00:00
    change_column_types - 2026-07-07 18:01:15.802000+00:00

  Pending:
    (none)
</code></pre>
<p>If you don't specify a migrations file, the <code>sqlite-utils migrate data.db</code> command will scan the current directory and its subdirectories for files called <code>migrations.py</code> and apply any <code>Migrations()</code> instances it finds in them.</p>
<p>You can also execute migrations <a href="https://sqlite-utils.datasette.io/en/stable/migrations.html#applying-migrations-in-python">from Python code</a> using the <code>migrations.apply(db)</code> method, which is useful for building tools that manage their own database schemas over multiple versions. My own <a href="https://llm.datasette.io/">LLM tool</a> has been using a version of this pattern for several years now, as shown in <a href="https://github.com/simonw/llm/blob/0.31/llm/embeddings_migrations.py">llm/embeddings_migrations.py</a>.</p>
<h4 id="prior-art">Prior art</h4>
<p>My favorite implementation of this pattern remains <a href="https://docs.djangoproject.com/en/6.0/topics/migrations/">Django's Migrations</a>, developed by Andrew Godwin based on his earlier project <a href="https://github.com/andrewgodwin/south">South</a>. Fun fact: Andrew, Russ Keith-Magee, and I presented our competing approaches to schema migrations for Django on the <a href="https://www.youtube.com/watch?v=VSq8m00p1FM">Schema Evolution panel</a> at the very first DjangoCon back in 2008! My attempt was called <a href="https://simonwillison.net/2008/Sep/3/dmigrations/">dmigrations</a>, developed with a team at Global Radio in London.</p>
<p>Django's migrations can be automatically generated from model definitions and include the ability to roll back to a previous version. The <code>sqlite-utils</code> approach is deliberately simpler: unlike Django, <code>sqlite-utils</code> encourages programmatic table creation rather than a model definition ORM, so there isn't anything we can use to automatically generate migrations.</p>
<p>I decided to skip rollback, since in my experience it's a feature that is rarely used. With a SQLite project, an easy way to achieve rollback is to create a copy of your database file before you apply the migrations!</p>
<h4 id="migrating-from-sqlite-migrate">Migrating from sqlite-migrate</h4>
<p>The design of <code>sqlite-utils</code> migrations is three years old now - I had originally released it as a separate package called <a href="https://github.com/simonw/sqlite-migrate">sqlite-migrate</a>, which never quite graduated beyond a beta release.</p>
<p>I've used that package in enough places now that I'm confident in the design, so I've decided to promote it to a feature of <code>sqlite-utils</code> to make it available by default to all of the other tools in the growing sqlite-utils/Datasette/LLM ecosystem.</p>
<p>I made <a href="https://github.com/simonw/sqlite-migrate/releases/tag/0.2">one last release</a> of <code>sqlite-migrate</code>, which switches it to depend on <code>sqlite-utils&gt;=4</code> and replaces the <code>__init__.py</code> file with the following:</p>
<pre><span class="pl-k">from</span> <span class="pl-s1">sqlite_utils</span> <span class="pl-k">import</span> <span class="pl-v">Migrations</span>

<span class="pl-s1">__all__</span> <span class="pl-c1">=</span> [<span class="pl-s">"Migrations"</span>]</pre>
<p>Any existing project that depends on <code>sqlite-migrate</code> should continue to work without alterations.</p>
<h4 id="everything-else-in-sqlite-utils-4-0">Everything else in sqlite-utils 4.0</h4>
<p>Here are the release notes for this version, with some inline annotations:</p>
<blockquote>
<p>The 4.0 release includes some minor backwards-incompatible fixes (hence the major version number bump) and introduces three major new features:</p>
<ul>
<li>
<a href="https://sqlite-utils.datasette.io/en/stable/migrations.html#migrations">Database migrations</a>, providing a structured mechanism for evolving a project’s schema over time. (<a href="https://github.com/simonw/sqlite-utils/issues/752">#752</a>)</li>
</ul>
</blockquote>
<p>I think of migrations as the signature new feature, hence this blog post.</p>
<blockquote>
<ul>
<li>
<a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-atomic">Nested transaction support</a> via <code>db.atomic()</code>, plus numerous improvements to how transactions work across the library. (<a href="https://github.com/simonw/sqlite-utils/issues/755">#755</a>)</li>
</ul>
</blockquote>
<p><code>sqlite-utils</code> has long had a confused relationship with database transactions, partly because when I started designing the library back in 2018 I didn't yet have a great feel for how those worked in SQLite itself.</p>
<p>Adding migrations to the core library made me determined to finally crack this nut, since transactions make migration systems a whole lot safer and easier to reason about.</p>
<p>I ended up building this around a <code>db.atomic()</code> context manager which looks like this:</p>
<pre><span class="pl-k">with</span> <span class="pl-s1">db</span>.<span class="pl-c1">atomic</span>():
    <span class="pl-s1">db</span>.<span class="pl-c1">table</span>(<span class="pl-s">"dogs"</span>).<span class="pl-c1">insert</span>({<span class="pl-s">"id"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"name"</span>: <span class="pl-s">"Cleo"</span>}, <span class="pl-s1">pk</span><span class="pl-c1">=</span><span class="pl-s">"id"</span>)
    <span class="pl-s1">db</span>.<span class="pl-c1">table</span>(<span class="pl-s">"dogs"</span>).<span class="pl-c1">insert</span>({<span class="pl-s">"id"</span>: <span class="pl-c1">2</span>, <span class="pl-s">"name"</span>: <span class="pl-s">"Pancakes"</span>})</pre>
<p>SQLite supports <a href="https://sqlite.org/lang_savepoint.html">Savepoints</a>, and as a result <code>db.atomic()</code> can be nested to carry out transactions inside of transactions. It's pretty neat!</p>
<blockquote>
<ul>
<li>Support for <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-compound-foreign-keys">compound foreign keys</a>, including creation, transformation and introspection through <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-introspection-foreign-keys">table.foreign_keys</a>. (<a href="https://github.com/simonw/sqlite-utils/issues/594">#594</a>)</li>
</ul>
</blockquote>
<p>This came about when I asked a coding agent to review all open issues and PRs for things that should be included in a 4.0 release since they would represent breaking changes if I added them later, and it correctly identified that compound foreign keys were exactly that kind of feature.</p>
<p>I started with a breaking change to the <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-introspection-foreign-keys">table.foreign_keys</a> introspection method, and then decided to see if Claude Fable 5 could handle the more fiddly job of integrating compound foreign key <em>creation</em> into the library. The API design it helped create felt <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#compound-foreign-keys">exactly right to me</a> - consistent with how the rest of the library worked already.</p>
<blockquote>
<p>Other notable changes include:</p>
<ul>
<li>Upserts now use SQLite’s <code>INSERT ... ON CONFLICT ... DO UPDATE SET</code> syntax, detect existing table primary keys automatically and reject records that are missing required primary key values. (<a href="https://github.com/simonw/sqlite-utils/issues/652">#652</a>)</li>
</ul>
</blockquote>
<p>This was the change that first pushed me to consider a breaking-change 4.0 version bump. I built this to help support <a href="https://github.com/simonw/sqlite-chronicle">sqlite-chronicle</a>, which uses triggers to keep track of rows in a table that have been inserted, updated or deleted.</p>
<blockquote>
<ul>
<li>
<code>db.query()</code> now executes immediately and rejects statements that do not return rows; use <code>db.execute()</code> for writes and DDL.</li>
</ul>
</blockquote>
<p>Probably the <a href="https://sqlite-utils.datasette.io/en/stable/upgrading.html#python-api-changes">most disruptive breaking change</a> - I've had to update a few places in my own code to switch from <code>db.query()</code> to <code>db.execute()</code> as a result.</p>
<blockquote>
<ul>
<li>CSV and TSV imports now detect column types by default, while inserts into existing tables preserve those tables’ column types. (<a href="https://github.com/simonw/sqlite-utils/issues/679">#679</a>)</li>
</ul>
</blockquote>
<p>The <code>sqlite-utils insert data.db creatures creatures.csv --detect-types</code> flag was a later addition to allow column types (text, integer, real) to be automatically detected based on the data in a CSV. It should be the default, and releasing a 4.0 means I can make it so.</p>
<blockquote>
<ul>
<li>
<code>table.extract()</code> and <code>extracts=</code> no longer create lookup table records for all-<code>null</code> values. (<a href="https://github.com/simonw/sqlite-utils/issues/186">#186</a>)</li>
</ul>
</blockquote>
<p>The oldest issue addressed by this release - the underlying bug was opened (by me) in October 2020.</p>
<blockquote>
<p>See <a href="https://sqlite-utils.datasette.io/en/stable/upgrading.html#upgrading-3-to-4">Upgrading from 3.x to 4.0</a> for details on backwards-incompatible changes.</p>
<p>The detailed release notes for the features and fixes shipped during the 4.0 pre-release cycle are available in <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0a0">4.0a0</a>, <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0a1">4.0a1</a>, <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0rc1">4.0rc1</a>, <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0rc2">4.0rc2</a>, <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0rc3">4.0rc3</a> and <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-0rc4">4.0rc4</a>.</p>
</blockquote>
<p>The upgrade guide was entirely written by Claude Fable 5, Claude Opus 4.8 and GPT-5.5. The same is true of the release notes.</p>
<p>This is the kind of documentation I've slowly become comfortable outsourcing to the robots. It doesn't need to convince people of anything, or express any opinions - its job is to be as accurate and detailed as possible. I've reviewed the release notes closely and can confirm they are accurate and comprehensive.</p>
<h4 id="claude-fable-5-helped-a-lot">Claude Fable 5 helped a lot</h4>
<p>I released the first alpha of sqlite-utils 4.0 <a href="https://sqlite-utils.datasette.io/en/stable/changelog.html#a0-2025-05-08">over a year ago</a>. I've been dragging my heels on the stable release because of the amount of work it would take to track down and clean up the many other minor design flaws that a major version number allowed me to take on.</p>
<p>Assistance from Claude Fable 5 (and to a lesser extent Opus 4.8 and GPT-5.5) gave me just the boost I needed to overcome inertia and make the most of the time I could afford to spend on this library.</p>
<p>Fable has <em>really good taste</em> in API design, and is <a href="https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/">relentlessly proactive</a> if you give it a more open goal. My most successful prompt was a review task that I issued against what I thought was the last release candidate:</p>
<blockquote>
<p><code>review the changes on main since the last tagged 3.x release - I am about to ship them as sqlite-utils 4.0, a stable version that promises no backwards-incompatible fixes for a very long time.</code></p>
<p><code>review the changelog and upgrade guide, and write yourself scratch scripts to try out all of the new features in v4 - save those scripts but don't commit them</code></p>
</blockquote>
<p>I tried this with GPT-5.5 xhigh in Codex Desktop and Fable 5 in Claude Code.</p>
<p>GPT-5.5 <a href="https://gist.github.com/simonw/823fdecc031371d56dce39537adc0096">wrote 5 Python scripts</a> and didn't turn up anything particularly interesting - its <a href="https://github.com/simonw/sqlite-utils/issues/769#issuecomment-4899982463">final report is here</a>.</p>
<p>Fable 5 <a href="https://gist.github.com/simonw/95800bf584f8e437f1cf0d48d9ef81e6">wrote 12 scripts</a>, identified 4 release blockers and 10 additional issues <a href="https://github.com/simonw/sqlite-utils/issues/769#issuecomment-4900034150">in its report</a>, and built a neat <a href="https://gist.githubusercontent.com/simonw/95800bf584f8e437f1cf0d48d9ef81e6/raw/c43918b36a129bba1d2f2a129117aa11c85146c0/12_bug_repros.py">combined repro script</a>, which, when run, output the following:</p>
<pre><code>=== 1. Failed db.execute() write leaves an implicit transaction open ===
  in_transaction after failed write: True
  BUG: table 'other' silently lost when connection closed

=== 2. Leading ';' bypasses the query() first-token scanner ===
  BUG: raised OperationalError: no such savepoint: sqlite_utils_query
  BUG: row persisted despite rollback (count=1)

=== 3. Rejected write PRAGMA via query() still takes effect ===
  BUG: user_version=5 after 'rejected' statement (docs say no effect)

=== 4. Implicit compound FK resolves pk columns in table order, not PK order ===
  BUG: other_columns reported as ('b', 'a'), should be ('a', 'b')
  BUG: transform of valid data raised IntegrityError: FOREIGN KEY constraint failed

=== 5. ForeignKey (now a dataclass) is no longer hashable ===
  BUG: cannot use 'sqlite_utils.db.ForeignKey' as a set element (unhashable type: 'ForeignKey')

=== 6. Mixed ForeignKey objects and tuples in foreign_keys= rejected ===
  BUG: foreign_keys= should be a list of tuples

=== 7. insert --csv into an EXISTING table transforms its column types ===
  BUG: existing zip '01234' is now 1234 (column type: int)

=== 8. insert(pk=, alter=True) regression: InvalidColumns before alter runs ===
  BUG: InvalidColumns: Invalid primary key column ['id'] for table t with columns ['a']

=== 9. migrate --stop-before an already-applied migration applies everything ===
  BUG: m2 was applied despite --stop-before m1 (m1 already applied)

=== 10. ensure_autocommit_on() silently commits an open transaction ===
  BUG: row survived rollback (count=1) - transaction was committed
</code></pre>
<p>I found myself agreeing with almost all of them. Here's <a href="https://github.com/simonw/sqlite-utils/pull/779">the PR with 16 commits</a> where we worked through them in turn.</p>
<p>There's no doubt in my mind that sqlite-utils 4.0 is a significantly higher-quality release than if I had built it without the assistance of the latest frontier models.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/schema-migrations">schema-migrations</a>, <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/sqlite-utils">sqlite-utils</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/agentic-engineering">agentic-engineering</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
