import os
import filecmp
import shutil
from unittest import TestCase
from html_to_django import converter


class ConverterTests(TestCase):
    def test_convert_file(self) -> None:
        shutil.copytree(
            os.path.abspath("tests/test_project"),
            os.path.abspath("tests/test_project_test_result"),
            dirs_exist_ok=True
        )
        converter.convert_file(
            os.path.abspath("tests/test_project_test_result/test.html")
        )
        self.assertTrue(filecmp.cmp(
            os.path.abspath("tests/test_project_test_result/test.n.html"),
            os.path.abspath("tests/test_project_expected_result/test.n.html")
        ))
