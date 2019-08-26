"""Pythonic API for Polymer labels."""

from moretools import isstring

from .element import Element
from .polymer import Polymer


class Label(Polymer.Component):

    def __init__(
            self, text=None, html_class=None, html_span_class=None,
            **html_attrs):

        super(Label, self).__init__('iron-label', html_class=html_class, **html_attrs)
        html_span_class = ((
            list(html_span_class) if not isstring(html_span_class)
            else html_span_class.split()
        ) if html_span_class is not None else [])

        with self:
            span = Element('span', html_class=['label'] + html_span_class)
        if text is not None:
            span.text = text

    @property
    def text(self):
        return self.children[0].text

    @property
    def target(self):
        return self.__dict__.get('target')

    @target.setter
    def target(self, element):
        assert element in self.children
        element._element.set('iron-label-target', None)
        self.__dict__['target'] = element
