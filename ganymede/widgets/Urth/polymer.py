"""
Pythonic API for PolymerElements.
"""

from .component import Component


class Meta(type(Component)):

    def paper(cls, name, html_class=None, **html_attrs):
        return cls('paper-' + name, html_class=html_class, **html_attrs)

    def iron(cls, name, html_class=None, **html_attrs):
        return cls('iron-' + name, html_class=html_class, **html_attrs)


class Polymer(Component, metaclass=Meta):

    def __init__(self, name, html_class=None, **html_attrs):
        super().__init__(name, html_class=html_class,
                         package_owner='PolymerElements',
                         version_spec='^1',
                         **html_attrs)
