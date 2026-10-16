"""Regression tests for release validation, distinct from scientific suites."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from check_release import check_reading_text, check_release
from inspect_hosted_render import snapshot_problems


class ReadingChecks(unittest.TestCase):
    def test_valid_math_and_table(self):
        text = '| A | B |\n|---|---|\n| $\\lvert x\\rangle$ | $\\lVert X\\rVert$ |\n\n$$\n|x|\\qquad\\text{(1)}\n$$\n'
        self.assertEqual(check_reading_text(text, 'fixture'), 1)

    def test_unescaped_ket_in_table(self):
        with self.assertRaisesRegex(AssertionError, 'table cells'):
            check_reading_text('| A | B |\n|---|---|\n| $|x\\rangle$ | yes |\n', 'fixture')

    def test_duplicate_label(self):
        with self.assertRaisesRegex(AssertionError, 'repeated equation'):
            check_reading_text('$$\nx\\qquad\\text{(1)}\n$$\n\n$$\ny\\qquad\\text{(1)}\n$$\n', 'fixture')

    def test_labels_in_math_fences(self):
        with self.assertRaisesRegex(AssertionError, 'repeated equation'):
            check_reading_text('```math\nx\\qquad\\text{(1)}\n```\n\n```math\ny\\qquad\\text{(1)}\n```\n', 'fixture')

    def test_fenced_examples_are_not_tables(self):
        self.assertEqual(check_reading_text('```text\n| a |\n| a | b |\n$$\n```\n', 'fixture'), 0)

    def test_unclosed_fence(self):
        with self.assertRaisesRegex(AssertionError, 'code fence'):
            check_reading_text('```python\nx=1\n', 'fixture')

    def test_unclosed_math(self):
        with self.assertRaisesRegex(AssertionError, 'display mathematics'):
            check_reading_text('$$\nx\n', 'fixture')

    def test_result_integrity_and_explicit_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'docs').mkdir(); (root/'results').mkdir()
            for name in ('README.md', 'AGENTS.md', 'llms.txt'):
                (root/name).write_text('# Fixture\n')
            content = b'{"all_passed": true}\n'
            path = root/'results/scientific-closure.json'; path.write_bytes(content)
            result = {'all_passed': True, 'suites': [{'script': 'verify_scientific_closure.py',
                'output_sha256': hashlib.sha256(content).hexdigest(), 'summary': {'all_passed': True}}]}
            summary = root/'results/verification.json'; summary.write_text(json.dumps(result))
            self.assertEqual(check_release(root)['tracked_certificate_files'], 1)
            path.write_bytes(content+b' ')
            with self.assertRaisesRegex(AssertionError, 'certificates differ'):
                check_release(root)
            path.write_bytes(content)
            result['suites'][0]['summary']['all_passed'] = 'true'
            summary.write_text(json.dumps(result))
            with self.assertRaisesRegex(AssertionError, 'explicit success flag'):
                check_release(root)

    def test_legacy_tag_in_math_fence(self):
        with self.assertRaisesRegex(AssertionError, 'legacy equation tag'):
            check_reading_text('```math\nx=y\\tag{1}\n```\n', 'fixture')

    def test_legacy_tag_in_dollar_display(self):
        with self.assertRaisesRegex(AssertionError, 'legacy equation tag'):
            check_reading_text('$$\nx=y\\tag{1}\n$$\n', 'fixture')

    def test_ready_math_with_unsupported_layout_is_not_a_pass(self):
        state = {'heading': 'Fixture', 'markers': 1, 'ready': 1,
                 'page_width': 1180, 'errors': [], 'marker_errors': 0,
                 'native_layout_errors': [{'element': 'mlabeledtr'}]}
        self.assertEqual(snapshot_problems(state, 1, 'Fixture', 1180),
                         ['1180px: unsupported native MathML equation layout'])

    def test_valid_hosted_snapshot(self):
        state = {'heading': 'Fixture', 'markers': 1, 'ready': 1,
                 'page_width': 390, 'errors': [], 'marker_errors': 0,
                 'native_layout_errors': [], 'table_columns': [[2, 2]]}
        self.assertEqual(snapshot_problems(state, 1, 'Fixture', 390), [])


if __name__ == '__main__':
    unittest.main()
