# Auth for Agents: Let AI Sign Up for Your Product with auth.md (Michael Grinich, WorkOS)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=nSkmXakJ6eo

## TL;DR
Grinich argues the missing primitive in the agent stack is registration: agents can call tools via MCP, but they cannot sign up for a service without a human filling forms, solving CAPTCHAs, and copying API keys. WorkOS's answer is auth.md, an open spec (a markdown file a service publishes) that tells agents how to register legitimately, which identity proofs are accepted, what scopes and free-tier limits apply, and how a human claims the account later. The core mechanism is an ID-JAG (Identity Assertion JWT Authorization Grant), an IETF OAuth draft: the agent's harness mints a signed assertion of the user's identity, the service verifies it against a trust list and returns an API token. The pitch is commercial ("make something agents want") and the narrow scope is the right call. Signup is the step most hostile to agents today.

## Key Takeaways
- **Agents are now choosing vendors.** Coding agents pick email, deploy, and database providers during long autonomous runs. A product an agent cannot sign up for silently loses that funnel.
- **Legacy anti-bot defenses block good agents too.** Login boxes are hardened against automation, and cloud browser vendors advertise CAPTCHA breaking. CAPTCHAs no longer separate humans from bots, so the fix is verifiable agent identity, not better challenges.
- **MCP does not cover registration.** MCP auth today still requires a human to sign in and consent per server. auth.md handles first contact, then normal APIs and MCP take over.
- **What auth.md declares:** service capabilities, registration instructions, accepted identity proofs, supported auth flows (SSO, email, MFA), scopes and entitlements, free-tier constraints for unverified agents, and the human/org claim process.
- **Flow:** discovery (agent finds the auth.md) → agent sends ID-JAG signed by its identity provider → service verifies (or verifies out of band) → access token returned → standard API calls. Demo: agent deploys an app to Cloudflare with a 72-hour unverified grant, zero human clicks beyond "yes."
- **Payments stay downstream.** No card required up front. x402-style agent payment rails can come later, mirroring the PLG/freemium playbook.
- **Open spec, vendor-neutral claim:** GitHub repo, self-hostable, one-click in WorkOS. Salesforce's "API is the UI" (Agentforce/Slack exposed via API, MCP, CLI) is cited as proof of the headless trend.

## Architecture & Optimization Mechanics
- **Trust model:** the service does not trust the agent. It trusts the identity provider that signed the ID-JAG (e.g., the lab or harness vendor vouching for the logged-in user). This is a federation model, the same shape as SSO, just with an agent as the client.
- **Risk dial per service:** a database can give unverified agents a small free slice. Email senders or anything touching the physical world should require verified identity or out-of-band confirmation before any capacity. The spec exposes this dial instead of mandating one policy.
- **Fallback:** where no trusted IdP exists (self-hosted harnesses like OpenClaw or Pi), the spec falls back to an RFC 8628 device-code-style claim ceremony in which the human confirms in a browser.
- **Weak point:** the spec standardizes the handshake, not abuse economics. If agent IdPs are permissive, services inherit Sybil and token-fraud problems at agent speed. Trust lists of IdPs become the new gatekeeper, likely concentrating power in a few lab and identity vendors.

## Grounded Context (Web Enrichment)
auth.md launched in May 2026 with Cloudflare and Firecrawl as launch partners (the talk's "fire call" is Firecrawl). WorkOS's docs show a `/agent/identity` registration endpoint and three registration types: identity_assertion (ID-JAG), service_auth, and anonymous, plus the RFC 8628 claim fallback. The "built on existing standards" claim holds up. ID-JAG is draft-ietf-oauth-identity-assertion-authz-grant (authors from Okta and Ping Identity), which profiles RFC 8693 token exchange plus RFC 7523 JWT bearer grants. Okta markets the same pattern as Cross App Access (XAA) and MCP adopted it as the Enterprise-Managed Authorization extension, so auth.md rides on a primitive that the enterprise identity stack is already converging on.

Caveat: ID-JAG is still an Internet-Draft (rev 03 to 04 in spring 2026), not an RFC, and its original design assumes an enterprise IdP both parties trust for SSO. Stretching it to consumer agents signing up anonymously is WorkOS's extension, not IETF consensus. Cloudflare-side implementation details are not publicly documented beyond the partnership. The growth-boom claim is speculative: no adoption numbers were given.

## Real-World Application / Actionable Step
- **For any service or eval harness Amit exposes** (e.g., an internal routing or compression API), publish an auth.md-style manifest and let agents get a scoped, rate-limited trial token. That makes the service usable by autonomous research agents without manual key provisioning.
- **For routing work:** agent-originated traffic will carry identity metadata (IdP, scopes, trial vs verified). Treat it as a routing feature: send unverified-trial agent calls to the cheapest model tier and verified or paying ones to quality tiers.
- **Do not build on it for anything sensitive yet.** Wait for ID-JAG to stabilize and for at least one major lab harness to ship as a trusted IdP.
