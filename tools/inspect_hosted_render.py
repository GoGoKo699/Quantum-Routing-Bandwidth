"""Inspect actual GitHub Markdown in Chromium; save screenshots and DOM diagnostics.

Run separately from the offline scientific checks. It uses no credentials and
only reads public pages of this repository at a supplied immutable commit.
A blocked or unrendered page is a failure, never a successful visual check.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

REPOSITORY = 'GoGoKo699/Quantum-Routing-Bandwidth'
PAGES = ('README.md', 'docs/learning.md', 'docs/learning-bridges.md',
         'docs/milestones.md', 'docs/bandwidth.md', 'docs/mixed-helpers.md',
         'docs/accuracy-and-resources.md', 'docs/theorem-map.md')

SNAPSHOT = r'''() => {
  const article = document.querySelector('article.markdown-body') || document.querySelector('.markdown-body');
  if (!article) return {article: false};
  function elements(root) {
    let out = [...root.querySelectorAll('*')];
    for (const item of [...out]) if (item.shadowRoot) out.push(...elements(item.shadowRoot));
    return out;
  }
  const all = elements(article);
  const markers = all.filter(x => x.localName === 'math-renderer');
  const errors = all.filter(x => x.matches('mjx-merror,merror,.MathJax_Error,[data-mjx-error],[data-mml-node="merror"]'));
  const nodes = markers.map(x => {
    const inner = elements(x.shadowRoot || x);
    return {ready: inner.some(y => y.matches('mjx-container,svg,math,img')),
      error: /Math rendering failed|Undefined control sequence|ParseError|Unable to render expression/i.test(x.textContent || '')};
  });
  return {article: true, heading: article.querySelector('h1')?.textContent?.trim(),
    markers: markers.length, ready: nodes.filter(x => x.ready).length,
    errors: errors.map(x => (x.getAttribute('data-mjx-error') || x.textContent || '').slice(0,180)),
    marker_errors: nodes.filter(x => x.error).length,
    rendered_containers: all.filter(x => x.localName === 'mjx-container').length,
    page_width: document.documentElement.scrollWidth, viewport: window.innerWidth,
    table_columns: [...article.querySelectorAll('table')].map(t => [...t.rows].map(row => row.cells.length))};
}'''


def source_math_count(text: str) -> int:
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    displays = re.findall(r'\$\$.*?\$\$', text, re.S)
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.S)
    return len(displays) + len(re.findall(r'(?<!\\)\$(?:\\.|[^$])+?(?<!\\)\$', text))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', required=True)
    parser.add_argument('--output', type=Path, default=Path('build/hosted-render'))
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.ref):
        parser.error('--ref must be a full immutable Git commit SHA')
    from playwright.sync_api import sync_playwright
    root = Path(__file__).resolve().parents[1]
    args.output.mkdir(parents=True, exist_ok=True)
    report = {'repository': REPOSITORY, 'ref': args.ref,
              'scope': 'Actual public GitHub rendering; automated DOM/layout checks and screenshot evidence, not scientific review.',
              'pages': []}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={'width': 1180, 'height': 900}, color_scheme='light')
        page = context.new_page()
        for name in PAGES:
            row = {'file': name, 'checks': [], 'problems': []}
            expected = source_math_count((root/name).read_text())
            row['expected_math'] = expected
            url = f'https://github.com/{REPOSITORY}/blob/{args.ref}/{quote(name)}'
            row['url'] = url
            try:
                response = page.goto(url, wait_until='domcontentloaded', timeout=45000)
                row['http_status'] = response.status if response else None
                if not response or response.status != 200:
                    raise RuntimeError(f'GitHub returned {row["http_status"]}')
                page.locator('article.markdown-body, .markdown-body').first.wait_for(timeout=30000)
                for width in (1180, 390):
                    page.set_viewport_size({'width': width, 'height': 900})
                    markers = page.locator('math-renderer')
                    for i in range(markers.count()):
                        markers.nth(i).scroll_into_view_if_needed(timeout=5000)
                        page.wait_for_timeout(50)
                    # Give lazy MathJax rendering a bounded final settling period.
                    for _ in range(20):
                        state = page.evaluate(SNAPSHOT)
                        if state.get('ready', 0) >= expected:
                            break
                        page.wait_for_timeout(250)
                    state = page.evaluate(SNAPSHOT)
                    title = (root/name).read_text().splitlines()[0].removeprefix('# ')
                    if state.get('heading') != title:
                        row['problems'].append(f'{width}px: missing expected document title')
                    if state.get('markers') != expected or state.get('ready', 0) < expected:
                        row['problems'].append(f'{width}px: missing or unfinished mathematics')
                    if state.get('errors') or state.get('marker_errors'):
                        row['problems'].append(f'{width}px: mathematical rendering error')
                    if state.get('page_width', 0) > width+3:
                        row['problems'].append(f'{width}px: page-level horizontal overflow')
                    if any(len(set(cols)) > 1 for cols in state.get('table_columns', [])):
                        row['problems'].append(f'{width}px: inconsistent rendered table cells')
                    row['checks'].append(state)
                    page.evaluate('window.scrollTo(0,0)')
                    page.screenshot(path=str(args.output/f'{name.replace("/", "_")}-{width}.png'), full_page=True)
            except Exception as exc:
                row['problems'].append(str(exc)[:1000])
            row['passed'] = not row['problems']
            report['pages'].append(row)
            print(json.dumps(row), flush=True)
            if row.get('http_status') in (403, 429) or any('ERR_' in x for x in row['problems']):
                # A transport or access failure cannot be repaired by repeatedly
                # requesting all the other pages from the same inaccessible host.
                break
        context.close(); browser.close()
    report['all_passed'] = len(report['pages']) == len(PAGES) and all(x['passed'] for x in report['pages'])
    (args.output/'report.json').write_text(json.dumps(report, indent=2)+'\n')
    print('HOSTED_RENDER_RESULT='+json.dumps(report), flush=True)
    if not report['all_passed']:
        sys.exit(1)


if __name__ == '__main__':
    main()
