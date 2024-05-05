from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-include": True}):
        element.string = f'{{% include "{element.get("dj-include")}" %}}'
        del element.attrs["dj-include"]
