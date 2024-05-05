from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-for-wrap": True}):
        element.insert_before(f"{{% for {element.get("dj-for-wrap")} %}}")
        element.insert_after("{% endfor %}")
        del element["dj-for-wrap"]
