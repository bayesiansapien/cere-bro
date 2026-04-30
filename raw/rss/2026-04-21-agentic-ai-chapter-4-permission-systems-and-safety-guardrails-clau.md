---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 4: Permission Systems and Safety Guardrails (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-4-permission-systems-and
published: 2026-04-21
author: Ken Huang
---

# Chapter 4: Permission Systems and Safety Guardrails (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>Permission systems are the safety layer between model intent and real-world action. They answer one question before every tool call: should this be allowed? The answer depends on who is asking, what mode the agent is in, and what the tool does. Without this layer, an autonomous agent is just a script with a language model attached &#8212; capable of deleting databases, overwriting system files, or executing arbitrary shell commands without any human in the loop. The permission system is what makes the difference between a demo and a production agent.</p><h2>2. Claude Code Implementation</h2><h3>PermissionMode Enum</h3><p>Claude Code defines five permission modes, each representing a different balance between automation and user control:</p><pre><code>// src/types/permissions.ts
// Five modes covering the full spectrum from fully interactive to fully automated
export type PermissionMode =
  | 'default'      // Ask the user before any potentially dangerous operation
  | 'auto'         // Classifier decides; no user interaction (headless/batch use)
  | 'plan'         // User approves a high-level plan first; tools run within that scope
  | 'acceptEdits'  // Auto-approve safe file edits; still ask about destructive ops
  | 'bubble'       // Subagent mode &#8212; inherit parent's permission context</code></pre><p><code>default</code> is for interactive sessions where the user wants full control. <code>auto</code> is for CI pipelines and batch jobs where no human is present. <code>plan</code> is for high-stakes operations where the user wants to review the strategy before any tool fires. <code>acceptEdits</code> is optimized for code review workflows. <code>bubble</code> ensures subagents cannot exceed the permissions of their parent &#8212; a critical safety property in multi-agent systems.</p><h3>The <code>canUseTool</code> Pipeline</h3><p>Every tool call passes through <code>canUseTool</code> before execution. The pipeline is layered:</p><pre><code>// src/hooks/useCanUseTool.tsx
// Pipeline: alwaysAllowRules &#8594; alwaysDenyRules &#8594; tool.checkPermissions &#8594; classifier &#8594; user dialog
const decisionPromise = forceDecision !== undefined
  ? Promise.resolve(forceDecision)                          // caller override
  : hasPermissionsToUseTool(tool, input, toolUseContext, assistantMessage, toolUseID)

return decisionPromise.then(async result =&gt; {
  if (result.behavior === "allow") {
    // Log the decision for audit trail
    ctx.logDecision({ decision: "accept", source: "config" })
    resolve(ctx.buildAllow(result.updatedInput ?? input, {
      decisionReason: result.decisionReason
    }))
    return
  }

  if (result.behavior === "deny") {
    // In auto mode, record the denial for analytics and notify the user
    recordAutoModeDenial({ toolName: tool.name, reason: result.decisionReason?.reason })
    resolve(result)
    return
  }

  // behavior === "ask": route to the right handler
  if (appState.toolPermissionContext.awaitAutomatedChecksBeforeDialog) {
    // Coordinator mode: wait for automated checks before showing any dialog
    const coordinatorDecision = await handleCoordinatorPermission({ ctx, ... })
    if (coordinatorDecision) { resolve(coordinatorDecision); return }
  }

  // Swarm worker: delegate the decision up to the team lead
  const swarmDecision = await handleSwarmWorkerPermission({ ctx, ... })
  if (swarmDecision) { resolve(swarmDecision); return }

  // Bash classifier: race a speculative check against a 2-second timeout
  if (feature("BASH_CLASSIFIER") &amp;&amp; result.pendingClassifierCheck) {
    const raceResult = await Promise.race([
      speculativePromise.then(r =&gt; ({ type: 'result', result: r })),
      new Promise(r =&gt; setTimeout(r, 2000, { type: 'timeout' }))
    ])
    if (raceResult.type === 'result' &amp;&amp; raceResult.result.confidence === 'high') {
      resolve(ctx.buildAllow(input, { decisionReason: { type: 'classifier' } }))
      return
    }
  }

  // Fall through to interactive dialog
  handleInteractivePermission({ ... }, resolve)
})</code></pre><p>The pipeline is designed so that the cheapest checks run first. Static rules (always-allow, always-deny) are evaluated before classifiers, and classifiers run before interactive dialogs. This minimizes latency for common cases while preserving safety for ambiguous ones.</p><h3>Rule Sources and Priority</h3><p>Rules come from four sources with a defined priority order:</p><pre><code>// src/Tool.ts
// Rules are keyed by pattern; each carries its source and decision
export type ToolPermissionRulesBySource = {
  [pattern: string]: {
    source: 'config' | 'user' | 'org' | 'classifier'
    decision: 'allow' | 'deny' | 'ask'
    reason?: string
  }
}
// Priority: deny &gt; ask &gt; allow; org &gt; user &gt; config &gt; classifier</code></pre><p><code>org</code> rules are set by administrators and cannot be overridden by users. <code>user</code> rules are set interactively. <code>config</code> rules come from the application config file. <code>classifier</code> rules are generated dynamically by the safety classifier. Deny rules always win over allow rules at the same priority level.</p><h3>Coordinator Mode and Swarm Delegation</h3><p>In multi-agent deployments, <code>awaitAutomatedChecksBeforeDialog</code> enables centralized permission management. Instead of each agent showing its own dialog, the coordinator collects all requests and presents them through a unified interface. Swarm workers delegate decisions up to the team lead, ensuring that no worker can approve actions the team lead would reject.</p><h2>3. Hermes Agent Implementation</h2><h3>Dangerous Pattern Detection (<code>approval.py</code>)</h3><p>Hermes takes a regex-based approach to dangerous command detection. The <code>DANGEROUS_PATTERNS</code> list is the single source of truth:</p><pre><code># hermes-agent/tools/approval.py
# Each tuple is (regex_pattern, human_readable_description)
# Covers filesystem destruction, SQL drops, shell injection, and self-termination
DANGEROUS_PATTERNS = [
    (r'\brm\s+-[^\s]*r',              "recursive delete"),
    (r'\bDROP\s+(TABLE|DATABASE)\b',  "SQL DROP"),
    (r'\bDELETE\s+FROM\b(?!.*\bWHERE\b)', "SQL DELETE without WHERE"),
    (r'\bTRUNCATE\s+(TABLE)?\s*\w',   "SQL TRUNCATE"),
    (r':\(\)\s*\{\s*:\s*\|\s*:\s*&amp;\s*\}\s*;\s*:', "fork bomb"),
    (r'\b(curl|wget)\b.*\|\s*(ba)?sh\b', "pipe remote content to shell"),
    (r'\b(pkill|killall)\b.*\b(hermes|gateway|cli\.py)\b', "kill hermes/gateway process"),
    # ... 30+ more patterns
]

def detect_dangerous_command(command: str) -&gt; tuple:
    """Returns (is_dangerous, pattern_key, description) or (False, None, None).
    
    Normalizes the command first: strips ANSI escapes, null bytes, and
    Unicode fullwidth characters to prevent obfuscation bypasses.
    """
    command_lower = _normalize_command_for_detection(command).lower()
    for pattern, description in DANGEROUS_PATTERNS:
        if re.search(pattern, command_lower, re.IGNORECASE | re.DOTALL):
            return (True, description, description)
    return (False, None, None)</code></pre><p>The normalization step is important &#8212; without it, a command like <code>&#65362;&#65357; -rf /</code> (using Unicode fullwidth characters) could bypass ASCII-only pattern matching.</p><h3>User Allowlist</h3><p>Once a user approves a pattern, it can be stored at three scopes:</p><pre><code># hermes-agent/tools/approval.py
# Three approval scopes: once (no storage), session (in-memory), always (config file)

def approve_session(session_key: str, pattern_key: str):
    """Approve a pattern for this session only &#8212; stored in memory."""
    with _lock:
        _session_approved.setdefault(session_key, set()).add(pattern_key)

def approve_permanent(pattern_key: str):
    """Add a pattern to the permanent allowlist &#8212; persisted to config.yaml."""
    with _lock:
        _permanent_approved.add(pattern_key)

def is_approved(session_key: str, pattern_key: str) -&gt; bool:
    """Check both permanent and session-scoped approvals.
    
    Also checks legacy regex-derived keys for backwards compatibility
    with older config.yaml entries.
    """
    aliases = _approval_key_aliases(pattern_key)
    with _lock:
        if any(alias in _permanent_approved for alias in aliases):
            return True
        session_approvals = _session_approved.get(session_key, set())
        return any(alias in session_approvals for alias in aliases)</code></pre><p>The alias system handles backwards compatibility: older config files stored regex-derived keys, newer ones store human-readable descriptions. Both are accepted.</p><h3><code>approval_callback</code>: Interactive TUI Approval</h3><p>The <code>approval_callback</code> in <code>callbacks.py</code> bridges the synchronous approval check into prompt_toolkit's async TUI:</p><pre><code># hermes-agent/hermes_cli/callbacks.py
def approval_callback(cli, command: str, description: str) -&gt; str:
    """Prompt for dangerous command approval through the TUI.
    
    Serializes concurrent requests via _approval_lock so parallel
    subagent tasks don't stomp on each other's prompts.
    Returns: 'once' | 'session' | 'always' | 'deny'
    """
    lock = getattr(cli, "_approval_lock", None)
    if lock is None:
        import threading
        cli._approval_lock = threading.Lock()
        lock = cli._approval_lock

    with lock:
        timeout = CLI_CONFIG.get("approvals", {}).get("timeout", 60)
        response_queue = queue.Queue()
        choices = ["once", "session", "always", "deny"]
        if len(command) &gt; 70:
            choices.append("view")  # let user inspect long commands before deciding

        # Push state into the CLI so the TUI can render the approval widget
        cli._approval_state = {
            "command": command,
            "description": description,
            "choices": choices,
            "selected": 0,
            "response_queue": response_queue,
        }
        cli._approval_deadline = _time.monotonic() + timeout
        cli._app.invalidate()  # trigger TUI redraw

        # Block until the user responds or the timeout fires
        while True:
            try:
                result = response_queue.get(timeout=1)
                cli._approval_state = None
                return result
            except queue.Empty:
                if _time.monotonic() &gt; cli._approval_deadline:
                    return "deny"  # timeout defaults to deny</code></pre><h3><code>clarify_callback</code>: Open-Ended Questions</h3><p>For non-approval questions &#8212; "which environment should I target?" &#8212; <code>clarify_callback</code> handles both multiple-choice and free-text input:</p><pre><code># hermes-agent/hermes_cli/callbacks.py
def clarify_callback(cli, question, choices):
    """Prompt for a clarifying question through the TUI.
    
    When choices is empty, renders a free-text input field.
    When choices is non-empty, renders a selection widget.
    Blocks until the user responds or the 120-second timeout fires.
    """
    is_open_ended = not choices
    cli._clarify_state = {
        "question": question,
        "choices": choices if not is_open_ended else [],
        "selected": 0,
        "response_queue": queue.Queue(),
    }
    cli._clarify_freetext = is_open_ended
    cli._app.invalidate()
    # ... blocking poll loop identical to approval_callback</code></pre><h3>Approval Integration in <code>terminal_tool.py</code></h3><p>The terminal tool calls <code>_check_all_guards</code> before executing any command. This runs both the regex-based dangerous command check and the optional tirith security scanner:</p><pre><code># hermes-agent/tools/terminal_tool.py (around line 1155)
# Pre-exec guard: runs before every shell command, skipped only when force=True
if not force:
    approval = _check_all_guards(command, env_type)
    if not approval["approved"]:
        if approval.get("status") == "approval_required":
            # Gateway mode: return a structured response asking the user
            return json.dumps({
                "output": "",
                "exit_code": -1,
                "error": approval.get("message", "Waiting for user approval"),
                "status": "approval_required",
                "command": approval.get("command", command),
                "description": approval.get("description", "command flagged"),
            })
        # CLI mode: command was blocked after user denied
        return json.dumps({
            "output": "",
            "exit_code": -1,
            "error": approval.get("message", "Command denied"),
            "status": "blocked"
        })</code></pre><p>Container environments (<code>docker</code>, <code>singularity</code>, <code>modal</code>) bypass the approval check entirely &#8212; the container boundary is treated as sufficient isolation.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!y_vh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bef0611-cc20-4ffa-a5bb-e2cd931aa44f_1045x515.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="515" src="https://substackcdn.com/image/fetch/$s_!y_vh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bef0611-cc20-4ffa-a5bb-e2cd931aa44f_1045x515.png" title="Comparison table" width="1045" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-4-permission-systems-and">
              Read more
          </a>
      </p>