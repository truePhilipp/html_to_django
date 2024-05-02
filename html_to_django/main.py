import bs4
from .formatters import formatters


def main() -> None:
    with open("test.html", "r") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

    for formatter in formatters:
        formatter.format(soup)

    with open("out.html", "w") as file:
        file.write("{% load static %}\n")
        file.write(soup.prettify(formatter=bs4.formatter.HTMLFormatter(indent=4)))


def command_entry() -> None:
    print("ok")
