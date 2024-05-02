from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-block": True}):
        element.insert_before(f"{{% block {element.get("dj-block")} %}}")
        element.insert_after("{% endblock %}")
        element.unwrap()
