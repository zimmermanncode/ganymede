from copy import copy

from IPython.display import display, HTML
import lxml.etree


class Element:

    def __init__(self, name, children=None, **html_attrs):
        self._element = lxml.etree.Element(name, attrib=html_attrs)
        self.children = list(children) if children is not None else []

    def __eq__(self, other):
        return (self._element.tag == other._element.tag and
                self._element.attrib == other._element.attrib and
                self._element.nsmap == other._element.nsmap and
                self.children == other.children)

    def __hash__(self):
        return hash((self._element.tag, tuple(self._element.attrib.items()),
                     tuple(self._element.nsmap.items()),
                     tuple(self.children or ())))

    def _element_tree(self):
        root = copy(self._element)
        for element in self.children:
            root.append(element._element_tree())
        return root

    def to_html(self):
        return lxml.etree.tounicode(self._element_tree(), method='html',
                                    pretty_print=True)

    def print_html(self):
        print(self.to_html())

    def display(self):
        display(HTML(self.to_html()))

    def __repr__(self):
        return "Urth.{} {}".format(
            type(self).__qualname__,
            lxml.etree.tounicode(self._element_tree()))
