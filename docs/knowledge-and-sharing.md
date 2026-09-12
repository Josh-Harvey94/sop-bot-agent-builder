# Knowledge, privacy and sharing

The intended model has two layers: stable reference knowledge to keep assessments consistent, and one user-supplied SOP for the current assessment. Combining a large collection of unrelated procedures makes scope and version control harder.

## Initial source set

| Source | Purpose | Treatment |
| --- | --- | --- |
| assessment-framework.txt | Definitions, effort heuristics, calculations and evidence classes | Generic reference provided with the kit |
| Locally approved governance | Actual organisational requirements | Optional; check authority, access and review date |
| Completed local context/glossary | Names, abbreviations and confirmed context | Optional; the blank template is not policy |
| Current SOP | The process being assessed | Supply for that conversation, one version at a time |

Keep completed local records, real procedures and test responses outside the public repository. `local/` is ignored by Git as a convenience, but review staged files before committing. The public examples contain invented process details.

## Configure narrowly

Add the generic TXT framework through the available Knowledge controls. Use governed SharePoint/OneDrive references for sensitive internal material where access must follow source permissions. Embedded uploads make their content available through the agent to users who can access it; a local upload does not retain the original file's sharing model. Test the actual recipient experience before sharing.

Leave broad web search, personal email and personal Teams grounding off for the baseline build. Microsoft states that Agent Builder cannot completely block general AI knowledge; prompting to use supplied evidence is a behavioural control, not a hard source-only guarantee. Evaluate grounding and unsupported claims in real tenant tests. See [Microsoft's knowledge documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge), checked 12 September 2026.

Do not upload this entire repository as knowledge. Build instructions, UI code, tests, examples and blank templates are maker resources. Only the reviewed framework and selected local reference documents belong in the configured knowledge set. The setup instructions remain in the Instructions field.

## Register every source

Use [knowledge-source-register.csv](../templates/knowledge-source-register.csv). Record name, purpose, owner, classification, personal data, permission basis, version, last review, next review, removal trigger and intended use. Remove obsolete and conflicting sources. Verify access as an intended user; the maker's access alone is insufficient evidence.

## Sharing scope

A public GitHub repository distributes the build material. Copilot sharing controls distribute an instance within a tenant. Choose chat access for users and edit access for maintainers, with local policy determining wider sharing. Source access and agent access are separate checks. [Microsoft's sharing documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents) explains these roles and the treatment of source permissions.

The repository does not contain a Teams app manifest or a tenant export. If you later export an agent using Microsoft's download facility, review the package and its knowledge dependencies separately before distributing it.

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](../assets/branding/a-jh-agent-badge.svg)](../assets/branding/README.md)
