"""Pythonic API for PolymerElements."""

from .component import Component


class PolymerComponent(Component):

    def __init__(self, tag, html_class=None, **html_attrs):
        super().__init__(
            tag, html_class=html_class,
            package_owner='PolymerElements', version_spec='^1',
            **html_attrs)


class Meta(type(Component)):

    Component = PolymerComponent

    def paper(cls, _tag, html_class=None, **html_attrs):
        return cls('paper-' + _tag, html_class=html_class, **html_attrs)

    def iron(cls, _tag, html_class=None, **html_attrs):
        return cls('iron-' + _tag, html_class=html_class, **html_attrs)


class Polymer(PolymerComponent, metaclass=Meta):
    pass
