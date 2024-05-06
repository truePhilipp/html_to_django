from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-attr": True}):
        for tag, value in [attr.split(";") for attr in element["dj-attr"].split("~")]:
            element[tag] = f"{{{{ {value} }}}}"
        del element.attrs["dj-attr"]
