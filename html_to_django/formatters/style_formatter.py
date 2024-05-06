from bs4 import BeautifulSoup


def parse_style(style: str) -> dict[str, str]:
    result: dict[str, str] = {}
    key_buffer = ""
    buffer = ""
    for char in style:
        if char == ":" and not key_buffer:
            key_buffer = buffer
            buffer = ""
        elif char == ";":
            result[key_buffer] = buffer
            key_buffer = ""
            buffer = ""
        elif char != " ":
            buffer += char
    if key_buffer and buffer:
        result[key_buffer] = buffer
    return result


def style_to_string(style: dict[str, str]) -> str:
    return ";".join([f"{name}:{value}" for name, value in style.items()])


def format(soup: BeautifulSoup) -> None:
    for element in soup.find_all(attrs={"dj-style": True}):
        style = parse_style(element["style"])
        dj_style = element.get("dj-style")
        for name, value, value_type in [declaration.split(";") for declaration in dj_style.split("~") if declaration]:
            style[name] = f"{{{{ {value} }}}}{value_type}"
        element["style"] = style_to_string(style)
        del element.attrs["dj-style"]
