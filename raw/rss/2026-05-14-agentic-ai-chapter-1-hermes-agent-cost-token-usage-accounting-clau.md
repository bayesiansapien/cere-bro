---
source: farmer/rss
feed: agentic-ai
farmed: 2026-05-15T03:31:59.641238+00:00
title: Chapter 1: Hermes Agent: Cost & Token-Usage Accounting (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-1-cost-and-token-usage-accounting
published: 2026-05-14
author: Ken Huang
---

# Chapter 1: Hermes Agent: Cost & Token-Usage Accounting (Claude Code vs. Hermes Agent)

<p>Before you read on &#8212; two quick announcements. First, you can now get 50% off a yearly subscription and unlock all paid content on Agentic AI, AI Security, and more: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p><p>Second, all previously written 15 Hermes Agent and Claude Code agentic harness design patterns are now available in a single book on Amazon: <a href="https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W">https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W</a></p><h2>1. Pattern Summary</h2><p>Iteration budgets cap how many <em>turns</em> an agent takes; cost accounting caps the <em>bill</em>. Every API call returns a usage object with at least four token buckets &#8212; fresh input, output, cache reads, cache writes &#8212; and a frontier-model agent that ignores them ships an unmonitored credit card to a process that can dispatch hundreds of tool calls per minute. The Cost &amp; Token-Usage Accounting pattern is the agent's internal economy: it normalizes provider-specific usage shapes into a canonical schema, multiplies tokens by per-million pricing tables, attributes spend to the right model and cache category, accumulates per-session totals, surfaces those totals to hooks and CLI commands, and warns or gates the user when spending crosses a threshold. Without it, prompt-caching wins are invisible, model routing becomes a guess, and there is no way to reconstruct <em>which</em> tool call burned through last month's budget. The harness can't optimize what it doesn't measure.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!yjhW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb13f289-9c60-48f6-ab49-b95ff5aad4a9_1800x960.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 1.1: One Ingest Point, Three Sinks" class="sizing-normal" height="960" src="https://substackcdn.com/image/fetch/$s_!yjhW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb13f289-9c60-48f6-ab49-b95ff5aad4a9_1800x960.png" title="Figure 1.1: One Ingest Point, Three Sinks" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 1.1.</em> The pattern's core shape: every API response is normalized into a canonical usage record, priced via a per-million weighted sum, and routed through a single ingest function that fans out to three sinks &#8212; per-model session totals, OpenTelemetry counters, and a threshold gate. Reading right-to-left along the bottom row tells you what the pattern is <em>for</em>: cost attribution, exportable metrics, and runaway-spend protection, all wired off one canonical shape.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's accounting flows through three concentric rings: a per-model pricing table in <code>src/utils/modelCost.ts</code>, a session-scoped cost tracker in <code>src/cost-tracker.ts</code>, and OpenTelemetry counters in <code>src/bootstrap/state.ts</code> that emit metrics to whatever backend the operator wires up.</p><h3>2.1 The pricing table &#8212; tiers, not flat rates</h3><p>Pricing lives as named <em>tiers</em> rather than per-model floats. Each tier is a frozen object with five categories: input, output, cache write, cache read, and web search requests. The next code chunk shows two of those tiers and how they're applied &#8212; note that cache reads cost a tenth of fresh input, and the structure is <code>as const satisfies ModelCosts</code> so adding a sixth category breaks every tier definition simultaneously.</p><pre><code>// src/utils/modelCost.ts
// Standard pricing tier for Sonnet models: $3 input / $15 output per Mtok
export const COST_TIER_3_15 = {
  inputTokens: 3,
  outputTokens: 15,
  promptCacheWriteTokens: 3.75,
  promptCacheReadTokens: 0.3,
  webSearchRequests: 0.01,
} as const satisfies ModelCosts

// Pricing tier for Opus 4/4.1: $15 input / $75 output per Mtok
export const COST_TIER_15_75 = {
  inputTokens: 15,
  outputTokens: 75,
  promptCacheWriteTokens: 18.75,
  promptCacheReadTokens: 1.5,
  webSearchRequests: 0.01,
} as const satisfies ModelCosts</code></pre><p>Models map onto tiers through a single dispatch table &#8212; the <code>MODEL_COSTS</code> record &#8212; keyed by canonical short name. Resolution is deliberately defensive: an unknown model falls back to the default main-loop model's tier rather than crashing, and the fallback is explicitly tagged. The next chunk shows that fallback path, including the <code>trackUnknownModelCost</code> side-effect that sets a session-wide flag the UI later renders as "(costs may be inaccurate due to usage of unknown models)".</p><pre><code>// src/utils/modelCost.ts
export function getModelCosts(model: string, usage: Usage): ModelCosts {
  const shortName = getCanonicalName(model)
  // ... fast-mode branch elided ...
  const costs = MODEL_COSTS[shortName]
  if (!costs) {
    trackUnknownModelCost(model, shortName)
    return (
      MODEL_COSTS[getCanonicalName(getDefaultMainLoopModelSetting())] ??
      DEFAULT_UNKNOWN_MODEL_COST
    )
  }
  return costs
}</code></pre><p>The actual dollar conversion is a single weighted sum. Five per-million rates, five token counts (web search is request-count not tokens), and a divide. The next chunk is the canonical per-call cost calculation &#8212; every other cost number in Claude Code traces back through this function:</p><pre><code>// src/utils/modelCost.ts
function tokensToUSDCost(modelCosts: ModelCosts, usage: Usage): number {
  return (
    (usage.input_tokens / 1_000_000) * modelCosts.inputTokens +
    (usage.output_tokens / 1_000_000) * modelCosts.outputTokens +
    ((usage.cache_read_input_tokens ?? 0) / 1_000_000) *
      modelCosts.promptCacheReadTokens +
    ((usage.cache_creation_input_tokens ?? 0) / 1_000_000) *
      modelCosts.promptCacheWriteTokens +
    (usage.server_tool_use?.web_search_requests ?? 0) *
      modelCosts.webSearchRequests
  )
}</code></pre><h3>2.2 Per-model session accumulation</h3><p>Session totals are not one big bucket. The cost tracker keeps a <code>modelUsage</code> record keyed by model name so a session that ran Sonnet for planning and Haiku for grunt work reports <em>both</em> token counts independently. The next chunk is the accumulator &#8212; note how it merges into an existing per-model record if one exists, creates a fresh one if not, and re-snapshots the model's <code>contextWindow</code> on every call so config changes mid-session don't desync the display.</p><pre><code>// src/cost-tracker.ts
function addToTotalModelUsage(cost: number, usage: Usage, model: string): ModelUsage {
  const modelUsage = getUsageForModel(model) ?? {
    inputTokens: 0, outputTokens: 0,
    cacheReadInputTokens: 0, cacheCreationInputTokens: 0,
    webSearchRequests: 0, costUSD: 0,
    contextWindow: 0, maxOutputTokens: 0,
  }
  modelUsage.inputTokens += usage.input_tokens
  modelUsage.outputTokens += usage.output_tokens
  modelUsage.cacheReadInputTokens += usage.cache_read_input_tokens ?? 0
  modelUsage.cacheCreationInputTokens += usage.cache_creation_input_tokens ?? 0
  modelUsage.webSearchRequests += usage.server_tool_use?.web_search_requests ?? 0
  modelUsage.costUSD += cost
  modelUsage.contextWindow = getContextWindowForModel(model, getSdkBetas())
  modelUsage.maxOutputTokens = getModelMaxOutputTokens(model).default
  return modelUsage
}</code></pre><h3>2.3 The ingestion path: one function, three sinks</h3><p>Every successful API response funnels through <code>addToTotalSessionCost</code>. It's the single ingestion point &#8212; the global counter, the per-model record, and the OpenTelemetry counters all update from the same call. The next chunk shows the dispatch: one call to the per-model accumulator, one to the global state setter, and a fan-out to four token-typed counter buckets.</p><pre><code>// src/cost-tracker.ts
export function addToTotalSessionCost(
  cost: number, usage: Usage, model: string,
): number {
  const modelUsage = addToTotalModelUsage(cost, usage, model)
  addToTotalCostState(cost, modelUsage, model)

  const attrs = isFastModeEnabled() &amp;&amp; usage.speed === 'fast'
    ? { model, speed: 'fast' } : { model }

  getCostCounter()?.add(cost, attrs)
  getTokenCounter()?.add(usage.input_tokens, { ...attrs, type: 'input' })
  getTokenCounter()?.add(usage.output_tokens, { ...attrs, type: 'output' })
  getTokenCounter()?.add(usage.cache_read_input_tokens ?? 0, { ...attrs, type: 'cacheRead' })
  getTokenCounter()?.add(usage.cache_creation_input_tokens ?? 0, { ...attrs, type: 'cacheCreation' })
  // ... advisor-tool recursion elided ...
  return cost
}</code></pre><p>Note the <code>attrs</code> object: every metric carries the <code>model</code> attribute, and the four token sub-counters carry a <code>type</code> attribute (<code>input</code> / <code>output</code> / <code>cacheRead</code> / <code>cacheCreation</code>). That's what makes the OTLP-exported time series sliceable &#8212; operators can group by model, by token type, or both, without re-instrumenting.</p><h3>2.4 The OpenTelemetry counters</h3><p>The cost and token counters are themselves declared as instruments at telemetry-init time. The harness exposes them as <code>AttributedCounter</code> objects &#8212; a thin wrapper that takes a value and an attributes bag. Here's where they're created:</p><pre><code>// src/bootstrap/state.ts
STATE.costCounter = createCounter('claude_code.cost.usage', {
  description: 'Cost of the Claude Code session',
  unit: 'USD',
})
STATE.tokenCounter = createCounter('claude_code.token.usage', {
  description: 'Number of tokens used',
  unit: 'tokens',
})</code></pre><p>The naming is conventional OpenTelemetry &#8212; <code>claude_code.cost.usage</code> and <code>claude_code.token.usage</code> &#8212; so any backend that scrapes OTLP can dashboard these without bespoke configuration. The unit (<code>USD</code>, <code>tokens</code>) is metadata the backend uses for axis labels and unit conversion.</p><h3>2.5 The threshold dialog &#8212; gating, not just reporting</h3><p>Claude Code doesn't only <em>report</em> spend, it interrupts the session at $5 of cumulative API spend. A <code>useEffect</code> watches the running total after every message; when it crosses the threshold, an analytics event fires and a modal pops up. The next chunk is the watcher &#8212; note the <code>haveShownCostDialog</code> guard that blocks the effect from firing on every subsequent message.</p><pre><code>// src/screens/REPL.tsx
useEffect(() =&gt; {
  const totalCost = getTotalCost();
  if (totalCost &gt;= 5 /* $5 */ &amp;&amp; !showCostDialog &amp;&amp; !haveShownCostDialog) {
    logEvent('tengu_cost_threshold_reached', {});
    // Mark as shown even if the dialog won't render (no console billing
    // access). Otherwise this effect re-fires on every message change for
    // the rest of the session &#8212; 200k+ spurious events observed.
    setHaveShownCostDialog(true);
    if (hasConsoleBillingAccess()) {
      setShowCostDialog(true);
    }
  }
}, [messages, showCostDialog, haveShownCostDialog]);</code></pre><p>The comment about "200k+ spurious events observed" is the key engineering detail: the threshold dialog is idempotent at the <em>session</em> level, not the <em>message</em> level, and the fix to that bug is now baked into the watcher's contract. When the user dismisses, the acknowledgment persists to the global config so the dialog never re-pops on subsequent sessions either. The dialog itself is a thin React component that renders title <code>"You've spent $5 on the Anthropic API this session."</code> and a single "Got it, thanks!" button (<code>src/components/CostThresholdDialog.tsx</code>).</p><h3>2.6 Resume semantics &#8212; costs persist across sessions</h3><p>Costs carry across <code>--resume</code>. When a session ends, <code>saveCurrentSessionCosts</code> writes the totals into the project config keyed by session ID; on resume, <code>restoreCostStateForSession</code> only restores if the IDs match. The next chunk shows the writer &#8212; every cost-bearing field, the per-model usage map, and the session ID are all serialized atomically:</p><pre><code>// src/cost-tracker.ts
export function saveCurrentSessionCosts(fpsMetrics?: FpsMetrics): void {
  saveCurrentProjectConfig(current =&gt; ({
    ...current,
    lastCost: getTotalCostUSD(),
    lastAPIDuration: getTotalAPIDuration(),
    lastTotalInputTokens: getTotalInputTokens(),
    lastTotalOutputTokens: getTotalOutputTokens(),
    lastTotalCacheCreationInputTokens: getTotalCacheCreationInputTokens(),
    lastTotalCacheReadInputTokens: getTotalCacheReadInputTokens(),
    lastModelUsage: Object.fromEntries(
      Object.entries(getModelUsage()).map(([model, usage]) =&gt; [model, usage])
    ),
    lastSessionId: getSessionId(),
  }))
}</code></pre><p>The session-ID gate matters: if you resume a <em>different</em> session, the costs do not bleed over &#8212; only an exact session-ID match is rehydrated, so you can't accidentally inflate the budget of session B with the spend of session A.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes pursues the same goal but with two structural differences forced by its model space. Hermes routes to ~200 models across Anthropic, OpenAI, Google, OpenRouter, Bedrock, and local Ollama instances &#8212; and each provider returns usage in a different shape. So Hermes splits the problem into a <em>normalizer</em> (everything becomes <code>CanonicalUsage</code>) and a <em>pricer</em> (everything becomes <code>CostResult</code> via per-million <code>Decimal</code> math). Both live in <code>hermes-agent/agent/usage_pricing.py</code>.</p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-1-cost-and-token-usage-accounting">
              Read more
          </a>
      </p>
