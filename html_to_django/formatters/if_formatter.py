from bs4 import BeautifulSoup


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-if": True}):
        element.insert_before(f"{{% if {element.get("dj-if")} %}}")

        participating_blocks = [element]

        current_sibling = element.find_next_sibling()
        while current_sibling is not None:
            if current_sibling.has_attr("dj-elif"):
                current_sibling.insert_before(f"{{% elif {current_sibling.get("dj-elif")} %}}")
                participating_blocks.append(current_sibling)
                current_sibling = current_sibling.find_next_sibling()
            elif current_sibling.has_attr("dj-else"):
                current_sibling.insert_before("{% else %}")
                participating_blocks.append(current_sibling)
                current_sibling = None
            else:
                current_sibling = None

        participating_blocks[-1].insert_after("{% endif %}")

        for block in participating_blocks:
            block.unwrap()
