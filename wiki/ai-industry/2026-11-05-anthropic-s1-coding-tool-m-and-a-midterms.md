# Anthropic's amended S-1, the coding-tool M&A wave, and the midterm verdict on data centers

**Sources:** AI Breakfast (Gmail, 11-04) citing [PPC Land on the S-1](https://ppc.land/anthropic-swings-to-567m-q3-operating-loss-on-5bn-of-short-term-compute/) · The Decoder: [Meta buys Conductor](https://the-decoder.com/meta-buys-ai-coding-startup-conductor-as-big-tech-races-to-lock-in-developers/), [Cat Wu to OpenAI](https://the-decoder.com/anthropic-loses-product-lead-catherine-wu-behind-claude-code-to-openai/), [Apple cuts AI budgets](https://the-decoder.com/apple-slashes-internal-ai-budgets-with-deeper-cuts-still-planned/), [Anthropic pays for news](https://the-decoder.com/anthropic-reverses-course-and-pays-for-news-content-for-the-first-time/), [Tencent Hy4](https://the-decoder.com/tencent-releases-hy4-with-vision-and-computer-use-claims-second-place-among-chinese-ai-models/) · [OpenAI acquires Pierre](https://openai.com/index/openai-to-acquire-pierre) · The Information (11-04/05) · Interconnects ([open model inference share](https://www.interconnects.ai/p/how-well-can-we-measure-open-model))

**TL;DR.** Anthropic's amended S-1 shows Q3 revenue of $16.96B (up 1,127% year on year, ~47% over Q2), a $567M operating loss driven by $5.0B of costlier short-term compute, positive $6.57B nine-month operating cash flow, and about $895.4B of purchase commitments and leases ($69.8B due within 12 months; Google Cloud alone ~$121.3B). Its risk factors say the RSP threshold for AI-accelerated progress "may imminently" be met. The same week, the value in coding agents moved to the tools around the model: OpenAI is buying Pierre (Git-compatible Code Storage for machines; OpenAI's own Pando backend cut median push latency ~80%), Meta is buying Conductor (run many coding agents at once), and Claude Code's founding product lead Cat Wu left for OpenAI, the third Claude Code departure in two weeks. Nathan Lambert estimates open-model inference is growing near-exponentially: Fireworks serves 40T+ tokens a day on customized models alone; Together says it briefly served more OpenRouter tokens than closed labs in October; Vercel's gateway went from under 10% open-weight tokens to nearly 80%.

## Funding and deals in the window

- Applied Compute raised $350M at $3.25B on $100M+ ARR.
- CrowdStrike paying ~$495M for Fiddler AI and Dreadnode; Palo Alto Networks in talks to buy Clutch Security (~$500M), its fifth deal this year.
- Weave (YC W25) raised a $13.5M Series A (Standard Capital) and launched Weave Router for coding-task model selection.
- Oracle filed to sell $20B of stock and bonds for its buildout; Meta sold $15B of AI bonds on $58B of orders.
- Marvell's all-stock bid for Lumentum (~$80B) may draw a rival bidder.
- China blocked SoftBank's $5.4B purchase of ABB Robotics.
- Cathedral (ex-DOGE security firm, $1.4B valuation) runs OpenAI's next security sprint after breaching Anthropic via its bug bounty.

## How it relates to prior wiki pages

- **Extends** the 10-27 S-1 page (the first prospectus) and 11-03 lab-finances page: revenue growth is real, the risk is commitments, not burn.
- **Confirms** the 11-04 LinkedIn and Menlo signals: buyers route and switch models, so lock-in moves to harness and repo tooling (Pierre, Conductor, Stainless in May).

Related: [Compute economics](../hardware/compute-economics.md) · [Agent harness engineering](../agentic-systems/agent-harness-engineering.md)
