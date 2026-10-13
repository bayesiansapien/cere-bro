# Building AIE: Open Q&A and Feedback Session with swyx

**Channel:** AI Engineer
**Published:** 2026-10-12 (recorded at AI Engineer World's Fair, Moscone West, June 29 to July 2, 2026)
**Source:** https://www.youtube.com/watch?v=snTZtttfL70

## TL;DR
An attendee feedback session on running the AI Engineer World's Fair. Almost no technical content. The signal: AIE is freezing World's Fair size (same Moscone venue and week in 2027, optimize instead of grow), expanding geographically via a TED/TEDx-style partner model (~40 countries queued, Bangalore likely first in India), scaling up academic poster sessions via a partnership with the ACM CAIS (agentic systems) conference, and replacing its vendor mobile app with an in-house web app built on the open session data (JSON, MCP, CLI) it already publishes. swyx's stated filter for content is "would you use it at work," which is why AI x-risk gets no track.

## Key Takeaways
- **Scale:** ~2,200 speaker applications for ~300 slots (CFP plus invites). swyx says ~7,000 attendees; press coverage reported 6,000+ across ~29 tracks. All sessions are recorded and posted to YouTube with per-track playlists.
- **How talks get selected:** applications are not blind. Reviewers (swyx plus trusted past speakers) watch prior recorded talks. Best lever for an unknown team: submit recordings of earlier talks, even low-view meetup ones, to prove you deliver "a banger." Slots skew to proprietary-model companies and recognizable names, then a few bets.
- **Format philosophy:** World's Fair is deliberately multi-track and expo-heavy. Single-track content lives at the smaller Summits. Talks are compressed to ~20 minutes because YouTube attention spans favor it. Longer 45 to 60 minute GDC-style deep dives exist in a dedicated workshop room each day.
- **Academic bridge:** AIE positions itself as anti-NeurIPS/ICLR (no submission cutoff six months out). It outsourced poster selection to CAIS this year. Not being an accredited venue is a feature: researchers can present already-published work to an industry audience without violating exclusivity rules. swyx floated a peer-reviewed journal in the long term.
- **Safety stance:** no x-risk track. swyx (self-described "a bit of a doomer") argues real-world frontier evals such as Andon Labs' Vending-Bench surface more concrete alignment failures than abstract x-risk discussion.
- **Upcoming:** AIE New York with a finance focus (October 12 to 14, 2026), plus partner events in Miami, Melbourne, Sydney, Paris, Singapore, and Shanghai (still TBD, slipped twice). A leadership-only retreat with an unconference format is being considered.
- **Ops failures acknowledged:** Monday workshop rooms overflowed with no pre-registration, attendee Wi-Fi was congested (separate speaker and sponsor networks existed), and the third-party app crashed and failed to sync with the web.

## Architecture & Optimization Mechanics
Not applicable as engineering content. The relevant mechanics are conference-as-information-pipeline:
- **Open data as UI strategy:** the schedule is published as JSON with MCP and CLI access, so attendees can vibe-code their own client. One attendee had Opus build an auto-touring talk browser. That is the "API is the UI" pattern applied to an event.
- **Leadership matching prototype:** organizers ran deep-research agents on each leadership-track attendee to build a "facebook" for intros. swyx says matching works where in-app chat never has.

## Grounded Context (Web Enrichment)
The World's Fair 2026 ran June 29 to July 2 at Moscone West. Contemporary coverage cited 6,000+ attendees, ~300 speakers, and ~29 tracks spanning agents, evals, retrieval, inference optimization, context engineering, and robotics/world models, so swyx's "7,000" is a rounded-up internal figure. The New York event he previewed is confirmed on ai.engineer for October 12 to 14, 2026, with a call for speakers aimed at banking, hedge funds, private equity, insurance, payments, and compliance, alongside non-finance coding, eval, and infra tracks. This video's publish date coincides with that event's opening. I could not independently verify the CAIS poster partnership details or the 2027 "no growth" commitment beyond this session.

## Real-World Application / Actionable Step
- **To speak at AIE 2027:** record a 20 minute talk on routing or compression results at a local meetup or internal venue now, and attach it to the CFP. Frame it against a broad trend (inference cost per token, agent token demand) rather than a narrow technique.
- **Use the poster track for papers.** Already-published compression or routing work can be presented without exclusivity conflicts, and the audience is hiring-heavy industry engineers.
- **Mine the archive instead of attending live.** Pull the inference and evals track playlists and route them through this wiki pipeline. That is higher signal per hour than attending the multi-track floor.
