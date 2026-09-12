# Josh Harvey creator identity

SOP Bot is **A JH Agent — Designed & built by Josh Harvey**. This kit uses the same identity as the SCC System Grip Agent: a small circuit JH mark, a clear creator signature and a discreet corner watermark.

| Asset | Use |
| --- | --- |
| [Original supplied logo](josh-harvey-logo-original.jpeg) | Full Josh Harvey / AI • AUTOMATION • IMPACT artwork, preserved unchanged |
| [JH monogram](jh-monogram.svg) | Scalable companion traced from the supplied circuit mark; light backgrounds |
| [White monogram](jh-monogram-white.svg) | Dark headers and interfaces |
| [Watermark](jh-watermark.svg) | 7% opacity mark in a clear corner |
| [A JH Agent badge](a-jh-agent-badge.svg) | Repository and document attribution |
| [Agent icon](jh-agent-icon.png) | 192 × 192 PNG for the agent's icon field where available |

Use **Designed & built by Josh Harvey** for creator attribution. The mark identifies authorship; it does not signify Microsoft, NHS or local governance approval. Describe adapted versions accurately, for example: “Adapted by [team] from SOP Bot, designed & built by Josh Harvey.”

## Placement

- Repository: full supplied logo in the main README and a compact badge on every Markdown document.
- HTML: small JH header mark, creator footer and light corner watermark. All images are embedded so each guide works offline.
- PDF: full supplied logo on the cover, creator signature and light corner watermark on all eight pages. Existing source content and page numbering are retained.
- Formatted assessments and handovers: place a small mark and template-design credit in the footer, with a watermark in a clear lower corner. Keep document content readable and distinguish the template creator from the local assessment author.
- Copy fields, reference knowledge, CSV/JSON and synthetic test inputs: use the surrounding README for attribution. Do not paste logo markup or extra branding into instructions or evidence cells.

## Maintenance

`python scripts/build-guide.py` retains branding on the generated HTML, starter-prompt guide and testing guide. Other Markdown documents use the same badge footer. Check logo links and contrast after layout changes.

The two reference downloads retain their `.original` filenames for link compatibility; version 1.0.1 adds branding to their original content. [Source notes](../../docs/source-notes.md) record the original and current checksums.

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](./a-jh-agent-badge.svg)](./README.md)
