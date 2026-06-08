# Building safe Payment Infrastructure for the autonomous economy

**Channel:** AI Engineer  
**Published:** 2026-06-06  
**Source:** https://www.youtube.com/watch?v=KLSuFPj2ld0  

## TL;DR
Steve Kaliski from Stripe introduces the infrastructure required to turn AI agents into economic actors. He argues that while discovery/exploration benefits from the non-determinism of LLMs, payments require absolute determinism. Stripe's solution involves **Shared Payment Tokens (SPTs)**, the **Machine Payments Protocol (MPP)**, and the **Agent to Commerce Protocol (ACP)** to enable secure, scoped, and programmable spending for autonomous agents.

## Key Takeaways
- **Determinism vs. Non-Determinism:** LLMs are great for finding "what to buy" (non-deterministic), but "how to pay" must be deterministic to prevent unauthorized spend or incorrect amounts.
- **Shared Payment Tokens (SPTs):** A security primitive that allows agents to share a credential with a merchant that is cryptographically locked to a specific seller, specific amount, and timeframe.
- **HTTP 402 "Payment Required":** Stripe is reviving this status code for machine-to-machine payments. When an agent hits a paid API, the server responds with a 402 challenge, which the agent fulfills using an SPT or crypto (USDC).
- **Agentic Commerce Protocol (ACP):** A standard for expressing product catalogs and checkout flows in machine-readable JSON, moving away from agents "scraping" or "stumbling through" human-centric UIs.

## Architecture & Optimization Mechanics
- **Blast Radius Reduction:** By using SPTs, the "blast radius" of an agent's spend is limited to the specific mandate (e.g., "$25 for groceries at Merchant X").
- **M2M Handshake:** The Machine Payments Protocol standardizes the payment handshake for ephemeral API interactions, often settling on the **Tempo blockchain** for sub-second finality or via USDC on **Base**.
- **Agent Wallets:** Stripe now supports programmable USDC wallets for agents, allowing for true autonomous spending without manual human intervention for every micro-transaction.

## Grounded Context (Web Enrichment)
Stripe, OpenAI, and Meta co-authored the **Agentic Commerce Protocol (ACP)** in late 2025 to standardize how agents interact with e-commerce platforms. This ecosystem is now being implemented across major platforms like Shopify and Amazon to provide "robot-friendly" product feeds.

The **Machine Payments Protocol (MPP)** has gained significant traction in the AI research community, particularly for **pay-per-token or pay-per-compute** models. Companies like **Cerebras** and **Groq** are reportedly exploring MPP to allow agents to "lease" inference compute in real-time using USDC, bypassing traditional enterprise billing cycles.

## Real-World Application / Actionable Step
- **Monetize Routing Services:** Amit can use the **MPP (402 challenge)** to monetize specialized LLM routing algorithms. If an external agent wants to use his optimal routing path, his API can issue a 402 challenge, requiring a micro-payment in USDC.
- **Action:** Review the Stripe `agentic-commerce` documentation to see how to implement Shared Payment Tokens for internal research tools that require paid API access (e.g., high-fidelity model calls).
