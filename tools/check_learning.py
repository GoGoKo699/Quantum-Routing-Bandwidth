"""Validate the common learning map; this does not assess learner progress."""
from __future__ import annotations
from pathlib import Path
import re


def check_learning(root: Path) -> dict[str, int]:
    text = (root/'docs/milestones.md').read_text()
    headers = list(re.finditer(r'^### (M\d{2})\. (.+)$', text, re.M))
    expected = [f'M{i:02d}' for i in range(1, 31)]
    assert [h[1] for h in headers] == expected, 'Expected exactly M01-M30 in order'
    split = text.index('## Narrative and innovation')
    assert sum(h.start() < split for h in headers) == 14, 'Background allocation changed'
    assert sum(h.start() > split for h in headers) == 16, 'Narrative allocation changed'
    assert 'QRB-W18-30-v1' in text
    edges = 0
    for i, header in enumerate(headers):
        end = headers[i+1].start() if i+1 < len(headers) else len(text)
        section = text[header.end():end]
        for field in ('Central question', 'Understanding target', 'Dependencies', 'Sources', 'Story role'):
            assert f'**{field}:**' in section, f'{header[1]} lacks {field}'
        match = re.search(r'\*\*Dependencies:\*\* (.*?)\. \*\*Teaching intensity:\*\* ([123])\.', section)
        assert match, f'{header[1]} lacks valid dependencies/intensity'
        deps = re.findall(r'M\d{2}', match[1])
        assert len(deps) == len(set(deps))
        assert all(d in expected[:i] for d in deps), f'{header[1]} has forward/cyclic dependency'
        assert deps or (i == 0 and match[1] == 'None')
        sources = section.split('**Sources:**', 1)[1].split('\n', 1)[0]
        assert re.search(r'\[[^\]]+\]\([^\s)]+\)', sources), f'{header[1]} needs a source pointer'
        edges += len(deps)
    learning = (root/'docs/learning.md').read_text()
    coaching = (root/'docs/coaching.md').read_text()
    agents = (root/'AGENTS.md').read_text()
    for name in ('README.md', 'llms.txt'):
        entry = (root/name).read_text()
        for target in ('docs/milestones.md', 'docs/learning.md', 'docs/coaching.md'):
            assert target in entry, f'{name} omits {target}'
    assert 'John Watrous' in learning and '2018' in learning
    assert 'https://jhwatrous.github.io/TQI.errata.pdf' in learning
    assert 'docs/coaching.md' in agents and 'docs/milestones.md' in agents
    assert 'q=\\min(2+f,6)' in coaching
    assert '1–3 targeted learning rounds' in coaching
    assert '60 challenge questions' in coaching
    assert 'M01–M30' in coaching
    assert '<details>' not in learning, 'Do not reintroduce a competing expandable-answer course'
    # Raw pipes inside a math cell can split a GitHub Markdown table before
    # MathJax sees it. Keep cell delimiters unambiguous in the new reading pages.
    for name in ('README.md', 'docs/learning.md', 'docs/learning-bridges.md'):
        columns = None
        for line in (root/name).read_text().splitlines():
            if line.startswith('|'):
                count = len(re.findall(r'(?<!\\)\|', line))
                columns = count if columns is None else columns
                assert count == columns, f'Ambiguous table pipe in {name}: {line}'
            else:
                columns = None
    # Link destinations, math, and bibliography are checked across the full repository
    # by check_repository.py. Here we check the map's fields and dependency graph.
    return {'milestones': len(headers), 'background': 14, 'narrative': 16, 'dependency_edges': edges}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Learning-map checks require Python assertions.')
    print('PASS:', check_learning(Path(__file__).resolve().parents[1]))
