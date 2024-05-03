from unittest import TestCase
from bs4 import BeautifulSoup
from html_to_django.formatters import block_formatter


class BlockTests(TestCase):
    def test_basic(self):
        soup = BeautifulSoup('<div dj-block="content"></div>', "html.parser")
        block_formatter.format(soup)
        self.assertEqual("{% block content %}{% endblock %}", str(soup))
    
    def test_with_content(self):
        soup = BeautifulSoup('<div dj-block="content">Test</div>', "html.parser")
        block_formatter.format(soup)
        self.assertEqual("{% block content %}Test{% endblock %}", str(soup))
    
    def test_with_block_inside(self):
        soup = BeautifulSoup('<div dj-block="content"><div dj-block="inner">Test</div></div>', "html.parser")
        block_formatter.format(soup)
        self.assertEqual("{% block content %}{% block inner %}Test{% endblock %}{% endblock %}", str(soup))