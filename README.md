# HTML To Django

![tests workflow](https://github.com/truePhilipp/html_to_django/actions/workflows/tests.yml/badge.svg)
![stylecheck workflow](https://github.com/truePhilipp/html_to_django/actions/workflows/stylecheck.yml/badge.svg)

Converts HTML files with special attributes to Django templates.


# Installation
TODO: pip install instructions


# Usage
```bash
html_to_django [-h] [-r] path
```
Use `-r` to replace the original files, instead of creating new ones.
By default, new ones are created in place next to the existing files, with the extension `.n.html`.

You can also use the `html_to_django_r` command if you are unable to pass the `-r` parameter
(e.g. with the Bootstrap Studio "Export Script" setting).

## Attributes
To add Django template tags to your HTML files, you need to add special attributes to your HTML tags like this:
```html
<div dj-for="user in users">
    <p>{{ user.name }}</p>
</div>
```
This will be converted to:
```html
{% for user in users %}
<p>{{ user.name }}</p>
{% endfor %}
```

A complete list can be found in the [Attributes.md](Attributes.md) file.


# Contributing
To learn how to contribute to this project, please see [CONTRIBUTING.md](CONTRIBUTING.md)
