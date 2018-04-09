from .element import Element
from .component import Component


class Container(Element):

    def __init__(self, html_class=None, children=None, **html_attrs):
        html_class = list(html_class) if html_class is not None else []
        if 'container' not in html_class:
            html_class.insert(0, 'container')
        super().__init__('div', html_class=html_class, children=children,
                         **html_attrs)

    def urth_imports(self):
        links = set()
        for element in self.children:
            if isinstance(element, Container):
                links.update(element.urth_imports())
            if isinstance(element, Component):
                links.add(element.urth_import)
        return links

    def bower_endpoints(self):
        return {imp.bower_endpoint for imp in self.urth_imports()}

    def to_html(self):
        return "{}\n{}".format(
            "\n".join(imp.to_html() for imp in self.urth_imports()),
            super().to_html())


class HBox(Container):

    def __init__(self, children=None, **html_attrs):
        super().__init__(html_class=['flex-horizontal'],
                         children=children, **html_attrs)


class VBox(Container):

    def __init__(self, children=None, **html_attrs):
        super().__init__(html_class=['flex-vertical'],
                         children=children, **html_attrs)
