"""Dependency-free reading syntax and executed-certificate integrity checks."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re


def reading_pages(root: Path) -> list[Path]:
    return [root/'README.md', root/'AGENTS.md', root/'llms.txt',
            *sorted((root/'science').glob('*.md')), *sorted((root/'learning').glob('*.md')),
            *sorted((root/'references').glob('*.md')), root/'verification/README.md']


def check_reading_text(text: str, label: str) -> int:
    fence = None
    math_fence = False
    display = False
    table_width = None
    tables = 0
    labels = []
    for index, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        match = re.fullmatch(r'([`~]{3,})(.*)', stripped)
        if match:
            marks, info = match.groups()
            if fence is None:
                fence = marks
                math_fence = info.strip() == 'math'
            elif marks[0] == fence[0] and len(marks) >= len(fence) and not info.strip():
                fence = None
                math_fence = False
            table_width = None
            continue
        if stripped == '$$' and fence is None:
            display = not display
            table_width = None
            continue
        if math_fence or display:
            assert not re.search(r'\\tag\*?\{', line), f'{label}:{index}: unsafe native equation numbering'
            labels += re.findall(r'\\text\{\((\d+)\)\}', line)
        if fence or display:
            continue
        if stripped.startswith('|'):
            width = len(re.findall(r'(?<!\\)\|', stripped))
            if table_width is None:
                table_width = width
                tables += 1
            assert width == table_width, f'{label}:{index}: inconsistent Markdown table cells'
        else:
            table_width = None
    assert fence is None, f'{label}: unclosed code fence'
    assert not display, f'{label}: unclosed display mathematics'
    assert len(labels) == len(set(labels)), f'{label}: repeated equation label'
    return tables


def check_release(root: Path) -> dict[str, int]:
    tables = 0
    pages = reading_pages(root)
    for page in pages:
        assert not page.is_symlink(), f'Reading file is a symbolic link: {page}'
        tables += check_reading_text(page.read_text(), str(page.relative_to(root)))
    report = json.loads((root/'verification/results/verification.json').read_text())
    assert report.get('all_passed') is True, 'No explicit overall success'
    for suite in report['suites']:
        summary = suite['summary']
        flags = (summary.get('all_passed'), summary.get('all_assertions_passed'), summary.get('summary', {}).get('all_passed'))
        assert any(f is True for f in flags), 'No explicit suite success flag'
    closure = next(x for x in report['suites'] if x['script'] == 'verify_scientific_closure.py')
    raw = (root/'verification/results/scientific-closure.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == closure['output_sha256'], 'Tracked certificates differ from executed output'
    return {'reading_files': len(pages), 'tables': tables, 'tracked_certificate_files': 1}
