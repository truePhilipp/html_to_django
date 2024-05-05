from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-command": True}):
        element.string = f"{{% {element.get("dj-command")} %}}"
        element.unwrap()
