---
source: farmer/rss
feed: agentic-ai
farmed: 2026-05-02T06:18:04Z
title: Chapter 14: Model Routing and Provider Abstraction (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-14-model-routing-and-provider
published: 2026-05-01
author: Ken Huang
---

# Chapter 14: Model Routing and Provider Abstraction (Claude Code vs. Hermes Agent)

<h2>Pattern Summary</h2><p>Model routing is the decision layer between "the agent needs to call an LLM" and "this specific API endpoint gets called." It handles provider selection, API format translation, context window discovery, and graceful fallback when a provider fails. It matters because production agents can't be hardwired to one provider &#8212; costs change, APIs go down, and different tasks need different models. Both Claude Code and Hermes solve this problem, but from opposite directions: Claude Code bakes provider abstraction into a compile-time TypeScript layer with static model selection logic, while Hermes treats routing as a runtime concern &#8212; detecting API formats from URLs, building ordered fallback chains, and switching models live mid-session without restarting the agent.</p><h2>Claude Code Implementation</h2><p>Claude Code's provider abstraction is a clean compile-time layer. The harness supports four providers &#8212; Anthropic Direct (API key + OAuth), AWS Bedrock (credential refresh + Bearer Token), Google Vertex (GCP credentials refresh), and Azure Foundry (Azure AD + API key) &#8212; and the selection logic is resolved before the first API call.</p><p>Model selection happens through three functions that form a priority chain:</p><pre><code>// src/utils/model/model.js
// Returns the base configured model &#8212; reads from user settings or env
export function getMainLoopModel(): string { ... }

// Runtime resolution: permission mode and context size can override the base model.
// plan mode may use a lighter model; context &gt; 200K tokens triggers a larger one.
export function getRuntimeMainLoopModel({
  permissionMode,
  mainLoopModel,
  exceeds200kTokens,
}: {
  permissionMode: PermissionMode
  mainLoopModel: string
  exceeds200kTokens: boolean
}): string { ... }

// Subagent model resolution: explicit override &gt; agent definition &gt; parent model.
// This means a coordinator can spawn workers on cheaper models without config changes.
export function getAgentModel(
  agentModel: string | undefined,
  parentModel: string,
  explicitModel: string | undefined,
  permissionMode: PermissionMode,
): string { ... }</code></pre><p>The <code>getRuntimeMainLoopModel</code> function is where routing decisions happen at the turn level. If the user is in plan mode, the harness may route to a lighter model since plan mode only needs to produce a plan, not execute tools. If the accumulated context exceeds 200K tokens, it routes to a model with a larger window. These are static rules &#8212; no dynamic cost comparison, no live availability check.</p><p>When the primary model fails, Claude Code raises a <code>FallbackTriggeredError</code> and the query loop catches it:</p><pre><code>// src/query.ts &#8212; fallback handling inside the main query loop
try {
  for await (const message of deps.callModel({ ...params, model: currentModel })) {
    // stream assistant response chunks
  }
} catch (innerError) {
  if (innerError instanceof FallbackTriggeredError &amp;&amp; fallbackModel) {
    // Clear partial messages from the failed attempt
    assistantMessages.length = 0

    // Strip thinking signatures &#8212; extended thinking blocks use a format
    // that some fallback models (e.g. non-Claude) can't parse. Removing
    // them prevents a cascade of malformed-request errors on the retry.
    messagesForQuery = stripSignatureBlocks(messagesForQuery)

    // Inject synthetic tool_result blocks for any tool_use blocks that
    // never got a result (the failed turn left them dangling).
    yield* yieldMissingToolResultBlocks(assistantMessages, 'Model fallback triggered')

    currentModel = fallbackModel
    attemptWithFallback = true

    // Log the event for analytics &#8212; original_model tells you what failed
    logEvent('tengu_model_fallback_triggered', {
      original_model: innerError.originalModel,
      fallback_model: fallbackModel,
    })
    continue  // retry the same turn with the fallback model
  }
  throw innerError  // not a fallback error &#8212; propagate
}</code></pre><p>The key insight here is <code>stripSignatureBlocks</code>. Extended thinking produces cryptographically signed blocks that are model-specific. If you replay a conversation containing those blocks to a different model, the API rejects the request. Claude Code handles this automatically on fallback &#8212; it strips the signatures before retrying. This is a subtle but critical detail that most hand-rolled fallback implementations miss.</p><p>The design is opinionated: one fallback model, resolved at startup, applied uniformly. It's simple and reliable. What it doesn't do is support ordered fallback chains, live model switching, or per-task routing to different cost tiers.</p><h2>Hermes Agent Implementation</h2><p>Hermes treats routing as a first-class runtime concern. Every aspect of provider selection &#8212; API format, fallback ordering, context window size, and per-turn model choice &#8212; is resolved dynamically.</p><h3>API Mode Auto-Detection</h3><p>The first routing decision happens at <code>AIAgent.__init__</code>: which API format does this endpoint speak? Hermes infers this from the URL and provider name rather than requiring explicit configuration:</p><pre><code># run_agent.py &#8212; AIAgent.__init__
# Explicit override takes priority; otherwise infer from provider name and URL.
if api_mode in {"chat_completions", "codex_responses", "anthropic_messages"}:
    self.api_mode = api_mode
elif self.provider == "openai-codex":
    self.api_mode = "codex_responses"
elif self.provider == "anthropic" or (provider_name is None and "api.anthropic.com" in self._base_url_lower):
    self.api_mode = "anthropic_messages"
    self.provider = "anthropic"
elif self._base_url_lower.rstrip("/").endswith("/anthropic"):
    # Third-party endpoints (MiniMax, DashScope) use a /anthropic URL suffix
    # to signal Anthropic Messages API compatibility. Auto-detect these.
    self.api_mode = "anthropic_messages"
else:
    self.api_mode = "chat_completions"

# Direct OpenAI URLs use the Responses API, not Chat Completions.
# GPT-5.x tool calls with reasoning are rejected on /v1/chat/completions.
if self.api_mode == "chat_completions" and self._is_direct_openai_url():
    self.api_mode = "codex_responses"</code></pre><p>This matters because the three API formats have meaningfully different request shapes, streaming protocols, and tool-call conventions. Getting it wrong produces cryptic 400 errors. Hermes eliminates that class of misconfiguration entirely.</p><h3>Fallback Chain Construction</h3><p>Where Claude Code supports a single fallback model, Hermes supports an ordered chain:</p><pre><code># run_agent.py &#8212; AIAgent.__init__, fallback chain setup
# Accepts either a list (new format) or a single dict (legacy format).
if isinstance(fallback_model, list):
    # Filter out incomplete entries &#8212; both provider and model are required
    self._fallback_chain = [
        f for f in fallback_model
        if isinstance(f, dict) and f.get("provider") and f.get("model")
    ]
elif isinstance(fallback_model, dict) and fallback_model.get("provider") and fallback_model.get("model"):
    self._fallback_chain = [fallback_model]
else:
    self._fallback_chain = []

self._fallback_index = 0  # Pointer into the chain; advances on each activation

# Display the chain at startup so operators know what's configured
if self._fallback_chain and not self.quiet_mode:
    if len(self._fallback_chain) == 1:
        fb = self._fallback_chain[0]
        print(f"&#128260; Fallback model: {fb['model']} ({fb['provider']})")
    else:
        print(f"&#128260; Fallback chain ({len(self._fallback_chain)} providers): " +
              " &#8594; ".join(f"{f['model']} ({f['provider']})" for f in self._fallback_chain))</code></pre><p>When a provider fails, <code>_try_activate_fallback()</code> advances <code>_fallback_index</code> and rebuilds the client for the next entry in the chain. The chain is consumed in order &#8212; if all entries are exhausted, the error propagates.</p><h3>Context Window Discovery</h3><p>Hermes can't hardcode context lengths for 200+ models. Instead, <code>fetch_model_metadata()</code> pulls live data from OpenRouter and caches it for one hour:</p><pre><code># agent/model_metadata.py
# 1-hour TTL cache &#8212; avoids blocking HTTP on every API call
_MODEL_CACHE_TTL = 3600

def fetch_model_metadata(force_refresh: bool = False) -&gt; Dict[str, Dict[str, Any]]:
    """Fetch model metadata from OpenRouter (cached for 1 hour)."""
    global _model_metadata_cache, _model_metadata_cache_time

    if not force_refresh and _model_metadata_cache and \
       (time.time() - _model_metadata_cache_time) &lt; _MODEL_CACHE_TTL:
        return _model_metadata_cache  # Return cached data immediately

    try:
        response = requests.get(OPENROUTER_MODELS_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        cache = {}
        for model in data.get("data", []):
            model_id = model.get("id", "")
            entry = {
                "context_length": model.get("context_length", 128000),
                "max_completion_tokens": model.get("top_provider", {}).get("max_completion_tokens", 4096),
                "pricing": model.get("pricing", {}),
            }
            _add_model_aliases(cache, model_id, entry)
        _model_metadata_cache = cache
        _model_metadata_cache_time = time.time()
        return cache
    except Exception as e:
        return _model_metadata_cache or {}  # Serve stale cache on failure</code></pre><p>The cache is pre-warmed in a background thread at <code>AIAgent.__init__</code> time for OpenRouter sessions, so the first API call doesn't block on an HTTP request. When the model isn't in the OpenRouter catalog (local endpoints, custom deployments), Hermes falls back to <code>CONTEXT_PROBE_TIERS = [128_000, 64_000, 32_000, 16_000, 8_000]</code> &#8212; it tries each tier in descending order until one succeeds, then saves the result.</p><h3>Runtime Model Switching</h3><p>Hermes's <code>switch_model()</code> is a production necessity that Claude Code's compile-time provider abstraction doesn't address. An analyst mid-investigation shouldn't have to restart their session to switch from a fast model to a more capable one:</p><pre><code># run_agent.py &#8212; AIAgent.switch_model()
def switch_model(self, new_model, new_provider, api_key='', base_url='', api_mode=''):
    """Switch model/provider in-place without restarting the agent.
    
    Rebuilds the API client, re-evaluates prompt caching eligibility,
    and updates the context compressor's window size for the new model.
    Persists the change to _primary_runtime so it survives across turns.
    """
    # Determine api_mode from provider/URL if not explicitly provided
    if not api_mode:
        api_mode = determine_api_mode(new_provider, base_url)

    self.model = new_model
    self.provider = new_provider
    self.base_url = base_url or self.base_url
    self.api_mode = api_mode

    # Rebuild client for the new provider (Anthropic vs OpenAI-compatible)
    if api_mode == "anthropic_messages":
        self._anthropic_client = build_anthropic_client(api_key, base_url)
        self.client = None
    else:
        self.client = self._create_openai_client(
            {"api_key": api_key, "base_url": base_url or self.base_url},
            reason="switch_model",
            shared=True,
        )

    # Re-evaluate prompt caching &#8212; eligibility depends on provider + model
    self._use_prompt_caching = (
        ("openrouter" in (self.base_url or "").lower() and "claude" in new_model.lower())
        or (api_mode == "anthropic_messages")
    )

    # Update context compressor with the new model's context window
    if hasattr(self, "context_compressor") and self.context_compressor:
        new_context_length = get_model_context_length(
            self.model, base_url=self.base_url, provider=self.provider
        )
        self.context_compressor.context_length = new_context_length
        self.context_compressor.threshold_tokens = int(
            new_context_length * self.context_compressor.threshold_percent
        )

    # Invalidate cached system prompt &#8212; it may contain model-specific hints
    self._cached_system_prompt = None
    # Reset fallback state &#8212; new primary model, fresh fallback chain
    self._fallback_activated = False
    self._fallback_index = 0</code></pre><h3>Smart Model Routing</h3><p>For cost optimization, Hermes supports per-turn routing to a cheaper model for simple queries:</p><pre><code># agent/smart_model_routing.py
# Conservative by design: any signal of complexity keeps the primary model.
def choose_cheap_model_route(user_message, routing_config):
    cfg = routing_config or {}
    if not cfg.get("enabled"):
        return None  # Routing disabled &#8212; use primary model

    text = (user_message or "").strip()
    # Hard limits: long messages, multi-line, code blocks, URLs &#8594; primary model
    if len(text) &gt; cfg.get("max_simple_chars", 160): return None
    if len(text.split()) &gt; cfg.get("max_simple_words", 28): return None
    if text.count("\n") &gt; 1 or "```" in text or "`" in text: return None

    # Keyword check: any complexity signal &#8594; primary model
    words = {t.strip(".,:;!?") for t in text.lower().split()}
    if words &amp; _COMPLEX_KEYWORDS:  # debug, implement, analyze, docker, etc.
        return None

    return cfg.get("cheap_model")  # {"provider": "...", "model": "..."}</code></pre><p>The routing is intentionally conservative. A false negative (sending a simple query to the expensive model) costs a few cents. A false positive (sending a complex investigation to the cheap model) costs analyst time and potentially misses a threat.</p><h2>Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!C6ls!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e95ac95-0a31-4c50-a015-276b06678ddc_1072x513.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="513" src="https://substackcdn.com/image/fetch/$s_!C6ls!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e95ac95-0a31-4c50-a015-276b06678ddc_1072x513.png" title="Comparison table" width="1072" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>When to Use Which</h2><p><strong>Use Claude Code's approach when:</strong></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-14-model-routing-and-provider">
              Read more
          </a>
      </p>
