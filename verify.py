"""Run deterministic research checks in isolation and record an auditable summary."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
SUITES = (
    ('verify_workspace_construction.py', 'verify_workspace_construction.json'),
    ('verify_entropy_budget.py', 'verify_entropy_budget.json'),
    ('audit_conditional_rate.py', 'audit_conditional_rate.json'),
    ('audit_ensemble_cut.py', 'audit_ensemble_cut.json'),
    ('audit_translation_approximation.py', 'audit_translation_approximation.json'),
    ('recursive_three.py', 'recursive_three.json'),
    ('verify_finite_control.py', 'finite_control_results.json'),
    ('verify_full_nine.py', 'verify_full_nine.json'),
    ('verify_mixed_helpers.py', 'verify_mixed_helpers.json'),
    ('verify_scientific_closure.py', 'verify_scientific_closure.json'),
)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'build'/'verification')
    args = parser.parse_args()
    if not __debug__ or os.environ.get('PYTHONOPTIMIZE'):
        parser.error('Assertions are part of verification; do not enable Python optimization.')
    output = args.output.resolve()
    if output == ROOT or output == ROOT/'checks':
        parser.error('Use a dedicated output directory.')
    output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    report = {'scope': 'Deterministic numerical consistency checks; not independent proof review or hardware data.',
              'python': platform.python_version(), 'platform': platform.platform(), 'suites': [],
              'source_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in sorted((ROOT/'checks').glob('*.py'))}}
    for package in ('numpy', 'scipy'):
        report[package] = __import__(package).__version__
    with tempfile.TemporaryDirectory(prefix='qrb-checks-') as temporary:
        work = Path(temporary)
        for p in (ROOT/'checks').glob('*.py'):
            shutil.copy2(p, work/p.name)
        for script, filename in SUITES:
            print(f'Running {script}', flush=True)
            started = time.monotonic()
            run = subprocess.run([sys.executable, script], cwd=work, env=env,
                                 capture_output=True, text=True, timeout=300)
            log = output/(Path(script).stem+'.log')
            log.write_text(run.stdout+run.stderr)
            if run.returncode:
                raise RuntimeError(f'{script} failed; inspect {log}')
            data = json.loads((work/filename).read_text())
            if not (data.get('all_passed') or data.get('all_assertions_passed') or data.get('summary', {}).get('all_passed')):
                raise RuntimeError(f'{script} did not report success')
            shutil.copy2(work/filename, output/filename)
            brief = {k:v for k,v in data.items() if not isinstance(v, list)}
            for k,v in data.items():
                if isinstance(v, list):
                    brief[k+'_count'] = len(v)
            if script == 'verify_workspace_construction.py':
                brief['max_swap_isometry_error'] = max(x['isometry_operator_error'] for x in data['gate'])
                brief['max_route_isometry_error'] = max(x['isometry_operator_error'] for x in data['route'])
                brief['largest_route'] = max(data['route'], key=lambda x:x['physical_qubits'])
            if script == 'verify_mixed_helpers.py':
                brief['max_good_subspace_error'] = max(x['maximum_good_subspace_error'] for x in data['complete_routes'])
                brief['max_helper_block_leakage'] = max(x['maximum_helper_block_leakage'] for x in data['complete_routes'])
            report['suites'].append({'script': script, 'elapsed_seconds': round(time.monotonic()-started,3),
                                     'output_sha256': hashlib.sha256((output/filename).read_bytes()).hexdigest(),
                                     'summary': brief})
            print(f'PASS {script}', flush=True)
    report['all_passed'] = True
    (output/'summary.json').write_text(json.dumps(report, indent=2)+'\n')
    print(f'All {len(SUITES)} suites passed. Results: {output}', flush=True)

if __name__ == '__main__':
    main()
