#!/usr/bin/env python3
"""Design-rule lint for the portfolio canvas pages (source/*.dc.html + canvas.json).

  python3 tools/lint.py                  report; exit 1 on any error or ratchet increase
  python3 tools/lint.py --update-baseline  accept current counts as the new baseline
  python3 tools/lint.py --verbose          list every hit (page:line)
  PORTFOLIO_SRC=/path/to/pages python3 tools/lint.py   lint another folder

Rules live in tools/rules.json. Run before every export and every push.
"""
import json, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
SRC = os.environ.get('PORTFOLIO_SRC', os.path.join(REPO, 'source'))
R = json.load(open(os.path.join(HERE, 'rules.json')))
BASE_F = os.path.join(HERE, 'lint-baseline.json')
VERBOSE = '--verbose' in sys.argv

tok = {h.upper() for h in R['tokens_light'] + R['tokens_dark'] + R['neutral_ok']}
fonts_ok = {f.lower() for f in R['fonts_ok']}

def norm(h):
    h = h.upper()
    if len(h) == 4: h = '#' + ''.join(c * 2 for c in h[1:])
    return h

def strip_blobs(s):
    # base64 / blob payloads can contain accidental matches
    return re.sub(r'data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+', 'data:', s)

def visible_text(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<helmet>.*?</helmet>', ' ', s, flags=re.S)
    s = re.sub(r'<svg.*?</svg>', ' ', s, flags=re.S)
    return re.sub(r'<[^>]+>', ' ', s)

def lines_of(s, pat, flags=0):
    out = []
    for m in re.finditer(pat, s, flags):
        out.append(s.count('\n', 0, m.start()) + 1)
    return out

hits = {}   # page -> rule -> [lines]
def add(page, rule, ln): hits.setdefault(page, {}).setdefault(rule, []).append(ln)

pages = sorted(glob.glob(os.path.join(SRC, '*.dc.html')))
for p in pages:
    name = os.path.basename(p).replace('.dc.html', '')
    raw = strip_blobs(open(p, encoding='utf-8').read())
    # hex colours not in tokens (ratchet)
    for m in re.finditer(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', raw):
        if norm(m.group(0)) not in tok:
            add(name, 'hex_off_token', raw.count('\n', 0, m.start()) + 1)
    # gradients: on charts = error, elsewhere = ratchet
    for m in re.finditer(r'[^\n]{0,260}(?:linear|radial|conic)-gradient[^\n]{0,60}', raw):
        seg = m.group(0)
        ln = raw.count('\n', 0, m.start()) + 1
        if re.search(r'(class|id)="[^"]*\b(bar|bars|chart|barfill|fill-bar)\b', seg, re.I): add(name, 'chart_gradient', ln)
        else: add(name, 'gradient_other', ln)
    # strokes: outline and thick borders = error, 1px hairlines = ratchet
    for m in re.finditer(r'outline\s*:\s*(?!none|0\b)[^;"}]+', raw):
        if ':focus' in raw[max(0, m.start() - 160):m.start()]: continue   # keyboard focus rings are accessibility, allowed
        add(name, 'outline', raw.count('\n', 0, m.start()) + 1)
    for m in re.finditer(r'border(?:-[a-z]+)?\s*:\s*([2-9]|\d\d)px\s+(?:solid|dashed|dotted)', raw): add(name, 'thick_border', raw.count('\n', 0, m.start()) + 1)
    for m in re.finditer(r'border(?:-[a-z]+)?\s*:\s*1px\s+solid', raw): add(name, 'border_1px', raw.count('\n', 0, m.start()) + 1)
    # fonts
    for m in re.finditer(r'font-family\s*:\s*([^;"}]+)', raw):
        for f in re.split(r',', m.group(1)):
            f = f.strip().replace('\\', '').strip('\'"').lower()
            if f and f not in fonts_ok and not f.startswith('{{') and not f.startswith('var('):
                add(name, 'font_off_system:' + f, raw.count('\n', 0, m.start()) + 1)
    # banned visible words
    txt = visible_text(raw)
    for w in R['banned_visible_words']:
        for m in re.finditer(r'(?<![A-Za-z])' + re.escape(w) + r'(?![A-Za-z])', txt):
            add(name, 'banned_word:' + w, 0)

# canvas.json
cj = os.path.join(SRC, 'canvas.json')
if os.path.exists(cj):
    c = json.load(open(cj))
    for k, b in c.get('boards', {}).items():
        n = k.replace('.dc.html', '')
        if b.get('h') == 8000: add(n, 'board_height_8000', 0)
        if not os.path.exists(os.path.join(SRC, k)): add(n, 'board_missing_file', 0)
    for p in pages:
        if os.path.basename(p) not in c.get('boards', {}): add(os.path.basename(p), 'file_not_in_canvas_json', 0)

def kind(rule):
    base = rule.split(':')[0]
    if base in R['error_rules']: return 'error'
    return 'ratchet'

counts = {pg: {r: len(l) for r, l in rs.items()} for pg, rs in hits.items()}
if '--update-baseline' in sys.argv:
    json.dump({pg: {r: n for r, n in rs.items() if kind(r) == 'ratchet'} for pg, rs in counts.items()},
              open(BASE_F, 'w'), indent=1, sort_keys=True)
    print('baseline updated:', BASE_F); sys.exit(0)

base = json.load(open(BASE_F)) if os.path.exists(BASE_F) else {}
errors, worse, info = [], [], []
for pg in sorted(counts):
    for r, n in sorted(counts[pg].items()):
        k = kind(r)
        if k == 'error': errors.append((pg, r, n))
        else:
            b = base.get(pg, {}).get(r, 0)
            (worse if n > b else info).append((pg, r, n, b))

def show(title, rows, fmt):
    print('\n' + title)
    for row in rows: print('  ' + fmt(row))
    if not rows: print('  none')

show('ERRORS (must fix)', errors, lambda t: f'{t[0]:<28} {t[1]:<34} x{t[2]}' + (('  lines ' + ','.join(map(str, hits[t[0]][t[1]][:12]))) if VERBOSE else ''))
show('RATCHET INCREASES (worse than baseline)', worse, lambda t: f'{t[0]:<28} {t[1]:<34} {t[3]} -> {t[2]}')
tot = {}
for pg, r, n, b in info: tot[r] = tot.get(r, 0) + n
print('\nWithin baseline (info):', ', '.join(f'{r} {n}' for r, n in sorted(tot.items())) or 'none')
ok = not errors and not worse
print('\nRESULT:', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
