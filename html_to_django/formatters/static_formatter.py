from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-static": True}):
        tag, value = element.get("dj-static").split(";")
        element[tag] = f"{{% static '{value}' %}}"
        del element.attrs["dj-static"]
