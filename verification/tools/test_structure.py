"""Structural regressions; not additional scientific verification suites."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from check_release import check_reading_text, check_release
from check_learning import validate_map, check_learning
from inspect_hosted_render import snapshot_problems, source_math_count, page_names

ROOT = Path(__file__).resolve().parents[2]


class ReadingChecks(unittest.TestCase):
    def test_valid_table_and_math(self):
        text = '| A | B |\n|---|---|\n| $`\\lvert x\\rangle`$ | y |\n\n```math\nx\\qquad\\text{(1)}\n```\n'
        self.assertEqual(check_reading_text(text,'fixture'),1)

    def test_unescaped_pipe(self):
        with self.assertRaisesRegex(AssertionError,'table cells'):
            check_reading_text('| A | B |\n|---|---|\n| $|x\\rangle$ | y |\n','fixture')

    def test_unsafe_numbering(self):
        with self.assertRaisesRegex(AssertionError,'unsafe native'):
            check_reading_text('```math\nx\\tag{1}\n```','fixture')

    def test_duplicate_label(self):
        with self.assertRaisesRegex(AssertionError,'repeated equation'):
            check_reading_text('$$\nx\\text{(1)}\n$$\n\n```math\ny\\text{(1)}\n```','fixture')

    def test_nonmath_fence(self):
        self.assertEqual(check_reading_text('```text\n| a |\n| a | b |\n$$\n```','fixture'),0)

    def test_unclosed_fence(self):
        with self.assertRaisesRegex(AssertionError,'code fence'):
            check_reading_text('```python\nx=1','fixture')

    def test_short_closing_fence(self):
        with self.assertRaisesRegex(AssertionError,'code fence'):
            check_reading_text('````text\nx\n```','fixture')

    def test_unclosed_display(self):
        with self.assertRaisesRegex(AssertionError,'display mathematics'):
            check_reading_text('$$\nx','fixture')

    def test_result_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ('science','learning','references','verification/results'):
                (root/folder).mkdir(parents=True)
            for name in ('README.md','AGENTS.md','llms.txt','verification/README.md'):
                (root/name).write_text('# Fixture\n')
            raw = b'{"all_passed":true}\n'
            path = root/'verification/results/scientific-closure.json'
            path.write_bytes(raw)
            result = {'all_passed':True,'suites':[{'script':'verify_scientific_closure.py','output_sha256':hashlib.sha256(raw).hexdigest(),'summary':{'all_passed':True}}]}
            record = root/'verification/results/verification.json'
            record.write_text(json.dumps(result))
            self.assertEqual(check_release(root)['tracked_certificate_files'],1)
            path.write_bytes(raw+b' ')
            with self.assertRaisesRegex(AssertionError,'certificates differ'):
                check_release(root)
            path.write_bytes(raw)
            result['suites'][0]['summary']['all_passed']='true'
            record.write_text(json.dumps(result))
            with self.assertRaisesRegex(AssertionError,'explicit suite success'):
                check_release(root)


class HostedChecks(unittest.TestCase):
    def state(self):
        return {'article':True,'heading':'Title','markers':1,'ready':1,'errors':[],
                'marker_errors':0,'native_layout_errors':[],'literal_math_lines':[],
                'page_width':390,'table_columns':[[2,2]]}

    def test_ready_valid(self):
        self.assertEqual(snapshot_problems(self.state(),1,'Title',390),[])

    def test_ready_invalid_native(self):
        state = self.state();state['native_layout_errors']=[{'element':'mlabeledtr'}]
        self.assertTrue(any('native MathML' in p for p in snapshot_problems(state,1,'Title',390)))

    def test_unfinished(self):
        state=self.state();state['ready']=0
        self.assertTrue(snapshot_problems(state,1,'Title',390))

    def test_overflow_and_table(self):
        state=self.state();state['page_width']=500;state['table_columns']=[[2,3]]
        self.assertEqual(len(snapshot_problems(state,1,'Title',390)),2)

    def test_math_count(self):
        self.assertEqual(source_math_count('$`x_1`$\n\n```math\ny\n```\n\n$$z$$'),3)

    def test_new_pages(self):
        names=page_names(ROOT)
        self.assertIn('science/interpretation.md',names)
        self.assertIn('learning/MILESTONES.md',names)
        self.assertFalse(any('docs/' in name or 'coaching' in name for name in names))


class LearningChecks(unittest.TestCase):
    def text(self):
        return (ROOT/'learning/MILESTONES.md').read_text()

    def test_current_map(self):
        result=check_learning(ROOT)
        self.assertEqual((result['milestones'],result['background'],result['narrative']),(30,14,16))

    def test_missing_connection(self):
        with self.assertRaisesRegex(AssertionError,'Conceptual connection'):
            validate_map(self.text().replace('**Conceptual connection:**','**Other:**',1))

    def test_forward_dependency(self):
        with self.assertRaisesRegex(AssertionError,'Forward/cyclic'):
            validate_map(self.text().replace('**Dependencies:** M01.','**Dependencies:** M30.',1))

    def test_personal_procedure(self):
        with self.assertRaisesRegex(AssertionError,'Personal assessment'):
            validate_map(self.text()+'\nTeaching intensity: 3 learning rounds.\n')

    def test_missing_milestone(self):
        with self.assertRaisesRegex(AssertionError,'exactly M01'):
            validate_map(self.text().replace('### M30.','### M31.'))


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Structural tests require assertions.')
    unittest.main()
