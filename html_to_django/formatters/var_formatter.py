"""
Find tags with a "dj-var" attribute and replace its content with the
value enclosed in {{ }}.
"""


from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-var": True}):
        element.string = f"{{{{ {element.get("dj-var")} }}}}"
        del element.attrs["dj-var"]
