# Attributes

| dj-attr        | Dynamically assign attributes using Django template variables.                        |
|----------------|---------------------------------------------------------------------------------------|
| Syntax         | `<element dj-attr="attribute1;value1~attribute2;value2~attribute3;value3"></element>` |
| Example Input  | `<div dj-attr="class;my-class~id;my-id"></div>`                                       |
| Example Output | `<div class="{{ my-class }}" id="{{ my-id }}"></div>`                                 |

| dj-block       | Replace the element with Django block tags.         |
|----------------|-----------------------------------------------------|
| Syntax         | `<element dj-block="blockname">Content</element>`   |
| Example Input  | `<div dj-block="content">Content</div>`             |
| Example Output | `{% block content %}Content{% endblock %}`          |

| dj-command     | Replace the element with a Django template command.         |
|----------------|-------------------------------------------------------------|
| Syntax         | `<element dj-command="command"></element>`                  |
| Example Input  | `<div dj-command="url 'index'"></div>`                      |
| Example Output | `{% url 'index' %}`                                         |

| dj-for         | Replace the element with a Django template for loop.         |
|----------------|--------------------------------------------------------------|
| Syntax         | `<element dj-for="item in list">Content</element>`           |
| Example Input  | `<div dj-for="item in list"><p>Hello</p></div>`              |
| Example Output | `{% for item in list %}<p>Hello</p>{% endfor %}`             |

| dj-for-wrap    | Wrap the element within a Django template for loop.         |
|----------------|-------------------------------------------------------------|
| Syntax         | `<element dj-for-wrap="item in list">Content</element>`     |
| Example Input  | `<div dj-for-wrap="item in list">Content</div>`             |
| Example Output | `{% for item in list %}<div>Content</div>{% endfor %}`      |