# Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait (Al Chen, Cisco)

**Channel:** AI Engineer
**Published:** 2026-10-20
**Source:** https://www.youtube.com/watch?v=Bz1HFxQA1o8
**Domains:** ai-tech (primary)

## TL;DR
An AI-observability vendor's field lead explains how to cut time-to-production in air-gapped banks from a year to weeks. The lever is "show your work": prove a CVE is actually gone by having an agent write the exploit and test it against the bumped package, prove a ClickHouse cross-region restore is correct by checking row counts and replica convergence rather than job status, and prove your LLM-as-judge is not un-redacting PII in its reasoning trace. Every one of these costs extra compute; the theme is that zero leakage and data sovereignty are not free.

## Key Takeaways
- **Standard SaaS deployment fails at banks** because of outbound egress. Everything runs on-prem in the bank's VPC; the three pillars are build pipeline (image pulls into their cluster), data resiliency (what happens if a region dies mid-request), and leakage control (nothing sensitive reaches internal employees or leaves the VPC).
- **CVE remediation is combinatorial:** multiple images × multiple CVEs × multiple banks on different image versions × different scanners (Sysdig, Wiz, Prisma) × bank-specific severity policies and SLAs. Transient open-source dependencies carry CVEs the vendor cannot fix; the team reads upstream release notes to explain why.
- **Version conflicts:** one bank wants package 3.8, another says 3.8 has too many CVEs and wants older. The software still has to work.
- **Scanners check version strings, not exploitability.** Bumping to 2.6.2 says nothing about whether the exploit path still exists in your application code.
- **Harbor tasks as proof:** give an agent the CVE, the Docker image, and the instruction "write an exploit against the old version, then test whether the new version is still vulnerable." Run many trials in parallel (Docker, Modal, Daytona sandboxes) and report pass rates. Evidence, not a version number.
- **ClickHouse has no managed cross-region failover.** Redis and Postgres do; ClickHouse's own resiliency docs say it does not. Pattern: primary-region ClickHouse, backup job to a bucket, restore job into a DR region, replicas within that region. Relies on clickhouse-backup, an open-source tool maintained by Altinity, which competes with ClickHouse Inc.
- **Backup status is not data correctness.** Bad disk, bad node, bad migration, replication lag all produce stale data under a green job status. Check row counts across tables and replica convergence within a region.
- **Replication is a data-residency decision whether you meant it or not.** A bucket does not care if it is in Oregon or Virginia; jurisdiction law does. Pattern: replicate trace IDs and metadata cross-region, keep core trace payloads in one region.
- **The judge is a side door for PII.** UI redaction at SDK, gateway, or middleware level looks clean, but an LLM judge that reads raw traces and emits reasoning "so a human can verify" will quote the PII back in its explanation. Chen's challenge: read your judge system prompts and inspect judge traces for PII/MNPI.
- **Fix:** persist the score always; persist the reasoning only after a check confirms it contains no sensitive data; suppress otherwise. Upgrade: a second judge whose input is pre-redacted, so its reasoning is clean by construction. Cost: one more LLM call per request.
- **What actually delays production is organizational:** no image-approval process for the registry, no GPU procurement story, formal security reviews, custom LLM gateway or RBAC builds. "Vendors say a few weeks but didn't check against your cluster."

## Architecture & Optimization Mechanics
- **Judge cost doubling is a routing decision.** The clean-reasoning pattern means two judge calls per evaluated request. The second judge sees redacted input, which is a simpler task; it is the natural place for a smaller, cheaper model. Pair a frontier judge on raw traces for score with a small judge on redacted input for displayable reasoning, and the PII-safe path stops costing frontier tokens.
- **Agent-written exploits are a verifier with ground truth.** Unlike LLM-as-judge, "does the exploit succeed against the patched image" is a binary signal from the environment. Running N trials in parallel sandboxes and reporting a pass rate is the same methodology as Kormos's statistical eval runs (see the Coinbase unsupervised-agents page), with a harder check.
- **Row-count and convergence checks are cheap invariants.** They are the database equivalent of a numerical sanity check after a quantization pass: a green job status (or a finished calibration run) tells you nothing about whether the output is right.
- **On-prem inference means GPU procurement is on the critical path.** Chen lists "GPUs sourced and ready for inference" as a signal of a fast deployment. For banks, this is where model compression pays directly: a quantized judge that fits on existing hardware removes a months-long procurement step.

## Grounded Context (Web Enrichment)
The ClickHouse claim holds. Altinity's March 2025 DR webinar lays out four approaches (backups, single-region multi-AZ replication, cross-region replication, independent clusters) and rates backups cheapest but slow to restore with higher data loss, and cross-region replication broadest but complex to network and requiring a documented failover procedure. There is no managed cross-region failover service; the options are the SQL BACKUP/RESTORE commands, the Backup Database Engine added in ClickHouse 25.2, SYSTEM RESTORE REPLICA, or clickhouse-backup. A March 2026 OneUptime guide describes exactly Chen's pattern (primary-region S3 bucket copied to a DR-region bucket feeding a DR cluster) and recommends a tested failover runbook. Chen's framing that Altinity competes with ClickHouse Inc. is accurate; Altinity sells managed ClickHouse.

The judge-leakage point is not widely written up, which is the strongest reason to take it seriously. Most LLM-as-judge guidance (including Pamela Fox's workshop the day before, which recommends giving the judge the full trace) implicitly assumes the reasoning output is safe to persist. In a regulated deployment it is not. The scanner-vs-exploitability gap is well known in security circles and is why reachability analysis tools exist; using an agent to write a proof-of-concept per CVE is a newer practice that Anthropic's OSS Scanner (launched 8 October 2026) also follows: each finding ships with a reproducer and a candidate patch.

## Real-World Application / Actionable Step
- **Read your judge prompts today.** If any judge receives raw inputs and you persist its reasoning, you have Chen's side door. Add a sensitive-content check before persisting reasoning, or move to the redacted-input second judge.
- **Route the second judge to a small model.** Redacted-input reasoning is a good candidate for a quantized 7B to 14B model on-prem. Measure agreement with the frontier judge's score; if it holds, you have halved the marginal cost of the PII-safe pattern.
- **Add invariants to your pipelines.** For any job that reports success (backup, calibration, export), add one cheap correctness check (row count, checksum, perplexity delta) that must also pass. Green status without an invariant is Chen's "checking a box."
- **For any bank-adjacent deployment conversation,** lead with the organizational checklist (registry approval process, GPU procurement, security review path, gateway/RBAC ownership). Those, not the model, set the timeline.
