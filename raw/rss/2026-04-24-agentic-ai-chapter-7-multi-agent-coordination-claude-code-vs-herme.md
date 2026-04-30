---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 7: Multi-Agent Coordination (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-7-multi-agent-coordination
published: 2026-04-24
author: Ken Huang
---

# Chapter 7: Multi-Agent Coordination (Claude Code vs. Hermes Agent)

<p></p><h2>1. Pattern Summary</h2><p>Multi-agent coordination is how complex tasks escape the single-context trap. One agent has one context window, one model, and one thread of execution &#8212; that ceiling is real. Multi-agent systems break it by decomposing work into parallel streams, assigning specialized roles, and isolating execution environments so agents can't corrupt each other's state. The pattern matters because the hardest real-world tasks &#8212; incident response, large-scale code refactors, competitive research &#8212; are inherently parallel and inherently risky to run in a single shared context.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's <code>AgentTool</code> is the orchestration hub. It supports five distinct execution modes, each solving a different coordination problem:</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!8uPC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c0c5898-5177-4dc2-bfe2-5e34be62a93b_588x277.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="277" src="https://substackcdn.com/image/fetch/$s_!8uPC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c0c5898-5177-4dc2-bfe2-5e34be62a93b_588x277.png" title="Comparison table" width="588" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><strong>Fork subagents and prompt cache sharing.</strong> The fork path is the most cache-efficient mode. When a fork agent is spawned, the parent's already-rendered system prompt is passed directly to the child:</p><pre><code>// src/tools/AgentTool/AgentTool.tsx
// Fork path: pass parent's rendered system prompt to child so the API
// sees identical bytes and can reuse the cached KV computation.
if (isForkPath) {
  if (toolUseContext.renderedSystemPrompt) {
    forkParentSystemPrompt = toolUseContext.renderedSystemPrompt
  } else {
    // Fallback: recompute &#8212; may diverge from parent's cached bytes
    forkParentSystemPrompt = buildEffectiveSystemPrompt({ ... })
  }
  promptMessages = buildForkedMessages(prompt, assistantMessage)
}</code></pre><p>The child also receives <code>useExactTools: true</code>, meaning it gets the parent's exact tool array rather than a filtered subset. This is what makes fork agents feel like continuations of the parent rather than fresh agents.</p><p><strong>Worktree isolation.</strong> When <code>isolation: 'worktree'</code> is set, the agent gets its own git worktree &#8212; a separate filesystem branch that can't contaminate the parent's working tree:</p><pre><code>// Create a git worktree scoped to this agent's ID
if (effectiveIsolation === 'worktree') {
  const slug = `agent-${earlyAgentId.slice(0, 8)}`
  worktreeInfo = await createAgentWorktree(slug)
}

// After completion: keep worktree only if it has changes
const changed = await hasWorktreeChanges(worktreePath, headCommit)
if (!changed) {
  await removeAgentWorktree(worktreePath, worktreeBranch, gitRoot)
}</code></pre><p><strong>Async backgrounding mid-execution.</strong> A sync agent can be promoted to background while it's running. The parent races the agent's iterator against a background signal:</p><pre><code>// Race: next agent message vs. user-triggered background promotion
const raceResult = backgroundPromise
  ? await Promise.race([
      nextMessagePromise.then(r =&gt; ({ type: 'message', result: r })),
      backgroundPromise  // resolves if user clicks "send to background"
    ])
  : { type: 'message', result: await nextMessagePromise }</code></pre><p><strong>SendMessage routing.</strong> Named agents are registered in a global name registry so any agent can address them by name:</p><pre><code>// Register name &#8594; agentId so SendMessage can route to this agent
if (name) {
  rootSetAppState(prev =&gt; {
    const next = new Map(prev.agentNameRegistry)
    next.set(name, asAgentId(asyncAgentId))
    return { ...prev, agentNameRegistry: next }
  })
}</code></pre><p><strong>Teammate constraints.</strong> Teams are flat &#8212; a teammate cannot spawn other teammates, and in-process teammates cannot spawn background agents. This prevents unbounded nesting:</p><pre><code>// Flat roster enforcement: teammates cannot spawn teammates
if (isTeammate() &amp;&amp; teamName &amp;&amp; name) {
  throw new Error('Teammates cannot spawn other teammates &#8212; the team roster is flat.')
}</code></pre><h2>3. Hermes Agent Implementation</h2><p>Hermes takes a Python-native approach: child agents are full <code>AIAgent</code> instances constructed on the main thread and run in a <code>ThreadPoolExecutor</code>. The key files are <code>delegate_tool.py</code> (single and batch delegation) and <code>mixture_of_agents_tool.py</code> (parallel model aggregation).</p><p><strong>`_run_single_child()` &#8212; the execution unit.</strong> Each child runs <code>run_conversation()</code> in its own thread and returns a structured result dict:</p><pre><code># hermes-agent/tools/delegate_tool.py
def _run_single_child(task_index, goal, child=None, parent_agent=None, **_kwargs):
    # Each child is a full AIAgent with its own iteration budget.
    # The parent blocks on this thread until the child's run_conversation() returns.
    child_start = time.monotonic()
    try:
        result = child.run_conversation(user_message=goal)
        summary = result.get("final_response") or ""
        # Status is derived from the child's exit condition, not just completion
        status = "interrupted" if result.get("interrupted") else (
            "completed" if summary else "failed"
        )
        return {
            "task_index": task_index,
            "status": status,
            "summary": summary,
            "exit_reason": "completed" if result.get("completed") else "max_iterations",
            "tokens": {
                "input": getattr(child, "session_prompt_tokens", 0),
                "output": getattr(child, "session_completion_tokens", 0),
            },
        }
    finally:
        # Always unregister child from interrupt propagation list
        if hasattr(parent_agent, '_active_children'):
            with parent_agent._active_children_lock:
                parent_agent._active_children.remove(child)</code></pre><p><strong>`_active_children` &#8212; interrupt propagation.</strong> The parent maintains a list of all running children. When the parent receives an interrupt, it propagates to every child:</p><pre><code># hermes-agent/run_agent.py
# Initialized in AIAgent.__init__:
self._delegate_depth = 0        # 0 = top-level; incremented per child generation
self._active_children = []      # All currently running child AIAgents
self._active_children_lock = threading.Lock()

# In AIAgent.interrupt():
with self._active_children_lock:
    children_copy = list(self._active_children)
for child in children_copy:
    try:
        child.interrupt(message)  # Cascade interrupt down the tree
    except Exception as e:
        logger.debug("Failed to propagate interrupt to child agent: %s", e)</code></pre><p><strong>`_delegate_depth` &#8212; infinite delegation guard.</strong> Children cannot spawn grandchildren beyond <code>MAX_DEPTH = 2</code>:</p><pre><code># hermes-agent/tools/delegate_tool.py
MAX_DEPTH = 2  # parent(0) -&gt; child(1) -&gt; grandchild rejected(2)

depth = getattr(parent_agent, '_delegate_depth', 0)
if depth &gt;= MAX_DEPTH:
    return json.dumps({"error": "Delegation depth limit reached. Subagents cannot spawn further subagents."})

# When building a child, increment its depth
child._delegate_depth = getattr(parent_agent, '_delegate_depth', 0) + 1</code></pre><p><strong>Batch parallel execution.</strong> Multiple tasks run concurrently via <code>ThreadPoolExecutor</code>, capped at <code>MAX_CONCURRENT_CHILDREN = 3</code>:</p><pre><code># hermes-agent/tools/delegate_tool.py
# Batch mode: submit all children to the thread pool, collect as they complete
with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_CHILDREN) as executor:
    futures = {
        executor.submit(_run_single_child, i, t["goal"], child, parent_agent): i
        for i, t, child in children
    }
    for future in as_completed(futures):
        entry = future.result()
        results.append(entry)
        # Print per-task completion line above the spinner in real time
        icon = "&#10003;" if entry["status"] == "completed" else "&#10007;"
        spinner_ref.print_above(f"{icon} [{entry['task_index']+1}/{n_tasks}] ...")</code></pre><p><strong>`mixture_of_agents_tool.py` &#8212; parallel model aggregation.</strong> This is a different coordination pattern: instead of delegating tasks to specialized agents, it fans out the same query to multiple frontier models and aggregates the results:</p><pre><code># hermes-agent/tools/mixture_of_agents_tool.py
# Layer 1: Query all reference models in parallel using asyncio.gather
# Temperature 0.6 encourages diverse perspectives across models
model_results = await asyncio.gather(*[
    _run_reference_model_safe(model, user_prompt, REFERENCE_TEMPERATURE)
    for model in ref_models  # claude-opus-4.6, gemini-3-pro, gpt-5.4-pro, deepseek-v3.2
])

# Layer 2: Aggregator synthesizes the successful responses into one answer
# Temperature 0.4 keeps the synthesis focused and consistent
aggregator_system_prompt = _construct_aggregator_prompt(
    AGGREGATOR_SYSTEM_PROMPT,
    [content for _, content, success in model_results if success]
)
final_response = await _run_aggregator_model(aggregator_system_prompt, user_prompt)</code></pre><p><strong>Terminal backends.</strong> Hermes children can execute in six different environments depending on the <code>platform</code> parameter: local shell, Docker container, SSH remote, Modal serverless, Daytona workspace, or Singularity container. This is configured at the <code>AIAgent</code> level and inherited by children.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!vO29!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff72fd58-14ec-4b04-9f44-1dfbdbec76bb_1057x515.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="515" src="https://substackcdn.com/image/fetch/$s_!vO29!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff72fd58-14ec-4b04-9f44-1dfbdbec76bb_1057x515.png" title="Comparison table" width="1057" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-7-multi-agent-coordination">
              Read more
          </a>
      </p>