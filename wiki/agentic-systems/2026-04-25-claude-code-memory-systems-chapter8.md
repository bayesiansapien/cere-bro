# Claude Code Memory Systems: Chapter 8 Analysis

**Date:** 2026-04-25  
**Sources:** [Ken Huang Substack](https://kenhuangus.substack.com/p/chapter-8-memory-systems-and-state)  
**Raw:** raw/gmail/2026-04-25-starred.md

---

## TL;DR

Chapter 8 of Ken Huang's Claude Code vs. Hermes Agent comparative series dissects how each system handles memory continuity across sessions. Claude Code uses file-backed transcripts with eager flush (write before the API call, not after), an LRU cache for file reads, and path-set deduplication for CLAUDE.md injection. Hermes Agent uses SQLite with FTS5 (full-text search) for episodic recall. The two approaches are complementary: Claude Code optimizes for crash safety and session portability; Hermes optimizes for searchable history across many sessions.

---

## Claude Code Memory Architecture

### The QueryEngine State Container

```typescript
export class QueryEngine {
  private mutableMessages: Message[]           // Full conversation, grows each turn
  private loadedNestedMemoryPaths = new Set<string>()  // Dedup for CLAUDE.md injection
  private discoveredSkillNames = new Set<string>()     // Telemetry
}
```

`mutableMessages` is the source of truth. Every user message, assistant response, tool call, and tool result is appended. The session lives in RAM; the transcript on disk is the durable backup.

### Eager Flush — The Key Design Decision

Most systems write the transcript after the API responds. Claude Code writes it *before* sending the request:

```typescript
// Pre-emptive persistence BEFORE the API call
if (persistSession && messagesFromUserInput.length > 0) {
  const transcriptPromise = recordTranscript(messages)
  if (isBareMode()) {
    void transcriptPromise  // Fire-and-forget in SDK mode
  } else {
    await transcriptPromise  // Block for durability in interactive mode
  }
}
```

Mode-aware: interactive sessions block on the write (crash safety first), SDK sessions fire-and-forget (speed first). This means if the process is killed mid-inference, the user's message is already on disk and the session can resume. The Claude Code postmortem (04-24) revealed that a caching bug corrupted this mechanism, causing the perceived "shrinkflation" — context was being cleared before it should have been.

### LRU Cache with Clone-on-Spawn

File reads are cached across turns. When a nested agent spawns, it gets a clone of the parent's cache. Changes propagate back on completion:

```typescript
const engine = new QueryEngine({
  readFileCache: cloneFileStateCache(getReadFileCache()),  // Child gets own copy
})
try {
  yield* engine.submitMessage(prompt, { uuid: promptUuid })
} finally {
  setReadFileCache(engine.getReadFileState())  // Propagate child's reads back to parent
}
```

This pattern avoids double file reads in nested agents while keeping parent and child state isolated during execution.

### CLAUDE.md Auto-Injection with Deduplication

CLAUDE.md files are prefetched in parallel before the API call, then injected as tool results. The `loadedNestedMemoryPaths` set prevents re-injection across turns even if the LRU cache evicts the file entry:

```typescript
using pendingMemoryPrefetch = startRelevantMemoryPrefetch(state.messages, state.toolUseContext)
// Later:
const memoryAttachments = filterDuplicateMemoryAttachments(
  await pendingMemoryPrefetch.promise,
  toolUseContext.readFileState,
)
```

Two dedup mechanisms: cache-level (LRU hits) and session-level (path set). The session-level set is the safety net for long sessions where cache eviction is likely.

### Context Compaction and Preserved Tail

When context compacts, a "preserved tail" is written to the transcript so `--resume` can reconstruct post-compaction state:

```typescript
if (message.type === 'system' && message.subtype === 'compact_boundary') {
  const tailUuid = message.compactMetadata?.preservedSegment?.tailUuid
  if (tailUuid) {
    const tailIdx = this.mutableMessages.findLastIndex(m => m.uuid === tailUuid)
    await recordTranscript(this.mutableMessages.slice(0, tailIdx + 1))
  }
}
```

This is the mechanism that cere-bro's own session resumption relies on.

---

## Hermes Agent Memory Architecture

Hermes takes a database-first approach: all history in SQLite with WAL mode for concurrent access, plus FTS5 for full-text search:

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
    content,
    content=messages,   -- backed by messages table
    content_rowid=id
);
-- Triggers keep FTS index in sync automatically
CREATE TRIGGER IF NOT EXISTS messages_fts_insert AFTER INSERT ON messages BEGIN
    INSERT INTO messages_fts(rowid, content) VALUES (new.id, new.content);
END;
```

FTS5 content table: the index stays in sync with the source table automatically via triggers. This is O(log n) search across all sessions ever stored, without full-table scans.

**Three memory layers:**
- Working memory: live conversation (equivalent to `mutableMessages`)
- Episodic memory: SQLite FTS5 across all prior sessions — searchable by any keyword
- Procedural memory: markdown playbooks for reusable skills (equivalent to CLAUDE.md)

---

## Comparison

| Concern | Claude Code | Hermes Agent |
|---------|-------------|--------------|
| Session persistence | File-backed transcripts | SQLite WAL |
| History search | None (file-based only) | FTS5 across all sessions |
| Crash safety | Eager flush (pre-API write) | WAL (atomic commits) |
| Memory injection | CLAUDE.md auto-prefetch | Markdown playbook retrieval |
| Nested agents | Clone-on-spawn + propagate-back | Separate process, explicit handoff |

The gap: Claude Code has no cross-session search. Hermes has no eager-flush crash safety. A production agent needs both.

---

## Prior Context

**Directly extends Claude Code Architecture (04-17, 04-19):** Prior pages covered the permission model and tool execution loop. This chapter fills in the memory layer — how state persists across turns, crashes, and compaction boundaries.

**Explains the Claude Code postmortem (04-24):** The caching bug that caused "shrinkflation" corrupted the LRU cache and flush pipeline described here. Understanding the eager flush mechanism makes clear why the bug had outsized impact: it broke the durability guarantee that the entire session resume system relies on.

**Connects to Claude Code vs Hermes Permissions (04-23):** Chapter 7 covered the permission model. Chapter 8 covers memory. Together they paint a complete picture of where Claude Code's agent architecture is robust (permissions, crash safety) and where it's incomplete (no episodic search).

---

## Related Pages

- [Claude Code Architecture](2026-04-19-claude-code-architecture.md)
- [Claude Code vs Hermes Permissions](2026-04-23-claude-code-vs-hermes-permissions.md)
- [GPT-5.5 System Card](../llms-foundation-models/2026-04-24-gpt-55-launch-system-card.md)
