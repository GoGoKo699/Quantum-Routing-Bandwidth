"""Validate the reader-independent 30-milestone map and public learning boundary."""
from __future__ import annotations
from pathlib import Path
import re

MAP_ID = 'QRB-W18-30-v1'
PERSONAL = re.compile(r'Revise\s*(?:→|->|–|-)\s*Learn|teaching intensity|learning rounds|challenge questions|failed challenges|retry rules|question count|passing requirement', re.I)

def validate_map(text: str) -> dict[str, int]:
    headers = list(re.finditer(r'^### (M\d{2})\. (.+)$', text, re.M))
    expected = [f'M{i:02d}' for i in range(1, 31)]
    assert [h[1] for h in headers] == expected, 'Expected exactly M01-M30 in order'
    assert MAP_ID in text, 'Missing stable map identifier'
    split = text.index('## Narrative and innovation')
    assert sum(h.start() < split for h in headers) == 14, 'Background allocation changed'
    assert sum(h.start() > split for h in headers) == 16, 'Narrative allocation changed'
    assert not PERSONAL.search(text), 'Personal assessment procedure in the common map'
    edges = 0
    for i, h in enumerate(headers):
        end = headers[i+1].start() if i+1 < len(headers) else len(text)
        section = text[h.end():end]
        for field in ('Central question', 'Understanding target', 'Dependencies', 'Conceptual connection', 'Sources', 'Story role'):
            assert f'**{field}:**' in section, f'{h[1]} lacks {field}'
        dep = re.search(r'\*\*Dependencies:\*\* ([^\n]+)', section)
        assert dep, f'{h[1]} lacks dependencies'
        ids = re.findall(r'M\d{2}', dep[1])
        assert len(ids) == len(set(ids)) and all(d in expected[:i] for d in ids), 'Forward/cyclic dependency'
        assert ids or (i == 0 and dep[1].strip() == 'None.'), 'Missing prerequisite'
        sources = section.split('**Sources:**', 1)[1].split('\n', 1)[0]
        assert re.search(r'\[[^\]]+\]\([^\s)]+\)', sources), 'Missing scientific source pointer'
        connection = section.split('**Conceptual connection:**', 1)[1].split('\n', 1)[0]
        assert len(connection.split()) >= 12, 'Conceptual connection is not explanatory'
        edges += len(ids)
    return {'milestones': 30, 'background': 14, 'narrative': 16, 'dependency_edges': edges}

def check_learning(root: Path) -> dict[str, int]:
    report = validate_map((root/'learning/MILESTONES.md').read_text())
    for p in (root/'learning').glob('*.md'):
        assert not PERSONAL.search(p.read_text()), f'Personal assessment procedure in {p.name}'
    for name in ('README.md', 'llms.txt'):
        text = (root/name).read_text()
        for target in ('learning/MILESTONES.md', 'learning/WATROUS_BRIDGE.md', 'science/README.md', 'verification/README.md'):
            assert target in text, f'{name} omits {target}'
    anchor = (root/'learning/WATROUS_BRIDGE.md').read_text()
    assert 'John Watrous' in anchor and '2018' in anchor
    assert 'https://jhwatrous.github.io/TQI.errata.pdf' in anchor
    assert not (root/'docs').exists(), 'Obsolete documentation tree retained'
    assert not any('coach' in p.name.lower() for p in root.rglob('*.md') if 'build' not in p.parts), 'Public personal guide retained'
    return report
