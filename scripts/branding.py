"""Shared, offline creator branding for generated documentation. Standard library only."""
import base64
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/branding'


def data_uri(name):
    mime = 'image/png' if name.endswith('.png') else 'image/svg+xml'
    return f'data:{mime};base64,' + base64.b64encode((ASSETS / name).read_bytes()).decode()


def brand_markdown(path, text):
    text = text.split('<!-- JH creator signature -->')[0].rstrip()
    relative = Path(os.path.relpath(ASSETS, path.parent)).as_posix()
    return text + f'\n\n<!-- JH creator signature -->\n\n---\n\n[![A JH Agent — Designed & built by Josh Harvey]({relative}/a-jh-agent-badge.svg)]({relative}/README.md)\n'


def brand_html(page, edition):
    # Replace only our own blocks, allowing a branded reference to be the input.
    page = re.sub(r'<!-- JH:(\w+) -->.*?<!-- /JH:\1 -->\n?', '', page, flags=re.S)
    mark, white, watermark = [data_uri(name) for name in ('jh-monogram.svg', 'jh-monogram-white.svg', 'jh-watermark.svg')]
    head = f'''<!-- JH:HEAD -->
<meta name="author" content="Josh Harvey">
<link rel="icon" type="image/png" href="{data_uri('jh-agent-icon.png')}">
<style>
.jh-hero{{display:flex;align-items:center;gap:12px;margin:0 0 24px;font-size:12px;line-height:1.5;position:relative;z-index:1}}
.jh-hero img{{width:42px;height:28px;object-fit:contain;flex:none}}.jh-hero strong{{font-size:14px}}.jh-hero span{{color:#d7edf4}}
.jh-signature{{display:flex;align-items:center;justify-content:center;gap:12px;padding:20px 28px 12px;font-size:12px;line-height:1.6;color:var(--muted)}}
.jh-signature img{{width:34px;height:23px;flex:none}}.jh-signature strong{{color:var(--ink)}}
.jh-watermark{{position:fixed;right:18px;bottom:14px;width:64px;height:42px;pointer-events:none;z-index:8}}
@media(max-width:650px){{.jh-watermark{{width:44px;height:29px;right:10px;bottom:10px}}.jh-signature{{padding-right:54px}}}}
@media print{{.jh-hero img{{content:url('{mark}')}}.jh-hero span{{color:#60758a}}.jh-watermark{{width:38px;height:25px;right:0;bottom:0}}.jh-signature{{break-inside:avoid}}body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
</style>
<!-- /JH:HEAD -->'''
    page = page.replace('</head>', head + '\n</head>', 1)
    hero = f'<!-- JH:HERO --><div class="jh-hero"><img src="{white}" alt="Josh Harvey circuit JH logo"><div><strong>A JH Agent</strong><br><span>Designed &amp; built by Josh Harvey</span></div></div><!-- /JH:HERO -->'
    page = page.replace('<header class="hero">', '<header class="hero">' + hero, 1)
    footer = f'<!-- JH:FOOTER --><footer class="jh-signature"><img src="{mark}" alt=""><div><strong>Designed &amp; built by Josh Harvey</strong><br>SOP Bot · {edition} · AI · AUTOMATION · IMPACT</div></footer><!-- /JH:FOOTER -->'
    page = page.replace('</body>', footer + '\n</body>', 1)
    page = page.replace('<body>', f'<body>\n<!-- JH:WATERMARK --><img class="jh-watermark" src="{watermark}" alt="" aria-hidden="true"><!-- /JH:WATERMARK -->', 1)
    return page
