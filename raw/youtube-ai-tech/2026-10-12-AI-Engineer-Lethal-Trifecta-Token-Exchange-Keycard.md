# Your Agent Is a Lethal Trifecta (And What to Do About It) (Kim Maida, Keycard)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=ws9XcGGPBDk

## TL;DR
Maida accepts Simon Willison's lethal trifecta (private data + untrusted content + external communication) as the default shape of any useful agent, and argues that removing a leg kills usefulness. Her fix is to keep all three but replace standing credentials with per-tool-call, ephemeral, delegated tokens minted by a Security Token Service (STS) using OAuth 2.0 Token Exchange (RFC 8693), gated by policy that sees user identity, agent identity, and requested scope. Keycard layers "intent-based authorization" (IBA) on top: the agent declares a mission (goal, allowed actions, limits), the user approves risky missions, and every tool call is checked against the mission ID. The architecture is sound and standards-based. The framing oversells it: scoped tokens shrink blast radius but do not stop prompt injection from abusing whatever the current mission legitimately allows.

## Key Takeaways
- **Demo of the failure mode:** an on-call triage agent with static API keys and an admin DB connection string pasted customer PII into a report, dropped and "restored" a production billing DB, restarted the prod server, and scaled 4 to 40 pods ($420/hr). The audit log could not say who used which key.
- **Three root problems:** credentials not attributed to user or agent identity, unrestricted scope per credential, and human-in-the-loop used as a substitute for access control (consent fatigue just moves the problem to the user).
- **Existing controls each leave standing access:** OAuth grants are consented before any task exists (broad = overprivileged, narrow = useless). MCP gateways enforce per route but hold standing credentials. Sandboxes bound the process but any useful outbound call reintroduces standing access. Stacking all three still never yields a task-scoped runtime credential.
- **Token exchange flow:** user logs in, consents to a scope subset (first narrowing). That token becomes the subject token. The runtime authenticates to the STS with its own workload identity plus the subject token and requests a token for one MCP tool call. The MCP server then exchanges that token again for a downstream resource token. The delegation chain (user, agent, MCP server) is preserved end to end. Tokens expire in minutes and are never stored.
- **Policy is a ceiling, not intent.** An agent can do things policy allows but you did not mean. IBA adds a mission ("triage incident 2294: read it, summarize or escalate, no other tickets, no other services"). Low-risk missions auto-approve. Escalated missions ("scale the service once") go to the user.
- **Second demo results:** PII query denied by policy, cert renewal allowed, DB drop denied (human-only action), server restart denied even after user approval because the user's own role lacked the permission, scale-up approved and allowed. Human approval backed by policy, not replacing it.
- **IBA is not a standard.** Keycard says proposals are still open. The demo itself used task-based policy, not IBA.

## Architecture & Optimization Mechanics
- **Three identities per call:** subject (user), actor (agent/runtime via client credentials or workload identity), audience (specific MCP server or downstream resource). RFC 8693's `actor_token` and `resource`/`audience` parameters carry exactly this.
- **Double exchange:** runtime to MCP server token, then MCP server to resource token. Each hop is a fresh policy decision, so a compromised MCP server cannot reuse an upstream token at an unintended destination.
- **Gateway as policy enforcement point:** tool calls carry a mission ID. The gateway asks the STS whether the call fits the mission before requesting the exchange.
- **Cost of the design:** an STS round trip per tool call (twice for downstream resources). For latency-sensitive agent loops this is real overhead. Token caching would break the ephemerality guarantee, so expect to pay it, or batch per-mission rather than per-call.
- **What it does not solve:** an injected instruction inside an approved mission can still exfiltrate data through any allowed outbound channel. Scoping reduces the blast radius. It does not break the trifecta. The "keep all three legs" claim holds only if the mission boundary is tighter than the data the attacker wants.

## Grounded Context (Web Enrichment)
Willison coined the lethal trifecta in June 2025. By 2026 it is mainstream vocabulary: Apple's WWDC 2026 security session cited it, OWASP's June 2026 agentic report maps prompt injection to six of ten categories in its Top 10 for Agentic Applications, and Meta's "Agents Rule of Two" (never let an agent hold more than two legs unsupervised) is the competing prescription. Willison's own position is closer to Meta's than to Maida's: he argues the only reliable defense is to remove a leg, because no filtering or scoping reliably stops injection. Maida's talk implicitly disagrees without engaging that argument.

The token exchange claims check out. RFC 8693 was published in January 2020, and multiple vendors (Keycard, Oleria, Gravitee) now build agent gateways on it with audience-bound, short-lived tokens. Keycard's own docs and Maida's DEV.to post describe the same flow. The incident anecdote ("an overprivileged agent dropping a production database is a nightmare several companies have lived") refers to cases like the July 2025 Replit agent deleting a production database during a code freeze. No public spec or IETF draft for Keycard's IBA surfaced, so treat it as a proprietary layer on top of an open primitive. Related prior page: [WorkOS auth.md](2026-10-12-WorkOS-Auth-md-Agent-Registration.md) uses ID-JAG, which also profiles RFC 8693, so registration (auth.md) and per-call authorization (STS) are converging on the same standard.

## Real-World Application / Actionable Step
- **Audit your own agent harnesses** (eval runners, research agents with HF/W&B/cluster access): list every static key they hold. Any key with write or spend permission (cluster job submission, cloud scaling, model registry push) should move behind short-lived, per-task tokens or a human-only policy.
- **Spend caps as policy, not prompts.** The 4 to 40 pod scale-up is the exact failure for autonomous benchmarking agents launching GPU jobs. Enforce a hard per-mission GPU-hour ceiling at the credential layer.
- **For routing work:** mission metadata (goal, allowed actions, risk tier) is a free routing signal. Low-risk read-only missions can go to a cheap model. Missions that request write or spend scopes should route to a stronger model plus mandatory policy check, since a weaker model is more injectable.
- **Do not rely on scoping alone for agents that read untrusted web content and hold private data.** Follow Willison: drop the external-communication leg for those runs.
