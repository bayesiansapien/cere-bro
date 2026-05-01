---
source: farmer/rss
feed: agentic-ai
farmed: 2026-05-01T08:07:09.911670+00:00
title: Chapter 13: MCP Integration — Connecting Agents to the World (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting
published: 2026-04-30
author: Ken Huang
---

# Chapter 13: MCP Integration — Connecting Agents to the World (Claude Code vs. Hermes Agent)

<p><em>Bonus Chapter 13 of the Agentic AI Harness Engineering series</em></p><h2>1. Pattern Summary</h2><p>MCP (Model Context Protocol) is the USB-C of AI agents: a standard protocol that lets any agent connect to any tool server without custom integration code. Instead of writing a bespoke Python wrapper every time you want to expose a new capability &#8212; a vulnerability scanner, a SIEM query engine, a threat intel feed &#8212; you write one MCP server and any compliant agent can discover and call its tools automatically. The pattern matters because it decouples the agent harness from specific tool implementations, enabling a marketplace of reusable tool servers that outlive any single agent project. Both Claude Code and Hermes implement MCP clients, but they make very different architectural choices about connection lifecycle, server-initiated requests, and credential safety. This chapter covers those choices in depth.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's MCP client spans 24 files and roughly 12,000 lines in <code>src/services/mcp/</code>. The design is TypeScript-native, async-first, and tightly integrated with the QueryEngine that drives every conversation turn.</p><h3>mcpClients and QueryEngine</h3><p>MCP clients are instantiated at session start and passed directly into the <code>QueryEngine</code> constructor. Every call to <code>ask()</code> receives the same <code>mcpClients</code> map, so the engine always has a live reference to every connected server:</p><pre><code>// src/query/QueryEngine.ts (simplified)
// mcpClients is a Map&lt;serverName, McpClient&gt; built at session startup
const engine = new QueryEngine({
  tools: builtinTools,
  mcpClients,          // MCP servers injected alongside built-in tools
  permissionMode,
});

// Inside ask(), MCP tools are merged with built-in tools before each turn
const allTools = [
  ...builtinTools,
  ...buildMcpTools(mcpClients),  // dynamic &#8212; reflects current server state
];</code></pre><p>The <code>mcpClients</code> parameter is not optional. If you construct a <code>QueryEngine</code> without it, MCP tools simply don't exist for that session. This is intentional: Claude Code treats MCP as a first-class input to the engine, not a plugin bolted on afterward.</p><h3>Tool Namespacing: <code>mcp__server__tool</code></h3><p>Every MCP tool gets a namespaced name using double underscores as separators: <code>mcp__server-name__tool-name</code>. This convention is enforced at discovery time and serves two purposes. First, it prevents collisions between MCP tools and built-in tools that might share short names like <code>search</code> or <code>run</code>. Second, it makes the provenance of every tool call visible in logs and transcripts &#8212; you can immediately see that <code>mcp__github__create_issue</code> came from the GitHub MCP server, not a built-in.</p><pre><code>// src/services/mcp/McpToolBuilder.ts (simplified)
// Tool names are prefixed at discovery time, not at call time
function buildMcpTools(clients: Map&lt;string, McpClient&gt;): Tool[] {
  const tools: Tool[] = [];
  for (const [serverName, client] of clients) {
    for (const mcpTool of client.listTools()) {
      tools.push({
        // Double-underscore namespace: mcp__&lt;server&gt;__&lt;tool&gt;
        name: `mcp__${serverName}__${mcpTool.name}`,
        description: mcpTool.description,
        inputSchema: mcpTool.inputSchema,
        // Delegate execution back to the MCP client
        handler: (args) =&gt; client.callTool(mcpTool.name, args),
      });
    }
  }
  return tools;
}</code></pre><h3>Dynamic Discovery and AgentTool Dependencies</h3><p>Tools are discovered at session start and refreshed between turns. If a server sends a <code>notifications/tools/list_changed</code> notification, Claude Code re-fetches the tool list before the next turn begins. This means a long-running session can pick up new tools from a server that was updated mid-conversation.</p><p>The <code>AgentTool</code> type (used for sub-agent spawning, covered in cc7) has a <code>requiredMcpServers</code> field. When a sub-agent declares that it needs a specific MCP server, the coordinator ensures that server is connected before the sub-agent starts. This is the cleanest expression of MCP as a first-class dependency: agents can declare their external tool requirements the same way they declare their built-in tool requirements.</p><pre><code>// src/tools/AgentTool.ts (simplified)
// Sub-agents can declare which MCP servers they need
const forensicsAgent: AgentTool = {
  name: "forensics_agent",
  description: "Deep log analysis agent",
  // Coordinator will ensure these servers are connected before spawning
  requiredMcpServers: ["splunk-mcp", "elastic-mcp"],
  handler: async (args, { mcpClients }) =&gt; {
    // mcpClients is pre-populated with the required servers
    return spawnSubAgent(args, mcpClients);
  },
};</code></pre><h3>Connection Management</h3><p>MCP server connections live in <code>src/services/mcp/</code>. Each server gets a dedicated client object that manages the transport (stdio or HTTP) and exposes a typed <code>callTool</code> method. The connection lifecycle is tied to the session: servers connect when the session starts and disconnect when it ends. Claude Code's async TypeScript runtime handles concurrency natively &#8212; no background threads needed.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes's MCP client lives in a single file: <code>hermes-agent/tools/mcp_tool.py</code>. It's 1,900+ lines of carefully engineered Python that solves a hard problem: running an async MCP protocol client from a synchronous Python agent loop, with production-grade reliability features that Claude Code's TypeScript implementation gets for free from the runtime.</p><h3>Config Structure</h3><p>MCP servers are declared in <code>~/.hermes/config.yaml</code> under <code>mcp_servers</code>. Each server entry supports either stdio or HTTP transport, plus optional sampling configuration:</p><pre><code># ~/.hermes/config.yaml
mcp_servers:
  # Stdio transport: spawns a subprocess
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    env: {}                  # merged with safe baseline env (PATH, HOME, etc.)
    timeout: 120             # per-tool-call timeout in seconds
    connect_timeout: 60      # initial connection timeout

  # HTTP transport: connects to a remote server
  remote_api:
    url: "https://my-mcp-server.example.com/mcp"
    headers:
      Authorization: "Bearer ${REMOTE_API_KEY}"  # ${VAR} interpolated from .env
    timeout: 180

  # Sampling enabled: this server can request LLM completions
  analysis:
    command: "npx"
    args: ["-y", "analysis-server"]
    sampling:
      enabled: true
      model: "gemini-3-flash"   # override model for sampling requests
      max_tokens_cap: 4096
      timeout: 30
      max_rpm: 10               # rate limit: 10 LLM calls per minute
      max_tool_rounds: 5        # prevent infinite tool loops</code></pre><h3>The Background Event Loop: <code>_mcp_loop</code></h3><p>This is the architectural centerpiece of Hermes's MCP client. Python's asyncio and threading don't mix cleanly &#8212; you can't just <code>await</code> an async MCP session from a synchronous tool handler. Hermes solves this with a dedicated daemon thread that runs its own asyncio event loop forever:</p><pre><code># hermes-agent/tools/mcp_tool.py

# Module-level: one event loop, one thread, for all MCP servers
_mcp_loop: Optional[asyncio.AbstractEventLoop] = None
_mcp_thread: Optional[threading.Thread] = None
_lock = threading.Lock()  # protects all module-level state

def _ensure_mcp_loop():
    """Start the background event loop thread if not already running."""
    global _mcp_loop, _mcp_thread
    with _lock:
        if _mcp_loop is not None and _mcp_loop.is_running():
            return
        _mcp_loop = asyncio.new_event_loop()
        _mcp_loop.set_exception_handler(_mcp_loop_exception_handler)
        # daemon=True: thread dies when the main process exits
        _mcp_thread = threading.Thread(
            target=_mcp_loop.run_forever,
            name="mcp-event-loop",
            daemon=True,
        )
        _mcp_thread.start()

def _run_on_mcp_loop(coro, timeout: float = 30):
    """Schedule a coroutine on the MCP loop and block the caller until done.
    
    This is the bridge between the synchronous agent loop and the async
    MCP protocol. run_coroutine_threadsafe() is thread-safe by design.
    """
    future = asyncio.run_coroutine_threadsafe(coro, _mcp_loop)
    return future.result(timeout=timeout)  # blocks the calling thread</code></pre><p>Every tool call from the agent loop goes through <code>_run_on_mcp_loop</code>. The agent thread blocks, the MCP loop handles the async protocol, and the result comes back as a plain Python value. Clean separation, no asyncio leaking into the agent.</p><h3>MCPServerTask: One Task Per Server</h3><p>Each MCP server runs as a long-lived <code>asyncio.Task</code> on the background loop. The task keeps the transport context alive &#8212; the <code>async with stdio_client(...)</code> or <code>async with streamablehttp_client(...)</code> block stays open for the entire session. This is required by anyio's cancel-scope semantics: the context manager that opens a connection must be entered and exited in the same task.</p><pre><code># hermes-agent/tools/mcp_tool.py

class MCPServerTask:
    """One long-lived asyncio Task per MCP server.
    
    The entire connection lifecycle runs inside this task so anyio
    cancel-scopes are entered and exited in the same context.
    """

    async def _run_stdio(self, config: dict):
        """Connect via stdio transport (spawns a subprocess)."""
        safe_env = _build_safe_env(config.get("env"))  # filter dangerous env vars
        command, safe_env = _resolve_stdio_command(config["command"], safe_env)
        server_params = StdioServerParameters(command=command, args=config.get("args", []), env=safe_env)
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write, **self._sampling.session_kwargs()) as session:
                await session.initialize()
                self.session = session
                await self._discover_tools()
                self._ready.set()          # signal: tools are available
                await self._shutdown_event.wait()  # hold until shutdown

    async def _run_http(self, config: dict):
        """Connect via StreamableHTTP transport (remote server)."""
        headers = dict(config.get("headers") or {})
        async with streamable_http_client(config["url"], http_client=http_client) as (read, write, _):
            async with ClientSession(read, write, **self._sampling.session_kwargs()) as session:
                await session.initialize()
                self.session = session
                await self._discover_tools()
                self._ready.set()
                await self._shutdown_event.wait()</code></pre><h3>Automatic Reconnection with Exponential Backoff</h3><p>If a server connection drops, <code>MCPServerTask.run()</code> catches the exception and retries with exponential backoff, up to 5 attempts. The backoff starts at 1 second and caps at 60 seconds:</p><pre><code># hermes-agent/tools/mcp_tool.py

async def run(self, config: dict):
    """Long-lived coroutine with automatic reconnection."""
    retries = 0
    backoff = 1.0  # seconds, doubles each retry

    while True:
        try:
            if self._is_http():
                await self._run_http(config)
            else:
                await self._run_stdio(config)
            break  # clean shutdown &#8212; exit the loop

        except Exception as exc:
            self.session = None

            # First connection failure: report immediately, don't retry
            if not self._ready.is_set():
                self._error = exc
                self._ready.set()
                return

            # Don't reconnect if shutdown was requested
            if self._shutdown_event.is_set():
                return

            retries += 1
            if retries &gt; _MAX_RECONNECT_RETRIES:  # 5 retries max
                logger.warning("MCP server '%s' giving up after %d attempts", self.name, retries)
                return

            # Exponential backoff: 1s, 2s, 4s, 8s, 16s (capped at 60s)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, _MAX_BACKOFF_SECONDS)</code></pre><h3>SamplingHandler: Server-Initiated LLM Requests</h3><p>This is Hermes's most distinctive MCP feature. The MCP spec allows servers to request LLM completions from the client &#8212; a server can say "I need you to summarize this data before I return the result." Hermes implements this via <code>SamplingHandler</code>, a callable class that acts as the <code>sampling_callback</code> for <code>ClientSession</code>:</p><pre><code># hermes-agent/tools/mcp_tool.py

class SamplingHandler:
    """Handles sampling/createMessage requests from an MCP server.
    
    When an MCP server calls sampling/createMessage, this handler:
    1. Rate-limits the request (sliding window, configurable RPM)
    2. Resolves which model to use (config override &gt; server hint)
    3. Converts MCP message format to OpenAI format
    4. Offloads the sync LLM call to a thread (non-blocking)
    5. Returns CreateMessageResult or ErrorData back to the server
    """

    async def __call__(self, context, params):
        # Rate limit: sliding window over the last 60 seconds
        if not self._check_rate_limit():
            return self._error(f"Rate limit exceeded ({self.max_rpm}/min)")

        # Convert MCP messages to OpenAI format
        messages = self._convert_messages(params)
        max_tokens = min(params.maxTokens, self.max_tokens_cap)

        # Offload sync LLM call to thread &#8212; keeps the event loop unblocked
        def _sync_call():
            return call_llm(task="mcp", model=self._resolve_model(params.modelPreferences),
                           messages=messages, max_tokens=max_tokens, timeout=self.timeout)

        response = await asyncio.wait_for(
            asyncio.to_thread(_sync_call), timeout=self.timeout
        )

        # Dispatch: tool_calls response vs text response
        choice = response.choices[0]
        if choice.finish_reason == "tool_calls" and choice.message.tool_calls:
            return self._build_tool_use_result(choice, response)  # server gets tool calls back
        return self._build_text_result(choice, response)          # server gets text back</code></pre><p>The sampling callback is passed to <code>ClientSession</code> at connection time. When the server sends a <code>sampling/createMessage</code> request, the MCP SDK invokes the callback directly on the background event loop. The LLM call is offloaded to a thread via <code>asyncio.to_thread()</code> so it doesn't block the event loop while waiting for the API response.</p><h3>Credential Stripping</h3><p>Any error message that reaches the LLM is first passed through <code>_sanitize_error()</code>, which strips credential-like patterns using a compiled regex:</p><pre><code># hermes-agent/tools/mcp_tool.py

# Patterns that look like credentials &#8212; all get replaced with [REDACTED]
_CREDENTIAL_PATTERN = re.compile(
    r"(?:"
    r"ghp_[A-Za-z0-9_]{1,255}"      # GitHub PAT
    r"|sk-[A-Za-z0-9_]{1,255}"      # OpenAI-style key
    r"|Bearer\s+\S+"                  # Bearer token
    r"|token=[^\s&amp;,;\"']{1,255}"    # token=...
    r"|key=[^\s&amp;,;\"']{1,255}"      # key=...
    r"|API_KEY=[^\s&amp;,;\"']{1,255}"  # API_KEY=...
    r"|password=[^\s&amp;,;\"']{1,255}" # password=...
    r"|secret=[^\s&amp;,;\"']{1,255}"   # secret=...
    r")",
    re.IGNORECASE,
)

def _sanitize_error(text: str) -&gt; str:
    """Strip credential-like patterns before returning error text to the LLM."""
    return _CREDENTIAL_PATTERN.sub("[REDACTED]", text)</code></pre><p>Every error path &#8212; tool call failures, connection errors, sampling errors &#8212; runs through <code>_sanitize_error</code> before the text is returned to the agent. If a VirusTotal API key appears in an HTTP error response, the LLM never sees it.</p><h3><code>register_mcp_servers()</code>: Integration into the Tool Registry</h3><p>The public entry point is <code>register_mcp_servers()</code>. It starts the background loop, connects to all configured servers in parallel via <code>asyncio.gather()</code>, and registers each server's tools into the Hermes tool registry under the prefix <code>mcp_{server_name}_{tool_name}</code>. One server failing doesn't block the others &#8212; <code>return_exceptions=True</code> ensures partial success. After registration, tools appear as <code>mcp_filesystem_read_file</code>, <code>mcp_github_create_issue</code>, etc. The agent loop sees them as ordinary tools with no special handling required.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!nJWA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd811c2a7-b882-4eeb-9c45-6f703e23e7b3_991x625.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="625" src="https://substackcdn.com/image/fetch/$s_!nJWA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd811c2a7-b882-4eeb-9c45-6f703e23e7b3_991x625.png" title="Comparison table" width="991" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting">
              Read more
          </a>
      </p>
