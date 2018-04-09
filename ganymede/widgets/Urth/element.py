from copy import copy

from IPython.display import display, HTML
import lxml.html


CONTEXT_STACK = []


class Element:

    def __init__(self, tag, html_class=None, children=None, **html_attrs):
        self._element = lxml.html.Element(tag)
        html_class = list(html_class) if html_class is not None else []
        html_attrs.setdefault('class', ' '.join(html_class))
        # Element(tag, attrib=...) doesn't support None values,
        # but HtmlElement.set() does (for valueless HTML attributes)
        for key, value in html_attrs.items():
            self._element.set(key, value)
        self.children = list(children) if children is not None else []
        # are we inside a `with` context of another Element?
        if CONTEXT_STACK:
            CONTEXT_STACK[-1].children.append(self)

    def __enter__(self):
        CONTEXT_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc, traceback):
        assert CONTEXT_STACK[-1] is self
        CONTEXT_STACK.pop(-1)
        if exc is not None:
            raise exc.with_traceback(traceback)

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

    @property
    def text(self):
        return self._element.text

    @text.setter
    def text(self, value):
        if value is not None:
            value = str(value)
        self._element.text = value

    def to_html(self):
        return lxml.html.tostring(self._element_tree(), encoding='unicode',
                                  pretty_print=True)

    def print_html(self):
        print(self.to_html())

    def display(self):
        display(HTML(self.to_html()))

    def __repr__(self):
        return "Urth.{} {}".format(
            type(self).__qualname__,
            lxml.html.tostring(self._element_tree(), encoding='unicode',
                               pretty_print=True))
