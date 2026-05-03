# lint

Health check for the wiki. Finds structural issues, stale content, gaps, and missing index entries.

---

## Instructions

When invoked, run all checks below and report findings grouped by severity. Fix what you can fix automatically; flag what needs user attention.

---

### Check 1: Orphan summary pages

Find summary pages (files with a date prefix like `2026-05-01-*.md`) in `wiki/` that:
- Have no links pointing to any concept page
- Are not referenced in `wiki/index.md`

These pages are dead ends — they add no value to the knowledge graph.

**Auto-fix:** Add missing index.md entries for any pages that exist but aren't listed.
**Flag:** Pages with no concept page links — user should add connections.

---

### Check 2: Stale concept pages

Find concept pages that haven't been updated while ≥3 new summary pages on the same topic have been ingested since the concept page was last modified.

Compare file modification times or check the log.md for ingest entries vs. concept page update entries.

**Flag:** "These concept pages may be out of date: [list]. They cover X topic but haven't been updated since [date], while Y summaries on this topic have been ingested."

---

### Check 3: Topics without concept pages

Find topics that appear in ≥3 summary pages but have no concept page (no non-date-prefixed .md file in the topic directory).

**Flag:** "These topics have enough summaries to warrant a concept page: [list]. Create one with /ingest or manually."

---

### Check 4: index.md completeness

Walk `wiki/` and compare every .md file (except index.md, log.md, and daily-digest/**) against entries in `wiki/index.md`.

**Auto-fix:** Add missing entries to index.md in the correct topic section.
**Report:** How many were missing and were added.

---

### Check 5: log.md consistency

Check that every directory in `wiki/` that has summary files also has corresponding log.md entries.

Also check for log entries that reference pages that don't exist (deleted or renamed pages).

**Flag:** Broken log references — "These log entries reference pages that no longer exist: [list]."

---

### Check 6: wiki-config.json vs. wiki/ structure

Compare topic keys in `wiki-config.json` with directories that actually exist in `wiki/`.

**Flag:**
- Topics in wiki-config.json with no wiki/ directory → "These configured topics have no wiki directory yet: [list]."
- wiki/ directories with no entry in wiki-config.json → "These wiki directories are not in wiki-config.json: [list]. Are these intentional topic folders?"

---

### Check 7: Source links

Spot-check 10 random summary pages and verify that:
- The `**Raw:**` link points to a file that exists in `raw/`
- External URLs in `**Links:**` lines are present (not empty)

**Flag:** Pages with missing raw links or empty URL placeholders.

---

### Check 8: Daily digest continuity

Look at the date range of daily digests in `wiki/daily-digest/`. Flag gaps longer than 7 days where raw sources exist but no digest was written.

**Flag:** "No digest written for [date range] but raw sources exist for those dates."

---

### Report format

```
# Wiki health check — <YYYY-MM-DD>

## Fixed automatically
- Added N missing entries to index.md
- ...

## Issues to address

### High priority
- [Issue description] — [specific files or pages]

### Medium priority
- [Issue description] — [specific files or pages]

### Low priority / suggestions
- [Suggestion]

## Stats
- Total summary pages: N
- Total concept pages: N
- Daily digests: N (spanning YYYY-MM-DD to YYYY-MM-DD)
- Topics with concept pages: N / M configured
- Orphan pages: N
```

---

### When nothing is wrong

If no issues are found:
```
Wiki is healthy.

Stats:
- N summary pages across M topics
- N concept pages
- N daily digests
- index.md: complete
- log.md: no broken references
```
