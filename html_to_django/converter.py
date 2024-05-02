import bs4
import sys
import os
from glob import glob
from .formatters import formatters


def convert_file(path: str, overwrite: bool = False) -> None:
    with open(path, "r") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

    for formatter in formatters:
        formatter.format(soup)

    if overwrite:
        out_path = path
    else:
        out_path = path.replace(".html", ".n.html")
    with open(out_path, "w") as file:
        file.write("{% load static %}\n")
        # indent=4 will be re added when https://github.com/python/typeshed/pull/11855 is accepted
        file.write(soup.prettify(formatter=bs4.formatter.HTMLFormatter()))


def convert_dir(path: str, overwrite: bool = False) -> None:
    for filepath in glob(f"{path}/**/*.html", recursive=True):
        convert_file(filepath, overwrite)


def command_entry() -> None:
    path = os.path.abspath(sys.argv[1])
    if os.path.isdir(path):
        convert_dir(path)
    elif os.path.isfile(path):
        convert_file(path)
