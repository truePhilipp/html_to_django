HTML To Django
===

Convert HTML files with special syntax to Django template files.

Installation
---
TODO: pip install instructions

Usage
---
```bash
html_to_django <path to file or folder to convert>
```

Development
===

Testing
---
```bash
python -m unittest discover tests --verbose
```

Stylechecks
---
```bash
mypy --strict html_to_django
```
and
```bash
pycodestyle --max-line-length 120 html_to_django
```