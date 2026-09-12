"""Validate the distributable kit without contacting Copilot or external services."""
import csv
import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)

config = json.loads((ROOT / 'agent/configuration.json').read_text())
for field, limit in [('name',30),('description',1000),('instructions',8000)]:
    text = (ROOT / f'agent/{field}.txt').read_text(encoding='utf-8').strip()
    require(0 < len(text.encode('utf-16-le')) // 2 <= limit, f'{field} exceeds {limit} characters or is empty')
instructions = (ROOT / 'agent/instructions.txt').read_text(encoding='utf-8').strip()
require(instructions.endswith('Finding automation unsuitable is a successful assessment.'), 'Instructions ending missing')
for i in range(1,9):
    require(re.search(rf'^{i}\. [A-Z -]+ -', instructions, re.M), f'Output section {i} missing')
require('not a Microsoft import manifest' in config['format'], 'Configuration should explain manual setup')
for key in ['instructionsFile','starterPromptsFile','optionalLocalContextTemplate']:
    require((ROOT / config[key]).is_file(), f'Missing {config[key]}')
for name in config['knowledgeFiles']:
    require((ROOT / name).is_file(), f'Missing {name}')
page = (ROOT / 'docs/index.html').read_text(encoding='utf-8')
copied = re.search(r'id="instructionText">(.*?)<button', page, re.S)
require(copied and html.unescape(copied.group(1)).strip() == instructions, 'Guide instructions differ from canonical text')
require(len(re.findall(r'\bdata-task\b', page.split('<script>')[0])) == 12, 'Expected twelve build tasks')
require('No positive payback' in page and 'Annual maintenance/support hours' in page, 'Calculator safeguards absent')
require('SopGuideCore.readiness' in page and "tests.every(value => value === 'pass')" in page, 'Readiness logic missing')
scenarios = json.loads((ROOT / 'tests/scenarios.json').read_text())
require(len(scenarios) == 12 and len({t['id'] for t in scenarios}) == 12, 'Expected twelve unique test scenarios')
for case in scenarios:
    require(case['prompt'] and case['expected'], f'Incomplete scenario {case["id"]}')
    if case['file']:
        path = ROOT / case['file']
        require(path.is_file() and 'SYNTHETIC' in path.read_text(), f'Missing or unlabelled synthetic file: {path}')
with (ROOT / 'templates/test-evidence.csv').open(encoding='utf-8',newline='') as stream:
    evidence = list(csv.DictReader(stream))
require([row['Test ID'] for row in evidence] == [case['id'] for case in scenarios], 'Evidence rows differ from test pack')
require(all(row['Status'] == 'NOT RUN' for row in evidence), 'Public evidence template must not imply tests were run')
for name, expected in json.loads((ROOT / 'docs/downloads/source-checksums.json').read_text()).items():
    require(hashlib.sha256((ROOT / 'docs/downloads' / name).read_bytes()).hexdigest() == expected, f'Original file changed: {name}')

def check_link(source, target):
    target = html.unescape(target)
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith(('#','//')):
        return
    resolved = (source.parent / unquote(parsed.path)).resolve()
    require(resolved.is_relative_to(ROOT.resolve()), f'Link escapes repository: {source.relative_to(ROOT)} -> {target}')
    require(resolved.exists(), f'Broken local link: {source.relative_to(ROOT)} -> {target}')

class Links(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            require(values['id'] not in self.ids, f'Duplicate HTML id: {values["id"]}')
            self.ids.add(values['id'])
        for key in ('href','src'):
            if key in values:
                check_link(self.source,values[key])

for path in ROOT.rglob('*.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        check_link(path,target)
Links(ROOT / 'docs/index.html').feed(page)
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix in {'.txt','.md','.json','.html','.csv','.js','.cjs','.py','.yml'} and '.git' not in path.parts:
        text = path.read_text(encoding='utf-8')
        for pattern in [r'https://[^\s<>]+\.sharepoint\.com', r'outlook\.office365\.com/owa', r'C:\\Users\\', r'gh[pousr]_[A-Za-z0-9]{30,}']:
            # Avoid matching the validator's own pattern literals.
            if path.name != 'validate.py':
                require(not re.search(pattern,text,re.I), f'Potential private source/credential in {path.relative_to(ROOT)}')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: instruction limits, configuration, guide consistency, synthetic tests, blank evidence, original checksums, local links and private-source scan.')
