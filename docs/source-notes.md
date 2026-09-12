# Source and adaptation notes

Prepared on 12 September 2026 from the user-supplied material in **SOP BOT Agent Builder Guide**:

- The source Markdown recreation guide attached to that conversation.
- The conversation's requests and written outputs.
- [Original interactive HTML](downloads/SOP_Bot_Agent_Builder_Interactive_Guide.original.html).
- [Original eight-page shareable PDF](downloads/SOP_Bot_Agent_Builder_Shareable_Guide.original.pdf).

Version 1.0.1 adds Josh Harvey creator branding to the supplied HTML and PDF while retaining their reference content. The `.original` filenames remain for existing links; they now mean original-content references, not byte-identical files. [source-original-checksums.json](downloads/source-original-checksums.json) records the unmodified supplied files; [source-checksums.json](downloads/source-checksums.json) verifies the current branded downloads. Their named NHS organisation is original context, not a claim that a new user's instance represents that organisation. The source Markdown contained internal SharePoint and email references; its concepts informed this kit, while private links and the raw conversation were not republished. Linked internal documents were not independently fetched or validated for this release.

## Which version to follow

Use **agent/instructions.txt**, the current Markdown build guide and **docs/index.html** for a new build. The original downloads are snapshots and have known limitations:

- The original HTML's readiness indicator uses acceptance ticks without requiring completed build tasks or passed tests.
- Its introductory progress label claims twelve tasks, but it contains eleven task checkboxes; the current guide adds an explicit capability/scope check as task twelve.
- Its benefit calculator has no separate maintenance field and does not reject out-of-range inputs in its calculation logic.
- Its instructions name a specific organisation and ask for complete-document reading without explicitly handling unreadable or truncated source content.
- The PDF is a compact summary. Its test evidence is in an appendix; it does not reproduce every interactive state or the full acceptance checklist. Its instruction page is densely typeset.

## Changes in the public kit

- Organisation-neutral default with optional local adaptation.
- Explicit handling of inaccessible content and provisional assessments.
- Clear separation between complete reviews, clarity reviews and quick triage.
- Clarified staff multipliers, net maintenance deductions, overlapping benefits and no-positive-payback cases.
- Preserved six recommendations, four effort bands and eight assessment sections.
- Preserved four starter prompts and nine source test themes; added three edge-case tests.
- Added fictional SOPs, a worked assessment and editable operational records.
- Made readiness depend on build tasks, all tests and displayed controls; retained explicit owner validation.
- Added progress export, safe copy fallback and storage failure messaging to the browser guide.

## Official platform references

Checked on 12 September 2026. Microsoft controls feature availability; verify your tenant's interface and entitlements at build time.

| Topic | Primary reference |
| --- | --- |
| Configure fields and test panel | [Build agents](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) |
| Knowledge sources, embedded files and grounding limits | [Add knowledge](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge) |
| Roles, sharing and updates | [Share and manage agents](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents) |
| Eligibility and licensing | [Prerequisites](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites) |

The effort bands, verdict categories and assessment structure come from the supplied SOP Bot material; they are not Microsoft guarantees. The local software checks validate the kit, not the behaviour of an agent in a tenant. No Copilot execution or local organisational approval is claimed for this release.

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](../assets/branding/a-jh-agent-badge.svg)](../assets/branding/README.md)
