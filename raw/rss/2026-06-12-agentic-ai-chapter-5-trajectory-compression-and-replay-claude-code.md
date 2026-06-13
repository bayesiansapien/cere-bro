---
source: farmer/rss
feed: agentic-ai
farmed: 2026-06-13T03:33:50.390237+00:00
title: Chapter 5: Trajectory Compression and Replay (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-5-trajectory-compression
published: 2026-06-12
author: Ken Huang
---

# Chapter 5: Trajectory Compression and Replay (Claude Code vs. Hermes Agent)

<p></p><h2>1. Pattern Summary</h2><p>Trajectory compression and replay is the <em>post-session</em> counterpart to in-flight context management. Once a conversation has finished &#8212; successful or aborted, ten turns or ninety &#8212; the harness still has to do something with the saved record. That record is large, expensive to store at scale, mostly redundant for replay, and usually too long to feed back into a model for fine-tuning or evaluation. Trajectory compression shrinks the saved record on disk; replay reads the compressed JSONL back, reconstructs a chain, and continues, audits, or trains from where the live session left off.</p><p>This pattern is genuinely distinct from in-flight compaction (Chapter 6) and from live observability (Chapter 9). In-flight compaction operates on the <em>active</em> message array inside a running session and has a single goal: keep the next API call under the model's context window. It is reactive, online, and bounded by the threshold ladder. Trajectory compression operates on the <em>saved</em> JSONL after the session has ended &#8212; there is no live context window to fit, no pending API call to unblock; the goal is durability, transferability, and replay fidelity. Live observability (Chapter 9) emits structured events while the agent runs, mostly to logs and SIEM streams; those events are append-only and unaware of each other. Trajectory compression treats the entire conversation as a single artifact, applies turn-level surgery (protect head, protect tail, summarize the middle), and writes a schema-stable JSONL whose every line is self-describing.</p><p>Three operations define the pattern. <strong>Selective field stripping</strong> removes message attributes (parent UUIDs, sidechain markers, REPL wrappers, image attachments) that were useful at runtime but pollute the saved record. <strong>Message-pair grouping</strong> preserves logical units &#8212; a tool<em>use and its tool</em>result must travel together &#8212; so a downstream consumer can never see one without the other. <strong>Schema-stable JSONL export</strong> writes one self-contained JSON object per line with a fixed key set, so the file streams cleanly into HuggingFace datasets, Splunk, or a replay loop without bespoke parsing. Replay is the inverse: read the JSONL, walk the chain backward from the leaf, splice over compaction boundaries, and surface a coherent message sequence to the model or the auditor.</p><p>Before you read on &#8212; two quick announcements. First, you can now get 50% off a yearly subscription and unlock all paid content on Agentic AI, AI Security, and more: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p><p>Second, all previously written 15 Hermes Agent and Claude Code agentic harness design patterns are now available in a single book on Amazon: <a href="https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W">https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W</a></p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!qN3I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64a66b94-328f-480b-971d-4e8bf77971a2_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 5.1: Trajectory compression pipeline" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!qN3I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64a66b94-328f-480b-971d-4e8bf77971a2_1800x1080.png" title="Figure 5.1: Trajectory compression pipeline" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 5.1.</em> Trajectory compression is the post-session counterpart to in-flight context compaction. The pipeline walks a raw transcript through stripping, grouping, and JSONL export so the same artifact can serve resume, training, audit, and archive.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's trajectory layer is the JSONL session file itself: every conversation is persisted as an append-only <code>.jsonl</code> under <code>~/.claude/projects/&lt;project&gt;/&lt;sessionId&gt;.jsonl</code>, and "compression" happens both at write time (selective field stripping) and at read time (byte-level dead-branch excision plus chain reconstruction). The harness writes incrementally during the session and replays the file when the user calls <code>--resume</code> or <code>loadTranscriptFromFile</code>.</p><h3>2.1 Selective field stripping at write time</h3><p>Every call to <code>recordTranscript</code> runs <code>cleanMessagesForLogging</code> first. This is the gate between the live in-memory message array and the on-disk record. Messages that are valuable at runtime but hazardous to persist &#8212; ephemeral progress ticks, training-sensitive attachments &#8212; are dropped before they ever hit disk. Note how the function changes behavior based on <code>getUserType()</code>: external (non-Anthropic) users get an additional REPL-rewriting pass, so shared transcripts contain the underlying Bash/Read calls instead of the wrapper REPL tool.</p><pre><code>// src/utils/sessionStorage.ts (line 4450)
export function cleanMessagesForLogging(
  messages: Message[],
  allMessages: readonly Message[] = messages,
): Transcript {
  const filtered = messages.filter(isLoggableMessage) as Transcript
  return getUserType() !== 'ant'
    ? transformMessagesForExternalTranscript(
        filtered,
        collectReplIds(allMessages),
      )
    : filtered
}</code></pre><p>The filter step is <code>isLoggableMessage</code>. It documents an explicit policy: progress messages never persist (they are UI-only), and most attachments are dropped for non-Anthropic users because they may contain training-sensitive context.</p><pre><code>// src/utils/sessionStorage.ts (line 4351)
export function isLoggableMessage(m: Message): boolean {
  if (m.type === 'progress') return false
  // We deliberately filter out most attachments for non-ants because
  // they have sensitive info for training that we don't want exposed.
  if (m.type === 'attachment' &amp;&amp; getUserType() !== 'ant') {
    if (
      m.attachment.type === 'hook_additional_context' &amp;&amp;
      isEnvTruthy(process.env.CLAUDE_CODE_SAVE_HOOK_ADDITIONAL_CONTEXT)
    ) {
      return true
    }
    return false
  }
  return true
}</code></pre><p>A second stripping function, <code>removeExtraFields</code>, runs when the transcript is exported to consumers. It drops two runtime-only fields &#8212; <code>isSidechain</code> (used to route subagent messages) and <code>parentUuid</code> (used to walk the in-memory chain) &#8212; that have no meaning outside the session.</p><pre><code>// src/utils/sessionStorage.ts (line 1814)
export function removeExtraFields(
  transcript: TranscriptMessage[],
): SerializedMessage[] {
  return transcript.map(m =&gt; {
    const { isSidechain, parentUuid, ...serializedMessage } = m
    return serializedMessage
  })
}</code></pre><p>This is the schema-stabilisation step: the on-disk record always has the same keys regardless of whether the message came from the root agent, a sidechain, or a resumed session.</p><h3>2.2 The append-only JSONL invariant</h3><p>Claude Code writes one JSON object per line and never rewrites earlier lines. This invariant is what makes everything else possible &#8212; replay, chain walks, byte-level filtering, and compaction-boundary handling all rely on parents appearing at earlier file offsets than children. The cost is that every rewind, fork, or compaction leaves dead messages on disk forever; the next two subsections handle that.</p><h3>2.3 Compaction boundaries as replay anchors</h3><p>When in-flight compaction fires, the harness writes a <code>compact_boundary</code> system message into the JSONL with a <code>preservedSegment</code> field recording the head, tail, and anchor UUIDs of the surviving region. On replay, <code>applyPreservedSegmentRelinks</code> walks the JSONL from the latest leaf backward, finds the compaction boundary, and patches the parent pointers so the post-compact chain points at the boundary's anchor instead of the deleted prefix.</p><p>The function deletes everything physically before the absolute-last boundary that isn't part of the preserved segment. This is offline trajectory surgery &#8212; the JSONL stays append-only, but the in-memory replay chain is re-stitched.</p><pre><code>// src/utils/sessionStorage.ts (line 1942)
// Prune everything physically before the absolute-last boundary that
// isn't preserved. preservedUuids empty when !segIsLive &#8594; full prune.
const toDelete: UUID[] = []
for (const [uuid] of messages) {
  const idx = entryIndex.get(uuid)
  if (
    idx !== undefined &amp;&amp;
    idx &lt; absoluteLastBoundaryIdx &amp;&amp;
    !preservedUuids.has(uuid)
  ) {
    toDelete.push(uuid)
  }
}
for (const uuid of toDelete) messages.delete(uuid)</code></pre><p>The append-only write guarantees parents appear at earlier offsets, so this in-memory prune is safe: nothing the surviving chain needs gets dropped.</p><h3>2.4 Byte-level dead-branch excision before parse</h3><p>Sessions accumulate dead branches: every rewind, ctrl-Z, or fork leaves an orphaned chain in the JSONL. Naive replay parses every line and then <code>buildConversationChain</code> discards everything not reachable from the leaf &#8212; but by that point JSON.parse has already paid the cost. The pre-filter operates on raw bytes before <code>parseJSONL</code>, dropping dead lines without parsing them. Measured savings are dramatic on fork-heavy sessions.</p><pre><code>// src/utils/sessionStorage.ts (line 3226-3236)
// Byte-level pre-filter that excises dead fork branches before parseJSONL.
//
// Every rewind/ctrl-z leaves an orphaned chain branch in the append-only
// JSONL forever. buildConversationChain walks parentUuid from the latest
// leaf and discards everything else, but by then parseJSONL has already
// paid to JSON.parse all of it. Measured on fork-heavy sessions:
//
//   41 MB, 99% dead: parseJSONL 56.0 ms -&gt; 3.9 ms (-93%)
//   151 MB, 92% dead: 47.3 ms -&gt; 9.4 ms (-80%)</code></pre><p>This is offline compression in the most literal sense &#8212; bytes that contributed nothing to the live session are excised before they are parsed back into objects.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!C3wx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb0ec1a-e691-4542-bde6-a70bd647defc_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 5.2: Structural vs. semantic compression" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!C3wx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb0ec1a-e691-4542-bde6-a70bd647defc_1800x1080.png" title="Figure 5.2: Structural vs. semantic compression" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 5.2.</em> Claude Code performs structural surgery &#8212; <code>cleanMessagesForLogging</code>, field stripping, and byte-level dead-branch excision &#8212; entirely without LLM calls. Hermes's <code>trajectory_compressor.py</code> instead protects the head and tail and asks a cheap auxiliary model to summarise the compressible middle into a single human turn.</p><h3>2.5 Replay via <code>loadTranscriptFromFile</code></h3><p>Replay is the inverse of write. The function reads either a <code>.jsonl</code> or <code>.json</code> file, builds a UUID-keyed map of messages, and reconstructs the chain backward from the latest leaf using <code>buildConversationChain</code>. The result is a <code>LogOption</code> containing a clean transcript plus all the side-channels (summaries, custom titles, file-history snapshots, attribution snapshots).</p><pre><code>// src/utils/sessionStorage.ts (line 2294)
export async function loadTranscriptFromFile(
  filePath: string,
): Promise&lt;LogOption&gt; {
  if (filePath.endsWith('.jsonl')) {
    const {
      messages, summaries, customTitles, tags,
      fileHistorySnapshots, attributionSnapshots,
      contextCollapseCommits, contextCollapseSnapshot,
      leafUuids, contentReplacements, worktreeStates,
    } = await loadTranscriptFile(filePath)</code></pre><p>After loading, the function picks the most recent leaf and walks backward to build the chain. This is the canonical replay path &#8212; <code>--resume</code> uses it, the log browser uses it, and external transcripts loaded via the SDK use it.</p><pre><code>// src/utils/sessionStorage.ts (line 2316)
    // Find the most recent leaf message using pre-computed leaf UUIDs
    const leafMessage = findLatestMessage(messages.values(), msg =&gt;
      leafUuids.has(msg.uuid),
    )

    if (!leafMessage) {
      throw new Error('No valid conversation chain found in JSONL file')
    }

    // Build the conversation chain backwards from leaf to root
    const transcript = buildConversationChain(messages, leafMessage)</code></pre><p>The leaf-walk is what makes replay deterministic: regardless of how many dead branches the JSONL contains, the chain is exactly the path from the latest live leaf back to the root.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes draws a sharper line between <em>saving</em> a trajectory (<code>agent/trajectory.py</code>) and <em>compressing</em> it post-hoc (<code>trajectory_compressor.py</code>). The save path emits a ShareGPT-format JSONL whose schema is fixed and whose primary downstream consumer is a HuggingFace fine-tuning pipeline. The compressor is a separate batch tool that reads those JSONL files, summarises the middle of each long trajectory through a cheap auxiliary LLM, and writes a <code>_compressed</code> directory whose entries fit a target token budget.</p><h3>3.1 The save path: ShareGPT JSONL</h3><p><code>save_trajectory()</code> is the simplest possible writer. It appends one JSON object per line, routes failed runs to a separate file, and never rewrites. The schema is four fields: the conversation array, a timestamp, the model name, and a completion flag.</p><pre><code># hermes-agent/agent/trajectory.py (line 30)
def save_trajectory(trajectory: List[Dict[str, Any]], model: str,
                    completed: bool, filename: str = None):
    """Append a trajectory entry to a JSONL file."""
    if filename is None:
        filename = "trajectory_samples.jsonl" if completed else "failed_trajectories.jsonl"

    entry = {
        "conversations": trajectory,
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "completed": completed,
    }</code></pre><p>The entry is then written with <code>ensure_ascii=False</code> so non-ASCII characters (model output, foreign-language content) round-trip cleanly, and with a try/except so a failed write logs a warning rather than killing the agent.</p><pre><code># hermes-agent/agent/trajectory.py (line 51)
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.info("Trajectory saved to %s", filename)
    except Exception as e:
        logger.warning("Failed to save trajectory: %s", e)</code></pre><p>This is selective field stripping at the schema boundary: internal Python message objects are converted to ShareGPT format (<code>from</code>/<code>value</code> pairs) and everything that doesn't fit that schema is dropped before the write.</p><p>The conversion itself happens in <code>_convert_to_trajectory_format</code> on the agent. The first preprocessing step is critical for storage cost: image-bearing tool results are replaced with their text summary so trajectories stay text-only.</p><pre><code># run_agent.py (line 4258)
def _convert_to_trajectory_format(self, messages, user_query, completed):
    """Convert internal message format to trajectory format for saving."""
    # Normalize multimodal tool results &#8212; trajectories are text-only, so
    # replace image-bearing tool messages with their text_summary to avoid
    # embedding ~1MB base64 blobs into every saved trajectory.
    messages = [_trajectory_normalize_msg(m) for m in messages]
    trajectory = []</code></pre><p>A 1 MB base64 blob in every conversation would explode the JSONL size for any agent that takes screenshots. Stripping multimodal payloads at the trajectory boundary is the equivalent of Claude Code's progress-message filter.</p><h3>3.2 The compressor: configuration</h3><p><code>trajectory_compressor.py</code> is the smoking gun for the offline pattern. It is a standalone tool &#8212; not part of the agent loop &#8212; that reads completed JSONL files and produces a <code>_compressed/</code> directory of JSONL files that fit a target token budget. The configuration class declares the contract: which turns are protected, what the target budget is, which LLM does the summarisation, and how aggressive the parallelism is.</p><pre><code># hermes-agent/trajectory_compressor.py (line 82)
@dataclass
class CompressionConfig:
    """Configuration for trajectory compression."""
    # Tokenizer
    tokenizer_name: str = "moonshotai/Kimi-K2-Thinking"
    trust_remote_code: bool = True

    # Compression targets
    target_max_tokens: int = 15250
    summary_target_tokens: int = 750</code></pre><p>The protected-turn block is the core policy. The first system, human, GPT, and tool messages are always preserved (they anchor the trajectory's intent), and the last four turns are always preserved (they hold the conclusion). Everything in between is compressible.</p><pre><code># hermes-agent/trajectory_compressor.py (line 93)
    # Protected turns
    protect_first_system: bool = True
    protect_first_human: bool = True
    protect_first_gpt: bool = True
    protect_first_tool: bool = True
    protect_last_n_turns: int = 4

    # Summarization (OpenRouter)
    summarization_model: str = "google/gemini-3-flash-preview"
    base_url: str = OPENROUTER_BASE_URL
    api_key_env: str = "OPENROUTER_API_KEY"
    temperature: float = 0.3</code></pre><p>Cheap, fast summarisation models (Gemini Flash, Kimi) are a deliberate choice &#8212; the goal is throughput across thousands of trajectories, not perfect summary quality.</p><h3>3.3 Finding the protected indices</h3><p><code>_find_protected_indices</code> is a pure function that scans the trajectory once, locates the first occurrence of each role, marks the last N turns as protected, and returns the inclusive bounds of the compressible middle region.</p><pre><code># hermes-agent/trajectory_compressor.py (line 482)
def _find_protected_indices(self, trajectory):
    """Find indices of protected turns."""
    n = len(trajectory)
    protected = set()

    # Track first occurrences
    first_system = first_human = first_gpt = first_tool = None

    for i, turn in enumerate(trajectory):
        role = turn.get("from", "")
        if role == "system" and first_system is None:
            first_system = i
        elif role == "human" and first_human is None:
            first_human = i
        elif role == "gpt" and first_gpt is None:
            first_gpt = i
        elif role == "tool" and first_tool is None:
            first_tool = i</code></pre><p>The "first occurrence" rule is what differentiates this from a naive head-and-tail protection. A trajectory whose system message comes after a few human turns still gets the system message protected; what matters is <em>which roles</em> appear in the head, not their absolute position.</p><p>The second half resolves the compressible region: head-protected indices fall in the first half of the trajectory, tail-protected indices fall in the second half, and the compressible region runs from <code>max(head) + 1</code> to <code>min(tail)</code>.</p><pre><code># hermes-agent/trajectory_compressor.py (line 520)
    # Determine compressible region
    # Start after the last protected head turn
    head_protected = [i for i in protected if i &lt; n // 2]
    tail_protected = [i for i in protected if i &gt;= n // 2]

    compressible_start = max(head_protected) + 1 if head_protected else 0
    compressible_end = min(tail_protected) if tail_protected else n

    return protected, compressible_start, compressible_end</code></pre><p>If the trajectory is short, head and tail protections may overlap and the compressible region collapses to empty &#8212; the compressor will skip the trajectory and emit it unchanged.</p><h3>3.4 The compression algorithm</h3><p><code>compress_trajectory</code> is the heart of the file. It first counts tokens; if the trajectory is already under budget it returns unchanged with <code>skipped_under_target=True</code>. Otherwise it computes how much it needs to save and accumulates compressible turns from the start of the middle region until that target is met.</p><pre><code># hermes-agent/trajectory_compressor.py (line 740)
        # Check if compression needed
        if total_tokens &lt;= self.config.target_max_tokens:
            metrics.skipped_under_target = True
            metrics.compressed_tokens = total_tokens
            metrics.compressed_turns = len(trajectory)
            metrics.compression_ratio = 1.0
            return trajectory, metrics</code></pre><p>The skip path is critical for batch throughput: most short trajectories never need compression, and short-circuiting them saves thousands of API calls per batch.</p><p>The accumulation loop walks the compressible region one turn at a time, summing token counts, and stops as soon as the accumulated savings exceed the target. This is "compress only as much as needed" &#8212; the rest of the middle stays intact, so the model still sees real tool calls and responses after the inserted summary.</p><pre><code># hermes-agent/trajectory_compressor.py (line 759)
        # Calculate how much we need to save
        tokens_to_save = total_tokens - self.config.target_max_tokens

        # Net savings = (sum of N turns' tokens) - summary_target_tokens
        target_tokens_to_compress = tokens_to_save + self.config.summary_target_tokens

        # Accumulate turns from compress_start until we have enough savings
        accumulated_tokens = 0
        compress_until = compress_start

        for i in range(compress_start, compress_end):
            accumulated_tokens += turn_tokens[i]
            compress_until = i + 1  # Exclusive end

            # Check if we have enough savings
            if accumulated_tokens &gt;= target_tokens_to_compress:
                break</code></pre><p>Reassembly is the last step. The protected head is copied through first, with an optional notice appended to the system message warning the model that some prior turns have been summarised.</p><pre><code># hermes-agent/trajectory_compressor.py (line 798)
        # Build compressed trajectory
        compressed = []

        # Add head (turns before compression region)
        for i in range(compress_start):
            turn = trajectory[i].copy()
            # Add notice to system message
            if turn.get("from") == "system" and self.config.add_summary_notice:
                turn["value"] = turn["value"] + self.config.summary_notice_text
            compressed.append(turn)</code></pre><p>The summary then replaces the compressed middle as a single human turn, and the protected tail is copied through unchanged. Inserting the summary as a <code>human</code> turn rather than an assistant turn is deliberate &#8212; the model interprets it as user-provided context rather than its own previous output.</p><pre><code># hermes-agent/trajectory_compressor.py (line 808)
        # Add summary as human message
        compressed.append({
            "from": "human",
            "value": summary
        })

        # Add tail (turns after compression region)
        for i in range(compress_until, len(trajectory)):
            compressed.append(trajectory[i].copy())</code></pre><p>This is a small but important detail for replay: the model continues reasoning from the summary as if a human had pasted it in.</p><h3>3.5 Per-trajectory metrics</h3><p>Every compressed trajectory carries its own metrics record so post-hoc analysis can reconstruct exactly what was stripped and how much was saved. The metrics class is a dataclass with field defaults; the compressor mutates it in place during compression and the result is attached to the JSONL entry as a <code>compression_metrics</code> field if <code>metrics_per_trajectory</code> is enabled.</p><pre><code># hermes-agent/trajectory_compressor.py (line 182)
@dataclass
class TrajectoryMetrics:
    """Metrics for a single trajectory compression."""
    original_tokens: int = 0
    compressed_tokens: int = 0
    tokens_saved: int = 0
    compression_ratio: float = 1.0

    original_turns: int = 0
    compressed_turns: int = 0
    turns_removed: int = 0

    turns_compressed_start_idx: int = -1
    turns_compressed_end_idx: int = -1
    turns_in_compressed_region: int = 0

    was_compressed: bool = False
    still_over_limit: bool = False
    skipped_under_target: bool = False</code></pre><p>This is the auditability surface. A compliance reviewer reading a compressed JSONL can see exactly which turns were compressed (<code>turns_compressed_start_idx</code>/<code>_end_idx</code>), how many tokens were saved, and whether the trajectory still exceeds the target after compression.</p><h3>3.6 Async batch processing</h3><p>The compressor is built for throughput. <code>_process_directory_async</code> loads every JSONL file in the input directory, fans out one async task per entry, and uses an <code>asyncio.Semaphore</code> to cap concurrent API calls.</p><pre><code># hermes-agent/trajectory_compressor.py (line 1030)
        # Create semaphore for rate limiting
        semaphore = asyncio.Semaphore(self.config.max_concurrent_requests)

        # Tracking for progress display (thread-safe with lock)
        progress_lock = asyncio.Lock()
        compressed_count = 0
        skipped_count = 0
        api_calls = 0
        in_flight = 0

        # Results storage: {file_path: {entry_idx: (processed_entry, metrics)}}
        results = {f: {} for f in jsonl_files}</code></pre><p>Each entry is processed under the semaphore, with a per-trajectory timeout that defaults to five minutes. Trajectories that time out are marked failed but don't abort the batch &#8212; the runner advances to the next entry.</p><pre><code># hermes-agent/trajectory_compressor.py (line 1056)
                try:
                    # Apply per-trajectory timeout
                    processed_entry, metrics = await asyncio.wait_for(
                        self.process_entry_async(entry),
                        timeout=self.config.per_trajectory_timeout
                    )
                    results[file_path][entry_idx] = (processed_entry, metrics)</code></pre><p>After all tasks complete, results are written back per file in original order so the compressed JSONL preserves entry ordering &#8212; a property HuggingFace dataset loaders rely on.</p><h2>4. Side-by-Side Comparison</h2><p>The two systems answer the same question &#8212; <em>what does the saved record look like, and how do we replay it?</em> &#8212; but they answer it from opposite sides of the agent lifecycle.</p><p>Claude Code embeds trajectory work into the harness itself. Every message is funnelled through <code>cleanMessagesForLogging</code> before it lands on disk, so the JSONL is the single source of truth from the moment the session starts. Compaction boundaries are written inline as system messages with <code>preservedSegment</code> metadata, so replay can splice over them without external state. The append-only invariant is a hard architectural commitment: the file grows monotonically, dead branches stay on disk, and a byte-level pre-filter excises them at load time. Replay is first-class &#8212; <code>loadTranscriptFromFile</code> is the same code path as <code>--resume</code>, so the same JSONL serves both production resume and offline audit.</p><p>Hermes draws a hard line between save and compress. <code>save_trajectory()</code> in <code>agent/trajectory.py</code> is fewer than thirty lines; it appends one ShareGPT entry per session and goes home. The heavy lifting lives in <code>trajectory_compressor.py</code>, a standalone batch tool that reads completed JSONL files post-hoc and emits a <code>_compressed/</code> directory. This separation is what enables Hermes's primary use case: generating training data for fine-tuning. A Hermes shop typically runs the agent against thousands of prompts, accumulates raw trajectories overnight, and runs the compressor in the morning to fit each one inside the target context window of the next training run.</p><p>The compression strategies differ in kind, not degree. Claude Code performs <em>structural</em> compression &#8212; it strips fields, drops progress messages, excises dead branches, and prunes pre-compact prefixes. There is no LLM call in the compression path; everything is deterministic surgery. Hermes performs <em>semantic</em> compression &#8212; it identifies the compressible middle, sums tokens until the savings target is met, and calls a cheap auxiliary LLM (Gemini Flash, Kimi) to summarise that middle into a single human turn. The trade-off is direct: Claude Code's compression is free and lossless within the chain it preserves; Hermes's compression costs API calls but achieves higher ratios because it can collapse twenty turns of routine tool calls into a 750-token summary.</p><p>Replay also differs. Claude Code's replay is <em>operational</em> &#8212; the JSONL is loaded back into the active QueryEngine, parent UUIDs are walked, compaction boundaries are spliced, and the session resumes mid-flight. Hermes's compressed trajectories are usually <em>consumed</em>, not resumed: they feed a fine-tuning loop or an evaluation harness, where the conversation is replayed turn-by-turn against a new model rather than continued. The schema-stable JSONL is the contract; the consumer chooses what to do with it.</p><p>A final asymmetry is metrics. Claude Code's per-message metadata is rich &#8212; usage tokens, tool-use IDs, parent UUIDs, sidechain markers, custom titles, file history snapshots &#8212; and most of it is preserved through the JSONL for replay fidelity. Hermes attaches a compact <code>compression_metrics</code> block (original tokens, compressed tokens, tokens saved, compression ratio, indices of the compressed region) to every compressed entry. The Claude Code metadata is for <em>resuming the session</em>; the Hermes metadata is for <em>auditing the compression decision</em>.</p><h2>5. When to Use Which</h2><p>Use Claude Code's approach when the saved trajectory needs to support production resume. The append-only JSONL with inline compaction boundaries is the right design when a user might <code>--resume</code> a session days later, fork it, rewind it, or hand it off between agents. The byte-level dead-branch pre-filter is what makes 150 MB session files load in under 10 ms &#8212; a property you cannot easily retrofit if you start with a less disciplined format. If your harness is interactive, long-lived, and rewind-heavy, the Claude Code design pays for its complexity many times over.</p><p>Use Hermes's approach when the saved trajectory is primarily a <em>training artifact</em> or an <em>audit record</em>. The ShareGPT format is immediately consumable by HuggingFace dataset loaders, the per-trajectory timeout makes batch processing robust to misbehaving entries, and the post-hoc compressor lets you target any context window &#8212; 16K for a small open-source model, 200K for Claude &#8212; without changing the agent. The <code>_compressed/</code> output directory pattern is a clean separation: the raw JSONL is the source of truth, the compressed JSONL is a derived artifact that can be regenerated whenever the target budget changes.</p><p>The hybrid is straightforward. Use Claude Code's selective field stripping and compaction-boundary patterns at write time so the on-disk record stays clean and replay-safe. Layer Hermes's offline compressor on top as a separate batch step that reads the JSONL and produces a <code>_compressed/</code> variant for training and long-term archive. The two approaches operate on different timescales &#8212; Claude Code at every turn, Hermes after the session ends &#8212; so they compose without conflict. The one rule that must hold across both: the JSONL line schema must be stable. Once you have downstream consumers depending on the field set, schema drift will cost you more than any compression algorithm will save.</p><h2>6. Defensive Cyber Agent Application</h2><p>A 90-iteration threat-hunt trajectory is the canonical compression target for a defensive cyber agent. The session opens with an alert (the IOC anchor), runs through dozens of routine recon tool calls (port scans, DNS lookups, log greps), dwells in the middle on confirmation pivots, and closes with a remediation decision. The full JSONL is multiple megabytes; the audit record needs to be small enough to attach to a SIEM ticket, fast to grep, and annotated with the MITRE ATT&amp;CK techniques each tool call exercised.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!oiuA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81e21ac6-2ef6-48b2-9401-5213b0758bef_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 5.3: Threat-hunt trajectory compression with MITRE TTPs" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!oiuA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81e21ac6-2ef6-48b2-9401-5213b0758bef_1800x1080.png" title="Figure 5.3: Threat-hunt trajectory compression with MITRE TTPs" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 5.3.</em> A 90-iteration threat hunt compresses from ~180,000 tokens to ~8,000 tokens by preserving the IOC alert verbatim, summarising the recon middle into a single human turn, keeping the last six remediation turns intact, and tagging every surviving tool call with its MITRE ATT&amp;CK technique.</p><p>The pattern is offline trajectory work: compress after the hunt is over, preserve the alert and the remediation verbatim, summarise the recon middle, and tag every surviving turn with its MITRE TTP. The schema is fixed so any compliance reviewer or downstream training pipeline can consume it without bespoke parsing.</p><p>The configuration class carries the cyber-specific knobs. The header declares the imports and the token budget &#8212; small enough to attach the compressed trajectory to a SIEM ticket without truncation.</p><pre><code># cyber_threat_hunt_compressor.py
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import json
from datetime import datetime, timezone


@dataclass
class CyberCompressionConfig:
    """Compression policy for a defensive cyber threat-hunt trajectory."""

    # Token target &#8212; small enough to attach to a SIEM ticket
    target_max_tokens: int = 8_000
    summary_target_tokens: int = 600</code></pre><p>The protection knobs declare the IOC turn and the last six remediation turns as non-negotiable. The TTP map is the cyber-specific addition &#8212; it routes every tool call to its MITRE ATT&amp;CK technique so the compressed record is annotated for compliance review.</p><pre><code>    # Always preserve verbatim &#8212; the IOC anchor and remediation tail
    protect_alert_turn: bool = True
    protect_last_remediation_turns: int = 6

    # MITRE ATT&amp;CK annotation &#8212; per-tool TTP mapping
    tool_to_ttp: Dict[str, str] = field(default_factory=lambda: {
        "port_scan":     "T1046 &#8212; Network Service Discovery",
        "dns_lookup":    "T1018 &#8212; Remote System Discovery",
        "process_list":  "T1057 &#8212; Process Discovery",
        "isolate_host":  "M1030 &#8212; Network Segmentation",
        "kill_process":  "M1040 &#8212; Behavior Prevention on Endpoint",
    })</code></pre><p>The annotation step runs first. Every surviving turn is enriched with its MITRE TTP code, so the compressed JSONL is a SIEM-friendly audit record without any post-processing.</p><pre><code>def annotate_with_ttp(
    trajectory: List[Dict[str, Any]],
    config: CyberCompressionConfig,
) -&gt; List[Dict[str, Any]]:
    """Tag each tool turn with its MITRE ATT&amp;CK technique."""
    annotated = []
    for turn in trajectory:
        annotated_turn = turn.copy()
        if turn.get("from") == "tool":
            tool_name = turn.get("tool_name", "")
            ttp = config.tool_to_ttp.get(tool_name)
            if ttp:
                annotated_turn["ttp"] = ttp
        annotated.append(annotated_turn)
    return annotated</code></pre><p>Next, the protection logic identifies the IOC turn (the first user message that contains an IOC marker) and reserves the last N turns as the remediation block.</p><pre><code>def find_protected_indices(
    trajectory: List[Dict[str, Any]],
    config: CyberCompressionConfig,
) -&gt; tuple[int, int, int]:
    """Return (alert_idx, compress_start, compress_end)."""
    n = len(trajectory)

    # The IOC anchor is the first human turn whose value contains an IOC marker
    alert_idx = -1
    for i, turn in enumerate(trajectory):
        if turn.get("from") == "human" and "[IOC]" in turn.get("value", ""):
            alert_idx = i
            break

    # Compressible region: after the alert, before the remediation tail
    compress_start = alert_idx + 1 if alert_idx &gt;= 0 else 0
    compress_end = max(compress_start, n - config.protect_last_remediation_turns)
    return alert_idx, compress_start, compress_end</code></pre><p>The summary itself is generated by a cheap auxiliary model. The first step builds bullets &#8212; one per turn &#8212; that include the role, TTP annotation, and a 300-character snippet. The bullet form is what makes the summary structured rather than free-form.</p><pre><code>def summarize_recon_middle(
    middle_turns: List[Dict[str, Any]],
    summarizer_fn,  # callable: str -&gt; str
    target_tokens: int,
) -&gt; str:
    """Produce a SIEM-ready narrative summary of the recon middle."""
    bullets = []
    for turn in middle_turns:
        role = turn.get("from", "")
        ttp = turn.get("ttp", "")
        snippet = turn.get("value", "")[:300]
        bullets.append(f"[{role}{' / ' + ttp if ttp else ''}] {snippet}")</code></pre><p>The prompt is shaped to emit SIEM-narrative style &#8212; observation, evidence, implication &#8212; rather than a free-form chat summary. The output is prefixed with <code>[RECON SUMMARY]</code> so any downstream consumer can trivially distinguish summarised turns from real ones.</p><pre><code>    prompt = (
        f"Summarize the following recon turns from a threat hunt. Target "
        f"~{target_tokens} tokens. Emit findings in SIEM-narrative style "
        f"(observation -&gt; evidence -&gt; implication). Tag each finding with "
        f"its MITRE TTP if present.\n\n" + "\n".join(bullets)
    )
    summary_text = summarizer_fn(prompt)
    return f"[RECON SUMMARY] {summary_text.strip()}"</code></pre><p>The reassembly step puts the pieces back together. The function first runs annotation and protection-index discovery, then preserves the alert anchor &#8212; everything up to and including the IOC turn is copied through verbatim.</p><pre><code>def compress_threat_hunt(
    trajectory: List[Dict[str, Any]],
    config: CyberCompressionConfig,
    summarizer_fn,
) -&gt; Dict[str, Any]:
    """Compress a threat-hunt trajectory into a SIEM-attachable JSONL entry."""
    annotated = annotate_with_ttp(trajectory, config)
    alert_idx, c_start, c_end = find_protected_indices(annotated, config)

    compressed: List[Dict[str, Any]] = []

    # Preserve everything up to and including the alert
    if alert_idx &gt;= 0:
        compressed.extend(annotated[: alert_idx + 1])
    elif c_start &gt; 0:
        compressed.extend(annotated[:c_start])</code></pre><p>The recon middle is then summarised into a single human turn and the remediation tail is appended verbatim. The result is a single JSONL-ready dict with the conversations array, a timestamp, and a <code>compression_metrics</code> block for audit traceability.</p><pre><code>    # Compress the recon middle
    middle = annotated[c_start:c_end]
    if middle:
        summary = summarize_recon_middle(
            middle, summarizer_fn, config.summary_target_tokens,
        )
        compressed.append({"from": "human", "value": summary})

    # Preserve the remediation tail verbatim
    compressed.extend(annotated[c_end:])
    return {
        "conversations": compressed,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "compression_metrics": {
            "original_turns": len(trajectory),
            "compressed_turns": len(compressed),
            "alert_idx": alert_idx,
            "compressed_region": [c_start, c_end],
        },
    }</code></pre><p>The replay path is the inverse and equally simple: read the JSONL, walk the conversations array, and surface each turn with its TTP annotation to the auditor or to a downstream training run. Because the schema is stable &#8212; three top-level keys, a known turn structure &#8212; the replay code does not need to know whether the trajectory was compressed or not.</p><pre><code>def replay_compressed_trajectory(
    jsonl_path: str,
):
    """Stream compressed threat-hunt trajectories one entry at a time."""
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            yield {
                "timestamp": entry["timestamp"],
                "alert_idx": entry.get("compression_metrics", {}).get("alert_idx", -1),
                "turns": entry["conversations"],
            }</code></pre><p>What this design encodes is the cyber audit contract: the alert is non-negotiable, the remediation is non-negotiable, the recon is summarisable but must be MITRE-tagged, and the JSONL line schema is stable. A 90-iteration threat hunt that originally consumed 180,000 tokens compresses to roughly 8,000 tokens &#8212; small enough to attach to a Splunk ticket &#8212; without losing the IOC anchor, the remediation decisions, or the TTP coverage record. That is the offline trajectory pattern in its sharpest form: take a long live session, surgically reduce it to its load-bearing turns plus a structured summary, and emit a schema-stable artifact that any downstream tool can consume without bespoke parsing.</p><p><strong>For paid subscribers &#8212; a hands-on deep dive continues below.</strong></p><p>Everything up to this point is free. The <strong>Going Deeper</strong> section that follows is available to paid subscribers only. It adds three things the reviewers asked for: (1) a <strong>concrete, runnable worked example</strong> with real code from the Claude Code and Hermes repositories; (2) a <strong>comparison of this pattern against MCP, A2A, and adjacent architectures</strong>, showing how and why this approach differs; and (3) <strong>project-driven Claude Code exercises</strong> &#8212; hands-on assignments you can build in realistic scenarios.</p><p>You can unlock this section &#8212; and every paid deep-dive across the whole Agentic AI and AI Security series &#8212; at 50% off a yearly subscription here: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-5-trajectory-compression">
              Read more
          </a>
      </p>
