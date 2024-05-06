import bs4
import sys
import os
import argparse
from glob import glob
from .formatters import formatters


def get_required_libraries(soup: bs4.BeautifulSoup) -> set[str]:
    libs = set()
    for element in soup.find_all(attrs={"dj-libs": True}):
        libs |= set(element.get("dj-libs").split(";"))
        del element.attrs["dj-libs"]
    return libs


def convert_file(path: str, overwrite: bool = False) -> None:
    with open(path, "r") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

    required_libraries = get_required_libraries(soup)

    for formatter in formatters:
        formatter.format(soup)

    if overwrite:
        out_path = path
    else:
        out_path = path.replace(".html", ".n.html")
    with open(out_path, "w") as file:
        for lib in required_libraries:
            file.write(f"{{% load {lib} %}}\n")
        file.write(soup
                   .prettify(formatter=bs4.formatter.HTMLFormatter(indent=4))
                   .replace("&quot;", '"'))  # Could this cause any issues? (maybe in attributes)


def convert_dir(path: str, overwrite: bool = False) -> None:
    for filepath in glob(f"{path}/**/*.html", recursive=True):
        convert_file(filepath, overwrite)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("html_to_django")
    parser.add_argument("path", help="""
    The path to a file (or folder of files) to be converted.
    In case a folder is passed, ALL html files in it (recursivly) will be converted.
    """, type=str)
    parser.add_argument("-r", "--replace", help="""
    Replace the input file(s).
    """, action='store_true')
    return parser.parse_args()


def command_entry() -> None:
    args = parse_args()
    path = os.path.abspath(args.path)
    if os.path.isdir(path):
        convert_dir(path, args.replace)
    elif os.path.isfile(path):
        convert_file(path, args.replace)
    else:
        sys.exit(f'The path "{path}" does not exist.')
