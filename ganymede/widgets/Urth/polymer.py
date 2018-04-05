"""
Pythonic API for PolymerElements.
"""

from .component import Component


class Meta(type(Component)):

    def paper(cls, name, **html_attrs):
        return cls('paper-' + name, **html_attrs)

    def iron(cls, name, **html_attrs):
        return cls('iron-' + name, **html_attrs)


class Polymer(Component, metaclass=Meta):

    def __init__(self, name, **html_attrs):
        super().__init__(name, package_owner='PolymerElements',
                         version_spec='^1', **html_attrs)
