---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 11: Hook / Event-Driven Automation (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation
published: 2026-04-28
author: Ken Huang
---

# Chapter 11: Hook / Event-Driven Automation (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>The hook pattern lets an agent harness react to events &#8212; file changes, tool invocations, task completions, scheduled timers &#8212; without polling or tight coupling between components. Instead of the agent loop checking "did anything change?", the harness registers callbacks that fire automatically when something happens. This matters because autonomous agents running 24/7 need to enforce policies (block a dangerous tool call before it executes), integrate with external systems (push findings to a SIEM after every scan), and schedule work without human prompting (run a nightly vulnerability sweep at 2am). Hooks are the mechanism that makes all of that possible without rewriting the core agent loop.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's hook system is IDE-native and event-driven. Hooks are declared in a JSON configuration and the harness fires them at well-defined lifecycle points. There are ten event types:</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!LGUf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93fe9986-2418-48c1-a0e5-bf830bbff3aa_526x507.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="507" src="https://substackcdn.com/image/fetch/$s_!LGUf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93fe9986-2418-48c1-a0e5-bf830bbff3aa_526x507.png" title="Comparison table" width="526" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p>Each hook has one of two actions: <code>runCommand</code> (execute a shell command) or <code>askAgent</code> (invoke the agent itself with a prompt). The <code>askAgent</code> action is what makes hooks composable &#8212; a hook can trigger a full agent turn, which can itself call tools, write files, or send notifications.</p><p>A minimal hook configuration looks like this:</p><pre><code>// .kiro/hooks/my-hooks.json
// Hooks are declared as an array; each entry maps an event to an action.
{
  "hooks": [
    {
      "id": "lint-on-save",
      "name": "Lint TypeScript on save",
      "description": "Run ESLint whenever a .ts file is edited",
      "eventType": "fileEdited",
      "hookAction": "runCommand",
      "filePatterns": "**/*.ts",
      "command": "npm run lint -- --fix"
    },
    {
      "id": "post-tool-audit",
      "name": "Audit tool use",
      "description": "After every write operation, log what changed",
      "eventType": "postToolUse",
      "hookAction": "askAgent",
      "toolTypes": "write",
      "outputPrompt": "Summarize what was just written and why, then append a one-line entry to audit.log"
    }
  ]
}</code></pre><h3>preToolUse for Access Control</h3><p>The most powerful hook type is <code>preToolUse</code>. It fires <em>before</em> the tool executes and can block execution entirely. This is the harness-level equivalent of a firewall rule &#8212; the agent cannot bypass it because the check happens in the harness, not in the tool itself.</p><pre><code>// preToolUse hook that blocks destructive shell commands
// The agent sees a denial message and must choose a different path.
{
  "id": "block-rm-rf",
  "name": "Block destructive shell commands",
  "eventType": "preToolUse",
  "hookAction": "askAgent",
  "toolTypes": "shell",
  "outputPrompt": "A shell command is about to run. If it contains 'rm -rf', 'DROP TABLE', or 'format', respond with BLOCK and explain why. Otherwise respond with ALLOW."
}</code></pre><p>The <code>toolTypes</code> field accepts built-in categories (<code>read</code>, <code>write</code>, <code>shell</code>, <code>web</code>, <code>spec</code>) or a regex pattern for MCP tool names. Using <code>"*"</code> catches every tool call.</p><h3>Circular Dependency Detection</h3><p>Because <code>askAgent</code> hooks can themselves trigger tool calls, which can trigger more hooks, the harness includes automatic circular dependency detection. If hook A triggers a tool call that would fire hook A again, the harness breaks the cycle. You do not need to configure this.</p><h3>askAgent vs runCommand</h3><p>Use <code>runCommand</code> when the response is deterministic: linting, formatting, pushing metrics. Use <code>askAgent</code> when the response requires judgment: reviewing a diff, deciding whether to block a tool call. The tradeoff is latency &#8212; <code>runCommand</code> is fast, <code>askAgent</code> adds an LLM round-trip.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes does not have a single "hook system" &#8212; instead, it achieves the same goals through two complementary mechanisms: a <strong>cron scheduler</strong> for time-based automation and <strong>gateway callbacks</strong> for event-driven responses.</p><h3>Cron Scheduler: Time-Based Hooks</h3><p>The cron module (<code>hermes-agent/cron/</code>) provides a full job scheduling system. Jobs are stored as JSON in <code>~/.hermes/cron/jobs.json</code> and the scheduler checks for due jobs every 60 seconds from a background thread in the gateway.</p><pre><code># hermes-agent/cron/jobs.py
# parse_schedule() converts human-readable strings into structured schedule dicts.
# This supports one-shot, interval, cron expression, and ISO timestamp formats.

def parse_schedule(schedule: str) -&gt; Dict[str, Any]:
    """
    Parse schedule string into structured format.
    
    Examples:
        "every 30m"        &#8594; recurring every 30 minutes
        "0 2 * * *"        &#8594; cron expression (2am daily)
        "0 0 * * 0"        &#8594; cron expression (midnight Sunday)
        "2026-02-03T14:00" &#8594; one-shot at timestamp
    """
    schedule_lower = schedule.lower()
    
    # "every X" pattern &#8594; recurring interval
    if schedule_lower.startswith("every "):
        duration_str = schedule[6:].strip()
        minutes = parse_duration(duration_str)
        return {"kind": "interval", "minutes": minutes}
    
    # 5-field cron expression (requires croniter package)
    parts = schedule.split()
    if len(parts) &gt;= 5:
        croniter(schedule)  # validates the expression
        return {"kind": "cron", "expr": schedule}
    
    # ISO timestamp &#8594; one-shot
    if 'T' in schedule:
        dt = datetime.fromisoformat(schedule)
        return {"kind": "once", "run_at": dt.isoformat()}</code></pre><p>Creating a job is a single function call:</p><pre><code># hermes-agent/cron/jobs.py
# create_job() persists a job to ~/.hermes/cron/jobs.json with secure file permissions.
# The job carries its own model, provider, skills, and delivery target.

job = create_job(
    prompt="Scan all open ports on the internal network and report new findings",
    schedule="0 2 * * *",          # nightly at 2am (cron expression)
    name="Nightly vulnerability scan",
    deliver="telegram:soc-channel", # push results to Telegram SOC channel
    skills=["nmap-analyst"],        # load a skill (runbook) before running
)</code></pre><p>The scheduler's <code>run_job()</code> function spins up a full <code>AIAgent</code> instance for each job, with an inactivity-based timeout to prevent hung jobs from blocking the queue:</p><pre><code># hermes-agent/cron/scheduler.py
# run_job() creates a fresh AIAgent per job execution.
# The inactivity timeout kills jobs that stop making progress (hung API calls, stuck tools).

def run_job(job: dict) -&gt; tuple[bool, str, str, Optional[str]]:
    from run_agent import AIAgent
    
    agent = AIAgent(
        model=turn_route["model"],
        max_iterations=max_iterations,
        disabled_toolsets=["cronjob", "messaging", "clarify"],
        quiet_mode=True,
        skip_memory=True,   # cron jobs don't update user memory representations
        platform="cron",
        session_id=_cron_session_id,
        session_db=_session_db,  # persists output for session_search
    )
    
    # Poll every 5 seconds; kill if idle for more than HERMES_CRON_TIMEOUT seconds
    _cron_future = _cron_pool.submit(agent.run_conversation, prompt)
    while True:
        done, _ = concurrent.futures.wait({_cron_future}, timeout=5.0)
        if done:
            result = _cron_future.result()
            break
        idle_secs = agent.get_activity_summary().get("seconds_since_activity", 0)
        if idle_secs &gt;= _cron_inactivity_limit:
            raise TimeoutError(f"Job '{job_name}' idle for {idle_secs}s")</code></pre><h3>Gateway Callbacks: Platform Event Hooks</h3><p>The gateway (<code>hermes-agent/gateway/run.py</code>) handles incoming messages from 15+ platforms (Telegram, Discord, Slack, Matrix, etc.). Each incoming message is an event that can trigger agent execution. The gateway is the Hermes equivalent of Claude Code's <code>fileEdited</code> and <code>promptSubmit</code> hooks &#8212; it fires when something arrives from the outside world.</p><h3>Approval Callbacks: The preToolUse Equivalent</h3><p>Hermes implements pre-execution access control through the <code>approval_callback</code> in <code>hermes_cli/callbacks.py</code>. When a tool is flagged as dangerous, the harness pauses execution and routes the decision to the user through the TUI before the tool runs:</p><pre><code># hermes-agent/hermes_cli/callbacks.py
# approval_callback() is the Hermes equivalent of Claude's preToolUse hook.
# It blocks tool execution until the user approves, denies, or times out.
# Uses a threading.Lock to serialize concurrent approval requests from parallel subtasks.

def approval_callback(cli, command: str, description: str) -&gt; str:
    lock = getattr(cli, "_approval_lock", None)
    if lock is None:
        import threading
        cli._approval_lock = threading.Lock()
        lock = cli._approval_lock

    with lock:
        # Choices: once / session / always / deny
        # "view" is added for commands longer than 70 chars so the user
        # can inspect the full command before deciding.
        choices = ["once", "session", "always", "deny"]
        if len(command) &gt; 70:
            choices.append("view")

        cli._approval_state = {
            "command": command,
            "description": description,
            "choices": choices,
            "response_queue": response_queue,
        }
        cli._approval_deadline = _time.monotonic() + timeout

        # Block until user responds or timeout expires
        while True:
            try:
                result = response_queue.get(timeout=1)
                return result  # "once", "session", "always", or "deny"
            except queue.Empty:
                if _time.monotonic() &gt;= cli._approval_deadline:
                    return "deny"  # timeout &#8594; safe default is deny</code></pre><p>The <code>clarify_callback</code> and <code>sudo_password_callback</code> follow the same queue-based blocking pattern for open-ended questions and privilege escalation respectively.</p><h2>4. Side-by-Side Comparison Table</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!uwUJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7bb4da39-6646-41fd-9449-8d884e2d03da_1049x635.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="635" src="https://substackcdn.com/image/fetch/$s_!uwUJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7bb4da39-6646-41fd-9449-8d884e2d03da_1049x635.png" title="Comparison table" width="1049" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p><strong>Use Claude Code hooks when:</strong></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-11-hook-event-driven-automation">
              Read more
          </a>
      </p>