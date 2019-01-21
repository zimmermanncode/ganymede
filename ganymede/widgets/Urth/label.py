"""Pythonic API for Polymer labels."""

from .element import Element
from .polymer import Polymer


class Label(Polymer.Component):

    def __init__(
            self, text=None, html_class=None, **html_attrs):

        super().__init__('iron-label', html_class=html_class, **html_attrs)
        with self:
            span = Element('span', html_class=['label'])
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
