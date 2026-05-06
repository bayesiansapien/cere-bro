# Claude Code vs. Hermes Agent: Permission System Architectures

**Date:** 2026-04-23  
**Source:** Ken Huang Substack  
**Links:** [Post](https://kenhuangus.substack.com/p/chapter-4-permission-systems-and)  
**Raw:** parallel daily digest 2026-04-23

---

## TL;DR

Ken Huang's source-code-level comparison of Claude Code and Hermes Agent reveals two different architectural philosophies for agent safety. Claude Code is probabilistic and layered (static rules → classifier → interactive dialog), with organizational deny rules that always win. Hermes is deterministic and pattern-based (30+ regex patterns), with containers as the trust boundary. Neither solves the problem completely — Claude Code is adaptive but error-prone; Hermes is predictable but brittle.

---

## Claude Code Permission Architecture

```
canUseTool pipeline (evaluated in order):
  1. Static allow/deny rules (organizational → user → config)
     deny always wins at equal priority; org rules cannot be overridden
  2. ML classifier (speculative bash classifier)
     races against 2-second timeout; ambiguous cases escalate
  3. Interactive dialog
     user approves/denies; response cascades to parent in multi-agent trees

Five permission modes:
  default    → fully interactive
  auto       → trusted, no interactive prompts
  plan       → review plan before execution
  acceptEdits→ auto-approve file edits only
  bubble     → sub-agents inherit (cannot exceed) parent permissions

Multi-agent: coordinator mode centralizes permission collection
             swarm workers delegate decisions upward
```

**Key properties:**
- Deny always wins over allow at equal priority
- Organizational rules cannot be overridden by users or config
- Classifier can approve ambiguous commands within a time budget (graceful fallback)
- Bubble mode prevents privilege escalation in multi-agent trees

---

## Hermes Agent Permission Architecture

```
Command evaluation pipeline:
  1. Normalization: strip ANSI escapes, null bytes, Unicode fullwidth chars
     (prevents obfuscation bypass of pattern matching)
  2. 30+ DANGEROUS_PATTERNS regex matching:
     - Filesystem: rm -rf, mkfs, dd
     - Database: DROP TABLE, TRUNCATE, DELETE
     - Shell injection: eval, exec, $(cmd)
     - Self-termination: kill -9, shutdown
  3. Approval dialog (if pattern matched):
     - Three scopes: once / session / always
     - Alias system for backwards compatibility
     - Threading lock: serializes concurrent requests (prevents race conditions)
     - Configurable timeout: defaults to DENY

Container bypass: Docker, Singularity, Modal environments skip approval entirely
                  Container boundary treated as sufficient isolation
```

**Key properties:**
- Deterministic: same command always gets same classification
- Auditable: pattern list is static and inspectable
- Container bypass is an explicit trust boundary (not an omission)
- Normalization step is practically important — fullwidth Unicode can fool naive regex

---

## Comparison

| Dimension | Claude Code | Hermes |
|-----------|-------------|--------|
| Classification | ML classifier (adaptive) | Regex patterns (deterministic) |
| Novel attack surfaces | Classifier may catch | Pattern list misses |
| Auditability | Lower (classifier is a black box) | Higher (pattern list is static) |
| Container trust | Bubble mode (permission inheritance) | Full bypass (container = trust) |
| Failure mode | False negatives from classifier errors | False negatives from novel patterns |
| Multi-agent | Coordinator + bubble mode (explicit) | Threading lock (serializes) |

---

## Relation to Prior Wiki Knowledge

**Directly extends Claude Code Architecture (04-19)**: that page documented the overall while-loop + ML permission classifier + compaction architecture. This deep dive goes into the classifier pipeline specifics and the multi-agent permission propagation model that wasn't in the prior analysis.

**Connects to persistent agent infrastructure (04-23)**: Kimi K2.6's 4,000 coordinated steps require permission decisions at scale. Claude Code's coordinator mode and Hermes' threading lock are both early attempts at this, but neither has been tested at that scale.

**Connects to Anthropic Mythos breach (04-23)**: Mythos was accessed through a third-party environment — i.e., a container-equivalent. Hermes' container bypass bet is tested by exactly this incident: container isolation is not impenetrable.

---

## Open Questions

1. How does Claude Code's classifier perform on novel jailbreak patterns that weren't in its training distribution? The 2-second timeout fallback to interactive dialog is graceful, but what's the false negative rate?
2. Hermes' container bypass assumes containers are fully isolated. The Mythos breach shows this assumption can fail through third-party environments. What's the right threat model for a container boundary?
3. When a multi-agent system has 300 sub-agents (Kimi K2.6), Claude Code's coordinator mode centralizes all permission collection. Does this create a permission bottleneck that limits throughput?

---

## Related Pages

- [Claude Code Architecture](2026-04-19-claude-code-architecture.md)
- [Persistent Agent Infrastructure](2026-04-23-persistent-agent-infrastructure.md)
- [Query/Agent Loop: Claude Code vs Hermes](2026-04-20-query-agent-loop-claude-vs-hermes.md)
