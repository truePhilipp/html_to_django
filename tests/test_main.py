from html_to_django import main
from unittest import TestCase


class TestTocHTMLParser(TestCase):
    def test_command_entry(self):
        main.command_entry()
        self.assertEqual(0, 0)
