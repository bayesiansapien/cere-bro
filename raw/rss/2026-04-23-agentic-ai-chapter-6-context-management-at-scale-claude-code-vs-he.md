---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 6: Context Management at Scale (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-6-context-management-at-scale
published: 2026-04-23
author: Ken Huang
---

# Chapter 6: Context Management at Scale (Claude Code vs. Hermes Agent)

<p></p><h2>1. Pattern Summary</h2><p>Context management is how agents survive long conversations. Every LLM has a finite context window; every real task eventually exceeds it. The question is not whether you'll hit the limit, but how gracefully you handle it. A naive agent crashes with a <code>prompt_too_long</code> error and loses everything. A well-engineered harness detects the approaching limit early, applies the cheapest possible remedy first, and falls back to progressively more expensive strategies only when needed &#8212; all without interrupting the user's workflow.</p><h2>2. Claude Code Implementation</h2><p>Claude Code treats context management as a five-strategy pipeline ordered strictly by cost. Cheap local operations run first; expensive API calls are a last resort.</p><p><strong>The five strategies in cost order:</strong></p><ol><li><p><strong>Snip</strong> &#8212; removes specific message ranges locally, no API call</p></li><li><p><strong>Micro-compact</strong> &#8212; edits cached prompt-cache entries instead of re-sending unchanged content</p></li><li><p><strong>Context collapse</strong> &#8212; archives old messages and projects a collapsed view at query time</p></li><li><p><strong>Auto-compact</strong> &#8212; summarizes old conversation history via an API call (proactive)</p></li><li><p><strong>Reactive compact</strong> &#8212; catches <code>prompt_too_long</code> API errors as an emergency fallback</p></li></ol><p><strong>Token thresholds</strong> define a soft-landing zone rather than a hard wall:</p><pre><code>// src/services/compact/autoCompact.ts
// The effective window reserves 20K tokens for the compaction summary output.
// This guarantees there's always room to generate the summary itself.
export function getEffectiveContextWindowSize(model: string): number {
  const reservedTokensForSummary = Math.min(
    getMaxOutputTokensForModel(model),
    MAX_OUTPUT_TOKENS_FOR_SUMMARY,  // 20,000 tokens reserved
  )
  return getContextWindowForModel(model, getSdkBetas()) - reservedTokensForSummary
}</code></pre><p>The threshold ladder works like this: at ~70% of the effective window, auto-compact triggers proactively. At ~90%, a warning surfaces to the user. At ~98%, new requests are blocked entirely and manual compaction is required. This layered approach means the system has three chances to recover before it ever fails.</p><p><strong>Circuit breaker</strong> prevents runaway API spend when compaction itself is broken:</p><pre><code>// src/services/compact/autoCompact.ts
// After 3 consecutive compaction failures, stop trying.
// Avoids burning API budget on a persistently failing operation.
if (
  tracking?.consecutiveFailures !== undefined &amp;&amp;
  tracking.consecutiveFailures &gt;= MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES  // 3
) {
  return { wasCompacted: false }
}</code></pre><p><strong>Preserved segments</strong> ensure crash recovery works after compaction. When a compact boundary is written, the system records the <code>tailUuid</code> &#8212; the last message kept after compaction. If the process crashes, the resume path uses this UUID to find exactly where to restart, rather than guessing.</p><p><strong>GC after compact boundary</strong> prevents memory leaks in long-running sessions:</p><pre><code>// src/QueryEngine.ts
// Once a compact boundary is emitted, release all pre-compact messages
// from the in-memory array. Without this, the array grows without bound
// even though the context window is being managed correctly.
if (msg.subtype === 'compact_boundary' &amp;&amp; msg.compactMetadata) {
  const mutableBoundaryIdx = this.mutableMessages.length - 1
  if (mutableBoundaryIdx &gt; 0) {
    this.mutableMessages.splice(0, mutableBoundaryIdx)  // drop pre-compact messages
  }
}</code></pre><p>The design philosophy here is defense in depth: each strategy is a fallback for the one before it, and the system degrades gracefully rather than failing suddenly.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes takes a simpler, more focused approach: one primary compression strategy backed by prompt caching to reduce the cost of repeated context.</p><p><strong>ContextCompressor</strong> is a self-contained class with its own LLM client for summarization. It uses a structured summary template (Goal, Progress, Decisions, Files, Next Steps) and supports iterative updates &#8212; each subsequent compaction updates the previous summary rather than starting from scratch.</p><p><strong>`should_compress_preflight()`</strong> runs a cheap token estimate before every API call, catching the need to compress before the request is even sent:</p><pre><code># hermes-agent/agent/context_compressor.py
# Pre-flight check using rough character-count estimate.
# Runs before every API call &#8212; no LLM needed, just arithmetic.
def should_compress_preflight(self, messages: List[Dict[str, Any]]) -&gt; bool:
    rough_estimate = estimate_messages_tokens_rough(messages)
    return rough_estimate &gt;= self.threshold_tokens</code></pre><p>The threshold defaults to 50% of the model's context window, giving plenty of headroom for the summary to be generated and the tail to be preserved.</p><p><strong>Prompt caching</strong> via <code>apply_anthropic_cache_control()</code> is Hermes's primary cost-reduction mechanism. It places up to four <code>cache_control</code> breakpoints using the <code>system_and_3</code> strategy:</p><pre><code># hermes-agent/agent/prompt_caching.py
# Places cache_control markers on: system prompt (breakpoint 1) +
# last 3 non-system messages (breakpoints 2-4).
# Anthropic's maximum is 4 breakpoints per request.
def apply_anthropic_cache_control(
    api_messages: List[Dict[str, Any]],
    cache_ttl: str = "5m",
    native_anthropic: bool = False,
) -&gt; List[Dict[str, Any]]:
    messages = copy.deepcopy(api_messages)
    marker = {"type": "ephemeral"}
    if cache_ttl == "1h":
        marker["ttl"] = "1h"

    breakpoints_used = 0
    if messages[0].get("role") == "system":
        _apply_cache_marker(messages[0], marker)  # cache the stable system prompt
        breakpoints_used += 1

    remaining = 4 - breakpoints_used
    non_sys = [i for i in range(len(messages)) if messages[i].get("role") != "system"]
    for idx in non_sys[-remaining:]:  # cache the last 3 non-system messages
        _apply_cache_marker(messages[idx], marker)

    return messages</code></pre><p><strong>Frozen snapshot pattern</strong>: the system prompt is built once at session start and never mutated mid-session. This is critical for cache efficiency &#8212; if the system prompt changes, Anthropic's cache prefix is invalidated and you pay full input cost again. By keeping the system prompt frozen, the first cache breakpoint hits on every turn after the first.</p><p><strong>Token estimation</strong> uses a model-agnostic character-count heuristic:</p><pre><code># hermes-agent/agent/model_metadata.py
# Rough estimate: ~4 characters per token. Fast enough for pre-flight checks.
# Not accurate enough for billing, but accurate enough for threshold decisions.
def estimate_tokens_rough(text: str) -&gt; int:
    return len(text) // 4

def estimate_messages_tokens_rough(messages: List[Dict[str, Any]]) -&gt; int:
    # Serialize each message to a string and count characters
    total_chars = sum(len(str(msg)) for msg in messages)
    return total_chars // 4</code></pre><p>The compression algorithm itself is a four-phase pipeline: (1) prune old tool results cheaply, (2) protect head messages (system prompt + first exchange), (3) find the tail boundary by token budget, (4) summarize the middle with a structured LLM prompt. On re-compression, the previous summary is updated iteratively rather than regenerated from scratch.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!4jh3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17a75801-9ecd-4ff0-a84d-ad5f5aa5d61b_1036x423.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="423" src="https://substackcdn.com/image/fetch/$s_!4jh3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17a75801-9ecd-4ff0-a84d-ad5f5aa5d61b_1036x423.png" title="Comparison table" width="1036" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-6-context-management-at-scale">
              Read more
          </a>
      </p>