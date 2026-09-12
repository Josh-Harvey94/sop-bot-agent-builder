# SOP Bot for Microsoft 365 Copilot

<p><img src="assets/branding/josh-harvey-logo-original.jpeg" alt="Josh Harvey — AI, Automation, Impact" width="170"></p>

**A JH Agent · Designed & built by Josh Harvey**

**Turn a standard operating procedure into a practical process-improvement assessment.**

SOP Bot maps a process, spots unclear or duplicated work, considers Microsoft automation options, estimates staff capacity released, and explains what should remain a human decision. This open build kit lets you recreate it in **Microsoft 365 Copilot Agent Builder** using copy-and-paste configuration. No coding, API key, or Copilot Studio project is required for the core build.

**[Start the step-by-step build](docs/build-guide.md)** · **[Interactive guide](https://josh-harvey94.github.io/sop-bot-agent-builder/)** · **[Download the complete repository](https://github.com/Josh-Harvey94/sop-bot-agent-builder/archive/refs/heads/main.zip)**

## Build your own

1. Download the repository using **Code → Download ZIP** and extract it. No GitHub account is needed to download a public repository.
2. In Microsoft 365 Copilot, choose **New agent → Skip to configure**.
3. Copy the [name](agent/name.txt), [description](agent/description.txt), and complete [instructions](agent/instructions.txt) into their matching fields.
4. Add the four [starter prompts](agent/starter-prompts.md).
5. Add [assessment-framework.txt](knowledge/assessment-framework.txt) as reference knowledge if your account supports it. Check the [knowledge setup](docs/knowledge-and-sharing.md) before adding local policies.
6. Run the [test pack](docs/testing.md) in a fresh chat for each scenario, using the supplied synthetic SOPs. Then create and share a bounded pilot within your organisation.

For a guided experience, open **docs/index.html** from the extracted folder in a browser. It works offline, includes copy buttons, progress tracking, a capacity calculator and a test-dependent release checklist. Use **Print / save as PDF** for a current handover copy. The hosted guide provides the same experience.

## What you get

| Folder | Contents |
| --- | --- |
| [agent](agent/) | Copy-ready instructions, name, description and four prompts; a configuration reference |
| [knowledge](knowledge/) | Portable assessment framework and optional local-context template |
| [docs](docs/) | Build, knowledge, calculations, testing, pilot and source notes; interactive guide |
| [examples](examples/) | Fictional SOPs and a complete worked assessment |
| [templates](templates/) | Ownership, baseline, assessment, source, test and release records |
| [assets/branding](assets/branding/README.md) | Supplied logo, monograms, watermark, creator badge and Copilot icon |
| [tests](tests/) | Agent evaluation scenarios and automated guide checks |
| [docs/downloads](docs/downloads/) | Original-content HTML and eight-page PDF with JH creator branding |

## What a complete assessment contains

1. Overall verdict, confidence and main caveat.
2. Purpose, trigger, outcome, scope, teams and systems.
3. A numbered current-process table.
4. SOP improvements, with proposed wording where useful.
5. Automation opportunities, effort, benefit, assumptions and dependencies.
6. Work that should remain human-led.
7. Overall benefit without double-counting.
8. One proportionate next step.

Each opportunity receives one of six recommendations: **Build**, **Pilot**, **Improve the process first**, **Assist, but keep a human decision**, **Not worth automating**, or **Do not automate**. These are advisory findings, including the label “Build”; they do not authorise implementation.

See the [worked assessment](examples/worked-assessment.md) for a fictional request-handling process. It illustrates the expected structure; it is not a measured Copilot result.

## Access and deployment

The build kit is public and reusable under the [MIT licence](LICENSE). Running an agent requires an eligible Microsoft 365 account, the relevant Copilot access and tenant permission. Features vary by licensing and admin policy. A public repository does not create a public Copilot endpoint or grant Microsoft licences. Each organisation builds and manages its own instance. See [Microsoft's prerequisites](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites).

This repository is a manual Agent Builder kit. `agent/configuration.json` records the settings; it is not an importable Microsoft agent manifest. The downloadable repository ZIP is a collection of source files, not a Teams sideload package.

## Local validation and maintenance

The supplied assets need no build step to use. Maintainers can regenerate the interactive guide and run checks with Python 3 and Node.js 20 or newer; there are no third-party package dependencies:

```sh
python scripts/build-guide.py
python scripts/validate.py
node --test tests/guide.test.cjs
```

Automated checks cover the copyable configuration, local links, guide consistency, capacity calculations and readiness logic. They do **not** run Copilot or establish clinical, organisational or production approval. Record tenant test results separately using the [test evidence template](templates/test-evidence.csv). The initial public release is a build kit awaiting each adopter's local evaluation.

## Origin and contribution

Created from Joshua Harvey's **SOP BOT Agent Builder Guide** conversation, source material, interactive HTML and shareable PDF, supplied on 12 September 2026. The default configuration is organisation-neutral; the original downloads retain their Cornwall and Isles of Scilly context. This is an independent community resource and does not imply NHS or Microsoft endorsement. [Source and change notes](docs/source-notes.md) explain the adaptations and reference-version limitations.

Improvements are welcome through [issues](https://github.com/Josh-Harvey94/sop-bot-agent-builder/issues) and pull requests. Use fictional examples when reporting problems; keep real SOPs, personal information and internal source links in your organisation's approved systems. See [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](assets/branding/a-jh-agent-badge.svg)](assets/branding/README.md)
