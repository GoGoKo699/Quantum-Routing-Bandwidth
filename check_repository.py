"""Check navigation, math delimiters, source provenance, syntax and the learning map."""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from verify import SUITES
from tools.check_learning import check_learning

ROOT = Path(__file__).resolve().parent
CONTACT = 'This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).'

def anchors(text: str) -> set[str]:
    found = set()
    for line in text.splitlines():
        if re.match(r'^#{1,6} ', line):
            title = re.sub(r'^#{1,6} ', '', line).lower()
            found.add(re.sub(r'[^\w\- ]', '', title).replace(' ', '-'))
    return found

def main() -> None:
    if not __debug__:
        raise RuntimeError('Repository checks require Python assertions.')
    markdown = [ROOT/'README.md', ROOT/'AGENTS.md', ROOT/'llms.txt', *sorted((ROOT/'docs').glob('*.md'))]
    link_count = 0
    for path in markdown:
        text = path.read_text()
        clean = re.sub(r'```.*?```', '', text, flags=re.S)
        assert '\\[' not in clean and '\\]' not in clean, f'Use dollar math: {path}'
        assert len(re.findall(r'^\$\$$', clean, flags=re.M)) % 2 == 0, f'Unclosed display math: {path}'
        inline = re.sub(r'\$\$.*?\$\$', '', clean, flags=re.S)
        assert len(re.findall(r'(?<!\\)\$', inline)) % 2 == 0, f'Unclosed inline math: {path}'
        assert '/mnt/data/' not in text and 'sandbox:' not in text, f'Local runtime path in {path}'
        for target in re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', clean):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            resolved = (path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            assert resolved.is_relative_to(ROOT), f'Link leaves repository: {path}: {target}'
            assert resolved.exists(), f'Missing link: {path}: {target}'
            if parsed.fragment and resolved.suffix == '.md':
                assert unquote(parsed.fragment) in anchors(resolved.read_text()), f'Missing anchor: {target}'
            link_count += 1
    sources = [ROOT/'verify.py', ROOT/'check_repository.py', *sorted((ROOT/'checks').glob('*.py')), *sorted((ROOT/'tools').glob('*.py'))]
    for path in sources:
        ast.parse(path.read_text(), filename=str(path))
    result = json.loads((ROOT/'results/verification.json').read_text())
    assert result['all_passed']
    assert [x['script'] for x in result['suites']] == [x[0] for x in SUITES]
    expected_sources = {str(p.relative_to(ROOT)) for p in (ROOT/'checks').glob('*.py')}
    assert set(result['source_sha256']) == expected_sources, 'Unrecorded or removed check source'
    for name, expected in result['source_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected, f'Stale result: {name}'
    license_bytes = (ROOT/'LICENSE').read_bytes()
    blob = b'blob '+str(len(license_bytes)).encode()+b'\0'+license_bytes
    assert hashlib.sha1(blob).hexdigest() == 'e17a781bf47c4aadf18b68fc593846a1193b86c1'
    assert CONTACT in (ROOT/'README.md').read_text()
    keys = re.findall(r'@\w+\{([^,]+),', (ROOT/'references.bib').read_text())
    assert keys and len(keys) == len(set(keys)), 'Missing or duplicate bibliography keys'
    assert set(keys).issubset({x.upper() for x in anchors((ROOT/'docs/related-work.md').read_text())})
    learning = check_learning(ROOT)
    print(f'PASS: {len(markdown)} reading files, {link_count} local links, {len(sources)} Python files, {len(SUITES)} verified suites, {len(keys)} references and {learning["milestones"]} milestones.')

if __name__ == '__main__':
    main()
