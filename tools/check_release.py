"""Dependency-free checks of reader-facing syntax and tracked result integrity."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re


def equation_labels(line: str, label: str, index: int) -> list[str]:
    """Use inline number text, not legacy MathML table rows, for equation labels."""
    if re.search(r'\\tag\*?\s*\{', line):
        raise AssertionError(f'{label}:{index}: legacy equation tag is unsafe in native MathML')
    return re.findall(r'\\qquad\s*\\text\{\(([^(){}]+)\)\}', line)


def check_reading_text(text: str, label: str) -> int:
    """Check Markdown structures that can silently change mathematical meaning."""
    fenced = re.compile(r'^([`~]{3,}).*$')
    in_fence = None
    math_fence = False
    display = False
    table_width = None
    tables = 0
    tags = []
    for index, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        match = fenced.fullmatch(stripped)
        if match:
            mark = match[1]
            if in_fence is None:
                in_fence = mark[0]
                math_fence = stripped[len(mark):].strip() == 'math'
            elif mark[0] == in_fence:
                in_fence = None
                math_fence = False
            table_width = None
            continue
        if in_fence:
            if math_fence:
                tags.extend(equation_labels(line, label, index))
            continue
        if stripped == '$$':
            display = not display
            table_width = None
            continue
        if display:
            tags.extend(equation_labels(line, label, index))
            continue
        if stripped.startswith('|'):
            width = len(re.findall(r'(?<!\\)\|', stripped))
            if table_width is None:
                table_width = width
                tables += 1
            if width != table_width:
                raise AssertionError(f'{label}:{index}: inconsistent Markdown table cells')
        else:
            table_width = None
    if in_fence is not None:
        raise AssertionError(f'{label}: unclosed code fence')
    if display:
        raise AssertionError(f'{label}: unclosed display mathematics')
    if len(tags) != len(set(tags)):
        raise AssertionError(f'{label}: repeated equation label on one page')
    return tables


def check_release(root: Path) -> dict[str, int]:
    pages = [root/'README.md', root/'AGENTS.md', root/'llms.txt', *sorted((root/'docs').glob('*.md'))]
    tables = 0
    for page in pages:
        if page.is_symlink():
            raise AssertionError(f'Reading file is a symbolic link: {page}')
        tables += check_reading_text(page.read_text(), str(page.relative_to(root)))
    report = json.loads((root/'results/verification.json').read_text())
    if report.get('all_passed') is not True:
        raise AssertionError('Recorded verification does not explicitly report success')
    for suite in report['suites']:
        summary = suite['summary']
        flags = (summary.get('all_passed'), summary.get('all_assertions_passed'),
                 summary.get('summary', {}).get('all_passed'))
        if not any(flag is True for flag in flags):
            raise AssertionError(f"No explicit success flag: {suite['script']}")
    closure = next(x for x in report['suites'] if x['script'] == 'verify_scientific_closure.py')
    certificate = root/'results/scientific-closure.json'
    if hashlib.sha256(certificate.read_bytes()).hexdigest() != closure['output_sha256']:
        raise AssertionError('Tracked scientific certificates differ from the recorded executed output')
    return {'reading_files': len(pages), 'tables': tables, 'tracked_certificate_files': 1}


if __name__ == '__main__':
    print('PASS:', check_release(Path(__file__).resolve().parents[1]))
