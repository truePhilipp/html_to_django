from bs4 import BeautifulSoup, Doctype, Tag


def format(soup: BeautifulSoup) -> None:
    if html := soup.find("html"):
        if isinstance(html, Tag):
            if html.has_attr("dj-remove-default"):
                if isinstance(soup.contents[0], Doctype):
                    soup.contents[0].extract()
                if head := html.find("head"):
                    if isinstance(head, Tag):
                        head.decompose()
                if body := html.find("body"):
                    if isinstance(body, Tag):
                        if script := body.find("script"):
                            if isinstance(script, Tag):
                                script.decompose()
                    body.unwrap()
                html.unwrap()
