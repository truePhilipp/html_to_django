from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-attr": True}):
        tag, value = element.get("dj-attr").split(";")
        element[tag] = f"{{{{ {value} }}}}"
        del element.attrs["dj-attr"]
