from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-for": True}):
        element.insert_before(f"{{% for {element.get("dj-for")} %}}")
        element.insert_after("{% endfor %}")
        element.unwrap()
