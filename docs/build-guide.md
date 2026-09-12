# Build SOP Bot in Copilot Agent Builder

Follow these steps in Microsoft 365 Copilot. Keep this repository open alongside the **Configure** tab. The [interactive guide](index.html) provides the same build journey with copy buttons and a checklist; download the repository and open that file locally if GitHub shows source code.

## 1. Establish the purpose and owner

Use this problem statement: “Teams need a consistent way to find unclear, repetitive or manually intensive work in SOPs and decide which improvements are worthwhile.” Initial users may include process owners, business support, operational managers, improvement teams and digital staff.

Complete the [agent record](../templates/agent-record.md): owner, deputy, sponsor, intended users, boundaries, version, review date and feedback route. Start with a stable administrative process that an owner can validate. Keep accountable clinical, safeguarding, workforce, legal and access-to-care decisions with people.

## 2. Check access

Use your work or school account with eligible Microsoft 365 Copilot access. Ask your administrator if Agent Builder is unavailable or a required knowledge feature is missing. Licensing and policy determine what your account can use; this public kit does not grant access.

Open Microsoft 365 Copilot and select **New agent → Skip to configure**. The manual route makes the configuration easy to reproduce. [Microsoft's build instructions](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) describe this path and document limits of 30 characters for the name, 1,000 for the description and 8,000 for instructions (checked 12 September 2026).

## 3. Configure the name and description

Copy the entire text of [name.txt](../agent/name.txt) and [description.txt](../agent/description.txt) into the corresponding fields. Where the icon control is available, upload the supplied [JH agent icon](../assets/branding/jh-agent-icon.png). Use the [branding guide](../assets/branding/README.md) for reusable logos and document watermarks. The portable default does not assume an NHS organisation. You can rename your local instance, staying within the platform limit.

## 4. Paste the complete instructions

Copy [instructions.txt](../agent/instructions.txt) into **Instructions**, without Markdown fences or headings from another document. Confirm the final **STYLE** section and the eight numbered output sections are present. If you personalise the opening, recount the final text against the platform limit.

Keep behaviour in this field. The knowledge framework supplies definitions and examples; uploading a longer instruction file is not a workaround for the instruction limit. After using the Describe tab to make changes, recheck all configured fields because it may rewrite them.

## 5. Add four starter prompts

For each entry in [starter-prompts.md](../agent/starter-prompts.md), add its title and full prompt text under **Starter prompts**. They cover a complete review, clarity, automation and quick triage. The user supplies the SOP after choosing a prompt.

## 6. Add the reference framework

In **Knowledge**, add [assessment-framework.txt](../knowledge/assessment-framework.txt), using upload or an approved SharePoint/OneDrive location available in your tenant. Wait for preparation to finish. If reference knowledge cannot be configured, the core behaviour remains in the instructions; test it before relying on the result.

For the initial build, use only this generic framework. Add locally approved governance and a completed glossary/context file when needed, with a named source owner. Leave broad web search and personal email/Teams grounding off for this focused assessment. The [knowledge and sharing guide](knowledge-and-sharing.md) explains embedded file exposure, source permissions and platform grounding limits.

Supply each SOP in the assessment conversation, not as permanent knowledge for every user. If attachments are unavailable, paste the synthetic SOP's full text. For a real document, use only input methods and material approved for your environment.

## 7. Keep optional capabilities proportionate

The core configuration requests no actions, flows, API connections or background execution. Code interpreter/document generation can be considered separately if available and locally approved; it is not required to follow this kit. Do not enable capabilities just because an instruction mentions a Microsoft tool. Keep the available default model/response mode initially, and record it with your test evidence.

## 8. Run the configuration and document tests

Open **Try it** (or the current test/preview panel). Start with the configuration prompt in [the test pack](testing.md). Then run each remaining scenario in a fresh chat, supplying exactly the named synthetic file or text. Log the observed response, expected behaviour, result and corrections in [test-evidence.csv](../templates/test-evidence.csv).

Check whole-document handling, recommendations, retained decisions and benefit arithmetic. The [worked assessment](../examples/worked-assessment.md) is a shape and calculation reference, not text the agent must reproduce verbatim.

## 9. Review readiness with an owner

Complete the full [acceptance checklist](testing.md#acceptance-checklist). The interactive guide requires every build task, every test and every displayed release control before showing its checklist as complete. That result is a local record of your ticks; it is not an independent approval or a live check of Copilot configuration.

## 10. Create and share a bounded pilot

After testing, select **Create**. In **Share**, add your intended pilot users with **Can chat**, and add individual maintainers with **Can edit** only where appropriate. Check the underlying knowledge permissions with a pilot user. Share the [advisory statement](../templates/sharing-statement.txt) and the feedback route.

Sharing occurs within your organisation and remains subject to tenant policy and each user's licence. Broader organisational distribution may require admin review. See [Microsoft's sharing guidance](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents). Users in other organisations can use this public repository to build their own instance.

## 11. Pilot one recommendation

Capture a baseline and have the process owner check the assessment. If an improvement is selected, validate its feasibility and required approvals separately; then trial one reversible change with a manual fallback. Compare observed net benefit, exceptions and support time with the estimate. Follow the [pilot guide](pilot-and-maintenance.md).

## 12. Maintain the instance

Record configuration versions, knowledge changes and test evidence. Re-run the relevant pack after changes and before widening access. Use **Update** in the authoring interface to make saved changes available to users, and recheck sharing/source access. The repository's release version is not an approval of your local agent.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| No New agent option | Confirm account, tenant policy and Copilot entitlement with your administrator. |
| Instructions appear truncated | Compare the ending with instructions.txt and count your edited text. |
| A file is still Preparing | Wait for source readiness and retry a new chat. |
| Users receive different answers | Check source permissions, configured capabilities, model mode and exact input version. |
| The SOP is unreadable or partial | Supply accessible text or the missing sections; retain a provisional assessment until available. |
| Agent claims it can deploy or approve | Correct configuration and fail the relevant tests before sharing. |
| Local HTML progress will not persist | The browser may block storage or clear it; keep an external evidence log. Copy blocks remain usable. |
| GitHub displays HTML code | Download ZIP, extract and open docs/index.html, or use the hosted guide linked in the README. |

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](../assets/branding/a-jh-agent-badge.svg)](../assets/branding/README.md)
