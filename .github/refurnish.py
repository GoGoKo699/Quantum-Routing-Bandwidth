"""One-time, branch-confined migration; removed before the furnished revision is merged."""
from pathlib import Path
import os
import posixpath
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
assert os.environ.get('GITHUB_REPOSITORY') == 'GoGoKo699/Quantum-Routing-Bandwidth'
assert os.environ.get('GITHUB_REF') == 'refs/heads/refurnish/current-guidance-20261017'
assert subprocess.check_output(['git','rev-parse','HEAD^'],cwd=ROOT,text=True).strip() == '39ad350c7563f0908034eef21a0024bd6121df13'
subprocess.run(['git','diff','--exit-code','HEAD^','--','docs','checks','results','references.bib','requirements.txt','verify.py','LICENSE'],cwd=ROOT,check=True)

mapping = {
 'docs/bandwidth.md':'science/bandwidth.md',
 'docs/mixed-helpers.md':'science/mixed-helpers.md',
 'docs/entropy-flow.md':'science/entropy-flow.md',
 'docs/control-models.md':'science/control-models.md',
 'docs/accuracy-and-resources.md':'science/accuracy-and-resources.md',
 'docs/theorem-map.md':'science/theorem-map.md',
 'docs/learning.md':'learning/WATROUS_BRIDGE.md',
 'docs/learning-bridges.md':'learning/WORKED_EXAMPLES.md',
 'docs/milestones.md':'learning/MILESTONES.md',
 'docs/related-work.md':'references/RELATED_WORK.md',
 'references.bib':'references/references.bib',
 'docs/verification.md':'verification/README.md',
 'verify.py':'verification/run_all.py',
 'requirements.txt':'verification/requirements.txt',
 'docs/coaching.md':None,
}
for folder in ('checks','results'):
 for p in (ROOT/folder).iterdir():
  if p.is_file():mapping[str(p.relative_to(ROOT))]='verification/'+str(p.relative_to(ROOT))
original={src:(ROOT/src).read_bytes() for src in mapping}

def relink(text,old,new):
 def link(m):
  label,target=m[1],m[2]
  if re.match(r'[a-zA-Z][\w+.-]*:',target) or target.startswith('//'):return m[0]
  path,sep,frag=target.partition('#')
  full=posixpath.normpath(posixpath.join(posixpath.dirname(old),path)) if path else old
  dest=mapping.get(full,full)
  if dest is None:return label
  relative=posixpath.relpath(dest,posixpath.dirname(new) or '.') if dest!=new or path else ''
  return f'[{label}]({relative}{sep}{frag})'
 return re.sub(r'\[([^\]\n]+)\]\(([^\s)]+)\)',link,text)

for src,dst in mapping.items():
 if dst is None:continue
 raw=original[src]
 if src.endswith('.md'):raw=relink(raw.decode(),src,dst).encode()
 out=ROOT/dst;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(raw)

connections = [
 'A routing operation must preserve relative phases as well as populations. This is why the same hardware is tested on unknown quantum data rather than a known classical label.',
 'The partial trace forgets correlations. The reference-assisted routing test later distinguishes outputs that have identical local density operators but carry different quantum information.',
 'Purification turns preservation of unknown information into preservation of entanglement. References supply a test of the operation without adding controllable qubits to the resource budget.',
 'A normalized Choi state describes one complete channel test; an inserted helper preparation instead fixes part of a larger isometry. Keeping these representations separate prevents the helper promise from becoming an arbitrary-input promise.',
 'Watrous uses root fidelity, whereas the verification programs report squared pure-target overlaps. The square and the trace-distance factor matter when transporting an accuracy bound into the converse.',
 'The diamond norm allows an inaccessible reference to accompany any payload input. The fixed helper purification makes joint restoration part of the output comparison without granting control of the preparation reference.',
 'Internal unitaries can concentrate polarization locally but cannot change the physical state\'s total entropy deficit. That conservation law remains available even when the control sequence is unrestricted.',
 'Relative entropy to a normalized exponential operator bounds a state-weighted second moment. This variational step connects preparation quality to usable interaction strength without requiring simultaneous diagonalization.',
 'An approximate swap must still establish mutual information between the payload/reference subsystems on opposite sides. Choosing those subsystems removes an unnecessary continuity penalty proportional to the helper count.',
 'Orthogonal Pauli coefficients add quadratically under normalized trace, while aligned extremal eigenvalues may add linearly. The proof needs the former together with the actual state\'s spectral weight, not an input-uniform replacement for operator norm.',
 'Treating module unitaries as instantaneous isolates the interface resource. Charging their duration changes the comparator, just as replacing individual contact bounds by an aggregate strength bound changes the theorem.',
 'A reversible basis permutation changes where a spectrum is supported, not its eigenvalues. A prescribed product of commuting conjugated evolutions then realizes a Hamiltonian average coherently, rather than randomizing the output channel.',
 'The probability of an entire zero-prefix subspace is the useful preparation promise. It controls a coherent operation on all payload inputs even though the compressed prefix bits need not be independently pure.',
 'The two helper tasks keep payload, contacts, allowed internal processing, and restoration obligations fixed. Identifying the one altered input promise is necessary before calling their times a resource separation.',
 'The bus dimension limits the conditional-log fluctuation factor even when the register includes large references. The remaining state-weighted interaction factor is where geometry and initialization enter.',
 'Cut-local terms cannot change the cut entropy. Removing them by an orthogonal coefficient projection is justified in normalized Frobenius norm, avoiding an unsupported operator-norm step.',
 'Gaussian-type spectral tails constrain the contact, while relative entropy constrains the evolving state. Their combination prevents unlimited internal processing from concentrating arbitrary weight in the strongest part of the spectrum.',
 'The payload marginals can remain maximally mixed throughout a perfect exchange. The reference cut reveals the required transfer through correlations and gives a payload-sized condition for approximate success.',
 'Integrating a state-dependent rate gives a lower bound on every permitted schedule, not merely on the constructed protocol. The ensemble version retains its common-input-control condition and permits specially prepared states outside that premise.',
 'The encoding separates the target\'s sign from the spectators\' magnitude. Because it is a bijection, the spectators\' unknown information is retained rather than erased to obtain the larger contact.',
 'Each block only needs a uniform marginal list because the contact is additive over blocks. Commutation then gives an exact finite-time operator identity, and reference preservation follows from identity on the spectator factors.',
 'Clean leaders can be reversibly correlated with the target so their block strengths add. The balanced partition relates this local mechanism to the total number of contacts and initialized helpers.',
 'A local gate identity becomes useful for routing only when the complete wire permutation, its phase, and the bus\'s original information are restored. The buffered sequence meets those requirements without a clean-bus assumption.',
 'An upper bound alone demonstrates feasibility; the entropy lower bound limits every admissible alternative. Their common exponent establishes optimal interaction-time scaling for each exact helper promise.',
 'Reversible concentration transfers entropy into qubits that the contact amplifier can use as occupied spectators. No pure qubits are created by a reset, and small bias is handled by the same bound or the no-concentration fallback.',
 'All gates are correct on the same invariant preparation sector with one common phase. This is why initial preparation error need not add gate by gate, whereas new control errors have a separate composition bound.',
 'The quantity one plus the total iid entropy deficit joins the unknown-helper and polarized-helper regimes. Uniformity in the bias is separate from uniformity as the allowed error tends to zero.',
 'Full rank forces every eigenstate component to implement the exact unitary when zero error is required. At nonzero error, spectral concentration permits discarding only a small weight in the error analysis; a broad maximally mixed component can prevent that concentration.',
 'A finite construction beats the full comparator class only when its upper bound lies below the class\'s lower bound. The resource analysis then determines whether that comparison concerns contact time, count, quadratic strength, or a fixed sum of strengths.',
 'The result joins a reference-assisted information requirement, a conserved preparation budget, and a coherent realization. Its significance is a matched interface-resource law with explicit initialization and accuracy assumptions, not an assertion of faster noisy hardware.'
]
p=ROOT/'learning/MILESTONES.md';text=p.read_text()
body=text[text.index('## Background and preliminaries'):text.index('## Completion')]
body=re.sub(r' \*\*Teaching intensity:\*\* [123]\.', '', body)
parts=list(re.finditer(r'^### (M\d{2})\.',body,re.M));out=[]
assert len(parts)==len(connections)==30
for i,h in enumerate(parts):
 end=parts[i+1].start() if i+1<len(parts) else len(body)
 section=body[h.start():end]
 section=section.replace('**Sources:**','**Conceptual connection:** '+connections[i]+'\n\n**Sources:**',1)
 out.append(section)
body=body[:parts[0].start()]+''.join(out)
intro='''# Thirty milestones for understanding routing bandwidth

**Map identifier: QRB-W18-30-v1.** The map contains exactly **30 project-defined milestones: 14 background/preliminary targets and 16 narrative/innovation targets**. Its questions, dependencies, and understanding targets are common to every reader.

The background connects quantum states, references, channels, entropy, spectral tools, probability, and the physical control model. M14 assembles those objects into the complete operational comparison. The narrative then joins a local information-flow estimate and a coherent contact construction into matching bandwidth laws; M30 integrates the results, their meaning, and their boundaries. This allocation follows the routing problem, not a textbook table of contents or a reader's assessment history.

The single educational anchor is John Watrous's *The Theory of Quantum Information*. The [Watrous bridge](WATROUS_BRIDGE.md) supplies section pointers and notation translations; [worked examples](WORKED_EXAMPLES.md) connect them to the research. The [scientific account](../science/README.md) owns the exact statements and proofs.

Each milestone has a central question, understanding target, earlier dependencies, conceptual connection, source pointers, and story role. Together they support understanding of the full contribution; specialist details remain in the linked proofs.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M06 | Unknown data, inaccessible references, complete operations, and accuracy |
| Background/preliminaries | M07–M14 | Entropy, spectral resources, and dynamical controls assembled into the task |
| Narrative/innovation | M15–M19 | Interface entropy rate, contact geometry, and the extensive-payload converse |
| Narrative/innovation | M20–M24 | Spectator-preserving amplification and matching exact endpoints |
| Narrative/innovation | M25–M28 | Imperfect initialization, joint restoration, and the limits of entropy-only reasoning |
| Narrative/innovation | M29–M30 | Finite certificates, resource normalization, attribution, and the full physical story |

'''
p.write_text(intro+body.rstrip()+'\n\n## Integration\n\nM14 joins the background into the precise routing task. M30 joins the converse, construction, accuracy convention, and resource boundaries into the complete scientific account. Continue from the map to the [proof dependencies](../science/theorem-map.md) or the [physical interpretation](../science/interpretation.md) for a connected specialist reading.\n')

p=ROOT/'learning/WATROUS_BRIDGE.md';text=p.read_text()
text=text.replace('| Receive guided instruction | Coaching protocol, following the same milestone map |\n','')
text=re.sub(r'The map is project-defined,.*?\n\n## Anchor and access','The map organizes the scientific dependencies for any reader. The selected sections provide a targeted route into the work; specialist details remain in the linked scientific proofs.\n\n## Anchor and access',text,flags=re.S)
text=text.replace('Progress and attempted answers belong to the learner\'s session, not these public source files. Merely reading or opening this guide does not pass a milestone.','The [physical interpretation](../science/interpretation.md) combines the three bridges into the resource comparison. The proofs, rather than these examples, establish the universal statements.')
p.write_text(text)
p=ROOT/'science/theorem-map.md';text=p.read_text()
text=re.sub(r'## 7\. Exposition structure\n.*?\n## 8\. Quantitative accuracy and resource guarantees','## 7. Physical synthesis\n\nThe [interpretation](interpretation.md) connects the interface geometry, reusable initialization, and complete-operation error to the exact endpoints and resource-budget comparisons. It separates achievable bandwidth from finite-control runtime.\n\n## 8. Quantitative accuracy and resource guarantees',text,flags=re.S)
p.write_text(text)
p=ROOT/'verification/run_all.py';text=p.read_text().replace('ROOT = Path(__file__).resolve().parent','ROOT = Path(__file__).resolve().parent.parent\nCHECKS = ROOT/\'verification\'/\'checks\'').replace("ROOT/'checks'","CHECKS")
p.write_text(text)
p=ROOT/'verification/checks/verify_entropy_budget.py';p.write_text(p.read_text().replace('proof in docs/bandwidth.md','proof in science/bandwidth.md'))
p=ROOT/'verification/README.md';text=p.read_text().replace('python -m pip install -r requirements.txt','python -m pip install -r verification/requirements.txt').replace('python tools/test_release_checks.py','python verification/tools/test_structure.py').replace('python verify.py','python verification/run_all.py').replace('python tools/inspect_hosted_render.py','python verification/tools/inspect_hosted_render.py')
text=text.replace('The verifier copies check sources','Run the commands from the repository root. The scientific programs are in `verification/checks/`; the runner copies check sources')
text=text.replace('Twelve regression tests exercise valid input and deliberately malformed material, including a ready-but-invalid native MathML layout;','Structural regression tests exercise valid input and deliberately malformed material, including a ready-but-invalid native MathML layout and a shared learning map contaminated by personal assessment rules;')
text=text.replace('opens thirteen actual public GitHub pages','opens the root README and every science, learning, reference, and verification Markdown page')
text=text.replace('Update tracked scientific results only from a successful associated run after changing scientific check sources.','Update tracked scientific provenance only from a successful associated run when paths or source programs change. Preserve numerical certificate bytes when their calculation is unchanged.')
p.write_text(text)
p=ROOT/'README.md';p.write_text(p.read_text().replace('How much reusable initialization increases the amount','How much does reusable initialization increase the amount'))
(ROOT/'.gitignore').write_text('__pycache__/\n*.py[cod]\n.venv/\nbuild/\nverification/checks/*.json\n.pytest_cache/\n')
# This migration changes no scientific assertion or displayed formula in the
# five canonical proof pages; verify that invariant before deleting old paths.
for name in ('bandwidth','mixed-helpers','entropy-flow','control-models','accuracy-and-resources'):
 before=original[f'docs/{name}.md'].decode();after=(ROOT/f'science/{name}.md').read_text()
 norm=lambda s:re.sub(r'\]\([^\s)]+\)','](LINK)',s)
 assert norm(before)==norm(after),f'Proof changed beyond links: {name}'
for folder in ('docs','checks','results','tools'):
 shutil.rmtree(ROOT/folder)
for name in ('verify.py','references.bib','requirements.txt'):
 (ROOT/name).unlink()
print('Migration complete; canonical scientific text unchanged except link destinations.')
