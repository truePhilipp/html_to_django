from bs4 import BeautifulSoup
from .style_formatter import parse_style, style_to_string


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-style-raw": True}):
        style = parse_style(element["style"])
        dj_style = element.get("dj-style-raw")
        for name, value in [declaration.split(";") for declaration in dj_style.split("~") if declaration]:
            style[name] = value
        element["style"] = style_to_string(style)
        del element.attrs["dj-style-raw"]
