from .element import Element
from .component import Component


class Container(Element):

    def __init__(self, html_class=None, children=None, **html_attrs):
        html_class = list(html_class) if html_class is not None else []
        if 'container' not in html_class:
            html_class.insert(0, 'container')
        html_attrs.setdefault('class', ' '.join(html_class))
        super().__init__('div', children=children, **html_attrs)

    def import_links(self):
        links = set()
        for element in self.children:
            if isinstance(element, Container):
                links.update(element.import_links())
            if isinstance(element, Component):
                links.add(element.import_link())
        return links

    def to_html(self):
        return "{}\n{}".format(
            "\n".join(link.to_html() for link in self.import_links()),
            super().to_html())


class HBox(Container):

    def __init__(self, children=None, **html_attrs):
        super().__init__(html_class=['flex-horizontal'],
                         children=children, **html_attrs)


class VBox(Container):

    def __init__(self, children=None, **html_attrs):
        super().__init__(html_class=['flex-vertical'],
                         children=children, **html_attrs)
