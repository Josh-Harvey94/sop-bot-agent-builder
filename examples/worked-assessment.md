# Worked assessment: routine office equipment requests

**Fictional, hand-authored example. This is not a recorded Copilot response or measured pilot result.**

Source: [administrative-request.txt](administrative-request.txt), version 0.1, all eight numbered steps. The separately referenced purchasing and retention procedures are unavailable. This assessment is provisional and limited to administrative capture, acknowledgement and reminders; those missing procedures must be checked before an implementation touching them.

## 1. Overall verdict

**PILOT** one combined administrative-support opportunity, after resolving the documentation gaps and confirming feasibility. The final manager decision remains human-led.

For illustration, assume 16 technical build hours, 40 cases per active week, 46 active weeks, one coordinator, five gross avoidable minutes per case, 70% realisation and 12 annual support hours. That gives **95.3 net staff hours per year**, **7.94 average monthly hours** and about **2.0 months build-only payback**. Confidence is **Low** until those assumptions and technical dependencies are verified. The licence, permissions and full one-off delivery effort are unconfirmed.

## 2. What the SOP does

An emailed request starts a standard office-equipment process. Business support checks and records it, a manager decides, and the requester receives an outcome. The shared mailbox and Excel tracker support administration. Purchasing follows another controlled procedure; the SOP delegates no purchase authority to automation.

## 3. Current process

| Step | Activity | Responsible role | System/document | Manual or supported | Issue | Automation potential |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Receive request | Requester / coordinator | Shared mailbox | Manual email | Variable completeness | Structured capture |
| 2 | Check fields and request missing information | Coordinator | Email | Manual | Exceptions create chasing | Field validation; human exception handling |
| 3 | Copy details and assign reference | Coordinator | Excel tracker | Manual | Duplicate entry | Record creation after validation |
| 4 | Acknowledge request | Coordinator | Email | Manual | Repetitive message | Template acknowledgement |
| 5 | Decide need and budget | Business Support Manager | Request record | Human decision | Absence cover undefined | Assemble information; retain decision |
| 6 | Review open cases and chase | Coordinator / manager | Tracker and email | Manual | Repeated checks | Bounded reminders; exceptions retained |
| 7 | Record decision and inform requester | Coordinator | Tracker and email | Manual | Decision provenance matters | Draft or send confirmed outcome under controls |
| 8 | Close record | Coordinator | Tracker | Manual | Separate retention policy | Status update subject to policy |

## 4. SOP improvements

The source itself identifies missing manager cover, acknowledgement timing and duplicate-request handling. It also references unavailable purchasing and retention procedures.

Suggested draft wording for owner review: “The coordinator sends an acknowledgement within the locally agreed target, checks for an existing open request before creating a new record, and routes decisions to the designated deputy when the manager is unavailable.” The target, duplicate-matching rule and deputy must be specified by the owner. They are not established facts.

## 5. Automation opportunities

**Opportunity 1: a single request administration workflow.**

| Assessment field | Advisory finding |
| --- | --- |
| Problem | Repeated copying, acknowledgement and chasing across mailbox and tracker |
| Proposed improvement | Structured request capture feeding a controlled tracker and acknowledgements/reminders |
| Candidate technology | Forms, SharePoint and Power Automate, with Outlook or Teams for messages |
| Effort | Small; illustrative 16 technical hours, within 1–3 days if a day is 8 hours |
| Calendar considerations | Owner availability, exceptions, source design, permission/licensing checks, testing and training |
| Capacity | 2.33 realised hours per active week before annual support; 95.33 net annual hours; 7.94 average net monthly hours |
| Calculation | 5 × 40 × 1 ÷ 60 × 46 × 0.70 − 12 = 95.33 net annual hours |
| Assumptions | All numerical inputs above are illustrative; no local measurement is claimed |
| Human activity retained | Budget/need decision, unusual requests, missing information, exception resolution and review of output |
| Risks/dependencies | Duplicate records, incorrect recipients, missing fields, permissions and manual fallback |
| Possible reviews | Process owner and digital/Power Platform team; data/records and other review where locally relevant |
| Confidence | Low until measured and technically validated |
| Recommendation | PILOT one bounded workflow after process clarification and local review |

This appears technically possible, but local licensing, permissions and governance must be confirmed.

## 6. What should remain human-led

The manager decides need and budget. An authorised person resolves unusual requests and missing context. The process owner approves changes to the SOP, confirms retention/purchasing dependencies and decides whether the pilot should proceed.

## 7. Overall benefit

Treat capture, copying and reminders as one combined opportunity. The five minutes already represent their combined potential saving, so do not add another five minutes for each feature. Maintenance is deducted once after the 70% realisation factor, which covers retained checks, exceptions and adoption.

Build-only payback is 16 ÷ (95.33 ÷ 12) = about 2.0 months. At 40% and 90% realisation, net annual capacity would be about 49.3 and 126 hours; build-only payback would be about 3.9 and 1.5 months. All scenarios exclude other one-off discovery, governance, testing and training hours and monetary costs. Full implementation payback will differ. No cash saving is established.

## 8. Recommended next step

Have the process owner validate the process gaps and time baseline with the intended coordinator, then take the single administrative workflow to the local digital team for a bounded feasibility and pilot decision. Keep the existing manual route available.

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](../assets/branding/a-jh-agent-badge.svg)](../assets/branding/README.md)
