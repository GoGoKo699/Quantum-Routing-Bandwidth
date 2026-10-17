"""Check canonical navigation, learning boundaries, syntax, and executed provenance."""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from verification.run_all import SUITES
from verification.tools.check_learning import check_learning
from verification.tools.check_release import check_release, reading_pages

ROOT = Path(__file__).resolve().parent
CONTACT = 'This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).'


def anchors(text: str) -> set[str]:
    found = set()
    occurrences = {}
    in_fence = False
    for line in text.splitlines():
        if line.startswith('```'):
            in_fence = not in_fence
        if not in_fence and re.match(r'^#{1,6} ', line):
            title = re.sub(r'^#{1,6} ', '', line).lower()
            slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
            count = occurrences.get(slug, 0)
            occurrences[slug] = count+1
            found.add(slug if count == 0 else f'{slug}-{count}')
    return found


def main() -> None:
    if not __debug__:
        raise RuntimeError('Repository checks require assertions.')
    pages = reading_pages(ROOT)
    links = 0
    for path in pages:
        text = path.read_text()
        clean = re.sub(r'```.*?```', '', text, flags=re.S)
        assert '/mnt/data/' not in text and 'sandbox:' not in text, f'Runtime path in {path}'
        assert not re.search(r'GoGoKo699/Guinevere|preferences/TUTORIALS', text), f'Private dependency in {path}'
        inline = re.sub(r'\$\$.*?\$\$', '', clean, flags=re.S)
        assert len(re.findall(r'(?<!\\)\$', inline)) % 2 == 0, f'Unclosed inline math: {path}'
        for target in re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', clean):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            assert dest.is_relative_to(ROOT), f'Link leaves repository: {target}'
            assert dest.exists(), f'Missing link in {path}: {target}'
            if parsed.fragment and dest.suffix == '.md':
                assert unquote(parsed.fragment) in anchors(dest.read_text()), f'Missing anchor in {path}: {target}'
            links += 1
    sources = [ROOT/'check_repository.py', ROOT/'verification/run_all.py',
               *sorted((ROOT/'verification/checks').glob('*.py')),
               *sorted((ROOT/'verification/tools').glob('*.py'))]
    for p in sources:
        ast.parse(p.read_text(), filename=str(p))
    result = json.loads((ROOT/'verification/results/verification.json').read_text())
    assert result.get('all_passed') is True
    assert [x['script'] for x in result['suites']] == [x[0] for x in SUITES], 'Incorrect suite coverage'
    expected = {str(p.relative_to(ROOT)) for p in (ROOT/'verification/checks').glob('*.py')}
    assert set(result['source_sha256']) == expected, 'Incorrect check-source coverage'
    for name, digest in result['source_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, f'Stale source record: {name}'
    license_bytes = (ROOT/'LICENSE').read_bytes()
    blob = b'blob '+str(len(license_bytes)).encode()+b'\0'+license_bytes
    assert hashlib.sha1(blob).hexdigest() == 'e17a781bf47c4aadf18b68fc593846a1193b86c1', 'License changed'
    assert CONTACT in (ROOT/'README.md').read_text()
    keys = re.findall(r'@\w+\{([^,]+),', (ROOT/'references/references.bib').read_text())
    assert keys and len(keys) == len(set(keys)), 'Invalid bibliography keys'
    assert set(keys).issubset({x.upper() for x in anchors((ROOT/'references/RELATED_WORK.md').read_text())})
    learning = check_learning(ROOT)
    release = check_release(ROOT)
    for old in ('docs', 'checks', 'results', 'manuscript', 'verify.py', 'references.bib', 'requirements.txt'):
        assert not (ROOT/old).exists(), f'Obsolete entrypoint retained: {old}'
    print(f'PASS: {len(pages)} reading files, {links} local links, {len(sources)} Python sources, {len(keys)} references, {len(SUITES)} scientific suites, {learning["milestones"]} milestones, {release["tables"]} tables.')


if __name__ == '__main__':
    main()
