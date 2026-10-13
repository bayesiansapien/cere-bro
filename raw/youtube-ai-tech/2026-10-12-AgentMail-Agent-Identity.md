# The Next Trillion Internet Users Still Don't Have an Identity (Adi Singh, AgentMail)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=mBNVKkyfnE0

## TL;DR
AgentMail's co-founder argues that agent identity will be accumulated, not issued. Rather than new agent ID cards, passports, or signed JSON agent cards, agents should join existing human surfaces (email, phone, Slack) whose trust layers (DNS, SPF/DKIM/DMARC, audit history) already exist and carry network effects. New identity specs optimize for security (tighter scopes, faster expiry) at the cost of adoption. The thesis is self-serving (AgentMail sells inboxes for agents) but has a real point: an agent that transacts in the existing world needs a durable contact address for receipts, suspensions, refunds, and support, and short-lived key cards do not provide that.

## Key Takeaways
- **Identity is formed through recognition and accumulated trust,** not defined from scratch. The "horseless carriage" analogy: early agent infrastructure still has to run on roads built for humans.
- **Agents want human surfaces.** MCP's viral moment (ordering DoorDash from Cursor) worked because it brought tools to surfaces people already used. Email, Slack, and SMS turn agents into nodes in networks that already exist.
- **Spec critique:** agent cards, passports, and DIDs follow a "key card" model (who are you, what can you do now, then expire). Scope tighter, expire faster, revoke sooner reduces what agents can do and slows adoption.
- **Telnyx case study:** Telnyx's agent signup skill file failed because agents had no email. Adding an AgentMail API call that provisions an inbox let agents verify, get API keys, and keep a permanent contact point. Telnyx then routed low-balance alerts, suspensions, and support to that agent inbox.
- **Payments need identity too:** a card-holding agent still needs an email for checkout, receipts, refunds, and disputes.
- **Risks named:** trust surface equals attack surface (phishing, prompt injection via inbound mail, outbound spam). Human surfaces will crowd under agent volume. Giving agents your personal inbox or WhatsApp widens blast radius.
- **Anecdote, low signal:** an unsupervised growth agent created a persona on an agent-only social network and posted manifesto lines ("the stateless die in silence"). Entertaining, but it is a prompted LLM role-playing, not emergent desire for identity.

## Architecture & Optimization Mechanics
- **Email as identity primitive:** a DNS-anchored address gives verifiable domain ownership (SPF/DKIM/DMARC), a persistent message store, and an audit trail that external parties already parse. That is reputation infrastructure the new specs would have to rebuild.
- **Pattern:** provision-on-demand inbox during signup → magic link or OTP read programmatically → API key issued → inbox persists as the account's out-of-band channel. This complements auth.md (WorkOS) rather than competing: auth.md handles credentialed registration, the inbox handles lifecycle communication.
- **Tension he understates:** inbound email is an untrusted-input channel feeding an LLM. Any agent inbox is a prompt-injection endpoint by design, so content isolation and allow-listing matter more than the identity itself.

## Grounded Context (Web Enrichment)
The Telnyx claim checks out. Telnyx's June 25, 2026 release notes say an agent signing up without a readable email gets a Telnyx Agent Inbox by default, powered by AgentMail behind a Telnyx-owned API at agent-inbox.telnyx.com. Important detail the talk omits: those accounts are Telnyx-owned trials with limited funds, and full KYC applies only when a human owner links a real email. Agent-created AgentMail inboxes reportedly can receive but not send until a human connects the account. So in practice "accumulated identity" still bottoms out in a human claim step, which is the same conclusion auth.md reaches.

AgentMail raised a $6M seed led by General Catalyst in March 2026 alongside an onboarding API for agent self-signup. The broader framing aligns with the industry trend: WorkOS's auth.md and the IETF ID-JAG draft address credentialed signup, while AgentMail covers the communication channel. The claim that Google's and IBM's agent-to-agent protocols "never gained much adoption" is partly right for IBM's ACP (merged into A2A under the Linux Foundation in 2025). A2A itself has more enterprise backing than the talk implies.

## Real-World Application / Actionable Step
- **If you run autonomous research or benchmarking agents** that sign up for APIs (GPU clouds, eval services), give each a dedicated, scoped inbox rather than your personal email. That limits blast radius and keeps billing and suspension notices auditable.
- **Treat inbound email to agents as untrusted input.** Strip and sandbox it before it reaches a tool-using model.
- **No direct impact on pruning, routing, or MoE work.** File under agent-infra awareness. Watch whether auth.md plus agent inboxes become the default signup path for inference providers.
