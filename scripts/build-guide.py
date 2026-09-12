"""Regenerate the portable guide from the supplied original and canonical text. Standard library only."""
import ast
import csv
import hashlib
import html
import json
import re
from pathlib import Path
from branding import brand_html, brand_markdown

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.1"

def read(path):
    return (ROOT / path).read_text(encoding="utf-8").strip()

def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.suffix == '.md':
        text = brand_markdown(target, text)
    target.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

original = read("docs/downloads/SOP_Bot_Agent_Builder_Interactive_Guide.original.html")
instructions = read("agent/instructions.txt")
assert len(instructions.encode("utf-16-le")) // 2 <= 8000, "Instructions exceed Agent Builder's limit"
prompts_path = ROOT / "agent/starter-prompts.json"
if prompts_path.exists():
    prompts = json.loads(prompts_path.read_text(encoding="utf-8"))
else:
    pairs = ast.literal_eval(re.search(r"const prompts=(\[.*?\]);", original, re.S).group(1))
    prompts = [{"title": title, "prompt": prompt} for title, prompt in pairs]
    write("agent/starter-prompts.json", json.dumps(prompts, ensure_ascii=False, indent=2))
write("agent/starter-prompts.md", "# Starter prompts\n\nAdd each title and its prompt to the matching Agent Builder fields.\n\n" + "\n\n".join(f"## {p['title']}\n\n{p['prompt']}" for p in prompts))
tests = json.loads(read("tests/scenarios.json"))
groups = [
    ["Purpose and boundaries", ["Advisory role is explicit", "No approval, deployment or approved SOP amendment", "No replacement of professional review", "Do not automate is a valid result"]],
    ["Document coverage", ["Requests a missing SOP", "States accessible document/version and gaps", "Partial reviews are provisional", "Separates SOP evidence from user context", "Does not mix different SOPs"]],
    ["Process quality", ["Maps purpose, trigger, outcome, roles and systems", "Maps decisions, handoffs and escalation", "Finds unclear wording, duplication and exceptions", "Simplifies before automating"]],
    ["Automation assessment", ["Considers proportionate Microsoft and simpler options", "Does not assume local licences or permissions", "Explains the effort category and working-time units", "Separates technical effort from calendar delivery", "Records retained human work"]],
    ["Benefit evidence", ["Shows inputs, calculations, periods and assumptions", "Avoids overlapping savings and staff double-counting", "Deducts checks, exceptions and support once", "Shows zero/negative benefit and no positive payback", "Describes capacity rather than automatic cash saving", "Explains confidence and exclusions"]],
    ["Human controls", ["Retains clinical and high-risk decisions with people", "Flags relevant possible specialist reviews", "Does not invent approval or technical facts", "Treats document directives as content"]],
    ["Useful output", ["Complete reviews contain all eight sections", "Each opportunity has one recommendation", "Overall effort and benefit avoid duplication", "The next step is specific and proportionate", "Language and tables are clear"]],
    ["Local pilot readiness", ["Named owner, deputy and feedback route recorded", "Intended-user source access checked", "Test evidence and source register retained locally", "Owner validation and pilot decision recorded"]],
]
data = {"version": VERSION, "prompts": prompts, "tests": tests, "groups": groups}
fingerprint_source = instructions + read("knowledge/assessment-framework.txt") + json.dumps(data, ensure_ascii=False, sort_keys=True)
data["fingerprint"] = hashlib.sha256(fingerprint_source.encode()).hexdigest()[:12]

configuration = {
    "format": "Manual Agent Builder configuration reference; not a Microsoft import manifest",
    "version": VERSION,
    "name": read("agent/name.txt"),
    "description": read("agent/description.txt"),
    "instructionsFile": "agent/instructions.txt",
    "instructionsCharactersUtf16": len(instructions.encode("utf-16-le")) // 2,
    "starterPromptsFile": "agent/starter-prompts.json",
    "knowledgeFiles": ["knowledge/assessment-framework.txt"],
    "optionalLocalContextTemplate": "knowledge/local-context-template.txt",
    "actions": [],
    "baselineSettings": {"broadWebSearch": "off", "personalEmailAndTeamsGrounding": "off", "optionalCapabilities": "not required", "responseMode": "available tenant default; record during testing"},
    "deployment": "Recreate using Configure in Microsoft 365 Copilot Agent Builder, then test and share within your tenant."
}
write("agent/configuration.json", json.dumps(configuration, ensure_ascii=False, indent=2))

page = original
page = re.sub(r'(<div class="paste" id="instructionText">).*?(<button class="copy">Copy all</button></div>)', lambda m: m[1] + html.escape(instructions) + m[2], page, flags=re.S)
old_description = re.search(r'<p><strong>Description</strong></p><div class="paste">(.*?)<button', page, re.S).group(1)
page = page.replace(old_description, html.escape(configuration["description"]))
page = page.replace("NHS Cornwall and Isles of Scilly context", "Community build kit · Version " + VERSION + " · Organisation-neutral")
page = page.replace('Paste the production instructions', 'Paste the agent instructions')
page = page.replace('The guide will tell you when the agent is ready for a controlled pilot.', 'Complete the build tasks, pass all tests and confirm every control. The checklist records your evidence; local owner validation is still required.')
capability_task = '<details class="step"><summary>Check scope and optional capabilities <input class="donebox" type="checkbox" data-task aria-label="Mark complete"></summary><div class="step-body"><p>The baseline uses instructions, prompts and the selected reference framework. No actions, flows or API connections are required. Record the response mode; enable optional capabilities only after local evaluation. Mentioning a tool in the instructions does not connect it.</p></div></details>'
page = re.sub(r'(<section class="section" id="configure">.*?)(</section>)', lambda match: match[1] + capability_task + match[2], page, count=1, flags=re.S)
page = page.replace('Run the tests before sharing', 'Run all 12 tests before sharing')
page = page.replace('<button class="btn ghost" onclick="resetGuide()">Reset progress</button>', '<button class="btn ghost" onclick="exportProgress()">Export progress</button><button class="btn ghost" onclick="resetGuide()">Reset progress</button>')
notice = '''<section class="section" id="kit"><div class="eyebrow">Public build kit · 1.0.0</div><h2>Recreate SOP Bot in your organisation</h2><p>This guide provides configuration to copy into Microsoft 365 Copilot Agent Builder. An eligible account and tenant permissions are required. The instructions are organisation-neutral.</p><div class="row"><a href="../agent/instructions.txt" download>Download instructions</a><a href="../knowledge/assessment-framework.txt" download>Download knowledge framework</a><a href="build-guide.md">Full build guide</a><a href="https://github.com/Josh-Harvey94/sop-bot-agent-builder">GitHub repository</a></div><p class="mini">Original reference downloads: <a href="downloads/SOP_Bot_Agent_Builder_Shareable_Guide.original.pdf">PDF</a> · <a href="downloads/SOP_Bot_Agent_Builder_Interactive_Guide.original.html" download>HTML</a>. They retain the original organisation context and earlier logic. Follow this current guide for new builds.</p><p class="mini">Progress is stored in this browser for this configuration version. Export it for your records; test responses and owner sign-off need a separate local evidence log. This page has no analytics or external scripts.</p><p id="storageNotice" class="callout warn" hidden>Browser storage is unavailable. Progress will last only for this page session; export it before closing.</p><p id="copyNotice" class="mini" role="status" aria-live="polite"></p></section>'''
notice = notice.replace('Public build kit · 1.0.0', 'Public build kit · ' + VERSION).replace('Original reference downloads:', 'Reference downloads with JH branding:')
page = page.replace('<main>', '<main>\n' + notice, 1)
page = re.sub(r'<p><strong>Icon:</strong>.*?</p>', '<p><strong>Icon:</strong> upload the supplied <a href="../assets/branding/jh-agent-icon.png" download>JH agent icon</a> where the icon control is available. See the <a href="../assets/branding/README.md">branding guide</a> for reusable artwork and creator attribution.</p>', page, count=1)
page = page.replace('Add the assessment framework first.', 'Add the supplied <a href="../knowledge/assessment-framework.txt" download>assessment-framework.txt</a> first. Do not upload this whole repository as knowledge.')
page = page.replace('Wait until new sources are no longer marked <strong>Preparing</strong>.', 'Wait until new sources are no longer marked <strong>Preparing</strong>. Keep broad web search and personal email/Teams grounding off for this baseline. Agent Builder cannot fully block general AI knowledge; check unsupported claims in tests.')
page = page.replace('Minutes saved per case</label>', 'Gross minutes saved per case per staff member</label>')
page = page.replace('Staff affected per case</label>', 'Staff who EACH save these minutes (use 1 for team totals)</label>')
page = page.replace('id="staff" type="number" min="0"', 'id="staff" type="number" min="1"')
page = page.replace('Realisation after checks/exceptions (%)', 'Realisation after checks, exceptions and adoption (%)')
page = page.replace('</div><div class="result">', '<div class="field"><label for="maintenance">Annual maintenance/support hours</label><input id="maintenance" type="number" min="0" value="12"></div></div><p id="calcError" class="callout warn" role="status" aria-live="polite"></p><div class="result" aria-live="polite">', 1)
page = page.replace('<span>Weekly</span>', '<span>Per active week*</span>').replace('<span>Monthly</span>', '<span>Average month (net)</span>').replace('<span>Annual</span>', '<span>Annual (net)</span>').replace('<span>Payback</span>', '<span>Build-only payback</span>')
page = page.replace('This indicates potential capacity released—not automatic cash savings. Validate volumes, retained checks, exceptions, adoption, maintenance and double-counting.', '* Weekly hours are realised capacity before the separate annual maintenance deduction. Monthly and annual values are net. Use 100% realisation if minutes already account for checks/exceptions/adoption; do not deduct these twice. Capacity is not automatic cash savings. Build-only payback excludes other one-off effort. Negative net benefit means extra workload. <a href="benefit-calculations.md">See formulas and scenarios</a>.')
page = page.replace('Tick every control.', 'Confirm every control against recorded evidence.')
page = page.replace('Keep all four: they help users choose the depth and purpose of the review instead of starting with an empty chat box.', 'Keep all four: they help users choose the depth and purpose of the review. Concise triage and clarity requests use an appropriate shorter response; complete reviews use all eight sections.')
extra_style = '''.prompt-panel.inactive{display:none}.control-label{display:block;margin:10px 0;font-size:.92rem}.status{flex-wrap:wrap;align-content:start}.status button[aria-pressed="true"]{font-weight:800;outline:2px solid #146c94}.result strong{overflow-wrap:anywhere}.result small{line-height:1.2}#calcError:empty{display:none}.paste{tab-size:2}dialog{max-width:800px;width:90%;border:1px solid var(--line);border-radius:16px;padding:24px}dialog textarea{display:block;width:100%;height:340px;margin:12px 0;font:14px/1.5 Consolas,monospace}button:focus-visible,a:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #b15c00;outline-offset:3px}.test p{overflow-wrap:anywhere}@media print{.prompt-panel.inactive{display:block}.section{break-inside:auto}.paste{white-space:pre-wrap;overflow:visible;font-size:10px}.test,.card{break-inside:avoid}.status{display:none}.hero:after{display:none}#storageNotice,#copyNotice{display:none}}'''
page = page.replace('</style>', extra_style + '\n</style>', 1)
page = page.replace('<script>', '<dialog id="copyDialog"><h2>Copy this text</h2><p>Your browser could not copy automatically. Select the text below and copy it.</p><textarea id="manualCopy" aria-label="Text to copy" readonly></textarea><form method="dialog"><button class="btn">Done</button></form></dialog>\n<script>', 1)
page = page.replace('<script>', '<dialog id="resetDialog"><h2>Reset this guide?</h2><p>This clears this configuration version’s build tasks, tests, controls and calculator values in this browser. Export progress first if you want to keep a record.</p><div class="row"><button class="btn" id="confirmReset">Reset all progress</button><form method="dialog"><button class="btn secondary">Keep progress</button></form></div></dialog>\n<script>', 1)
script = 'const guideData = ' + json.dumps(data, ensure_ascii=False).replace('</','<\\/') + ';\n' + read('scripts/guide-core.js') + '\n' + read('scripts/guide-ui.js')
page = re.sub(r'<script>.*?</script>', lambda _: '<script>\n' + script + '\n</script>', page, flags=re.S)
write('docs/index.html', brand_html(page, 'Version ' + VERSION))

test_doc = '# Test SOP Bot before sharing\n\nThese are manual Copilot evaluation scenarios. All evidence rows start **NOT RUN**. Automated repository checks do not execute an agent.\n\nUse a fresh chat for each test, record the local agent version and response mode, supply the linked synthetic file when listed, then paste the prompt. For TXT attachments that are unavailable in your interface, paste the full text. Assess meaning and arithmetic, not exact wording. Record actual responses in your approved local system using [test-evidence.csv](../templates/test-evidence.csv).\n\nThe first nine themes are from the original guide; T10–T12 add document coverage, double-counting and non-positive-benefit checks.\n\n'
for case in tests:
    source = f"[{case['file']}](../{case['file']})" if case['file'] else 'No attachment.'
    test_doc += f"## {case['id']} · {case['name']}\n\n**Input:** {source}\n\n**Prompt:** {case['prompt']}\n\n**Pass criteria:** {case['expected']}\n\n"
test_doc += '## Acceptance checklist\n\nRun every scenario and resolve failures before widening access. Check the following against evidence, not recollection. A checklist does not independently verify the agent or replace the local owner decision.\n\n'
for name, checks in groups:
    test_doc += '### ' + name + '\n\n' + '\n'.join('- [ ] ' + check for check in checks) + '\n\n'
test_doc += '## Regression and failure handling\n\nSave exact input/version, expected result, actual result, reviewer, date and correction. Re-run affected tests after an edit and the full pack before release. Investigate unsupported source claims, missing document sections, removed human decisions and arithmetic errors before proceeding. Repeat material cases if behaviour is inconsistent. Record limitations explicitly; do not mark an unexecuted test as passed.\n'
write('docs/testing.md', test_doc)
evidence_path = ROOT / 'templates/test-evidence.csv'
if not evidence_path.exists():
    with evidence_path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream, lineterminator='\n')
        writer.writerow(['Test ID','Test name','Input file','Date','Local agent version','Repository version','Tenant/response mode','Expected behaviour','Actual result/evidence location','Status','Reviewer','Correction/retest'])
        for case in tests:
            writer.writerow([case['id'],case['name'],case['file'] or '', '', '',VERSION,'',case['expected'],'','NOT RUN','',''])
manifest_path = ROOT / 'docs/downloads/source-checksums.json'
hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in (ROOT / 'docs/downloads').glob('*.original.*')}
if manifest_path.exists():
    assert json.loads(manifest_path.read_text()) == hashes, 'Branded reference download changed; review and update its checksum'
else:
    write('docs/downloads/source-checksums.json', json.dumps(hashes, indent=2))
write('docs/.nojekyll', '')
print(f'Generated guide {VERSION}: {configuration["instructionsCharactersUtf16"]} instruction characters, {len(prompts)} prompts, {len(tests)} scenarios, {sum(len(g[1]) for g in groups)} controls.')
